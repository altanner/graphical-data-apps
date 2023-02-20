# streamlit will create the user interface
import streamlit as st
# pandas will organise my data
import pandas as pd
# plotly will make pretty charts
import plotly.express as px

# use pandas to read my csv file into a dataframe
#demographics_df = pd.read_csv("demographics.csv")
demographics_df = px.data.gapminder()

# for my csv
#column_names = ["country","continent","year","life_exp","hdi_index","co2_consump","gdp","services"]
# for px.data.gapminder
column_names = ["country", "continent", "year", "lifeExp", "pop", "gdpPercap", "iso_alpha", "iso_num"]

st.set_page_config(layout="wide")

st.sidebar.image("globe.png")
st.sidebar.header("Demographic Data")
st.sidebar.write("Data explorer app")
with st.expander(label="World Demographics Data Explorer: click for instructions"):
    st.info("""##### World Demographics Data Explorer
    - This app explores information about social, economic and environmental development at local, national and global levels.
    - Please use the options in the sidebar to explore the dataset.
    - Draw a box to zoom on the chart. Return to normal zoom with a double-click.""")

st.sidebar.checkbox(
    label="Show data preview",
    help="If selected, display the data that is being used.",
    key="data_preview")

st.sidebar.radio(
    label="X-axis data",
    options=column_names,
    key="x_data")

st.sidebar.radio(
    label="Y-axis data",
    options=column_names,
    key="y_data") 

if st.session_state.data_preview == True:
    st.dataframe(demographics_df)

#chart = px.scatter(
#    demographics_df,
#    x=st.session_state.x_data,
#    y=st.session_state.y_data,
#    color="continent")


chart = px.scatter(
    demographics_df,
    x=st.session_state.x_data,
    y=st.session_state.y_data,
    animation_frame="year",
    animation_group="country",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=55,
    range_x=[100,100000],
    range_y=[25,90])


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

st.plotly_chart(chart, use_container_width=True)



#chart = px.parallel_coordinates(
#    wine_dataframe,
#    dimensions=column_names,
#    #color="class",
#    color_continuous_scale=px.colors.diverging.Tealrose)

#chart = px.violin(
 #   wine_dataframe,
  #  x="quality",
   # y="alcohol",)



    