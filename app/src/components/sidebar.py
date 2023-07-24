from dash import Dash, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from . import ids

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "right": 0,
    "top":0,
    "bottom": 0,
    "width": "15rem",
    "padding": "2rem 2rem",
    "background-color": "#9e9a99",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.

def render(app: Dash) -> html.Div:
    
    # @app.callback(
    #     Output(ids.NATIONS_DROPDOWN, "value"),
    #     Input(ids.SELECT_ALL_BUTTON, "n_clicks")
    # )
    # def select_all_nations(_: int) -> list[str]:
    #     return all_nations
    
    return html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Page 1", href="/page-1", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)