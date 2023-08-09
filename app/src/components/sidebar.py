from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from . import ids

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "right": 0,
    "top": 0,
    "bottom": 0,
    "width": "15rem",
    "padding": "2rem 2rem",
    "background-color": "#9e9a99",
}


def render(app: Dash) -> html.Div:
    return html.Div(
        [
            html.H2("Make Selection"),
            html.Hr(),
            "Exchange",
            dcc.RadioItems(
                options=[
                    {"label": x, "value": y}
                    for x, y in zip(["FTSE100", "Nasdaq"], ["^FTSE", "NQ=F"])
                ],
                inline=True,
                labelStyle={"margin": "0.5rem"},
                style={"display": "flex", "padding": "0rem"},
                id="exchange",
                value="^FTSE",
            ),
            html.Hr(),
            "Select stock for analysis",
            dcc.Dropdown(
                options=[{"label": x, "value": x} for x in ids.stocks],
                id="stock_id",
                value="AAPL",
            ),
        ],
        style=SIDEBAR_STYLE,
    )
