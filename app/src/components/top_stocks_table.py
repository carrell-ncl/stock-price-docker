import datetime
from dash import Dash, dash_table, html
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
from yahoofinancials import YahooFinancials

from . import ids

TABLE_STYLE = {
    "left": 0,
    "top": 0,
    "width": "24rem",
    # "length": "60rem",
    "position": "absolute",
    "padding": "1rem 0rem",
    # "padding": "6rem 2rem",
    "backgroundColor": "black",
    "display": "inline-block",
}


def render(app: Dash) -> html.Div:
    ## TODO HANDLE WEEKENDS AND HOLIDAYS

    # Define top 20 stocks
    stocks = ids.stocks

    stocks_df = pd.DataFrame()

    today_prices = list()
    yesterday_prices = list()
    for stock in stocks:
        stock_info = YahooFinancials(stock)
        previous = datetime.datetime.today() - datetime.timedelta(days=6)
        history = stock_info.get_historical_price_data(
            previous.strftime("%Y-%m-%d"),
            datetime.datetime.today().strftime("%Y-%m-%d"),
            "daily",
        )
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

    stocks_df["Stock"] = stocks
    stocks_df["Current"] = today_prices
    stocks_df["Previous"] = yesterday_prices
    stocks_df["change"] = round(stocks_df.Current - stocks_df.Previous, 2)

    stocks_df = stocks_df.round(2)

    stocks_df.to_dict("records")

    return html.Div(
        className="app-div",
        children=[
            html.H1("Live prices", style={"color": "white"}),
            html.Hr(),
            dash_table.DataTable(
                data=stocks_df.to_dict("records"),
                columns=[{"id": c, "name": c} for c in stocks_df.columns],
                style_cell_conditional=[
                    {"if": {"column_id": c}, "textAlign": "left"} for c in ["Stock"]
                ],
                style_data={"border": "1px solid blue"},
                style_header={"border": "1px solid red"},
                style_cell={"backgroundColor": "rgb(50, 50, 50)", "color": "white"},
                style_as_list_view=True,
                id="tbl",
            ),
        ],
        style=TABLE_STYLE,
    )
