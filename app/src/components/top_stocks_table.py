import datetime
from dash import Dash, dash_table, html
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
from yahoofinancials import YahooFinancials

from . import ids
from src.components.get_gainers import get_gainers

TABLE_STYLE = {
    "left": 0,
    "top": 40,
    "width": "24rem",
    # "length": "60rem",
    "position": "absolute",
    "padding": "1rem 0rem",
    # "padding": "6rem 2rem",
    "backgroundColor": "#353935",
    "display": "inline-block",
}

CONDITION_STYLES = [
        {
            'if': {
                'filter_query': '{Change} >= 0',
                'column_id': ['Current', 'Previous', 'Change', '%Change']
            },
            'color': 'green'
        },
        {
            'if': {
                'filter_query': '{Change} < 0',
                'column_id': ['Current', 'Previous', 'Change', '%Change']
            },
            'color': 'red'
        }]



def get_stock_table(stock_list: list[str]) ->pd.DataFrame():

    stocks_df = pd.DataFrame()

    # Ensure only buisiness days are selected
    today_working = datetime.datetime.today()

    if today_working.weekday() in (5,6):
        while today_working.weekday() >= 5:
            today_working -= datetime.timedelta(days=1)

    prev_working = today_working - datetime.timedelta(days=1)
    if prev_working.weekday() in (5,6):
        while prev_working.weekday() >= 5:
            prev_working -= datetime.timedelta(days=1)

    today_working = today_working + datetime.timedelta(days=1)
    today_prices = list()
    yesterday_prices = list()
    for stock in stock_list:
        stock_info = YahooFinancials(stock)
        history = stock_info.get_historical_price_data(
            prev_working.strftime("%Y-%m-%d"),
            today_working.strftime("%Y-%m-%d"),
            "daily",
        )
        # Ensure a value is returned
        if (
            history[stock]["prices"][-1]["close"]
            and history[stock]["prices"][0]["close"]
        ):
            today = [val["close"] for val in history[stock]["prices"]][-1]
            yesterday = [val["close"] for val in history[stock]["prices"]][0]
            today_prices.append(today)
            yesterday_prices.append(yesterday)
        else:
            today_prices.append(0)
            yesterday_prices.append(0)

    stocks_df["Stock"] = stock_list
    stocks_df["Current"] = today_prices
    stocks_df["Previous"] = yesterday_prices
    stocks_df["Change"] = stocks_df.Current - stocks_df.Previous
    stocks_df["%Change"] = (stocks_df.Change/stocks_df.Previous)*100

    stocks_df = stocks_df.round(2)

    return stocks_df

def render(app: Dash) -> html.Div:
    ## TODO HANDLE WEEKENDS AND HOLIDAYS

    # Define top 20 stocks
    stocks = ids.stocks.keys()
    gainers = get_gainers()

    stocks_df = get_stock_table([val for val in stocks][:12])
    gainers_df = get_stock_table(gainers[:5])

    # stocks_df.to_dict("records")

    return html.Div(
        className="app-div",
        children=[
            # html.Hr(),
            html.H4("Live prices", style={"color": "#F0EAD6"}),
            # html.Hr(),
            dash_table.DataTable(
                data=stocks_df.to_dict("records"),
                columns=[{"id": c, "name": c} for c in stocks_df.columns],
                style_cell_conditional=[
                    {"if": {"column_id": c}, "textAlign": "left"} for c in ["Stock"]
                ],
                style_data={"border_bottom": "1px solid blue"},
                style_header={"border": "1px solid red"},
                style_cell={"backgroundColor": "rgb(50, 50, 50)", "color": "white"},
                style_as_list_view=True,
                id="tbl",
                style_data_conditional=CONDITION_STYLES
                ),
                html.Hr(),
                html.H4("Top Gainers (24hrs)", style={"color": "#F0EAD6"}),
                dash_table.DataTable(
                data=gainers_df.to_dict("records"),
                columns=[{"id": c, "name": c} for c in stocks_df.columns],
                style_cell_conditional=[
                    {"if": {"column_id": c}, "textAlign": "left"} for c in ["Stock"]
                ],
                style_data={"border_bottom": "1px solid blue"},
                style_header={"border": "1px solid red"},
                style_cell={"backgroundColor": "rgb(50, 50, 50)", "color": "white"},
                style_as_list_view=True,
                id="tbl",
                style_data_conditional=CONDITION_STYLES
                )
                ],
        style=TABLE_STYLE
        
    )
