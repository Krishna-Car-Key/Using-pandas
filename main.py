import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("Best Company")

contents = """As of May 2023, Apple retained its dominance,
 holding the position of the world's largest company with a
  staggering market capitalisation of 2.75 trillion U.S. dollars. Despite
  occasional changes in the top spot, Apple's remarkable market 
  cap underscored its continued significance in the business world."""

st.write(contents)

st.subheader("Our Teams")

col1, empty1, col2, empty2, col3 = st.columns([2, 1, 2, 1, 2])

dv = pandas.read_csv("data.csv", sep=",")

with col1:
    for index, rows in dv[:4].iterrows():
        st.subheader(f"{rows['first name']}  {rows['last name']}")
        st.write(rows['role'])
        st.image(f"images/{rows['image']}")

with col2:
    for index, rows in dv[4:8].iterrows():
        st.subheader(f"{rows['first name']}  {rows['last name']}")
        st.write(rows['role'])
        st.image(f"images/{rows['image']}")

with col3:
    for index, rows in dv[8:].iterrows():
        st.subheader(f"{rows['first name']}  {rows['last name']}")
        st.write(rows['role'])
        st.image(f"images/{rows['image']}")

