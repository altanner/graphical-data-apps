---
title: "• Why build data apps?"
subtitle: "Visualise, organise, share and collaborate."

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

### What are data apps?
An **app** (short for "application") is a computer program that provides an interface that allows users to input commands, and for the program to respond. Of course, that definition covers nearly all computer programs! But today the word "app" in general, refers to a program focussed on a particular task.

A **data app** is a type of app that is designed to work with data, allowing exploration of a dataset without requiring specific technical skills, and in generating visualisations. A data app can also be a **web app**, if it is deployed to the internet so that others can use it, usually through a web browser.

As such, data apps provide an interface for exploration, prototyping, developing hypotheses, and creating visualisations. They also provide a means of sharing data with others. A data app can be simple (perhaps just visualising the contents of a data set) or sophisticated (including user log-ins and profiles, connections to databases, multi-page analyses, and interactive visualisations).

### Data apps in Python
Until recently, building data apps has required good knowledge of the core web programming languages - HTML, CSS and JavaScript. These languages are uncommon in research or education, because they are not designed for computation or data-processing. As such, a gap has existed between those with general-purpose code skills (for example in Python, R, C++ etc) and those with web skills. To address this, libraries have been developed to bridge this gap between the "back end" (code that handles data management and computation) and the "front end" (code that generates the user interface, to be used without requiring technical skills (sometimes "front end" refers to the interface itself, rather than the code that generates it)).

In Python, a popular library for data app development is [Streamlit](https://streamlit.io/). This library aims to make building data apps as streamlined as possible - and includes easy ways to deploy your app. Streamlit also integrates with some popular Python data visualisation libraries. Altogether, this means we can build good-looking, user-friendly dashboards, in pure Python!

### Goals
In this course, our goal is to create a data app using Streamlit to explore a dataset (in this case, of wine characteristics!). Along the way, we will learn
- the basics of the Streamlit API
- how to make "widgets", interactive parts of our app
- how to bring data into a dataframe, the core data format for Streamlit
- how to generate visualisations, aiding exploration of the data.



