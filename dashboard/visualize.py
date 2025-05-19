import pandas as pd
import plotly.express as px

def generate_dashboard(df: pd.DataFrame):
    """Generating a dashboard from a DataFrame"""
    fig1 = px.line(df, x='date', y='cases', title='Outbreak Trends')
    fig2 = px.bar(df, x='region', y='supplies', title='Medical Supply Distribution')
    fig3 = px.pie(df, names='disease', title='Disease Distribution')
    return fig1, fig2, fig3
