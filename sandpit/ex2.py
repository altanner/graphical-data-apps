import streamlit as st
import pandas as pd
import plotly.express as px

# use pandas to read our CSV file into a dataframe called "demo_df"
demo_df = pd.read_csv("demo_dataset.csv")

column_names = [
    "HDI index",
    "GDP per capita",
    "Life expectancy",
    "CO2 per capita",
    "Services"]

# put a title in the sidebar
with st.sidebar:
    st.title("World Demographics")
    user_name = st.text_input("Welcome - please enter your name.")
    animate_widget = st.checkbox(
        label = "Animate")
    year_widget = st.slider(
        label = "Year to chart",
        min_value = 1998,
        max_value = 2018,
        disabled = animate_widget)
    log_y_widget = st.checkbox(
        label = "Logarithmic Y-axis")
    x_data_widget = st.radio(
        label = "X-axis data",
        options = column_names)
    y_data_widget = st.radio(
        label = "Y-axis data",
        options = column_names)
    
# create two columns, of ratio 3:1
column1, column2 = st.columns([3, 1])

# place info box in first column
with column1:
    st.info("Welcome to the global demographic data explorer app!")
with column2:
    st.info(f"Hi {user_name}!")
    
# create two tabs
tab1, tab2 = st.tabs(["Data", "Visualisation"])

# display the dataframe in tab1
with tab1:
    st.dataframe(demo_df)

# build px chart object
if animate_widget == False:
    chart = px.scatter(
        data_frame = demo_df[demo_df["Year"] == year_widget],
        x = x_data_widget,
        y = y_data_widget,
        log_y = log_y_widget,
        color = "Continent",
        size = "CO2 per capita",
        hover_name = "Country",)
if animate_widget == True:
    chart = px.scatter(
        data_frame = demo_df,
        x = x_data_widget,
        y = y_data_widget,
        log_y = log_y_widget,
        color = "Continent",
        size = "CO2 per capita",
        hover_name = "Country",
        animation_frame = "Year",
        animation_group = "Country",)

# display the chart in tab2
with tab2:
    st.plotly_chart(chart)