import pandas as pd
import plotly_express as px

df = pd.read_csv("Copy+of+data+-+data.csv")
fig = px.scatter(df, x="date", y= "cases", color= "country", size_max= 45)

fig.show()