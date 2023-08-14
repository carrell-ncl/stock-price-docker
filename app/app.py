from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP
from src.components.layout import create_layout
from flask import Flask


server = Flask(__name__)
app = Dash(external_stylesheets=[BOOTSTRAP], server=server, use_pages=True)

app.title = "Stocks Dashboard"

app.layout = create_layout(app)

if __name__ == "__main__":
    app.debug = True,
    app.run_server(
        port=3000, 
        host="0.0.0.0"
        )
