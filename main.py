from dash import Dash, html, dcc, Input, Output
import plotly.express as px
from data import country_df, totals_df
from builders import make_table

stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap",
]

app = Dash(__name__, external_stylesheets=stylesheets)

bubble_map = px.scatter_geo(
    country_df,
    hover_name="Country_Region",
    color="Confirmed",
    locations="Country_Region",
    locationmode="country names",
    hover_data={
        "Confirmed": ":,",
        "Deaths": ":,",
        "Recovered": ":,",
        "Country_Region": False,
    },
    size="Confirmed",
    title="Confirmed By Country",
    size_max=40,
    template="plotly_dark",
    color_continuous_scale=px.colors.sequential.Plotly3,
)

bubble_map.update_layout(margin=dict(l=0, r=0, t=50, b=0))

bars_graph = px.bar(
    totals_df,
    x="condition",
    y="count",
    template="plotly_dark",
    title="Total Global Cases",
    hover_data={"count": ":,"},
    labels={
        "condition": "Condition",
        "count": "Count",
        "color": "Condition",
    },
)
bars_graph.update_traces(marker_color=["#e74c3c", "#8e44ad", "#27ae60"])

app.layout = html.Div(
    style={
        "minHeight": "100vh",
        "backgroundColor": "#111111",
        "color": "white",
        "fontFamily": "Open Sans, sans-serif",
    },
    children=[
        html.Header(
            style={"textAlign": "center", "paddingTop": "50px"},
            children=[html.H1("Corona Dashboard", style={"fontSize": 50})],
        ),
        html.Div(
            style={
                "display": "grid",
                "gridTemplateColumns": "repeat(4, 1fr)",
                "gap": 50,
            },
            children=[
                html.Div(
                    style={"gridColumn": "span 3"},
                    children=[dcc.Graph(figure=bubble_map)],
                ),
                html.Div(
                    children=[make_table(country_df)],
                ),
            ],
        ),
        html.Div(
            style={
                "display": "grid",
                "gridTemplateColumns": "repeat(4, 1fr)",
                "gap": 50,
            },
            children=[
                html.Div(children=[dcc.Graph(figure=bars_graph)]),
                html.Div(
                    children=[
                        dcc.Input(placeholder="What is your name?", id="hello-input"),
                        html.H2(children="Hello anonymous", id="hello-output"),
                    ]
                ),
            ],
        ),
    ],
)


@app.callback(
    Output("hello-output", "children"),
    [
        Input("hello-input", "value"),
    ],
)
def update_hello(value):
    return f"Hello {value}" if value else "Hello anonymous"


if __name__ == "__main__":
    app.run(debug=True)
