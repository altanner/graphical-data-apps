---
title: "4 • Getting started with charts"
subtitle: "How to control your graphing library."

date: 2023-02-14T00:00:00+01:00

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

{{< admonition type="tip" title="Plots, graphs or charts?" open=false >}}
The words **plot**, **chart** and **graph** are used interchangeably, but I will stick with **chart** in this course. The reason I prefer this term is because it feels more general: for example we could be making a map, and the word "graph" would not make sense. Also, the word "plot" is kind of reserved for some things in Python, and is in use by many graphic libraries.

*As always, beware what you name your files! For example, if you name a file something reasonable like `plotly.py`, it will conflict with instructions such as `import plotly`!*
{{< /admonition >}}

At the end of the last section, our running Python file creates a page, we added some layout components. In this section, we will be bringing data into the app, and creating our first visualisation.

## Bringing our data into the script
We will be using `pandas` to read our CSV file in. While we do not use `pandas` any further in this course, keep in mind that Streamlit is very much built with `pandas` in mind: data workflows and visualisations will usually expect to be working with dataframes.

### Loading up `pandas`
Firstly, we need to update our `import`s to include everything we need for the rest of this course. We will add both `pandas` and `plotly.express`, so we will have three `import`s in total, at the top of our script, with their conventional aliases, `st`, `pd` and `px` respectively:
```Python
import streamlit as st
import pandas as pd
import plotly.express as px
```
Now that we have `pandas` ready for use, we can read our dataset into a dataframe. We are using the dataset provided in the course materials, `demo_dataset.csv`, which will need to be in your working folder. Add this line **at the top of your script, below your `import`s**. The reason we put it near the top is because this code is not related to building the interface, so it is logical to place it before the page-build code.
```Python
demo_df = pd.read_csv("demo_dataset.csv")
```
### Viewing our data
Before we go any further, let's examine what is inside our dataframe. We can do this natively in Streamlit. Building on your script at the **end** of the script, add this to the end:
```Python
with tab1:
    st.dataframe(demo_df)
```
Save the file, and check what your app is showing. We can now see what we are working with - note that this dataframe is interactive, so it can be ordered and selected, but we will not be covering interactive dataframes today. For this course, we will leave `tab1` ("Data") as a quick way of checking what the data looks like, and `tab2` ("Visualisation") will be for our chart.

## Creating a chart
Now that we have our data available, we can begin work on visualising it. As mentioned, we are using [Plotly](https://plotly.com/python/), for a number of reasons:
- it has an intermediate learning curve
- the [documentation](https://plotly.com/python-api-reference/) is good
- the syntax is easy to use, without being over-simplified
- the graphs it creates are good-looking, customisable and interactive.

There are two steps to getting our data from the dataframe to into a graphic:
1. Creating a chart object
2. Asking Streamlit to present this chart object

### A basic scatter plot
Plotly works on dataframes, which we have ready for it. We will build up to a more sophisticated visualisation later, but as an absolute minimum, a Plotly scatter chart needs three things: 
1. The datafame Plotly is working with
2. The data to plot on the `x` axis (ie, one of the dataframe columns)
3. The data to plot on the `y` axis (another dataframe column)

For points [2] and [3], we need to choose two columns to plot. Set your dataframe to be displayed (using the checkbox we made earlier). Let's choose the columns `CO2 per capita` as our `x`, and `GDP per capita` as our `y`.
We create our chart object like this:
```Python
chart = px.scatter(
    data_frame=demo_df,
    x="CO2 per capita",
    y="GDP per capita")
```
Note that my indentation here is just to avoid a long, confusing line of code; anything inside brackets and separated by commas can be laid out in this way, and you will see later that our chart object can have lots of arguments, so it is good practice to keep this tidy!

OK, so we have built the `chart` object - now we ask Streamlit to show it to us by handing it to `st.plotly_chart()`. We will also put this into our second tab. Add this at the bottom of your script:
```Python
with tab2:
    st.plotly_chart(chart)
```
Save your file, and explore the visual! Investigate what the icons at the top right of your chart do. Double-clicking the chart resets, if you get lost, or click the "rescale" button (it is visible when you mouse over the chart, in the top right).

Before we move on, let's make better use of the space we have, by adding an argument to `st.plotly_chart(chart)`:
```Python
with tab2:
    st.plotly_chart(chart, use_container_width=True)
```
This is a useful argument to use, especially if you have a more complex layout with columns and containers.

### Customising our chart
This is a good start, but Plotly can do much better than this! Given there is more information in our dataframe, we use this to convey more. Let's colour our dots, using the Continent as our colouring key. This is done by adding to the arguments building our chart object:
```Python
chart = px.scatter(
    data_frame=demo_df,
    x="CO2 per capita",
    y="GDP per capita",
    color="Continent")
```
(Note that the `color` argument is spelled in International English!) Save, and notice the changes.

Currently, there is an issue with our chart which is making it unclear. Because we are handing the entire dataframe to `px.scatter` XXXXXXX

## Exercise: building a better visualisation
{{< admonition type="question" title="Exercise 2: better visuals" open=true >}}
So far, we have a chart which expresses three things: the CO2, GDP and continent of the countries in our dataset. In this exercise, we are adding arguments to `px.scatter()`, to include further data. (Here, when we say "assign", it means to use the equals sign to "put something into" a variable; for example `dog = "fido"` is assigning the string `"fido"` to a variable called `dog`.)
1. We can control the size of points. Add a parameter called `size`, and assign the column name `"Services"` to it (note that any dataframe column name is a string).
2. Our mouse-over is not very useful right now. Add a parameter called `hover_name`, and assign `"Country"` to it.
3. The chart can use the vertical space a bit better. Add a parameter called `height`, and give an integer value to this in pixels (choose a height suitable for your screen; for me, `height=650` fits best, but for you it might be different).
{{< /admonition >}}

{{< admonition type="warning" title="Exercise 2 solution" open=false >}}
Your Streamlit script should look similar to this:
```Python
import streamlit as st
import pandas as pd
import plotly.express as px

# use pandas to read CSV file into a dataframe
demo_df = pd.read_csv("demo_dataset.csv")

# set the tab title and page width
st.set_page_config(page_title="Demo App", layout="wide")

# build the sidebar
with st.sidebar:
    # put a title in the sidebar
    st.title("World Demographics")

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
    data_frame=demo_df,
    x="HDI index",
    y="GDP per capita",
    color="Continent",
    size="CO2 per capita",
    hover_name="Country",
    height=650)

# display the chart in tab2
with tab2:
    st.plotly_chart(chart, use_container_width=True)
```
{{< /admonition >}}
