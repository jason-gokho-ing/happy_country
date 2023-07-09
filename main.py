import streamlit as st
import pandas as pd
import plotly.express as px

st.title("In Search of Happiness")

x_axis = st.selectbox("Select the data for the x-axis",
                      ('happiness', 'gdp',
                       'generosity', 'corruption'), key='x_axis')

y_axis = st.selectbox("Select the data for the y-axis",
                      ('happiness', 'gdp',
                       'generosity', 'corruption'), key='y_axis')

df = pd.read_csv("happy.csv")

match x_axis:
    case "happiness":
        x_array = df['happiness']

    case "gdp":
        x_array = df['gdp']

    case "generosity":
        x_array = df['generosity']

    case "corruption":
        x_array = df['corruption']

match y_axis:
    case "happiness":
        y_array = df['happiness']

    case "gdp":
        y_array = df['gdp']

    case "generosity":
        y_array = df['generosity']

    case "corruption":
        y_array = df['corruption']

st.subheader(f"{x_axis} and {y_axis}")

figure1 = px.scatter(x=x_array, y=y_array,
                     labels={"x": x_axis, "y": y_axis})

st.plotly_chart(figure1)
