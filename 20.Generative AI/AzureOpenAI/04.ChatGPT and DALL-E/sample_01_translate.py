import openai
import openai as openai2
import os
import streamlit as st

openai.api_key = "cb284a91af4a483a9d427533b0ae6a18"
openai.api_base = "https://helloairadgpt.openai.azure.com/"
openai.api_type = 'azure'
openai.api_version = "2023-05-15"
user_prompt = ''

st.header('Welcome to ChatGPT', divider='rainbow')
st.write('안녕하세요 반갑습니다. 생성형 화가 입니다.')

# st.write('먼저 여러분의 이름을 입력하세요')
content = st.text_area('표현 하려는 작품을 설명해 주세요')

if(content):
    st.write('입력해 주신 내용을 프롬프트로 만들기 위해서 영어로 번역해 보겠습니다. ')

    button_click = st.button('번역')

    if(button_click):
        st.write('번역중')

        with st.spinner('Wait for it...'):
            resume = openai.ChatCompletion.create(
                engine="devgpt35", # engine = "deployment_name".
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "이 내용을 영어로 번역해줘 그리고 번역된 결과만 보여줘 " + content},
                    ]
            )
            st.success('Done!')

        st.write('## 번역 결과')
        st.divider()
        prompt = resume.choices[0].message.content
        st.write(prompt)
        
