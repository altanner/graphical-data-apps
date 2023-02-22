---
title: "3 • Getting started with layout"
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
st.title("A graphical data app")
```

Save the file (remember that Jupyter Lab will show a circle next to files that have unsaved modifications, in their tab), and then move to your Terminal tab. If you aren't already, move into the folder where your Python file is saved (using the Terminal command line), and run the script:

```Shell
streamlit run data_app.py
```

The terminal should report something along the lines of *"You can now view your Streamlit app in your browser"* - so, have a look, where it will have opened a new tab for you. A browser-ready page made with two lines of code! Note that the Terminal is now engaged with running Streamlit, so you will not be able to interact with it (it will still respond to non-Streamlit output, for example a `print()` call. You can stop the Terminal using `ctrl-c`.

{{< admonition type="tip" title="Python scripts for Streamlit are unusual" open=false >}}
In the script we just created, notice that common features of Python are absent. There are currently no variables or functions, no familiar `print` or `return` values - so how is it doing anything?

In the terminal, we ran `streamlit run data_app.py`, not `python data_app.py`. So, we are asking `streamlit` itself to interpret the Python file, when typically we ask the Python interpreter (a program) to interpret our Python script (a file). As such, `streamlit` will read our file, understand that `st` lines are directly calling the Streamlit API, and create / update the interface (the Streamlit browser tab) accordingly.
{{< /admonition >}}

## [The Streamlit API](https://docs.streamlit.io/library/api-reference)
Before building more of the page, let's find out where to get information on how to use Streamlit. Streamlit has [clear documentation](https://docs.streamlit.io/library/api-reference), complete with embedded examples. Let's have a look through some of the main sections.

{{< admonition type="tip" title="What is an API?"  open=False >}}
An API is an Application Programming Interface. It can be a confusing term, not least because all three words in it have vague definitions. Here though, we are using Streamlit, interfacing via Python - think of the API as the "control panel" to make it run (as opposed to the wires and code behind the control panel). Every time we write some Python with `st.<something>()`, we are asking the Streamlit API to do something, using syntax that is consistent with Python.
{{< /admonition >}}

### [Text elements](https://docs.streamlit.io/library/api-reference/text)
You now have a browser tab with your Streamlit app running. Let's add a couple of extra things, so you can see how the output of your script affects the app tab. We can add text using the [text elements](https://docs.streamlit.io/library/api-reference/text) section of the API. Try adding this **below your `st.title()` line**

```Python
st.write("Here is some text which is placed below the title for our app!")
```

The documentation has other text element examples - we will return to these in the Exercise in a moment.

Save the file, and notice that the Streamlit tab will say **Source file changed** and offers you **Rerun** and **Always rerun**. (If you can't see these, click the ***i*** symbol in the top right.) Select **Always rerun** - now, every time we save the file, Streamlit will automatically rebuild the page for us.

### [Page layout](https://docs.streamlit.io/library/api-reference/layout)
We want to be able to control where things appear on the page. Streamlit provides several ways to control page-layout, for example:

- containers (think of these as horizontally-arranged blocks, or rows)
- columns (vertical blocks)
- expanders (vertical blocks that can be minimised)
- sidebars.

### [Sidebars](https://docs.streamlit.io/library/api-reference/layout/st.sidebar)
Sidebars are a typical component of a data app, providing a tidy place to store controls, that can also be minimised to make best use of the browser window. We'll create a sidebar, by adding this to the bottom of your script:

```Python
with st.sidebar:
    st.write("This text is in our sidebar.")
```
Here we are using `with` notation. This programming syntax is commonly used to make code cleaner and easier to read. It also automates some processes in the background, for example opening and closing resources. Writing Python for Streamlit, we will see that we use `with` blocks for many layout instructions, for example `expander`, `tabs` and `columns`. See [the API docs](https://docs.streamlit.io/library/api-reference/layout) for more details.

### [Columns](https://docs.streamlit.io/library/api-reference/layout/st.columns)
Columns allow us to vertically partition the app. Creating them requires setting _how many_ there are, then using them with `with`, as in the sidebar example. Here we are creating two columns:

```Python
column1, column2 = st.columns(2)

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

### Other useful layout tools
While you can explore the docs more fully in your own time, and as you need for your own projects, we will just point out a few useful items, to give you a feel for what is possible:
- [images and other media elements](https://docs.streamlit.io/library/api-reference/media) (including video and audio)
- [info and progress boxes](https://docs.streamlit.io/library/api-reference/status) (useful for highlighting instructions, results and outputs)
- [interactive tables](https://docs.streamlit.io/library/api-reference/data)

{{< admonition type="tip" title="Customisations." open=false >}}
By default, Streamlit provides either a dark or light themed interface (user-system dependent), with their peach-red brand colour for highlighting, buttons, outlines etc. These can all be customised, through building your own theme, or using extra scripts to make specific changes. We don't teach these in this course, but if you would like to learn more, search the documentation or for tutorials.
{{< /admonition >}}

## Building a World Demographics Data Visualisation
{{< admonition type="question" title="Exercise: build your app's layout." open=true >}}
Through the rest of this course we will be making a demographics data app. This uses a publicly accessible dataset with statistics on countries of the world, and how they have changed in the past few decades.
Our first exercise is to prepare our data app for this! We will edit some of the things we have already made, and create some new items as well.
Your goal in this exercise is to refer to the Streamlit API docs, and add some structure to the app. To keep things neat, we are going to put most interface items into the sidebar, so the main body has plenty of space for our visualisation (we'll start to make that in the next section).
1. Change the title of the page to "World Demographics". Put it in the sidebar.
2. Add an image to the sidebar, below the title, using `st.image()` - the name of the image is `globe.png`, we downloaded it earlier (or click it here if you need it again). The file `globe.png` needs to be in the same folder as your Python script.
3. Add an information box, using `st.info()`, to the top of your sidebar. This will contain the text "Welcome to the global demographic data explorer app!"
{{< /admonition >}}


{{< admonition type="question" title="Exercise" open=true >}}
- Check back in 2023!
{{< /admonition >}}


{{< admonition type="note"  open=true >}}
- Check back in 2023!
{{< /admonition >}}


{{< admonition type="abstract"  open=true >}}
- Check back in 2023!
{{< /admonition >}}


{{< admonition type="info"  open=true >}}
- Check back in 2023!
{{< /admonition >}}


{{< admonition type="tip"  open=true >}}
- Check back in 2023!
{{< /admonition >}}


{{< admonition type="success"  open=true >}}
- Check back in 2023!
{{< /admonition >}}


{{< admonition type="question"  open=true >}}
- Check back in 2023!
{{< /admonition >}}


{{< admonition type="warning" open=true >}}
- Check back in 2023!
{{< /admonition >}}


{{< admonition type="failure"  open=true >}}
- Check back in 2023!
{{< /admonition >}}


{{< admonition type="danger"  open=true >}}
- Check back in 2023!
{{< /admonition >}}


{{< admonition type="bug"  open=true >}}
- Check back in 2023!
{{< /admonition >}}


{{< admonition type="example"  open=true >}}
- Check back in 2023!
{{< /admonition >}}


{{< admonition type="quote"  open=true >}}
- Check back in 2023!
{{< /admonition >}}


blahblah
