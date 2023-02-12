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
  enable: true
comment:
  enable: true
---

{{< admonition type="note" title="Glossary" open=false >}}
The words **library**, **module** and **package** roughly mean the same thing; it is entirely natural to be confused by this!
- **Library** : a collection of python files that expand the ability of python, using the `import` command. These are like accessories or modifications, typically giving you access to powerful, professional functions and classes written by collaborations of expert coders.
  - A library can be [standard](https://docs.python.org/3/library/index.html) (it comes built into python), for example `time` or `math`, or
  - 3rd party, so, not a core part of python itself and will need to be installed.
- **Package** : a library that is available for delivery to a package manager, such as `pip` or `conda`. [PyPI](https://pypi.org/) is the main package storehouse for python.
- **Module** : anything that is imported to a main running script. Libraries and packages are made of modules.
{{< /admonition >}}

### Expected experience
We try to be as inclusive as possible, but to get the most out of this course, you should have:
* experience of Python to an intermediate level; for example, you should understand **functions, conditionals, modules and loops**. If you have attended any of our [courses](https://milliams.com/courses/data_analysis_python/) on [data analysis](https://milliams.com/courses/applied_data_analysis/), you will be ready to approach this course.
* at least some experience of the [`pandas`](https://pandas.pydata.org/) library.
* [**Anaconda Navigator**](https://www.anaconda.com/products/distribution) installed. Alternatively, if you feel comfortable working in another IDE (for example [**VS Code**](https://code.visualstudio.com/Download) or [**PyCharm**](https://www.jetbrains.com/pycharm/), you are welcome to use those.
* a little experience of using the [command line](https://alleetanner.github.io/intro-to-command-line/) is very useful, but not essential.

### Getting set up
Before we begin, we will need a couple of files:

* the environment.yml file; this will update Python running in Anaconda so that we have all the dependencies that we need
* the dataset that we will be working with

Start Anaconda Navigator (you should see the welcome screen as in the image here). We are going to create a new “environment”. Think of this as creating a new, blank version of Python, where we will install additional functionality specific for the project we are working on. (We recommend creating a new environment for every project, as this lessens chances of conflicts, and prevents your “base” install of Python becoming overly-burdened with libraries that you don’t need.)

In Anaconda Navigator’s start screen, select “Environments” from the menu on the left. Now, at the bottom of the window, click “Import”, and select the environment.yml file that you downloaded. Name this new environment data-apps, then click to continue. Anaconda will now check that everything is in place, and install the dependencies. This can take a few minutes, so please be patient!

Once it is complete, you will see in the the Environments menu that `data-apps` now exists (probably below `base (root)`, which is your default Python install for Anaconda). Select `data-apps`, and return to the “Home” tab. We are now ready to start!
