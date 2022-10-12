import streamlit as st
import datetime

d = st.date_input(
    "날짜를 선택하세요",
    datetime.date.today())

st.write('선택한 날짜:',d)