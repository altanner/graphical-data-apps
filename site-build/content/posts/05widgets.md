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
The power of data apps is in allowing users to interact with data and visuals. One way that we can do this is by creating "widgets". A [widget] (https://docs.streamlit.io/library/api-reference/widgets) is any interactable part of the page, for example buttons, sliders, checkboxes and uploaders. The import difference between widgets and layout components (that we learned in [section 3](https://alleetanner.github.io/graphical-data-apps/posts/03layout/) is that **widgets set the values of variables**. We will see the Python syntax for this in a moment.

In the previous section, we created our first chart. This has some basic interactivity built-in, for example it can be zoomed and scaled, and it offers buttons to download PDF versions of the chart we have created. We also saw how the chart itself is built through a series of parameters. So far, we have assigned static values ("hard-coded") the chart parameters, for example we assigned the x-axis data to "Life expectancy" with the parameter `x="Life expectancy"`. We can instead assign a variable to this parameter - ie, **we can set the value of a widget to be the parameter of a chart**.

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

### A couple more widgets
You should now have a chart that only plots one year at a time. Let's get some more control over the chart, this time altering the type of axis. Currently, both `x` and `y` axes are linear, the default. 
1. year slider
2. radio buttons
3. 
At the end of the last section, you should have your Python script looking a little like this:
```Python
import streamlit as st

st.set_page_config(
    page_title="A Demographics Data App",
    layout="wide")

# use pandas to read csv file into a dataframe
demographics_df = pd.read_csv("demo_dataset.csv")

# create the sidebar
with st.sidebar:
    st.image("globe.png")
    st.header("Demographic Data")
    st.info("Welcome to the global demographic explorer data app.")

# create the information box at the top of the page
with st.expander(label="World Demographics Data Explorer: click for instructions"):
    st.info("""World Demographics Data Explorer
    - This app explores information about social, economic and environmental development at local, national and global levels.
    - Please use the options in the sidebar to explore the dataset.
    - Draw a box to zoom on the chart. Return to normal zoom with a double-click, or click the "autoscale" button.""")
```

## Plotly Express
There are a few popular graphing libraries in Python - for example `matplotlib`, `seaborn`, `ggplot`. We are going to use `plotly`, because it has an intermediate learning curve - the syntax is relatively accessible, the documentation is good, and the graphs it creates are very powerful. `plotly` comes with a simplified interface called `plotly.express`, which we will use.

To bring `plotly` functionality into our script we need to import it. While we are writing some imports, we also need `pandas` ready for action, so let's bring that into our script too. So, we will now have three imports at the top of our script:
```Python
import streamlit as st
import plotly.express as px
import pandas as pd
```
`px` is the conventional alias for `plotly.express`, and `pd` is the shortened name of `pandas`.


### Section title
* bullet1
* bullt2

Normal text body.

{{< admonition type="warning" open=true >}}
- Warning1
- Warning2
{{< /admonition >}}
{{< admonition type="info" open=true >}}
- Info1
- Info2
{{< /admonition >}}

### Another section
blahfdajkfhu aefuibahj rwefyugr

```
code goes herer
```
next setion blakfahuir wrafguighbarg

### Exercise
{{< admonition type="question" title="Questions" open=true >}}
a question box
- q1
- q2
{{< /admonition >}}
