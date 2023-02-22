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
Before we go any further, let's examine what is inside our dataframe. We can do this natively in Streamlit. Building on your script at the **end** of the script, add this to the end:
```Python

```
Save the file, and have a look at the browser tab displaying your app. We can now see what we are working with - note that this dataframe is interactive, so it can be ordered and selected, but we will not be covering interactive dataframes today.

We cover [widgets](ZXXXX) in the next section, but right now we want to quickly add a toggle for visibility of this dataframe. Go to your code block starting `with st.sidebar:`, and inside this block (ie, indented) add
```Python
df_view = st.checkbox(label="View dataframe")
```
Here we are assigning the state of the checkbox to the variable called `df_view`. A checkbox is a boolean, so it can only be `True` or `False`. We will use this value to trigger if Streamlit shows us the dataframe, by putting our `st.dataframe(demo_df)` into a conditional block:
```Python
if df_view == True:
    st.dataframe(demo_df)
```

## Plotly Express
There are a few popular graphing libraries in Python - for example `matplotlib`, `seaborn`, `ggplot`. We are going to use `plotly`, because it has an intermediate learning curve - the syntax is relatively accessible, the documentation is good, and the graphs it creates are good-looking, customisable and interactive. powerful.

### Creating a basic scatter plot
Plotly 


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
