import plotly.express as px
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "epoch": range(1, 11), #training iteration number
    "loss": [0.9, 0.8, 0.75, 0.7, 0.65, 0.6, 0.58, 0.55, 0.52, 0.5] #model error value
})

fig = px.line(
    df,
    x = "epoch",
    y = "loss",
    title = "line graph"
)

fig.add_annotation(
    x = 5,
    y = .8,
    text = "point",
    showarrow= True,
    startarrowhead= 5,
    ax = 0,
    ay = -50
)

fig.show()