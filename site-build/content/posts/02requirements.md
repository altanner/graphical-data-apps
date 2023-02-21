---
title: "2 ∙ Requirements and set up"
subtitle: "What you will need, and how to get your computer ready."

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

{{< admonition type="note" title="Glossary" open=false >}}
The words **library**, **module** and **package** are often used interchangeably, and they mean very similar things; it is entirely natural to be confused by this!
- **Library** : a collection of python files that expand the ability of python, using the `import` command. These are like accessories or modifications, typically giving you access to powerful, professional functions and classes written by collaborations of expert coders.
  - A library can be [standard](https://docs.python.org/3/library/index.html) (it comes built into python), for example `time` or `math`, or
  - 3rd party, so, written by people outside of the core Python developers, and as such will need to be installed using a package manager. `numpy` and `pandas` are 3rd party libraries with millions of users.
- **Package** : a library that is available for delivery to a **package manager**, such as `pip` or `conda`. [PyPI](https://pypi.org/) ("Python Package Index") is the main package repository for Python.
- **Module** : anything that is imported to a running script. Libraries and packages are made of modules.
- **Environment** : this has two meanings. 
  - A "Python Environment" is a specific installation of Python, available on your computer. Typically, users have a default install, called `base`, but we can have more. Think of each environment as a new, blank version of Python, where we will install additional functionality specific for the project we are working on. (It is good software engineering practice to create a new environment for every project. This lessens chances of conflicts, and prevents your `base` install of Python becoming overly-burdened with libraries that you don’t need.) 
  - The other meaning for "environment" is *the interface that you are using to develop code* - for example **VS Code**, **PyCharm**, **Jupyter Lab**, even the command line itself are interfaces, also known as environments. Confusing, I know!
{{< /admonition >}}

## Your experience
We try to be as inclusive as possible regarding your coding level, but to get the most out of this course, you should have:
* experience of Python to an intermediate level; for example, you should understand **functions, conditionals, loops and modules**. If you have attended any of our [courses](https://milliams.com/courses/data_analysis_python/) on [data analysis](https://milliams.com/courses/applied_data_analysis/), you will be ready to approach this course.
* [**Anaconda Navigator**](https://www.anaconda.com/products/distribution) installed. Alternatively, if you feel comfortable working in another IDE (for example [**VS Code**](https://code.visualstudio.com/Download) or [**PyCharm**](https://www.jetbrains.com/pycharm/), you are welcome to use those).
* a little experience of using the [command line](https://alleetanner.github.io/intro-to-command-line/) is useful, but not essential.

## Getting set up
We provide [some files](https://github.com/alleetanner/graphical-data-apps/raw/main/data-app-files.zip) we need for this course. Download this and unzip it. We also need an empty folder to work in. So, create an appropriate new folder, and copy the files into it.

Before we begin, we will need to create a new **environment** (see the glossary above for a definition!). We can do this using the `environment.yml` provided. An `environment.yml` file contains a list of the libraries (also known as dependencies) we need, in a format understood by `conda`, Anaconda's package manager. If you are interested, or if you need to do things manually, the libraries this installs are:

- `pandas` - allows us to [organise data into powerful formats](https://pandas.pydata.org/), most notably the dataframe
- `plotly` - an open-source graphing, charting and [data vis library](https://plotly.com/python/)
- `plotly-express` - plotly on [easy mode](https://plotly.com/python/plotly-express/)
- `streamlit` - our [data app interface builder](https://streamlit.io/)

### Anaconda Navigator
<img align="right" src="https://raw.githubusercontent.com/alleetanner/graphical-data-apps/main/assets/anaconda_screenshot.png" width="250" style="border-radius: 2%; margin-right: 15px; margin-left: 15px;" /> Start Anaconda Navigator (you should see the welcome screen, similar to the image here). We are going to create a new Python environment. 

In Anaconda Navigator’s start screen, select “Environments” from the menu on the left. Now, at the bottom of the window, click “Import”, and select the `environment.yml` file that you downloaded. Name this new environment `data-apps`, then click to continue. Anaconda will now install the dependencies we need. 

**This can take a few minutes, and you might be asked to click to confirm a couple of things, so please be patient!**

<img align="right" src="https://raw.githubusercontent.com/alleetanner/graphical-data-apps/main/assets/jupyterlab_launch.png" width="250" style="border-radius: 2%; margin-right: 15px; margin-left: 15px;" /> Once Anaconda has finished getting and installing our libraries, you will see in the the Environments menu that a new environment called `data-apps` now exists (probably below `base (root)`). Select `data-apps`, and return to the “Home” tab. From there, click the **Jupyter Lab** icon and a new tab will open in your browser containing a Jupyter Lab session. We are now ready to start!

### Arranging the Jupyter Lab tab
In the Jupyter Lab **file navigator** in the sidebar to the left, create a new folder to work in, and move into it. We are going to have two panes open: one **Python file** (a text editor), and one **Terminal**. You can open these either from the launch screen (with icons), or from the menu bar (*in* the Jupyter Lab tab menu, not the browser menu!), going **File** → **New** → **Python File** and **File** → **New** → **Terminal**. Name the Python file `data_app.py` (you might need to right-click on the file and select "*Rename*").

For this session, the most useful layout is with the Python file editor at the top, and Terminal below. This allows us to have a wide pane for the editor, and the terminal will only be running Streamlit (and occasionally reporting what is happening, and any errors), so we don't need it to take up too much space.

{{< admonition type="tip" title="Some reminders on editors, terminals and consoles."  open=False >}}
There are three panes in Jupyter Lab that we commonly use in our teaching:
- **Text editor** : this is a basic word-processor designed for code, that is opened when you create a new Python or plain text file.
- **Terminal** : this is a command-line (text based) version of your file manager (ie, Finder in MacOS, File Explorer in Windows). This is used to navigate the folders on your computer, and run commands.
- **Console** : in the context of Jupyter lab, the console runs Python *interactively*. This means you enter Python code line by line, which are immediately run - but it is not creating a script file. This is useful for understanding how code works, and prototyping a script.
{{< /admonition >}}

### If you are using an alternative IDE
Please skip this section if you are using Jupyter Lab / Anaconda.

If you prefer to use another interface, please be confident with installing new packages into your Python environment. You will need to be running both an editor and a terminal, as in the previous section. If you use the package manager `pip`, we have provided a [`requirements.txt` file here](https://raw.githubusercontent.com/alleetanner/graphical-data-apps/main/sandpit/requirements.txt), which will install the required packages. (`environment.yml` and `requirements.txt` are essentially identical, for `conda` and `pip` respectively.) Create a suitable new folder to work in, and move the `requirements.txt` file into that folder. A typical series of commands would be:

Create a new environment here, called `venv`:
```Shell
python -m venv ./venv
```

Activate this new environment:
```Shell
source ./venv/bin/activate
```

Use `pip` to acquire and install our dependencies:
```Shell
pip install -r requirements.txt
```
