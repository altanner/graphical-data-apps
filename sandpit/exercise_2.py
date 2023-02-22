import streamlit as st
import pandas as pd
import plotly.express as px

# use pandas to read CSV file into a dataframe
demo_df = pd.read_csv("demo_dataset.csv")

# set the tab title and page width
st.set_page_config(page_title="Demo App", layout="wide")

# build the sidebar
with st.sidebar:
    # put a title in the sidebar
    st.title("World Demographics")
    # dataframe visibility toggle
    df_view = st.checkbox(label="View dataframe")

# create two columns, of ratio 5:1
column1, column2 = st.columns([5,1])

# place info box in first column
with column1:
    st.info("Welcome to the global demographic data explorer app!")

# place image into second column
with column2:
    st.image("globe.png")

# show us the data if the sidebar toggle is switched
if df_view == True:
    st.dataframe(demo_df)

# build px chart object
chart = px.scatter(
    data_frame=demo_df,
    x="Life expectancy",
    y="GDP per capita",
    color="Continent",
    size="CO2 per capita",
    hover_name="Country",
    trendline="lowess",
    height=650)

# display the chart in the main app area
st.plotly_chart(chart, use_container_width=True)
