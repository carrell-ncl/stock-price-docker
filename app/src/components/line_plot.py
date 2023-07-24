from dash import Dash, dcc, html
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import datetime
import yfinance as yf

style = {"padding": "0rem 0rem", 'backgroundColor': 'black'}

def render (app: Dash, stock: str, stock_secondary: str) ->html.Div:
    # @app.callback(
    #     Output(ids.LINE_CHART, "children"),
    #     # Input(ids.NATIONS_DROPDOWN, "value")
    # )
    # def update_line_chart() -> html.Div:
        # ftse_df = yf.download('^FTSE',
        # start='1985-01-01',
        # end='2021-07-28',
        # progress=False)
        # fig = px.line(ftse_df, y="Close", title="FTSE100 Stock Prices")
        # return html.Div(dcc.Graph(figure=fig), id=ids.LINE_CHART)
    today = datetime.datetime.now()
    df = yf.download(stock,
    start='1985-01-01',
    end=today.strftime('%Y-%m-%d'),
    progress=False)

    dfs = yf.download(stock_secondary,
    start='1985-01-01',
    end=today.strftime('%Y-%m-%d'),
    progress=False)

    fig = make_subplots(rows=2, cols=1,
    subplot_titles=(f"{stock}100",stock_secondary),
    vertical_spacing = 0.1)

    fig.append_trace(go.Scatter(
        x=df.index,
        y=df.Close,
    ), row=1, col=1)

    fig.append_trace(go.Scatter(
        x=dfs.index,
        y=dfs.Close,
    ), row=2, col=1)


    # fig = px.line(df, y="Close", title=stock)
    fig.update_traces(line_color='chartreuse')
    fig.layout.template = 'plotly_dark'
    fig.update_layout(
        plot_bgcolor = "#474952", 
        width=800, height=650, 
        autosize=False, showlegend=False,
        margin=dict(l=20, r=20, t=20, b=20))
    fig.layout.annotations[0].update(x=0.025)
    fig.layout.annotations[1].update(x=0.025)

    return html.Div(dcc.Graph(figure=fig), style= style)
    # return html.Div(id=ids.LINE_CHART)


