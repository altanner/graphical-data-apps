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
Now that we have `pandas` ready for use, we can read our dataset into a dataframe. We are using the dataset provided in the course materials, `demo_dataset.csv`, which will need to be in your working folder.
```Python
demo_df = pd.read_csv("demo_dataset.csv")
```

## Plotly Express
There are a few popular graphing libraries in Python - for example `matplotlib`, `seaborn`, `ggplot`. We are going to use `plotly`, because it has an intermediate learning curve - the syntax is relatively accessible, the documentation is good, and the graphs it creates are good-looking, customisable and interactive. powerful.

### Creating a basic scatter plot



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
