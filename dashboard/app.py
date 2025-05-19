import dash
from dash import html, dcc
from visualize import generate_dashboard
import pandas as pd

def run_dashboard():
    """Launching a local dashboard"""
    try:
        df = pd.read_csv("data/sample_data.csv")
        fig1, fig2, fig3 = generate_dashboard(df)

        app = dash.Dash(__name__)
        app.layout = html.Div([
            html.H1("OpenSana Dashboard", style={'textAlign': 'center'}),
            dcc.Graph(figure=fig1),
            dcc.Graph(figure=fig2),
            dcc.Graph(figure=fig3)
        ])

        app.run_server(debug=True, host='0.0.0.0', port=8050)
    except Exception as e:
        print(f"[ERROR] Failed to start dashboard: {e}")
