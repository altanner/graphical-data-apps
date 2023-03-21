---
title: "3 • Layout"
subtitle: "Writing and running our first script, and understanding app layout"

date: 2023-02-13T00:00:00+01:00

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

{{< admonition type="tip" title="Typing is better than copy-pasting" open=false >}}
We provide `code` blocks through this course, which you can copy and paste to build your scripts. However, we **strongly recommend** that learners type out code manually. This might seem a minor point, but the benefits are:
- you get a feel for code syntax: spaces, quotes, indentation, colons, `under_scores`, etc,
- you gain a better understanding of what `(the) [different] {brackets}` do,
-  **most important of all**, ***you will make mistakes!*** You can't learn without making mistakes, understanding what went wrong, and addressing the issue.
{{< /admonition >}}

## Creating your first page
We have a text editor open, to begin let's rename this to make it clear what it is. Do this by saving the file, or going "Save as", and naming it `data_app.py` (you might need to right-click on the file and select "*Rename*").

We will start the script by asking Python to make the `streamlit` library available to our script:

```Python
import streamlit as st
```

Here, we are `import`ing the Streamlit library, and giving it the name `st` - this is the conventional alias for Streamlit, a little like we shorten `numpy` to `np` and `pandas` to `pd` (an alias doesn't do anything other than save us typing the whole word every time!)

Below this, let's enter our first Streamlit command:

```Python
st.title("Hello world!")
```

Save the file (remember that Jupyter Lab will show a circle next to files that have unsaved modifications, in their tab), and then move to your Terminal tab. If you aren't already, move into the folder where your Python file is saved (using the Terminal command line), and run the script:

```Terminal
streamlit run data_app.py
```

The terminal should report something along the lines of *"You can now view your Streamlit app in your browser"* - so, have a look, where it will have opened a new tab for you. A browser-ready page made with two lines of code! Note that the Terminal is now engaged with running Streamlit, so you will not be able to interact with it (it will still respond to non-Streamlit output, for example a `print()` call. You can stop the Terminal serving your data app by using `ctrl-c`.

## Exercise 1: First edits
{{< admonition type="question" title="Exercise 1: making your first page edits" open=true >}}
Our minimal-viable-app is up and running, and this gives us something to build on. The goal of this exercise is to start to get familiar with the workflow of editing your Python file, saving, and viewing the changes in your browser.

When you save your first change to your Python file, the app will say **Source file changed**, and asks **Rerun** or **Always rerun**. (If you can't see these, click the ***i*** symbol in the top right.) Select **Always rerun** - every time we save the file, Streamlit will automatically rebuild the page for us.

Try the following edits, saving after each step to see the changes in the app's tab in your browser.
1. Change your app's title to something you like.
2. Below this, add a subtitle with `st.subtitle()`; remember that what you put inside the brackets is a string, so you will need `"`quotes`"` around it!
3. Move your subtitle line to be above your title line in the script, and notice the changes to your app.
4. Move the subtitle back down again.
5. Use `st.write()` to add a sentence below your subtitle.
{{< /admonition >}}

{{< admonition type="warning" title="Exercise 1 solution" open=false >}}
Your script should look something like this:
```Python
import streamlit as st

st.title("Here, this is a title.")

st.subtitle("Subtitles are a little bit smaller than titles.")

st.write("Here is some normally formatted text. Very vanilla text.")
```
{{< /admonition >}}

These are all text elements. To learn more see the [text elements section of the Streamlit API documentation](https://docs.streamlit.io/library/api-reference/text). The [status elements](https://docs.streamlit.io/library/api-reference/status) are similar and useful for laying out your app: we will use these in a moment.

## Page layout
So far we know how to present some text, but we want to [control where and how things appear on the page](https://docs.streamlit.io/library/api-reference/layout). We will use three layout components in our app: sidebars, columns and tabs.

### Sidebars
[Sidebars](https://docs.streamlit.io/library/api-reference/layout) are a typical component of a data app, providing a tidy place to store controls, that can also be minimised to make best use of the browser window. We'll create a sidebar, by adding this to your script:

```Python
with st.sidebar:
    st.write("This text is in our sidebar.")
```

Here we are using `with` notation. This programming syntax makes the logical flow of your code easy to follow. It also automates some processes in the background, for example opening and closing resources. We will use `with` blocks for many layout instructions, for example, `tabs` and `columns` and `expander`. See [the API docs](https://docs.streamlit.io/library/api-reference/layout) for more details.

### Columns
[Columns](https://docs.streamlit.io/library/api-reference/layout) allow us to vertically partition the layout. Unlike sidebars, **columns must always be created before they can be used**. We set _how many_ columns we want, then place code inside `with` blocks as appropriate, just as in the sidebar example. Here we are creating two columns:

```Python
column1, column2 = st.columns(2)
```

and then we can place items into those columns, for example:

```Python
with column1:
    st.write("Here is column 1")
    
with column2:
    st.write("This is column 2")
```

We can create any number of columns we like, for example `column1, column2, column3 = st.columns(3)` would create three columns of equal width. We can control the widths by passing a **list of the ratios** of the column widths (note the `[`square`]` brackets (a list) inside the `(`round`)` brackets (the parameters of `st.columns()`):

```Python
column1, column2 = st.columns([1, 4])
```

This will create two columns, with the right hand one being four times wider than the left hand one.

### Tabs
[Tabs](https://docs.streamlit.io/library/api-reference/layout) allow our app to have separate tabs, for example to hold different graphs, input items or explanation. (These act like but are not true separate pages - but [multi-page apps](https://docs.streamlit.io/library/get-started/multipage-apps) can be made.) Just like with columns, **we first need to define our tabs**, with a list of their names:

```Python
tab1, tab2 = st.tabs(["Data", "Visualisation"])
```

Just like with columns, to put things into a tab, we use a `with` block, for example:

```Python
with tab1:
    st.write("Here is a tab.")
```

Give that a try and check how it looks in the app (remember to save to see the changes).

{{< admonition type="tip" title="More layout options and customisations." open=false >}}
While you can explore the docs more fully in your own time, and as you need for your own projects, we will just point out a few useful items, to give you a feel for what is possible:

- [images and other media elements](https://docs.streamlit.io/library/api-reference/media) (including video and audio)
- [info and progress boxes](https://docs.streamlit.io/library/api-reference/status) (useful for highlighting instructions, results and outputs)
- [interactive tables](https://docs.streamlit.io/library/api-reference/data)

By default, Streamlit provides either a dark or light themed interface (user-system dependent), with their peach-red brand colour for highlighting, buttons, outlines etc. These can all be customised, through building your own theme, or using extra scripts to make specific changes. If you would like to learn more, search the documentation or for tutorials.
{{< /admonition >}}

## Exercise 2: Preparing your app layout
{{< admonition type="question" title="Exercise 2: build your app's layout" open=true >}}
Through the rest of this course we will be building a **visualiser for World Demographics Data**. Our first exercise is to prepare our layout for this.

Preview each of your changes by saving your file, and you will immediately be able to see how things are looking in the apps' tab in your browser.
1. Remove the `st.write()` and `st.subtitle()` lines that we added earlier.
2. Change the **title** in the page to say "World Demographics".
3. Put your title in the sidebar.
4. Create **two** columns, with the left column being four times wider than the right one.
5. Add an information box to the **left hand column**, saying "Welcome to the global demographic data explorer app!" (use `st.info()`).
6. Leave the right hand column empty - but note how it allows us to control space on the page. We will use this space later.
7. Add text to each of your tabs. Test that everything looks as you expect it to look.
{{< /admonition >}}

{{< admonition type="warning" title="Exercise 2 solution" open=false >}}
The whole script should look something similar to this:
```Python
import streamlit as st

# build the sidebar
with st.sidebar:
    st.title("World Demographics")

# create two columns, of ratio 4:1
column1, column2 = st.columns([4,1])

# place info box in first column
with column1:
    st.info("Welcome to the global demographic data explorer app!")

# create two tabs
tab1, tab2 = st.tabs(["Data", "Visualisation"])

# put some text in the tabs to check they are working
with tab1:
    st.write("Here is tab one.")

with tab2:
    st.write("And this is tab two!")
```
{{< /admonition >}}

{{< admonition type="tip" title="The Streamlit API"  open=false >}}
Streamlit has [clear API documentation](https://docs.streamlit.io/library/api-reference), complete with embedded examples. It is a good place to build your skills in using documentation, since documentation for different libraries can vary in the clarity / density of the information provided.

An API is an **Application Programming Interface**. It can be a confusing term, but the essential word is "interface": think of the API as the "control panel" to make it run (as opposed to the wires and code behind the control panel). Every time we write some Python with `st.<something>()`, we are asking the Streamlit API to act, using syntax that is consistent with Python.
{{< /admonition >}}
