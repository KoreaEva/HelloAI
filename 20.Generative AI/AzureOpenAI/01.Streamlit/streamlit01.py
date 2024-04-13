import streamlit as st

st.write('# Progress')
st.write('---')
st.write('## raw data')
view = [10,50,30]
view

st.write('## bar chart')
st.bar_chart(view)
