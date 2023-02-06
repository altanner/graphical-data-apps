# streamlit will create the user interface
import streamlit as st
# pandas will organise my data
import pandas as pd
# plotly will make pretty charts
import plotly.express as px

# use pandas to read my csv file into a dataframe
titanic_dataframe = pd.read_csv("titanic.csv")

column_names = ["name","gender","age","class","embarked","country","ticket no","fare price","siblings aboard","family aboard","survived"]

st.set_page_config(layout="wide")

st.sidebar.image("titanic_image.png")
st.sidebar.header("RMS Titanic")
st.sidebar.write("Data explorer app")
st.info("""##### Titanic Data Explorer
- This app explores data related to the 1912 disaster at sea, where on its maiden voyage the RMS Titanic sank; over 1,500 of the 2,224 people aboard lost their lives.
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
    st.dataframe(titanic_dataframe)

chart = px.violin(
    titanic_dataframe,
    x=st.session_state.x_data,
    y=st.session_state.y_data,
    color="survived")

st.plotly_chart(chart, use_container_width=True)

#chart = px.scatter_matrix(
#    titanic_dataframe,
#    dimensions=column_names,
#    color="survived")

#chart = px.parallel_coordinates(
#    wine_dataframe,
#    dimensions=column_names,
#    #color="class",
#    color_continuous_scale=px.colors.diverging.Tealrose)

#chart = px.violin(
 #   wine_dataframe,
  #  x="quality",
   # y="alcohol",)



    