import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv("data.csv")

print(df.groupby("level")["attempt"].mean())

figure = go.Figure(go.Bar(
    x = df.groupby("level")["attempt"].mean(),
    y = ["Level 1","Level 2","Level 3", "Level 4"]
    ,orientation ="h"
))
figure.show()

#print((0.751445+ 0.863281+ 0.69811+ 0.734694)/4)
  
studentDetails = df.loc[ df["student_id"] == "TRL_mno"]

print(studentDetails.groupby("level")["attempt"].mean())

figure = go.Figure(go.Bar(
    x = studentDetails.groupby("level")["attempt"].mean(),
    y = ["Level 1","Level 2","Level 3", "Level 4"]
    ,orientation ="h"
))
#figure.show()


df1 = pd.read_csv("data.csv")
mean = df1.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
fig = px.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")
fig.show()


