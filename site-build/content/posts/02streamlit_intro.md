---
title: "• First steps"
subtitle: "Build a website with two lines of code!"

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

### Arranging the Jupyter Lab tab
If you followed the previous page, you should have a Jupyter Lab session open in a tab in your browser. In the Jupyter Lab file navigator to the left, create a new folder to work in, and move into it. We are going to have two panes open: one Python file, and one Terminal. You can open these either from the launch screen (with icons), or from the menu bar (*in* the Jupyter Lab tab menu, not the browser menu!), going *File* → *New* → *Python File* and *File* → *New* → *Terminal*. Name the Python file `data_app.py` (you might need to right-click on the file and select *Rename*).

For this session, we find the most useful layout is with the Python file editor at the top, and Terminal below. This allows us to have a wide pane for the editor, and the terminal will only be running Streamlit (and reporting any errors), so we don't need it to take up too much space.

{{< admonition type="tip" title="Some reminders on editors, terminals and consoles."  open=False >}}
There are three panes in Jupyter Lab that we commonly use in our teaching:
- **Text editor** : this is a basic word-processor designed for code, that is opened when you create a new Python or plain text file.
- **Terminal** : this is a command-line (text based) version of your file manager (ie, Finder in MacOS, File Explorer in Windows). This is used to navigate the folders on your computer, and run commands.
- **Console** : in the context of Jupyter lab, the console runs Python *interactively*. This means you enter Python code line by line, which are immediately run - but it is not creating a script file. This is useful for understanding how code works, and prototyping a script.
{{< /admonition >}}

### Creating your first page
In our text editor (of the Python file `data_app.py`), the first thing we need is to bring the `streamlit` library into our script:

```Python
import streamlit as st
```

Here, we are `import`ing the Streamlit library, and giving it the name `st` - this is the accepted standard alias for Streamlit (an alias doesn't do anything other than save us typing the whole word every time!)

Below this, let's enter our first Streamlit command:

```Python
st.write("Let's build a data app.")
```

Save the file (remember that Jupyter Lab will show a circle next to files that have unsaved modifications), and then move to your Terminal pane. If you aren't already, move into the folder where your Python file is saved (using the Terminal command line), and run the script:

```Shell
streamlit run data_app.py
```

You will now be able to view the Streamlit-built page in your browser, where it will have opened a new tab for you! For this course, it is useful to be able to arrange your windows so that both the Jupyter Lab and the Streamlit tabs are visible at the same time (you can drag the tab out of the browser to make a new window).

### Adding your first interface components

### The Streamlit API



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
