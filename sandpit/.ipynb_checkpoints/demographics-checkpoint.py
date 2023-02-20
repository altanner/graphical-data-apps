import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="A Demographics Data App",
    layout="wide")

# use pandas to read csv file into a dataframe
demographics_df = pd.read_csv("demo_dataset.csv")
#demographics_df = pd.read_csv("demo2.csv")

#demo2 = pd.read_csv("demo3.csv")


# for my csv
column_names = ["Life expectancy","HDI index","CO2 per capita","GDP per capita"]

#column_names = ["Country", "Continent", "Year", "Life expectancy", "Population", "GDP per capita"]

with st.sidebar:
    st.image("globe.png")
    st.header("Demographic Data")
    st.info("Welcome to the global demographic explorer data app.")
    st.checkbox(
        label="Show data preview",
        help="If selected, display the data that is being used.")
    year = st.slider(
        label="Year",
        min_value=1998,
        max_value=2018,
        value=2008)
    x_data = st.radio(
        label="X-axis data",
        options=column_names)
    y_data = st.radio(
        label="Y-axis data",
        options=column_names,
        index=1)
    size_data = st.radio(
        label="Size data",
        options=["CO2 per capita", "GDP per capita"])
    size_scale = st.slider(
        label="Size scale",
        min_value=10,
        max_value=90,
        value=30)

    
with st.expander(label="World Demographics Data Explorer: click for instructions"):
    st.info("""World Demographics Data Explorer
    - This app explores information about social, economic and environmental development at local, national and global levels.
    - Please use the options in the sidebar to explore the dataset.
    - Draw a box to zoom on the chart. Return to normal zoom with a double-click.""")

#chart_1 = px.scatter(
##    demographics_df.query(f"Year=={year}"),
#    y="GDP per capita",
##    x="Life expectancy",
#    size="Population",
#    size_max=60,
#    color="Continent",
#    hover_name="Country",
#    log_y=True)


#chart_1 = px.scatter(
#    demographics_df,
#    x=x_data,
#    y=y_data,
#    animation_frame="Year",
#    animation_group="Country",
#    size="Population",
#    color="Continent",
#    hover_name="Country",
#    log_x=True,
#    log_y=True,
#    size_max=64,
#    range_x=[100,100000],
#    range_y=[25,90])

chart_2 = px.scatter(
    demographics_df,
    x=x_data,
    y=y_data,
    size=size_data,
    size_max=size_scale,
    color="Continent",
    animation_frame="Year",
    animation_group="Country",
    hover_name="Country",
    height=700)





#st.plotly_chart(chart_1, use_container_width=True)
st.plotly_chart(chart_2, use_container_width=True)



#chart = px.scatter(
#    demographics_df,
#    x=x_data,
#    y=y_data,
#    animation_frame="Year",
#    animation_group="Country",
#    size="Population",
#    color="Continent",
#    hover_name="Country",
#    log_x=True,
#    log_y=True,
#    size_max=64,
#    range_x=[100,100000],
#    range_y=[25,90])


#chart = px.scatter(
#    demographics_df,
#    x=st.session_state.x_data,
#    y=st.session_state.y_data,
#    color="continent",
#    marginal_y="violin",
#    marginal_x="box",
#    trendline="ols",
#    template="simple_white")


#chart = px.scatter_matrix(
#    demographics_df,
#    dimensions=column_names,
#    color="continent")






    