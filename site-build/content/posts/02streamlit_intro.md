---
title: "• First steps"
subtitle: "Writing and running our first script."

date: 2023-02-12T00:00:00+01:00

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
- you get a feel for code syntax: spaces, quotes, indentation, colons, `under_scores`, etc (watch an experienced coder, and you might notice they adopt a different, deliberate cadence to their typing when writing code!)
- you gain a better understanding of what `(the) [different] {brackets}` do,
-  **most important of all**, ***you will make mistakes!*** You can't learn without making mistakes, understanding what went wrong, and addressing the issue.
{{< /admonition >}}

### Creating your first page
In our text editor (of the Python file `data_app.py`), the first thing we need is to bring the `streamlit` library into our script:

```Python
import streamlit as st
```

Here, we are `import`ing the Streamlit library, and giving it the name `st` - this is the conventional alias for Streamlit, a little like we shorten `numpy` to `np` and `pandas` to `pd` (an alias doesn't do anything other than save us typing the whole word every time!)

Below this, let's enter our first Streamlit command:

```Python
st.title("Hi - let's build a data app!")
```

Save the file (remember that Jupyter Lab will show a circle next to files that have unsaved modifications), and then move to your Terminal pane. If you aren't already, move into the folder where your Python file is saved (using the Terminal command line), and run the script:

```Shell
streamlit run data_app.py
```

The terminal should report something along the lines of `You can now view your Streamlit app in your browser` - so, have a look, where it will have opened a new tab for you! A browser-ready page made with two lines of code!

{{< admonition type="tip" title="Python scripts for Streamlit are unusual" open=false >}}
In the script we just created, notice that common features of Python are absent. There are currently no variables or functions, no familiar `print` or `return` values - so how is it doing anything?

In the terminal, we ran `streamlit run data_app.py`, not `python data_app.py`. So, we are asking `streamlit` itself to interpret the Python file, when typically we ask the Python interpreter (a program) to interpret our Python script (a file). As such, `streamlit` will read our file, understand that `st` lines are directly calling the Streamlit API, and create / update the interface (the Streamlit browser tab) accordingly.
{{< /admonition >}}

### Adding your first layout component
Hopefully, you now have a tab with your Streamlit app running. Let's add a couple of extra things, so you can see how the output of your script affects the app tab.

Add this to your script:

```Python
st.sidebar.write("This text is in our sidebar.")
```

Save the file, and notice that the Streamlit tab will say **Source file changed** and offers you **Rerun** and **Always rerun**. (If you can't see these, click the ***i*** symbol in the top right.) Select **Always rerun** - now, every time we save the file, Streamlit will automatically rebuild the page for us.

### [The Streamlit API](https://docs.streamlit.io/library/api-reference)
Before building more of the page, let's find out where to get information on how to use Streamlit. Streamlit has [clear documentation](https://docs.streamlit.io/library/api-reference), complete with embedded examples. Let's have a look through some of the main sections.

{{< admonition type="tip" title="What is an API?"  open=False >}}
An API is an Application Programming Interface. It can be a confusing term, not least because all three words in it have vague definitions. Here though, we are using Streamlit, interfacing via Python - think of the API as the "control panel" to make it run (as opposed to the wires and code behind the control panel). Every time we write some Python with `st.<something>()`, we are asking the Streamlit API to do something, using syntax that is consistent with Python.
{{< /admonition >}}

#### [Text elements](https://docs.streamlit.io/library/api-reference/text)
We can format our text using the [text elements](https://docs.streamlit.io/library/api-reference/text) section of the API. Add the lines below the line  script:

```Python
st.text("Plain text can be inserted like this.")
st.write("sadfklj.")
```

{{< admonition type="tip" title="Customisations." open=False >}}
By default, Streamlit provides either a dark or light themed interface (user-system dependent), with their peach-red brand colour for highlighting, buttons, outlines etc. These can all be customised, through building your own theme, or using extra scripts to make specific changes. We don't teach these in this course, but if you would like to learn more, just use a search engine!
{{< /admonition >}}

#### [Layout and containers](https://docs.streamlit.io/library/api-reference/layout)

So far, we have used `st.write()` and `st.sidebar()`. `st.write()` is a basic 



{{< admonition type="Exercise" title="Exercise: build your app's layout." open=true >}}
Your goal in this exercise is to refer to the Streamlit API docs, and add some structure to the app.
- Add a descriptive subtitle.

- Add a file uploader box to the sidebar (look in the "Input Widgets" section).
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
