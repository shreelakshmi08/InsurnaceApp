import streamlit as st
import time

st.write("STARTED ✅")

for i in range(5):
    st.write("Loading...", i)
    time.sleep(1)

st.write("FINISHED 🎉")