import streamlit as st

# set the tab title and page width
st.set_page_config(page_title="Demo App", layout="wide")

# build the sidebar
with st.sidebar:
    # put a title in the sidebar
    st.title("World Demographics")

# create two columns, of ratio 5:1
column1, column2 = st.columns([5,1])

# place info box in first column
with column1:
    st.info("Welcome to the global demographic data explorer app!")

# place image into second column
with column2:
    st.image("globe.png")
