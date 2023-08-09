from dash import Dash, dcc, html
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import datetime
from yahoofinancials import YahooFinancials
import pandas as pd

from . import ids

# CONTENT_STYLE = {
#     "margin-left": "24rem",
#     "margin-right": "18rem",
#     "padding": "1rem 0rem",
#     'backgroundColor': 'black',
# }

MEDAL_DATA = px.data.medals_long()


def render(app: Dash) -> html.Div:
    @app.callback(Output(ids.BAR_CHART, "children"), Input("stock_id", "value"))
    def update_bar_chart(nations: list[str]) -> html.Div:
        # filtered_data = MEDAL_DATA[MEDAL_DATA.nation.isin([nations])]
        # print(f"dfefe {filtered_data}")
        # fig = px.bar(filtered_data, x="medal", y="count", color="nation", text="nation")
        # print(nations)
        # return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

        today = datetime.datetime.now()

        # First stock query
        stock = "^FTSE"
        stock_info = YahooFinancials(stock)
        history = stock_info.get_historical_price_data(
            "2017-01-10", today.strftime("%Y-%m-%d"), "monthly"
        )
        date = [val["formatted_date"] for val in history[stock]["prices"]]
        close = [val["close"] for val in history[stock]["prices"]]
        df = pd.DataFrame({"date": date, "Close": close})

        # Seconnd stock query
        stock_info2 = YahooFinancials(nations)
        history2 = stock_info2.get_historical_price_data(
            "2017-01-10", today.strftime("%Y-%m-%d"), "monthly"
        )
        date = [val["formatted_date"] for val in history2[nations]["prices"]]
        close = [val["close"] for val in history2[nations]["prices"]]
        dfs = pd.DataFrame({"date": date, "Close": close})

        fig = make_subplots(
            rows=2,
            cols=1,
            subplot_titles=(f"{stock}100", nations),
            vertical_spacing=0.1,
        )

        fig.append_trace(
            go.Scatter(
                x=df.date,
                y=df.Close,
            ),
            row=1,
            col=1,
        )

        fig.append_trace(
            go.Scatter(
                x=dfs.date,
                y=dfs.Close,
            ),
            row=2,
            col=1,
        )

        # fig = px.line(df, y="Close", title=stock)
        fig.update_traces(line_color="chartreuse")
        fig.layout.template = "plotly_dark"
        fig.update_layout(
            plot_bgcolor="#474952",
            width=800,
            height=650,
            autosize=False,
            showlegend=False,
            margin=dict(l=20, r=20, t=20, b=20),
        )
        fig.layout.annotations[0].update(x=0.025)
        fig.layout.annotations[1].update(x=0.025)

        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    return html.Div(id=ids.BAR_CHART)
