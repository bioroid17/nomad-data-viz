from dash import Dash, html, dcc
import plotly.express as px

stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap",
]

app = Dash(__name__, external_stylesheets=stylesheets)

app.layout = html.Div(
    style={
        "minHeight": "100vh",
        "backgroundColor": "#111111",
        "color": "white",
        "fontFamily": "Open Sans, sans-serif",
    },
    children=[
        html.Header(
            style={
                "textAlign": "center",
                "paddingTop": "50px",
            },
            children=[
                html.H1(
                    "Corona Dashboard",
                    style={"fontSize": 50},
                )
            ],
        )
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
