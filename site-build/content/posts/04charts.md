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

At the end of the last section, our running Python file creates a page, lays out a couple of components. In this section, we will be bringing data into the app, and creating our first visualisation.

## Bringing our data into the script
We will be using `pandas` to read our CSV file in. While we do not use `pandas` any further in this course, keep in mind that `streamlit` is very much built with `pandas` in mind. Most of Streamlit data workflows and visualisations will expect to be working with dataframes, and this is the case now too.

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
st.dataframe(demo_df)
```
Save the file, and have a look at the browser tab displaying your app. We can now see what we are working with - note that this dataframe is interactive, so it can be ordered and selected, but we will not be covering interactive dataframes today.

We don't want to see this all the time, so we are going to add a checkbox to control this. (We cover [widgets](ZXXXX) in more depth in the next section, but right now we want to add a toggle.) Go to your code block starting `with st.sidebar:`, and inside this block (ie, indented) add
```Python
df_view = st.checkbox(label="View dataframe")
```
Here we are assigning the state of the checkbox to a variable called `df_view`. In Streamlit, a checkbox is a boolean, so it can only be `True` or `False`. We will use this value to trigger if Streamlit shows us the dataframe, by putting our `st.dataframe(demo_df)` into a conditional block. Find your line `st.dataframe(demo_df)`, and pop it into a conditional block:
```Python
if df_view == True:
    st.dataframe(demo_df)
```
Save this, and give it a test in the browser window.

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

For points [2] and [3], we need to choose two columns to plot. Set your dataframe to be displayed (using the checkbox we made earlier). Let's choose the columns `Life expectancy` as our `x`, and `GDP per capita` as our `y`.
We create our chart object like this:
```Python
chart = px.scatter(
    data_frame=demo_df,
    x="Life expectancy",
    y="GDP per capita")
```
Note that my indentation here is just to avoid a long, confusing line of code; anything inside brackets and separated by commas can be laid out in this way, and you will see later that our chart object can have lots of arguments, so it is good practice to keep this tidy!

OK, so we have built the `chart` object - now we ask Streamlit to show it to us by handing it to `st.plotly_chart()`. Add this at the bottom of your script:
```Python
st.plotly_chart(chart)
```
Save your file, and explore the visual! Investigate what the icons at the top right of your chart do.
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
