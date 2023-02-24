import streamlit as st
import pandas as pd
import plotly.express as px

# use pandas to read CSV file into a dataframe
demo_df = pd.read_csv("demo_dataset.csv")

# set the tab title and page width
st.set_page_config(page_title="Demo App", layout="wide")


### build the sidebar
with st.sidebar:
    
    # put a title in the sidebar
    st.title("World Demographics")
    
    year_widget = st.slider(
        label="Year",
        value=2008,
        min_value=1998,
        max_value=2018)
    
    log_x_widget = st.checkbox(
        label="Logarithmic X-axis")

    log_y_widget = st.checkbox(
        label="Logarithmic Y-axis")

    ### end of sidebar
    
### draw main page area
# create two columns, of ratio 5:1
column1, column2 = st.columns([5,1])

# place info box in first column
with column1:
    st.info("Welcome to the global demographic data explorer app!")

# place image into second column
with column2:
    st.image("globe.png")

# create two tabs
tab1, tab2 = st.tabs(["Data", "Visualisation"])    

# display the dataframe in tab1
with tab1:
    st.dataframe(demo_df)

# build px chart object
chart = px.scatter(
    data_frame=demo_df.query(f"Year=={year_widget}"),
    x="HDI index",
    y="GDP per capita",
    log_x=log_x_widget,
    log_y=log_y_widget,
    color="Continent",
    size="CO2 per capita",
    hover_name="Country",
    height=650)

# display the chart in tab2
with tab2:
    st.plotly_chart(chart, use_container_width=True)

### end of main page area