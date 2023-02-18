---
title: "∙ Requirements and set up"
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
{{< /admonition >}}

### Your experience
We try to be as inclusive as possible regarding your coding level, but to get the most out of this course, you should have:
* experience of Python to an intermediate level; for example, you should understand **functions, conditionals, modules and loops**. If you have attended any of our [courses](https://milliams.com/courses/data_analysis_python/) on [data analysis](https://milliams.com/courses/applied_data_analysis/), you will be ready to approach this course.
* at least a little experience of the [`pandas`](https://pandas.pydata.org/) library.
* [**Anaconda Navigator**](https://www.anaconda.com/products/distribution) installed. Alternatively, if you feel comfortable working in another IDE (for example [**VS Code**](https://code.visualstudio.com/Download) or [**PyCharm**](https://www.jetbrains.com/pycharm/), you are welcome to use those).
* a little experience of using the [command line](https://alleetanner.github.io/intro-to-command-line/) is useful, but not essential.

### Getting set up
Before we begin, we will need to create a new environment. To make this easy, download [this `environment.yml`]() file (just a list of the dependencies, in a format understood by `conda`, Anaconda's package manager. If you are interested, or you need to do things manually, the libraries this installs are:

- `numpy` - provides [numerical and mathematics tools](https://numpy.org/),
- `pandas` - allows us to [organise data into powerful formats](https://pandas.pydata.org/), most notably the dataframe,
- `plotly` - an open-source graphing, charting and [data vis library](https://plotly.com/python/),
- `plotly-express` - plotly on [easy mode](https://plotly.com/python/plotly-express/), perfect for beginners,
- `streamlit` - our [data app interface builder](https://streamlit.io/).

We will be working with a demonstration dataset built into the `plotly` library, so for this course we only need our environment file.

<img align="right" src="https://raw.githubusercontent.com/alleetanner/graphical-data-apps/main/assets/anaconda_screenshot.png" width="250" style="border-radius: 2%; margin-right: 15px; margin-left: 15px;" /> Start Anaconda Navigator (you should see the welcome screen, similar to the image here). We are going to create a new Python “environment” (see the glossary above for more detail on environments). 

Once you have the [the `environment.yml`](), we can use it to build a new Python environment. In Anaconda Navigator’s start screen, select “Environments” from the menu on the left. Now, at the bottom of the window, click “Import”, and select the `environment.yml` file that you downloaded (you might have to find it, in your default download folder). Name this new environment `data-apps`, then click to continue. Anaconda will now install the dependencies we need for this course. **This can take a few minutes, and you might be asked to click to confirm a couple of things, so please be patient!**

<img align="right" src="https://raw.githubusercontent.com/alleetanner/graphical-data-apps/main/assets/jupyterlab_launch.png" width="250" style="border-radius: 2%; margin-right: 15px; margin-left: 15px;" /> Once it is complete, you will see in the the Environments menu that `data-apps` now exists (probably below `base (root)`). Select `data-apps`, and return to the “Home” tab. From there, click the **Jupyter Lab** icon and a new tab will open in your browser containing a Jupyter Lab session. We are now ready to start!

### If you are using an alternative IDE
Please skip this section if you are using Jupyter Lab.

If you prefer to use another interface, please be confident with installing new packages into your Python environment. If you use the package manager `pip`, we have provided a [`requirements.txt` file here](), which will install the required packages. Create a suitable new folder to work in, and move the `requirements.txt` file into that folder. A typical series of commands would be:

* Create a new environment here, called `venv`:
```Shell
python -m venv ./venv
```

* Activate this new environment:
```Shell
source ./venv/bin/activate
```

* Use `pip` to acquire and install our dependencies:
```Shell
pip install -r requirements.txt
```
