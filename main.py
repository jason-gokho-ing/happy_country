import streamlit as st
import pandas as pd
import plotly.express as px
from geopy.geocoders import Nominatim

st.set_page_config(layout="wide")
df = pd.read_csv("happy.csv")
df = df.drop_duplicates()

with st.sidebar:
    st.sidebar.subheader("Methodology Explained:")
    st.sidebar.markdown("<p>The happiness scores and rankings use data from the Gallup World Poll."
                        "The scores are based on answers to the main life evaluation question asked in the "
                        "poll.<br><br>"
                        "This question, known as the Cantril ladder, asks respondents to think of a ladder with the "
                        "best"
                        "possible life for them being a 10 and the worst possible life being a 0 and to "
                        "rate their own current lives on that scale. <br><br>"
                        "The scores are from nationally representative samples for the years 2015-2019 and use the "
                        "Gallup"
                        "weights to make the estimates representative. <br><br>"
                        "<b>The columns following the happiness score estimate the extent to which each of six "
                        "factors –"
                        "economic production, social support, life expectancy, freedom, absence of corruption, "
                        "and generosity. </b></p>", unsafe_allow_html=True)

st.title("In Search of Happiness (2015-2019)")

year = st.selectbox("Select a year:", ('2015', '2016', '2017', '2018', '2019'))

x_axis = st.selectbox("Select the data for the x-axis",
                      ("gdp", "social_support", "health", "freedom", "generosity", "trust"),
                      key='x_axis')

y_axis = st.selectbox("Select the data for the y-axis",
                      ("gdp", "social_support", "health", "freedom", "generosity", "trust"),
                      key='y_axis')

if year == "2015":
    df = df.loc[df['year'] == 2015]
elif year == "2016":
    df = df.loc[df['year'] == 2016]
elif year == "2017":
    df = df.loc[df['year'] == 2017]
elif year == "2018":
    df = df.loc[df['year'] == 2018]
elif year == "2019":
    df = df.loc[df['year'] == 2019]

match x_axis:

    case "gdp":
        x_array = df['gdp']

    case "social_support":
        x_array = df['social_support']

    case "health":
        x_array = df['health']

    case "generosity":
        x_array = df['generosity']

    case "freedom":
        x_array = df['freedom']

    case "trust":
        x_array = df['trust']

match y_axis:
    case "gdp":
        y_array = df['gdp']

    case "social_support":
        y_array = df['social_support']

    case "health":
        y_array = df['health']

    case "generosity":
        y_array = df['generosity']

    case "freedom":
        y_array = df['freedom']

    case "trust":
        y_array = df['trust']

st.subheader(f"{x_axis} and {y_axis} for {year}")

figure1 = px.scatter(df, x=x_array, y=y_array, color=df['region'],
                     labels={"x": x_axis, "y": y_axis},
                     hover_name="country", hover_data=["country"])

st.plotly_chart(figure1)

col3, col4 = st.columns([2.6, 2.85])
df_top = df.sort_values(by=['ranking'], ascending=True)
df_bottom = df.sort_values(by=['ranking'], ascending=False)

with col3:
    df_top = df_top.head(10)
    st.subheader(f'Top 10 Happiest countries in {year} 😄')
    st.dataframe(data=df_top, column_order=('ranking', 'region', 'country', 'score'), hide_index=True)
with col4:
    df_bottom = df_bottom.head(10)
    st.subheader(f'Bottom 10 Happiest countries in {year} 😭')
    st.dataframe(data=df_bottom, column_order=('ranking', 'region', 'country', 'score'), hide_index=True)

df_raw = pd.read_csv("happy.csv")
df_raw = df_raw.sort_values(by=['country', 'year'], ascending=True)
df_raw = df_raw.drop_duplicates()
search_country = st.selectbox("Select a country for a detailed look:",
                              options=df_raw['country'].unique())
search_country.lstrip().rstrip()
country = df_raw.loc[df_raw['country'] == search_country]
st.dataframe(data=country, column_order=('region', 'country', 'year', "ranking", 'score', "gdp",
                                         "social_support", "health", "freedom",
                                         "generosity", "trust"'score'),
             hide_index=True, use_container_width=True)
