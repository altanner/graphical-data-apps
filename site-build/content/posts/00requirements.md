---
title: "∙ Requirements and Set Up"
subtitle: "What you will need, and how to get your computer ready."

date: 2023-02-10T00:00:00+01:00

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
The words **library**, **module** and **package** roughly mean the same thing; it is entirely natural to be confused by this!
- **Library** : a collection of python files that expand the ability of python, using the `import` command. These are like accessories or modifications, typically giving you access to powerful, professional functions and classes written by collaborations of expert coders.
  - A library can be [standard](https://docs.python.org/3/library/index.html) (it comes built into python), for example `time` or `math`, or
  - 3rd party, so, not a core part of python itself and will need to be installed.
- **Package** : a library that is available for delivery to a package manager, such as `pip` or `conda`. [PyPI](https://pypi.org/) is the main package storehouse for python.
- **Module** : anything that is imported to a main running script. Libraries and packages are made of modules.
- **Environment** : this has two related meanings. A "Python Environment" is a specific installation of Python, available on your computer. Typically, users have a default install, called `base`, but we can have more. Think of each environment as a new, blank version of Python, where we will install additional functionality specific for the project we are working on. (We recommend creating a new environment for every project, as this lessens chances of conflicts, and prevents your “base” install of Python becoming overly-burdened with libraries that you don’t need.) The other meaning for "environment" is *the interface that you are using to develop code* - for example VS Code, PyCharm, Jupyter Lab, even the command line itself are interfaces, also known as environments. Confusing, I know!
{{< /admonition >}}

### Expected experience
We try to be as inclusive as possible, but to get the most out of this course, you should have:
* experience of Python to an intermediate level; for example, you should understand **functions, conditionals, modules and loops**. If you have attended any of our [courses](https://milliams.com/courses/data_analysis_python/) on [data analysis](https://milliams.com/courses/applied_data_analysis/), you will be ready to approach this course.
* at least a little experience of the [`pandas`](https://pandas.pydata.org/) library.
* [**Anaconda Navigator**](https://www.anaconda.com/products/distribution) installed. Alternatively, if you feel comfortable working in another IDE (for example [**VS Code**](https://code.visualstudio.com/Download) or [**PyCharm**](https://www.jetbrains.com/pycharm/), you are welcome to use those).
* a little experience of using the [command line](https://alleetanner.github.io/intro-to-command-line/) is very useful, but not essential.

### Getting set up
Before we begin, we will need a couple of files (please download by clicking the links provided here):

* [this `environment.yml`]() file; this will update Python running in Anaconda so that we have all the dependencies that we need.
* [the dataset]() that we will be working with.

<img align="right" src="https://raw.githubusercontent.com/alleetanner/graphical-data-apps/main/assets/anaconda_screenshot.png" width="300" style="border-radius: 2%; margin-right: 15px;" /> Start Anaconda Navigator (you should see the welcome screen as in the image here). We are going to create a new Python “environment” (see the glossary above for more detail on environments). 

In Anaconda Navigator’s start screen, select “Environments” from the menu on the left. Now, at the bottom of the window, click “Import”, and select the `environment.yml` file that you downloaded (you might have to find it, in your default download folder). Name this new environment `data-apps`, then click to continue. Anaconda will now install the dependencies we need for this course. **This can take a few minutes, and you might be asked to confirm, so please be patient!**

<img align="right" src="https://raw.githubusercontent.com/alleetanner/graphical-data-apps/main/assets/jupyterlab_launch.png" width="300" style="border-radius: 2%; margin-right: 15px;" /> Once it is complete, you will see in the the Environments menu that `data-apps` now exists (probably below `base (root)`, your default Python install for Anaconda). Select `data-apps`, and return to the “Home” tab. From there, click the **Jupyter Lab** icon and a new tab will open in your browser of a Jupyter Lab session. We are now ready to start!

### If you are using an alternative IDE
Please skip this section if you are using Jupyter Lab.

If you prefer to use another interface, please be confident with installing new packages into your Python environment. If you use the package manager `pip`, we have provided a [`requirements.txt` file here](), which will install the required packages. Create a suitable new folder to work in, and move the `requirements.txt` file into that folder. A typical series of commands would be:

Create a new environment:
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
