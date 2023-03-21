---
title: "5 • Widgets"
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
The power of data apps is in allowing users to interact with data and visuals. We do this by creating "widgets". A [widget](https://docs.streamlit.io/library/api-reference/widgets) is any interactable part of the page, for example buttons, sliders, checkboxes and uploaders. An important difference between widgets and layout components is that **widgets set the values of variables**. We will see the Python syntax for this in a moment.

### First widget
Let's add our first widget. It will greet the user! We will need two things to do this - firstly, we want the user to be able to enter their name. Then, we send the name back to the interface - we will use the empty `column2` that we created earlier.

Firstly, we are going to use [`st.text_input()`](https://docs.streamlit.io/library/api-reference/widgets) widget, and place it below the title in the sidebar 

```Python
with sidebar:
    st.title("World Demographics")
    user_name = st.text_input("Welcome - please enter your name.")
```

Note that we are assigning the widget to a variable name, here called `user_name`. Like any variable, we can pass this around. Here, we will pass it to an [`f`string](https://realpython.com/python-f-strings/), in the code block for `column2`. We will use `st.info()` again, since it makes it clear where our column is. A a sensible place to put this line is below your code for `column1`:

```Python
with column1:
    st.info("Welcome to the global demographic data explorer app!")
with column2:
    st.info(f"Hi {user_name}!")
```

Save your script and check your app is working. Your first interactive widget-display pair! Learning how to use widgets to set variables, and layout elements to display them, is a core skill in data app development.

## Widgets and visuals
In the previous page we created a chart. This has some basic interactivity built-in, for example it can be zoomed and scaled, and it offers buttons to download PDFs of the chart we have created. We also saw how the chart itself is built through a series of parameters. So far, we manually assigned values ("hard-coded") to the chart parameters, for example we assigned the x-axis data to the "HDI index" column of the dataframe, with the parameter `x="HDI index"`. We can instead assign a variable to this parameter - ie, **we can set the value of a widget to be the parameter of a chart**.

You might have noticed that our dataset contains year information. We asked Plotly to use the entire dataframe as the data to plot, and this resulted in a strange chart where each country has multiple datapoints plotted, one for each year. We are going to fix this, by setting a widget to control which year the chart will display.

### A widget to control the chart
Years are integers, and our data spans 1998 to 2018. So, we need a widget to be able to select any of those integers. A perfect widget for this is a [slider](https://docs.streamlit.io/library/api-reference/widgets).

As with all of our widgets for this data app, we are going to put it in the sidebar - so be sure to put widget-assignment code *inside* the block starting `with st.sidebar:`. To create our slider, we add:

```Python
    year_widget = st.slider(
        label="Year",
        value=2008
        min_value=1998,
        max_value=2018)
```

Compared to the text input widget we used above, this one has four parameters: the label it will display, the initial value to use, and the lowest and highest values. Like with the chart parameters, clarity is aided by putting each parameter on a new line. Save the file and check the changes on your app.

### Connecting the widget to the chart
So far, the widget exists, and it creates the variable `year_widget`, but we need to send that into the code for the chart. Currently, `px.scatter()` has been told to plot the whole dataset, with the parameter `data_frame=demo_df`. We are going to change this so that it instead plots just the year selected by the widget. XXXXX can this be simpler? Change the parameter line chart to say `data_frame = demo_df.query(f"Year == {year_widget}")`, so the full parameter set for the chart will be:

```Python
chart = px.scatter(
    data_frame = demo_df.query(f"Year == {year_widget}")`,
    x = "HDI index",
    y = "GDP per capita",
    color = "Continent",
    size = "CO2 per capita",
    hover_name = "Country",
    height = 650)
```

Several things are happening here:
1. Given `demo_df` is a dataframe, we can use the method `.query()` to filter it.
2. Inside the `.query()` brackets we are filtering on year with `"Year == {year_widget}"`
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
    label = "Logarithmic X-axis")
log_y_widget = st.checkbox(
    label = "Logarithmic Y-axis")
```

Your `px.scatter()` now needs to have parameters related to these widgets, so the full parameters would be:
```Python
chart = px.scatter(
    data_frame = demo_df.query(f"Year == {year_widget}"),
    x = "HDI index",
    y = "GDP per capita",
    log_x = log_x_widget,
    log_y = log_y_widget,
    color = "Continent",
    size = "CO2 per capita",
    hover_name = "Country",
    height = 650)
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
    label = "X-axis data",
    options = column_names)
y_data_widget = st.radio(
    label = "Y-axis data",
    options = column_names)
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
x = "HDI index",
y = "GDP per capita",
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
        label = "Year",
        value = 2008,
        min_value = 1998,
        max_value = 2018)
    
    log_x_widget = st.checkbox(
        label = "Logarithmic X-axis")

    log_y_widget = st.checkbox(
        label = "Logarithmic Y-axis")
    
    # a list of options for axis data selectors
    column_names = [
        "HDI index",
        "GDP per capita",
        "Life expectancy",
        "CO2 per capita",
        "Services"]
    # x and y selector widgets
    x_data_widget = st.radio(
        label = "X-axis data",
        options = column_names)
    y_data_widget = st.radio(
        label = "Y-axis data",
        options = column_names,
        index = 1)

    ### end of sidebar
    
### draw main page area
# create two columns, of ratio 5:1
column1, column2 = st.columns([5,1])

# place info box in column1
with column1:
    st.info("Welcome to the global demographic data explorer app!")

# place welcome message into column2
with column2:
    st.info(f"Hi {user_name}!")

# create two tabs
tab1, tab2 = st.tabs(["Data", "Visualisation"])

# display the dataframe in tab1
with tab1:
    st.dataframe(demo_df)

# build px chart object
chart = px.scatter(
    data_frame = demo_df.query(f"Year == {year_widget}"),
    x = x_data_widget,
    y = y_data_widget,
    log_x = log_x_widget,
    log_y = log_y_widget,
    color = "Continent",
    size = "CO2 per capita",
    hover_name = "Country",
    height = 650)

# display the chart in tab2
with tab2:
    st.plotly_chart(chart, use_container_width=True)

### end of main page area
```
{{< /admonition >}}
