import datetime
from dash import Dash, dash_table, html
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import yfinance as yf

from . import ids

TABLE_STYLE = {
    "left": 0,
    "top":0,
    "width": "24rem",
    # "length": "60rem",
    "position": "absolute",
    "padding": "6rem 2rem",
    'backgroundColor': 'black',
    'display': 'inline-block'
}



def render(app: Dash) -> html.Div:
    ## TODO HANDLE WEEKENDS AND HOLIDAYS
    today = datetime.datetime.now()
    past = datetime.timedelta(days = 4)

    start_date = (today - past).strftime('%Y-%m-%d')
    end_date = today.strftime('%Y-%m-%d')

    # Define top 20 stocks
    stocks = ids.stocks

    vals = []
    names = []
    for stock in stocks:
        vals.append(yf.download(stock, 
                start_date,
                end_date)['Adj Close'].values)
        names.append(yf.Ticker(stock).info['longName'])
    
    vals = np.array(vals)
        

    stocks_df = pd.DataFrame()
    # stocks_df['Name'] = names
    stocks_df['Stock'] = stocks
    stocks_df['Latest'] = np.around(vals[:, 1],2)
    stocks_df['Previous'] = np.around(vals[:, 0],2)
    stocks_df['change'] = np.around(vals[:, 1]-vals[:, 0], 2)

    stocks_df.to_dict('records')

    return html.Div(
            className="app-div", 
            children=[
        html.H2("Live prices", style={'color':'white'}),

    dash_table.DataTable(
        data=stocks_df.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in stocks_df.columns],
        style_cell_conditional=[
        {
            'if': {'column_id': c},
            'textAlign': 'left'
        } for c in ['Stock']
    ],
        style_data={'border': '1px solid blue' },
        style_header={'border': '1px solid red'},
        style_cell= {'backgroundColor': 'rgb(50, 50, 50)', 'color': 'white'},
        style_as_list_view=True,
        id='tbl'
    )], 
    style=TABLE_STYLE,
    )
    