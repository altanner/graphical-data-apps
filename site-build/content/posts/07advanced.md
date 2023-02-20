---
title: "• Sharing, deploying"
subtitle: "Some further topics, and how to make your work public."

date: 2023-02-17T00:00:00+01:00

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
