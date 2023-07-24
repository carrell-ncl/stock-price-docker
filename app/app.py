from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP
from src.components.layout import create_layout
from flask import Flask


server = Flask(__name__)
app = Dash(external_stylesheets=[BOOTSTRAP], server=server)
app.title = "Stock Dashboard"
app.layout = create_layout(app)

if __name__ == "__main__":
    app.run()