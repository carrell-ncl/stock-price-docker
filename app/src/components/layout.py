from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

from src.components import line_plot, sidebar, top_stocks_table
# from src.components import inputs

def create_layout(app: Dash) -> html.Div:

    CONTENT_STYLE = {
        "margin-left": "24rem",
        "margin-right": "18rem",
        "padding": "1rem 0rem",
        'backgroundColor': 'black',
    }

    content= html.Div(style=CONTENT_STYLE,
            className="app-div", 
            children=[
                html.H1(app.title, style={'backgroundColor':'black', 'color':'white'}),
                html.Hr(),
                # html.Div(
                #     className="dropdown-container",
                #     children=[
                #         dropdown.render(app)
                #     ]
                # ),
                line_plot.render(app, '^FTSE', 'AAPL'),
                # line_plot.render(app, 'AAPL'),
                # html.Div(
                #     className="input-container",
                #     children=[
                #         inputs.render(app)
                #     ]
                # ),
            ]
        )

    return html.Div(
        [
        dbc.Col(sidebar.render(app)), 
        dbc.Col(content), 
        dbc.Col(top_stocks_table.render(app))], style={'backgroundColor': 'black'})