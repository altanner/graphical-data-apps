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
    
    # visualisation type checkbox
    animate_vis = st.checkbox(
        label="Animate")
    
    year_widget = st.slider(
        label="Year",
        value=2008,
        min_value=1998,
        max_value=2018,
        disabled=animate_vis)
    
    log_x_widget = st.checkbox(
        label="Logarithmic X-axis")

    log_y_widget = st.checkbox(
        label="Logarithmic Y-axis")
    
    # a list of options for axis data selectors
    column_names = [
        "HDI index",
        "GDP per capita",
        "Life expectancy",
        "CO2 per capita",
        "Services"]
    # x and y selector widgets
    x_data_widget = st.radio(
        label="X-axis data",
        options=column_names)
    y_data_widget = st.radio(
        label="Y-axis data",
        options=column_names,
        index=1)

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

if animate_vis == False:
    # build static px chart object
    chart = px.scatter(
        data_frame=demo_df.query(f"Year=={year_widget}"),
        x=x_data_widget,
        y=y_data_widget,
        log_x=log_x_widget,
        log_y=log_y_widget,
        color="Continent",
        size="CO2 per capita",
        hover_name="Country",
        height=650)
if animate_vis == True:
    # build animated px chart object
    chart = px.scatter(
        data_frame=demo_df,
        x=x_data_widget,
        y=y_data_widget,
        log_x=log_x_widget,
        log_y=log_y_widget,
        color="Continent",
        size="CO2 per capita",
        hover_name="Country",
        height=650,
        animation_frame="Year",
        animation_group="Country",)

# display the chart in tab2
with tab2:
    st.plotly_chart(chart, use_container_width=True)

### end of main page area