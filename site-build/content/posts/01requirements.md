---
title: "1 ∙ Requirements and set up"
subtitle: "What you will need, and how to get your computer ready."

date: 2023-02-11T00:00:00+01:00

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
- **Dependency** : anything that is required to get software to run. For example, here we need some libraries to be installed, so we are *dependent* on those being in place and working. In other contexts, "dependencies" might be single files, settings, or whole software packages.
{{< /admonition >}}

## Required experience
We try to be as inclusive as possible regarding your coding level, but to get the most out of this course, you should have:
* experience of Python to an intermediate level; for example, you should have experience of **functions** and **conditionals**. If you have attended any of our [courses](https://milliams.com/courses/data_analysis_python/) on [data analysis](https://milliams.com/courses/applied_data_analysis/), you are ready to approach this course. If you have only done [Intermediate Python](https://milliams.com/courses/intermediate_python/) you should also be fine!
* a little experience of using the [command line](https://alleetanner.github.io/intro-to-command-line/) is useful, but not essential.

## Setting up
To begin, we will use a command line, but this is the only part of the course that needs this. We provide instructions here for both Windows or MacOS (+ Linux), so follow the instructions relevant to you:

{{< admonition type="abstract" title="Windows" open=false >}}
In the Windows start button type `cmd` - this will open a command line for you. First, we make a new folder (a new directory) by typing, in the command line window
```Terminal
mkdir graphical-data-apps
```
then we move into that folder using the command
```Terminal
cd graphical-data-apps
```
We then create a new Python virtual environment (see the glossary box above for an explanation of what this is), with the command
```Terminal
python3 -m venv data_apps_env
```
which means, "run python, using the module called `venv`, and create a new environment called `data_apps_env`".

We then tell the terminal to use this environment:
```Terminal
data_apps_env\Scripts\activate
```
Finally, we install the required Python packages for this workshop:
```Terminal
pip install jupyterlab==3.6.3 streamlit==1.21.0 plotly_express==0.4.1
```
{{< /admonition >}}

{{< admonition type="abstract" title="MacOS & Linux" open=false >}}
We can get a command line interface by opening Spotlight (`command + space`) and typing `Terminal`. In this command line window, first, we create a new folder to work in
```Terminal
mkdir graphical-data-apps
```
then we move into that folder
```Terminal
cd graphical-data-apps
```
We then create a new Python virtual environment (see the glossary box above for an explanation of what this is), with the command
```Terminal
python3 -m venv ./data_apps_env
```
which means, "run python, using the module called `venv`, and create a new environment here `.` called `/data_apps_env`".

We then tell the terminal to use this environment as the Python install it is using.
```Terminal
source ./data_apps_env/bin/activate
```
Finally, we install the required Python packages for this workshop (this might take a couple of minutes:
```Terminal
pip install jupyterlab==3.6.3 streamlit==1.21.0 plotly_express==0.4.1
```
{{< /admonition >}}

Whichever operating system you are using, you are now ready to start, so finally run this command to open a Jupyter Lab session in your browser:
```Terminal
jupyter lab
```

## Jupyter Lab
In the Jupyter Lab **file navigator** in the sidebar to the left, find and move into the folder we made called `graphical-data-app` (this should be in your home folder, or another default location).

We are going to have two panes open: one **Python file** (a text editor), and one **Terminal**. You can open these either from the launch screen (with icons), or from the menu bar (*in* the Jupyter Lab tab menu, not the browser menu!), going **File** → **New** → **Python File** and **File** → **New** → **Terminal**.

For this session, a useful layout is with the Python file editor at the top, and Terminal below. This allows us to have a wide pane for the editor, and the terminal will only be running Streamlit (and occasionally reporting what is happening, and any errors), so we don't need it to take up too much space. In any case, layout as suits your screen best, and we are now ready to start!

{{< admonition type="tip" title="Some reminders on editors, terminals and consoles"  open=false >}}
There are three panes in Jupyter Lab that we commonly use in our teaching:
- **Text editor** : this is a basic word-processor designed for code, that is opened when you create a new Python or plain text file.
- **Terminal** : this is a command-line (text based) version of your file manager (ie, Finder in MacOS, File Explorer in Windows). This is used to navigate the folders on your computer, and run commands.
- **Console** : in the context of Jupyter lab, the console runs Python *interactively*. This means you enter Python code line by line, which are immediately run - but it does not create or edit a script file. This is useful for understanding how code works, and prototyping a script.
{{< /admonition >}}

{{< admonition type="warning" title="If you are using an alternative IDE"  open=false >}}
Please skip this section if you are using Jupyter Lab / Anaconda.

You are welcome to use another IDE, but please be confident with installing new packages into your Python environment. You will need to be running both an editor and a terminal, as in the previous section. If you use the package manager `pip`, we have provided a [`requirements.txt` file here](https://raw.githubusercontent.com/alleetanner/graphical-data-apps/main/requirements.txt), which will install the required packages. (`environment.yaml` and `requirements.txt` are essentially identical, for `conda` and `pip` respectively.) Create a suitable new folder to work in, and move the `requirements.txt` file into that folder. A typical series of commands would be:

Create a new environment here, called `venv`:
```Terminal
python -m venv ./venv
```

Activate this new environment:
```Terminal
source ./venv/bin/activate
```

Use `pip` to acquire and install our dependencies:
```Terminal
pip install -r requirements.txt
```

If you are interested, or if you need to do things manually, the libraries this installs are:

- `pandas` - allows us to [organise data into powerful formats](https://pandas.pydata.org/), most notably the dataframe
- `plotly` - an open-source graphing, charting and [data vis library](https://plotly.com/python/)
- `plotly-express` - plotly on [easier mode](https://plotly.com/python/plotly-express/)
- `streamlit` - the [data app interface builder](https://streamlit.io/)
{{< /admonition >}}
