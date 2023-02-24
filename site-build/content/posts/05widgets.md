---
title: "5 • Widgets and charts"
subtitle: "Creating an interface to control your visualisations."

date: 2023-02-15T00:00:00+01:00

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

## Widgets
The power of data apps is in allowing users to interact with data and visuals. One way that we can do this is by creating "widgets". A [widget](https://docs.streamlit.io/library/api-reference/widgets) is any interactable part of the page, for example buttons, sliders, checkboxes and uploaders. The important difference between widgets and layout components is that **widgets set the values of variables**. We will see the Python syntax for this in a moment.

In the previous section, we created our first chart. This has some basic interactivity built-in, for example it can be zoomed and scaled, and it offers buttons to download PDF versions of the chart we have created. We also saw how the chart itself is built through a series of parameters. So far, we have assigned static values ("hard-coded") the chart parameters, for example we assigned the x-axis data to "HDI index" with the parameter `x="HDI index"`. We can instead assign a variable to this parameter - ie, **we can set the value of a widget to be the parameter of a chart**.

### Improving our chart
You might have noticed that our dataset contains temporal information (what year each row of data refer to). Given we asked Plotly to use the entire dataframe as the data to plot, this resulted in a strange chart where each country has multiple datapoints plotted, one for each year. This is not ideal, but **we can improve the chart using a widget to chose what year to display**.

### First widget
Let's add our first widget. It will communicate to the chart which year to plot. In this case, we need a widget that selects an integer from a limited range of contiguous options. There are [several types of widgets](https://docs.streamlit.io/library/api-reference/widgets) that can do this, but for us, a good solution is a [slider](https://docs.streamlit.io/library/api-reference/widgets/st.slider).

As with all of our widgets for this data app, we are going to put it in the sidebar - so be sure to put code inside the code block starting `with st.sidebar:`. To create our slider, we add:

```Python
year_widget = st.slider(
    label="Year",
    value=2008
    min_value=1998,
    max_value=2018)
```

Notice that, unlike layout `st.` commands, we are assigning the widget to a variable, here called `year_widget`. The slider has four parameters: the label it will display, the initial value to use, and the lowest and highest values. Save the file and check the changes on your app (remember we are putting this in the sidebar!)

### Connecting the widget to the chart
So far, the widget exists, and it creates / updates the variable `year_widget`, but we need to pipe that into the code for the chart. Currently, `px.scatter()` has been told to plot the whole dataset, with the line `data_frame=demo_df`. We are going to change this so that it instead plots just the year selected by the widget. Change the parameter line to `data_frame=demo_df.query(f"Year=={year_widget}")` (and leave the rest of your parameters in place).

Several things are happening here:
1. Given `demo_df` is a dataframe, we can use the method `.query()` to filter it.
2. Inside the `.query()` brackets we are filtering on year with `"Year=={year_widget}"`
3. To insert our variable `year_widget`, we are creating an [f-string](https://realpython.com/python-f-strings/), with the variable name inside our curly brackets.

Save your script, and have a play with the app.

## Exercise 3a: A couple more widgets
You should now have a chart that only plots one year at a time. Let's get some more control over the chart, this time altering the type of axis. Currently, both `x` and `y` axes are linear, the default. For some of this data, a logarithmic scale might be appropriate, so let's add a widget to control that. We are going to add [checkboxes](https://docs.streamlit.io/library/api-reference/widgets/st.checkbox), as we briefly saw in the previous section.

{{< admonition type="question" title="Exercise 3a: Axis scale controls" open=true >}}
In your sidebar code block, and below your year slider widget, add two **checkbox widgets**
1. One with the label `"Logarithmic X-axis"`, assigning its value to a variable called `log_x_widget`
2. Another with the label `"Logarithmic Y-axis"`, assigning its value to a variable called `log_y_widget`
In your parameters for `px.scatter()`, add **two more parameters**:
1. `log_x`, being equal to the value of your widget labelled `"Logarithmic X-axis"` (ie, its variable)
2. `log_y`, being equal to the value of your widget labelled `"Logarithmic Y-axis"`
Don't forget to separate your parameters with commas!
{{< /admonition >}}

{{< admonition type="warning" title="Exercise 3a solutions" open=false >}}
Your sidebar block should now contain:
```Python
log_x_widget = st.checkbox(
    label="Logarithmic X-axis")
log_y_widget = st.checkbox(
    label="Logarithmic Y-axis")
```

Your `px.scatter()` now needs to have parameters related to these widgets, so the full parameters would be:
```Python
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
```
{{< /admonition >}}

Save your script and make sure everything is working in the app. The last widgets we will add allow us to control what data is represented on each axis.

## Completing our widgets
{{< admonition type="tip" title="Clarity is sacred!" open=false >}}
Apps should be easy to use. Visualisations should be easy to interpret. In this course, we are using an ideal dataset to assigning different types of data to different parts of our chart. In the real world, this is rare! You are likely to have data that doesn't make sense to plot, or is confusing, or over-whelms!

Almost always, _less is more_ when it comes to visualisations! So, while in this course we are being fairly maximal with our charting for teaching purposes, we recommend, in the real world, that you think carefully about what to present, and how to present it.
{{< /admonition >}}

Click your "View dataframe" toggle, and notice the names of the columns. There are eight columns, and currently
- **Continent** is represented by colour
- **Country** is reported in mouse-over tooptip
- **CO2** is represented by dot size
- **HDI index** is on the x-axis
- **GDP per capita** is on the y-axis
That leaves three columns that would could integrate into the chart: "Life expectancy", "Services", and "Year". We have already assigned the year to a slider (and in the next section we will make that even nicer!). As for the other two, for the sake of completeness, let's give the user the option of exploring these data too.

To do this, we will create two more widgets, this time [radio buttons](https://docs.streamlit.io/library/api-reference/widgets/st.radio). These are single-option, mutually-exclusive selectors (I think these are called "radio" because old radio buttons you would press, and it would deactivate the previous selection). In your sidebar code, and below your axis checkboxes, add:

```Python
x_data_widget = st.radio(
    label="X-axis data",
    options=column_names)
y_data_widget = st.radio(
    label="Y-axis data",
    options=column_names)
```

Save this... and you will get an error! The parameter `options` is expecting a list, but we gave it an undefined variable. Let's fix this, and connect it up, in this exercise

## Exercise 3b: Options and radio buttons

{{< admonition type="question" title="Exercise 3b: Options and radio buttons" open=true >}}
We already have our widgets ready, but we cannot use them until we tell them what the options are. These will be the names of columns in our dataframe (but not all of them):
1. Immediately above your `x_data_widget` lines (as above), define a list called `column_names`
2. The contents of this list will be five strings, all of them names of columns in the dataframe.
3. Three column names will _not_ be in your list: what are they, and why?
4. Link your widgets to the chart parameters. Currently, the `x` and `y` parameters are hard-coded:
```Python
x="HDI index",
y="GDP per capita",
```
Modify these so they respond to your widgets. Test your app is working.

5. You might notice that on first loading, the chart plots the same data on each axis, producing just a `x=y` straight line. Fix this by adding the parameter `index=1` to the end of your `y_data_widget` parameters. It will select index 1 (the _2nd_!) item from the list `column_names` as what to use on first loading.
{{< /admonition >}}

{{< admonition type="warning" title="Exercise 3b solution" open=false >}}
At this point, your whole script should look similar to this:
```Python
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

# build px chart object
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

# display the chart in tab2
with tab2:
    st.plotly_chart(chart, use_container_width=True)

### end of main page area
```
{{< /admonition >}}
