import dash
from dash import html, dcc

dash.register_page(__name__,     
    path='/test_page',
    title='test_page',
    name='test_page')

layout = html.Div(children=[
    html.H1(children='This is our Archive page'),

    html.Div(children='''
        This is our Archive page content.
    '''),

])