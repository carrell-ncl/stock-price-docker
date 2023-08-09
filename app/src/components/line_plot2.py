from dash import Dash, dcc, html
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import datetime
from yahoofinancials import YahooFinancials
import pandas as pd

from dash import Dash, dcc, html
import plotly.express as px
from dash.dependencies import Input, Output

from . import ids

MEDAL_DATA = px.data.medals_long()


def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"), Input(ids.NATIONS_DROPDOWN, "value")
    )
    def update_bar_chart(nations: list[str]) -> html.Div:
        # filtered_data = MEDAL_DATA[MEDAL_DATA.nation.isin(nations)]
        fig = px.bar(MEDAL_DATA, x="medal", y="count", color="nation", text="nation")
        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    return html.Div(id=ids.BAR_CHART)


# style = {"padding": "0rem 0rem", 'backgroundColor': 'black'}

# MEDAL_DATA = px.data.medals_long()
# stock = "^FTSE"

# def render (app: Dash) ->html.Div:
#     @app.callback(
#         Output("line_chart", "children"),
#         Input("stock dropdown", "value")
#     )
#     def update_bar_chart(stock_secondary: list[str]) -> html.Div:

#         # # First stock query
#         # stock_info = YahooFinancials(stock)
#         # history = stock_info.get_historical_price_data("2017-01-10", today.strftime('%Y-%m-%d'), "monthly")
#         # date = [val['formatted_date'] for val in history[stock]['prices']]
#         # close = [val['close'] for val in history[stock]['prices']]
#         # df = pd.DataFrame({'date':date, 'Close':close})

#         # # Second stock query
#         # stock_info2 = YahooFinancials(stock_secondary)
#         # history2 = stock_info2.get_historical_price_data("2017-01-10", today.strftime('%Y-%m-%d'), "monthly")
#         # date = [val['formatted_date'] for val in history2[stock_secondary]['prices']]
#         # close = [val['close'] for val in history2[stock_secondary]['prices']]
#         # dfs = pd.DataFrame({'date':date, 'Close':close})

#         # fig = make_subplots(rows=2, cols=1,
#         # subplot_titles=(f"{stock}100",stock_secondary),
#         # vertical_spacing = 0.1)

#         # fig.append_trace(go.Scatter(
#         #     x=df.date,
#         #     y=df.Close,
#         # ), row=1, col=1)

#         # fig.append_trace(go.Scatter(
#         #     x=dfs.date,
#         #     y=dfs.Close,
#         # ), row=2, col=1)


#         # # fig = px.line(df, y="Close", title=stock)
#         # fig.update_traces(line_color='chartreuse')
#         # fig.layout.template = 'plotly_dark'
#         # fig.update_layout(
#         #     plot_bgcolor = "#474952",
#         #     width=800, height=650,
#         #     autosize=False, showlegend=False,
#         #     margin=dict(l=20, r=20, t=20, b=20))
#         # fig.layout.annotations[0].update(x=0.025)
#         # fig.layout.annotations[1].update(x=0.025)

#         # filtered_data = MEDAL_DATA[MEDAL_DATA.nation.isin(nations)]
#         fig = px.bar(MEDAL_DATA, x="medal", y="count", color="nation", text="nation")
#         return html.Div(dcc.Graph(figure=fig), id="line_chart")

#     return html.Div(id="line_chart")

# # def render (app: Dash, stock: str, stock_secondary: str) ->html.Div:
# #     # @app.callback(
# #     #     Output(ids.LINE_CHART, "children"),
# #     #     # Input(ids.NATIONS_DROPDOWN, "value")
# #     # )

# #     today = datetime.datetime.now()

# #     # First stock query
# #     stock_info = YahooFinancials(stock)
# #     history = stock_info.get_historical_price_data("2017-01-10", today.strftime('%Y-%m-%d'), "monthly")
# #     date = [val['formatted_date'] for val in history[stock]['prices']]
# #     close = [val['close'] for val in history[stock]['prices']]
# #     df = pd.DataFrame({'date':date, 'Close':close})


# #     # Seconnd stock query
# #     stock_info2 = YahooFinancials(stock_secondary)
# #     history2 = stock_info2.get_historical_price_data("2017-01-10", today.strftime('%Y-%m-%d'), "monthly")
# #     date = [val['formatted_date'] for val in history2[stock_secondary]['prices']]
# #     close = [val['close'] for val in history2[stock_secondary]['prices']]
# #     dfs = pd.DataFrame({'date':date, 'Close':close})


# #     fig = make_subplots(rows=2, cols=1,
# #     subplot_titles=(f"{stock}100",stock_secondary),
# #     vertical_spacing = 0.1)

# #     fig.append_trace(go.Scatter(
# #         x=df.date,
# #         y=df.Close,
# #     ), row=1, col=1)

# #     fig.append_trace(go.Scatter(
# #         x=dfs.date,
# #         y=dfs.Close,
# #     ), row=2, col=1)


# #     # fig = px.line(df, y="Close", title=stock)
# #     fig.update_traces(line_color='chartreuse')
# #     fig.layout.template = 'plotly_dark'
# #     fig.update_layout(
# #         plot_bgcolor = "#474952",
# #         width=800, height=650,
# #         autosize=False, showlegend=False,
# #         margin=dict(l=20, r=20, t=20, b=20))
# #     fig.layout.annotations[0].update(x=0.025)
# #     fig.layout.annotations[1].update(x=0.025)

# #     return html.Div(dcc.Graph(figure=fig), style= style)
# #     # return html.Div(id=ids.LINE_CHART)
