---
title: "7 • Advanced topics II : sharing and deploying"
subtitle: "Powerful things that are worth pointing out."

date: 2023-02-17T00:00:00+01:00

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

## Options for sharing your data app
There are a few ways to share your app with people, and it will be worth doing a search for current options, as these will change with the times.

### Streamlit Cloud
The easiest way to deploy is through [Streamlit Cloud](https://streamlit.io/cloud). The only requirement is that you have a [GitHub](https://github.com/) account - the GitHub repo then acts as the source for the app being run by Streamlit Cloud. [Full instructions on how to do this are here](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app) - they are very easy to follow!

For small apps, hosting of your app is free. If data usage or visit counts are high, you might need to start a paid tier.

### Heroku
[Heroku](https://www.heroku.com/) is another cloud service provider with special channels for deploying Streamlit apps. For current instructions on how to do this, it will be best to do a search as those instructions will update often.

### Sharing Python code
If the person you are sharing with can run Python, you can just share your repository (or a folder of the script files). They can then install Streamlit, and run the app locally. This is a good option if you have data which needs to remain private.

### Streamlit Desktop App
This is fairly new in development, but it may be possible to create an [executable desktop app of Streamlit](https://discuss.streamlit.io/t/streamlit-wasm-electron-desktop-app/31655). Again, look up current articles and threads on the best way to do this.

## Some final things to highlight!
As of 2023, Streamlit is still rapidly acquiring new functionality. Here are some things that are very powerful for creating a more sophisticated app:
### Session state
The session state allows you to store variables across runs, and is generally useful for organising data across your app. Learn how to use it [here.](https://docs.streamlit.io/library/api-reference/session-state).
### Interactive dataframes
Being able to edit or add data in the native app is a useful feature. Check [here](https://blog.streamlit.io/editable-dataframes-are-here/) for current news on how this is done in Streamlit (keep in mind this link might change one day - if it doesn't work, do a search instead!)
### Data linkage
Streamlit is built to work with the APIs of major [data infrastructure and software](https://docs.streamlit.io/knowledge-base/tutorials/databases), including SQLite, AWS and MongoDB.
