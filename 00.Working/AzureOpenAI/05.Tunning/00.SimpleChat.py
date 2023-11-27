import openai
import streamlit as st

openai.api_key = "cb284a91af4a483a9d427533b0ae6a18"
openai.api_base = "https://helloairadgpt.openai.azure.com/"
openai.api_type = 'azure'
openai.api_version = "2023-05-15"

st.header('Welcome to ChatGPT', divider='rainbow')
st.write('안녕하세요 반갑습니다. ChatGPT의 세계로 오신 것을 환영합니다.')

# st.write('먼저 여러분의 이름을 입력하세요')
query = st.text_input('궁금한 내용을 입력하세요')

if(query):
    st.write(query + '가 궁금하셨군요.')

button_click = st.button('Query')

if(button_click):
    st.write('Thinking...')

    with st.spinner('Wait for it...'):
        resume = openai.ChatCompletion.create(
            engine="devgpt35", # engine = "deployment_name".
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query + "가 뭐니"}  
                ]
        )
        st.success('Done!')

    st.write('## Result')
    st.divider()
    st.write(resume.choices[0].message.content)