from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

from . import line_plot, sidebar, top_stocks_table


def create_layout(app: Dash) -> html.Div:
    CONTENT_STYLE = {
        "top": 40,
        "margin-left": "24rem",
        "margin-right": "18rem",
        "padding": "1rem 0rem",
        "backgroundColor": "#353935",
        "position": "absolute",
    }
    header = html.Div(
        style={"bottom": 40},
        className="app-div",
        children=[
            html.H1(app.title, style={"backgroundColor": "#353935", "color": "white"}),
        ],
    )

    content = html.Div(
        style=CONTENT_STYLE,
        className="app-div",
        children=[
            html.H4("History", style={"color": "#F0EAD6"}),
            line_plot.render(app),
        ],
    )

    return html.Div(
        className="app-div",
        children=[
            dbc.Col(header),
            dbc.Col(sidebar.render(app)),
            dbc.Col(content),
            dbc.Col(top_stocks_table.render(app)),
        ],
    )
