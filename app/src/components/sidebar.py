from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash
import dash_bootstrap_components as dbc
from . import ids
from src.components.get_gainers import get_gainers

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "right": 0,
    "top": 0,
    "bottom": 0,
    "width": "15rem",
    "padding": "2rem 2rem",
    "background-color": "#0096FF",
}

stocks_dropdown = list(ids.stocks) + get_gainers()[1]


def render(app: Dash) -> html.Div:
    return html.Div(
        [
            html.H2("Make Selection"),
            html.Hr(),
            html.H4("Exchange"),
            dcc.RadioItems(
                options=[
                    {"label": x, "value": y}
                    for x, y in zip(
                        ids.exchange.values(),
                        ids.exchange.keys(),
                    )
                ],
                # inline=False,
                labelStyle={},
                # style={},
                id="exchange",
                value="^FTSE",
            ),
            html.Hr(),
            "Stock selection",
            dcc.Dropdown(
                options=[{"label": x, "value": x} for x in stocks_dropdown],
                id="stock_id",
                value="AAPL",
            ),
        html.Hr(),
        html.H4("Stock forecaster"),
        html.Div(
            
        [
            html.Div(
                dcc.Link(
                    # "test_pge", href="tst_page",
                    f"{page['name']} - {page['path']}", href=page["relative_path"],
                    style={"color": "red"}
                ),
            )
            for page in dash.page_registry.values()
        ],
        style={'color': 'black'}
    ),
        ],
        style=SIDEBAR_STYLE,
    )
