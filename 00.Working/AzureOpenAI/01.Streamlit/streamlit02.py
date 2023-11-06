import streamlit as st

st.header('Welcome to ChatGPT', divider='rainbow')
st.write('안녕하세요 반갑습니다. ChatGPT의 세계로 오신 것을 환영합니다.')

# st.write('먼저 여러분의 이름을 입력하세요')
name = st.text_input('이름을 입력해 주세요')

if(name):
    st.write(name + '님 환영합니다.')

job = st.selectbox('여러분들의 직업을 선택하세요',('회사원','소프트웨어 개발자','군인','크리에이터','작가'))

if(job):
    st.write(job)

content = st.text_area('본인의 이력을 쓰세요')
st.write(content)

button_click = st.button('이력서 생성')
if(button_click):
    st.write('Clicked')