import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="A Demographics Data App",
    layout="wide")

# use pandas to read CSV file into a dataframe
demo_df = pd.read_csv("demo_dataset.csv")

# names of columns in the csv file
csv_column_names = [
    "Life expectancy",
    "HDI index",
    "CO2 per capita",
    "GDP per capita"]

### build the sidebar
with st.sidebar:
    
    # put a title in the sidebar
    st.title("World Demographics")
    # add an image
    st.image("globe.png")
    # add a blue info box 
    st.info("Welcome to the global demographic data explorer app.")

    # visualisation type checkbox
    animate_vis = st.checkbox(
        label="Animate",
        value=False)
    
    # year slider widget
    year = st.slider(
        label="Year",
        min_value=1998,
        max_value=2018,
        value=2008)
    
    # x and y selector widgets
    x_data = st.radio(
        label="X-axis data",
        options=csv_column_names)
    y_data = st.radio(
        label="Y-axis data",
        options=csv_column_names,
        index=1)
    
    # balloon size widgets
    balloon_size_data = st.radio(
        label="Size data",
        options=["CO2 per capita", "GDP per capita"])
    balloon_size_scale = st.slider(
        label="Size scale",
        min_value=10,
        max_value=50,
        value=30)

### end of sidebar!


column1, column2 = st.columns([1, 5])


with column1:
    st.write("This is column 1")
    
with column2:
    st.write("This is column 2")

st.write("outside of the column blocks, we get the main body")


# check if user wants an animation or static visual
if animate_vis == False:
    # use plotly.express to create static chart object
    chart = px.scatter(
        demo_df.query(f"Year=={year}"),
        y="GDP per capita",
        x="Life expectancy",
        color="Continent",
        hover_name="Country",
        size="GDP per capita",
        size_max=20,
        height=650)
else:
    # use plotly.express to create our animated chart object
    chart = px.scatter(
        demo_df,
        x=x_data,
        y=y_data,
        color="Continent",
        hover_name="Country",
        size=balloon_size_data,
        size_max=balloon_size_scale,
        animation_frame="Year",
        animation_group="Country",
        height=650)

# ask streamlit to display chart
st.plotly_chart(chart, use_container_width=True)










    