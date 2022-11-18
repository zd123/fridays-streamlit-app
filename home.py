import streamlit as st
import pandas as pd


st.header('Welcome to my website')
st.markdown('Here is some **important info**. ')
input_text = st.text_input('First name')
print(input_text)

