---
title: "5 • Widgets and charts"
subtitle: "Linking up your interface with your charts."

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

### Fixing our chart years
You might have noticed that our dataset contains temporal information (what year the data refer to). Given we asked Plotly to use the entire dataframe as the data to plot, and this resulted in a strange chart where each country has multiple datapoints plotted, one for each year. This is not ideal, but **we can improve the chart using a widget to chose what year to display**.

Let's add our first widget. The aim is to select a year. So, we need something that can select an integer. There are [several types of widgets](https://docs.streamlit.io/library/api-reference/widgets) that can do this, but for us, a good solution is a [slider](https://docs.streamlit.io/library/api-reference/widgets/st.slider).


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
