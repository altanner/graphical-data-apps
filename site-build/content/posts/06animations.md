---
title: "6 • Animations"
subtitle: "Motion adds an extra dimension!"

date: 2023-02-16T00:00:00+01:00

fontawesome: true
linkToMarkdown: true

toc:
  enable: true
  keepStatic: false
  auto: false
code:
  copy: true
math:
  enable: true
share:
  enable: false
comment:
  enable: false
---

In this extra section, we will introduce animations. Many of the graphics libraries include the ability to animate visuals, but always think carefully about whether this actually adds anything to your app. Some animations can also get quite technical to run nicely, but Plotly makes it relatively easy, especially with `px.scatter()`.

## Preparing our interface
To start we are going to add a simple toggle checkbox, as we did earlier, controlling if animation is enabled or not. As your first widget (ie, in your sidebar, just below your title, but above your "Year" slider) add this:
```Python
animate_vis = st.checkbox(
    label="Animate")
```
Remember to keep your indentation correct for the sidebar block. Save the file and confirm the checkbox is in the right place. We will connect this to the chart in just a moment! We are going to be animating on the "Year" column. As such, when "Animate" is selected, asking for the "Year" again is redundant.

### A widget controlling a widget!
We can solve this by making the "Animate" checkbox *also* control the "Year" slider. "Animate" is a checkbox, therefore it can take two values of `False` or `True`; this is also the value of `animate_vis`. We can pass that boolean variable to another widget, in this case the "Year" slider. We want "Year" to be disabled when "Animate" is enabled. We do this by adding `disabled=animate_vis` to the slider parameters:
```Python
year_widget = st.slider(
    label = "Year",
    value = 2008,
    min_value = 1998,
    max_value = 2018,
    disabled = animate_vis)
```
Save and check behaviour in our app. The checkbox and the year slider should now be mutually exclusive! Now that we have working widgets, we can actually create the animation.

## Conditional charting
We can tell the app if we want an animation, and it needs to respond to that. To do this, we will use a good old conditional. In this case, we are checking if "Animate" is selected or not. If this is `False` we just present a static chart (the one we have made already). If it is `True`, we build an animated chart.

So, the first block of our conditional is just what we have written already:
```Python
if animate_vis == False:
    chart = px.scatter(
        data_frame = demo_df[demo_df["Year"] == year_widget],
        x = x_data_widget,
        y = y_data_widget,
        log_x = log_x_widget,
        log_y = log_y_widget,
        color = "Continent",
        size = "CO2 per capita",
        hover_name = "Country",
        height = 650)
```
For the subsequent `else` block we need an alternate `px.scatter()`, which is very similar to what we are using already:
```Python
if animate_vis == True:
    chart = px.scatter(
        data_frame = demo_df,
        x = x_data_widget,
        y = y_data_widget,
        log_x = log_x_widget,
        log_y = log_y_widget,
        color = "Continent",
        size = "CO2 per capita",
        hover_name = "Country",
        height = 650,
        animation_frame = "Year",
        animation_group = "Country",)
```
There are **three** differences here. 

1. we no longer need to fiter the dataframe by year (notice the first parameter)
2. we need a parameter of `animation_frame`
3. we need a parameter of `animation_group`

The lines to draw the chart remains the same:
```Python
with tab2:
    st.plotly_chart(chart)
```

So, with both results of both conditionals in place, we are ready to test it - save the file, and check how things look in the app!

At this point, your whole script should look similar to this:
```Python
import streamlit as st
import pandas as pd
import plotly.express as px

# use pandas to read our CSV file into a dataframe called "demo_df"
demo_df = pd.read_csv("demo_dataset.csv")

# create a list for the radio buttons to select from
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
    st.info("Welcome to the global demographic data explorer app.")
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
        hover_name = "Country",
        height = 650)
if animate_widget == True:
    chart = px.scatter(
        data_frame = demo_df,
        x = x_data_widget,
        y = y_data_widget,
        log_y = log_y_widget,
        color = "Continent",
        size = "CO2 per capita",
        hover_name = "Country",
        height = 650,
        animation_frame = "Year",
        animation_group = "Country",)

# display the chart in tab2
with tab2:
    st.plotly_chart(chart)
```
