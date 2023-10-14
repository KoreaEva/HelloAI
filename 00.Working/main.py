import streamlit as st

st.header("Welcome to Python")
st.write('---')
st.write('# Test 1')


age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')