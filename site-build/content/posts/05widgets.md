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
Let's add our first widget. It will greet the user! We will need two things to do this - firstly, we want the user to be able to enter their name. Secondly, we will send that to the interface - we will use the empty element `column2` that we created earlier.

Firstly, we are going to use [`st.text_input()`](https://docs.streamlit.io/library/api-reference/widgets) widget, and place it below the title in the sidebar 

```Python
with st.sidebar:
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

Save your script and check your app is working. Your first interactive widget-display-pair! Learning how to use widgets to set variables, and layout elements to display them, is a core skill in data app development.

## Widgets and visuals
In the previous page we created a chart. This has some basic interactivity built-in, for example it can be zoomed and scaled, and it offers buttons to download PDFs of the chart we have created. We also saw how the chart itself is built through a series of parameters. So far, we manually assigned values ("hard-coded") to the chart parameters, for example we assigned the x-axis data to the "HDI index" column of the dataframe, with the parameter `x="HDI index"`. We can instead assign a variable to this parameter - ie, **we can set the value of a widget to be the parameter of a chart**.

You might have noticed that our dataset contains year information. We asked Plotly to use the entire dataframe as the data to plot, and this resulted in a strange chart where each country has multiple datapoints plotted, one for each year. We are going to fix this, by setting a widget to control which year the chart will display.

### A widget to control the chart
Years are integers, and our data spans 1998 to 2018. So, we need a widget to select any of those integers. A perfect widget for this is a [slider](https://docs.streamlit.io/library/api-reference/widgets).

As with all of our widgets for this data app, we are going to put it in the sidebar - so be sure to put widget-assignment code *inside* the block starting `with st.sidebar:`. To create our slider, we add:

```Python
year_widget = st.slider(
    label="Year to chart",
    min_value=1998,
    max_value=2018)
```

Compared to the text input widget we used above, this one has three parameters: the descriptive label it will display, and the lowest and highest values. Like with the chart parameters, clarity is aided by putting each parameter on a new line. Save the file and check the changes on your app.

### Connecting the widget to the chart
So far, the widget exists, and it stores a number in the variable `year_widget`, but it doesn't do anything. Currently, `px.scatter()` has been told to plot the whole dataset, with the parameter `data_frame = demo_df`. `demo_df` is a dataframe, so we can isolate the data we want by column value: `<the dataframe column> is equal to <a number>`, in this case with with `demo_df["Year"] == 2008`

We'll start by hard-coding this. Change your first parameter line in the chart, so it looks like:
```Python
chart = px.scatter(
    data_frame = demo_df[demo_df["Year"] == 2008],
    x = "HDI index",
    y = "GDP per capita",
    color = "Continent",
    size = "CO2 per capita",
    hover_name = "Country")
```

Save, and see what the chart has done in your app. Try changing `2008` to another number, between 1998 and 2018, save and notice the changes. Now, to make this interactive, we need to link the widget value to the chart parameters. We do this by replacing our hard-coded number with the appropriate variable, in this case `year_widget`:

```Python
chart = px.scatter(
    data_frame = demo_df[demo_df["Year"] == year_widget],
    x = "HDI index",
    y = "GDP per capita",
    color = "Continent",
    size = "CO2 per capita",
    hover_name = "Country")
```
Save your script, and have a play with the app.

## Exercise 5: A couple more widgets
You now have a chart that displays one year at a time. Let's get some more control over the chart, this time altering the type of axis. Currently, both `x` and `y` axes are linear, the default. For some of this data, a logarithmic scale might be appropriate, so let's add a widget to control that. We are going to add a [checkbox](https://docs.streamlit.io/library/api-reference/widgets). Checkboxes are booleans: the value they contain can either be `True` or `False`, which we will use as a toggle here.

{{< admonition type="question" title="Exercise 5: Axis scale controls" open=true >}}
In your sidebar code block, and below your year slider widget, add a `st.checkbox()`:
- Make the label read "Logarithmic Y-axis"
- Assigning the value of your checkbox to a variable called `log_y_widget`
In your parameters for `px.scatter()`, add a new parameter:
- `log_y`, being equal to the value of your widget labelled "Logarithmic Y-axis" (ie, the variable `log_y_widget`)
Don't forget to separate your parameters with commas!
{{< /admonition >}}

{{< admonition type="warning" title="Exercise 5 solutions" open=false >}}
Your script should look similar to this
```Python
import streamlit as st
import pandas as pd
import plotly.express as px

# use pandas to read our CSV file into a dataframe called "demo_df"
demo_df = pd.read_csv("demo_dataset.csv")

# put a title in the sidebar
with st.sidebar:
    st.title("World Demographics")
    user_name = st.text_input("Welcome - please enter your name.")
    year_widget = st.slider(
        label = "Year to chart",
        min_value = 1998,
        max_value = 2018)
    log_y_widget = st.checkbox(
        label = "Logarithmic Y-axis")
    
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
chart = px.scatter(
    data_frame = demo_df[demo_df["Year"] == year_widget],
    x = "HDI index",
    y = "GDP per capita",
    log_y = log_y_widget,
    color = "Continent",
    size = "CO2 per capita",
    hover_name = "Country")

# display the chart in tab2
with tab2:
    st.plotly_chart(chart)
```
{{< /admonition >}}

Save your script and make sure everything is working in the app. The last widgets we will add allow us to control what data is represented on each axis.

## Completing our widgets
Let's look at the raw data again, in tab1, and notice the names of the columns. There are eight columns, and currently six are integrated with our chart
- **Continent** is represented by colour
- **Country** is reported in mouse-over tooptip
- **Year** is controlled with our slider
- **CO2** is represented by dot size
- **HDI index** is on the x-axis
- **GDP per capita** is on the y-axis
but
- **Life expectancy** and
- **Services** are not used yet.

To do this, we will create two more widgets, this time [radio buttons](https://docs.streamlit.io/library/api-reference/widgets/st.radio). These are single-option, mutually-exclusive selectors (I think these are called "radio" because old radio buttons you would press to select a station, and it would deactivate the previous selection). In your sidebar code, and below your axis checkboxes, add:

```Python
x_data_widget = st.radio(
    label = "X-axis data",
    options = column_names)
y_data_widget = st.radio(
    label = "Y-axis data",
    options = column_names)
```

Save this... and you will get an error! The parameter `options` is expecting a list, but we gave it an undefined variable. Let's fix this, and connect it up, in this exercise.

## Exercise 6: Options and radio buttons

{{< admonition type="question" title="Exercise 6: Options and radio buttons" open=true >}}
The argument `options` is expecting a list. This will be the names of columns in our dataframe (but not all of them):
1. Above your sidebar block, define a list called `column_names`.
2. Set the contents of this list to be **five** strings: `"HDI index", "GDP per capita", "Life expectancy", "CO2 per capita", "Services"` 
3. Save your file, and check that the error in the app has been resolved.
4. Link your radio widgets to the chart parameters. Currently, the `x` and `y` parameters are hard-coded:
```Python
x = "HDI index",
y = "GDP per capita",
```
Modify `x` and `y` parameters so they respond to your widgets. Test your app is working.
{{< /admonition >}}

{{< admonition type="warning" title="Exercise 6 solution" open=false >}}
At this point, your whole script should look similar to this:
```Python
import streamlit as st
import pandas as pd
import plotly.express as px

# use pandas to read our CSV file into a dataframe called "demo_df"
demo_df = pd.read_csv("demo_dataset.csv")

# make a list of column names, to be passed to radio widgets
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
    year_widget = st.slider(
        label = "Year to chart",
        min_value = 1998,
        max_value = 2018)
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
chart = px.scatter(
    data_frame = demo_df[demo_df["Year"] == year_widget],
    x = x_data_widget,
    y = y_data_widget,
    log_y = log_y_widget,
    color = "Continent",
    size = "CO2 per capita",
    hover_name = "Country")

# display the chart in tab2
with tab2:
    st.plotly_chart(chart)
```
{{< /admonition >}}

## Next steps
If you have got to this point, congratulations, you have the basics of building a data app! The three topics we have covered (**layout**, **charts** and **widgets**) will get you a long way, so we encourage you to apply what you have learned to other elements available in the [Streamlit API](https://docs.streamlit.io/library/api-reference).

We provide some further content on the next pages. Firstly we give some pointers on how to deploy your app - but you will need to be registered with [GitHub](https://github.com/) to do this.

After that, we introduce further topics through making an animated chart. This includes some more advanced concepts, for example widgets controlling widgets, and conditional charting - but don't be daunted by this, if you have got this far you have the skills to approach these!

Finally, while we do not cover these in this course, we provide resources for further topics - for example building user logins, saving your data app's session state, and working with interactive dataframes.
