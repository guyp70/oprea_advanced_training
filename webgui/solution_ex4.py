from fast_dash import fastdash, Graph
import plotly.express as px

@fastdash()
def pro_grapher(m: float = 1, b: float = 0) -> Graph:
    generated_data = [(x, (m * x) + b) for x in range(100)]
    fig =  px.line(
        generated_data,
        title=f'(x * {m}) + {b} = y',
    )
    return fig.to_plotly_json()


# * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
