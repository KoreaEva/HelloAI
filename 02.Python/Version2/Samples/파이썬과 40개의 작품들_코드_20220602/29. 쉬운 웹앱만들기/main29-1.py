import streamlit as st

data_list = {5,5,6,6,7}
st.write('''
샘플데이터
''')

st.line_chart(data_list)