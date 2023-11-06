import openai
import streamlit as st

openai.api_key = "8a8e7d4d1700468f9bcafc6f48a89216"
openai.api_base = "https://helloairad.openai.azure.com/"
openai.api_type = 'azure'
openai.api_version = "2023-05-15"

st.header('Welcome to ChatGPT', divider='rainbow')
st.write('안녕하세요 반갑습니다. ChatGPT의 세계로 오신 것을 환영합니다.')

# st.write('먼저 여러분의 이름을 입력하세요')
name = st.text_input('작가명을 입력해 주세요')

if(name):
    st.write(name + '님 환영합니다.')

subject = st.text_input('시의 주제를 입력하세요')

if(subject):
    st.write(subject)

content = st.text_area('추가로 하고 싶은 이야기를 쓰세요')
st.write(content)

button_click = st.button('시 생성')

if(button_click):
    st.write('시 생성중')

    with st.spinner('Wait for it...'):
        resume = openai.ChatCompletion.create(
            engine="devmodel", # engine = "deployment_name".
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "작가의 이름은 " + name},
                {"role": "user", "content": "시의 주제는 " + subject},
                {"role": "user", "content": "상세 내용은" + content + '이다'},
                {"role": "user", "content": "시를 생성해줘"}        
                ]
        )
        st.success('Done!')

    st.write('## ChatGPT가 생성한 시')
    st.divider()
    st.write(resume.choices[0].message.content)