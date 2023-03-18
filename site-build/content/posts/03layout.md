---
title: "3 • Layout"
subtitle: "Writing and running our first script."

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
In our text editor (of the Python file `data_app.py`), the first thing we need is to bring the `streamlit` library into our script:

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

## Exercise 1: Preparing our app layout
{{< admonition type="question" title="Exercise 1: making your first page edits" open=true >}}
Our minimal-viable-app is running, but let's make our first edits. The goal of this exercise is to start to get familiar with the workflow of editing your Python file, saving, and viewing the changes in your browser.
1. Change your title to something else.
2. We can add a subtitle with `st.subtitle()`; add this to your app, and include a sentence which 
3. Move your subtitle to be above your title and notice the changes to your app.
{{< /admonition >}}

### Text elements
In the last exercise, you used a two different types of *text elements*. We are going to explore a few more of these, by looking at the documentation for Streamlit. Open the [text elements section of the API](https://docs.streamlit.io/library/api-reference/text) and have a look around. Try adding this **below your `st.title()` line**

```Python
st.write("Here is some text which is placed below the title for our app!")
```

The documentation has other text element examples - we will return to these in the Exercise in a moment.

Save the file, and notice that the Streamlit tab will say **Source file changed** and offers you **Rerun** and **Always rerun**. (If you can't see these, click the ***i*** symbol in the top right.) Select **Always rerun** - now, every time we save the file, Streamlit will automatically rebuild the page for us.

Before moving on to layout, we want to set how the app is presented (Streamlit will deal with layout for both desktop and mobile browsers, behind the scenes). Here we can add a title which will go in the browser tab. (We could also give it a favicon, but will skip that for now.)

Below your `import` command, but above everything else, add this line:

```Python
st.set_page_config(page_title="My data app", layout="wide")
```
Save, and we are ready for layout.

## Page layout
We want to [control where and how things appear on the page](https://docs.streamlit.io/library/api-reference/layout). We will use three layout components in our app: sidebars, columns and tabs.

### Sidebars
[Sidebars](https://docs.streamlit.io/library/api-reference/layout/st.sidebar) are a typical component of a data app, providing a tidy place to store controls, that can also be minimised to make best use of the browser window. We'll create a sidebar, by adding this to the bottom of your script:

```Python
with st.sidebar:
    st.write("This text is in our sidebar.")
```

Here we are using `with` notation. This programming syntax is commonly used to make code cleaner and easier to read. It also automates some processes in the background, for example opening and closing resources. Writing Python for Streamlit, we will see that we use `with` blocks for many layout instructions, for example `expander`, `tabs` and `columns`. See [the API docs](https://docs.streamlit.io/library/api-reference/layout) for more details.

### Columns
[Columns](https://docs.streamlit.io/library/api-reference/layout/st.columns) allow us to vertically partition the app. Creating them requires setting _how many_ there are, then placing code inside `with` blocks as appropriate, just as in the sidebar example. Here we are creating two columns:

```Python
column1, column2 = st.columns(2)
```
and then we can place items into those columns, for example"
```Python
with column1:
    st.write("Here is column 1")
    
with column2:
    st.write("This is column 2")
```
We can create any number of columns we like, for example `column1, column2, column3 = st.columns(3)` would create three columns. We can also control the widths by passing a list of the *ratios* of the columns:

```Python
column1, column2 = st.columns([1, 4])
```
This will create two columns, with the right hand one being four times wider than the left hand one.

### Tabs
[Tabs](https://docs.streamlit.io/library/api-reference/layout/st.tabs) allow our app to have different "pages". (These are not true pages - see [here for details](https://docs.streamlit.io/library/get-started/multipage-apps) on creating a true multi-page app.) Just like with columns, we first need to define our tabs, but with a list of their names. Here we are making four new tabs, with names:
```Python
tab1, tab2, tab3, tab4 = st.tabs(["Data", "Analysis", "Output", "Kittens"])
```
And like with columns, to put things into a tab, we use a `with` block, for example:
```Python
with tab4:
    st.image("kittens.png")
```
Give that a try and check how it looks in the app (remember to save to see the changes).

{{< admonition type="tip" title="More layout options and customisations." open=false >}}
While you can explore the docs more fully in your own time, and as you need for your own projects, we will just point out a few useful items, to give you a feel for what is possible:
- [images and other media elements](https://docs.streamlit.io/library/api-reference/media) (including video and audio)
- [info and progress boxes](https://docs.streamlit.io/library/api-reference/status) (useful for highlighting instructions, results and outputs)
- [interactive tables](https://docs.streamlit.io/library/api-reference/data)

By default, Streamlit provides either a dark or light themed interface (user-system dependent), with their peach-red brand colour for highlighting, buttons, outlines etc. These can all be customised, through building your own theme, or using extra scripts to make specific changes. If you would like to learn more, search the documentation or for tutorials.
{{< /admonition >}}

## Exercise 1: Preparing our app layout
{{< admonition type="question" title="Exercise 1: build your app's layout" open=true >}}
Through the rest of this course we will be building a **visualiser for World Demographics Data**. Our first exercise is to prepare our layout for this. We will edit some of the things we have already made, and create some new items as well. Preview each of your changes by saving your file, and you will immediately be able to see how things are looking in the apps' tab in your browser.
1. Remove the `st.write()` line that we added earlier.
2. Change the **title** in the page to "World Demographics". Put it in the sidebar.
3. Change the **browser tab title of the page** to "Demo App" (modify the contents of `st.set_page_config()`).
4. Create **two** columns in the main app space, with the left column being five times wider than the right one.
5. Add an information box to the **left hand column**, saying "Welcome to the global demographic data explorer app!" (use `st.info()`).
6. Add an image to the **right hand column**, using `st.image()`. We will use the image `globe.png`, included with the [course resources download](https://github.com/alleetanner/graphical-data-apps/raw/main/data-apps.zip) we got earlier
7. Create **two tabs** using `st.tabs()`, named "Data" and "Visualisation". Remember that `st.tabs()` takes a **list** (ie, you will have square and round brackets). We will be filling these tabs in the next section.
{{< /admonition >}}

{{< admonition type="warning" title="Exercise 1 solution" open=false >}}
The whole script should look something similar to this:
```Python
import streamlit as st

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
```
{{< /admonition >}}

{{< admonition type="tip" title="The Streamlit API"  open=false >}}
Streamlit has [clear API documentation](https://docs.streamlit.io/library/api-reference), complete with embedded examples. It is a good place to build your skills in using documentation, since documentation for different libraries can vary in the clarity / density of the information provided.

An API is an **Application Programming Interface**. It can be a confusing term, but the essential word is "interface": think of the API as the "control panel" to make it run (as opposed to the wires and code behind the control panel). Every time we write some Python with `st.<something>()`, we are asking the Streamlit API to act, using syntax that is consistent with Python.
{{< /admonition >}}
