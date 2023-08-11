from dash import Dash, dcc, html
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import datetime
from yahoofinancials import YahooFinancials
import pandas as pd

from . import ids

def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.LINE_CHART, "children"),
        Input("exchange", "value"),
        Input("stock_id", "value"),
    )
    def update_line_chart(exchange_code: str, stock_code: str) -> html.Div:
        today = datetime.datetime.now()

        stocks = ids.stocks
        exchange = ids.exchange

        # First stock query
        stock_info = YahooFinancials(exchange_code)
        exchange_name = exchange.get(exchange_code)
        history = stock_info.get_historical_price_data(
            "2019-01-10", today.strftime("%Y-%m-%d"), "daily"
        )
        date = [val["formatted_date"] for val in history[exchange_code]["prices"]]
        close = [val["close"] for val in history[exchange_code]["prices"]]
        df = pd.DataFrame({"date": date, "Close": close})
        df["av"] = df.Close.rolling(20).mean()

        # Seconnd stock query
        stock_info2 = YahooFinancials(stock_code)
        stock_name = stocks.get(stock_code)

        history2 = stock_info2.get_historical_price_data(
            "2019-01-10", today.strftime("%Y-%m-%d"), "daily"
        )
        date = [val["formatted_date"] for val in history2[stock_code]["prices"]]
        close = [val["close"] for val in history2[stock_code]["prices"]]
        dfs = pd.DataFrame({"date": date, "Close": close})
        dfs["av"] = dfs.Close.rolling(20).mean()

        fig = make_subplots(
            rows=2,
            cols=1,
            subplot_titles=[exchange_name, stock_name],
            vertical_spacing=0.1
        )

        fig.append_trace(
            go.Scatter(x=df.date, y=df.Close),
            row=1,
            col=1,
        )
        fig.append_trace(
            go.Scatter(x=df.date, y=df.av),
            row=1,
            col=1,
        )
        # fig.update_traces(line_color="red")

        fig.append_trace(
            go.Scatter(
                x=dfs.date,
                y=dfs.Close,
            ),
            row=2,
            col=1,
        )
        fig.append_trace(
            go.Scatter(
                x=dfs.date,
                y=dfs.av,
            ),
            row=2,
            col=1,
        )

        # fig = px.line(df, y="Close", title=stock)
        # fig.update_traces(line_color="chartreuse")
        fig.layout.template = "ggplot2"
        fig.update_layout(
            plot_bgcolor="#474952",
            paper_bgcolor='#353935',
            font = dict(color = 'white'),
            width=800,
            height=650,
            autosize=False,
            showlegend=False,
            margin=dict(l=20, r=20, t=20, b=20),
        )

        # fig.layout.annotations[0].update(x=0.025)
        # fig.layout.annotations[1].update(x=0.025)

        return html.Div(dcc.Graph(figure=fig), id=ids.LINE_CHART)

    return html.Div(id=ids.LINE_CHART)
