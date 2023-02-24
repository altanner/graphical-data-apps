---
title: "6 • Introduction to animations"
subtitle: "Animations add an extra dimension!"

date: 2023-02-16T00:00:00+01:00

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

In this final section, we will introduce animations. Many of the graphics libraries include the ability to animate visuals, but always think carefully about whether this actually adds anything to your app. Some animations can also get quite technical to run properly, but Plotly makes it relatively easy, especially with `px.scatter()`.

## A widget controlling a widget!
To start we are going to add a simple toggle checkbox, as we did earlier, controlling if animation is enabled or not. As your first widget (ie, in your sidebar, just below your title, but above your "Year" slider) add this:
```Python
animate_vis = st.checkbox(
    label="Animate")
```
Remember to keep your indentation correct for the sidebar block. Save the file and confirm the checkbox is in the right place. We will connect this to the chart in just a moment! Now, we are going to be animating on the "Year" column. As such, when "Animate" is selected, asking for the "Year" again with the slider doesn't make sense.

We can solve this by making the "Animate" checkbox also control the "Year" slider. "Animate" is a checkbox, therefore it can take two values of `False` or `True`; this is also the value of `animate_vis`. We can pass that boolean variable to another widget, in this case the "Year" slider. We want "Year" to be disabled when "Animate" is enabled. We do this by adding `disabled=animate_vis` to the slider parameters:
```Python
year_widget = st.slider(
    label="Year",
    value=2008,
    min_value=1998,
    max_value=2018,
    disabled=animate_vis)
```
Save and check behaviour in our app. The checkbox and the year slider should now be mutually exclusive! Now to actually create the animation.




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
