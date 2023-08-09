from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

from . import line_plot, sidebar, top_stocks_table, line_plot2

# from src.components import inputs


def create_layout(app: Dash) -> html.Div:
    CONTENT_STYLE = {
        "margin-left": "24rem",
        "margin-right": "18rem",
        "padding": "0rem 0rem",
        "backgroundColor": "black",
    }

    content = html.Div(
        style=CONTENT_STYLE,
        className="app-div",
        children=[
            html.H1(app.title, style={"backgroundColor": "black", "color": "white"}),
            html.Hr(),
            # html.Div(
            #     className="dropdown-container",
            #     children=[
            #         dropdown.render(app)
            #     ]
            # ),
            line_plot.render(app),
        ],
    )

    return html.Div(
        className="app-div",
        children=[
            dbc.Col(sidebar.render(app)),
            dbc.Col(content),
            dbc.Col(top_stocks_table.render(app)),
        ],
    )
    # ], style={'backgroundColor': 'white'})


# def create_layout(app: Dash) -> html.Div:
#     return html.Div(
#         className="app-div",
#         children=[
#             html.H1(app.title),
#             html.Hr(),
#             html.Div(
#                 className="dropdown-container",
#                 children=[
#                     dbc.Col(sidebar.render(app))
#                 ]
#             ),
#             line_plot2.render(app),
#             # html.Div(
#             #     className="input-container",
#             #     children=[
#             #         inputs.render(app)
#                 ]
#             )


# def create_layout(app: Dash) -> html.Div:
#     return html.Div(
#         className="app-div",
#         children=[
#             html.H1(app.title),
#             html.Hr(),
#             html.Div(
#                 className="sidebar-container",
#                 children=[
#                     sidebar.render(app)
#                 ]
#             ),
#             line_plot.render(app),
#             # html.Div(
#             #     className="input-container",
#             #     children=[
#             #         inputs.render(app)
#             #     ]
#             # ),
#         ]
#     )
