import openai
import streamlit as st

openai.api_key = "8a8e7d4d1700468f9bcafc6f48a89216"
openai.api_base = "https://helloairad.openai.azure.com/"
openai.api_type = 'azure'
openai.api_version = "2023-05-15"

def MakeResume(name, job, content):
    resume = openai.ChatCompletion.create(
    engine="devmodel", # engine = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "내 이름은" + name},
        {"role": "user", "content": job + ' 업종에 지원하기 위해서 이력서를 쓰고 있다.'},
        {"role": "user", "content": "상세 내용은" + content + '이다'},
        {"role": "user", "content": "이력서를 생성해줘"}        
        ]
    )
    result = resume.choices[0].message.content
    return result

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
    st.write('이력서 생성중')

    with st.spinner('Wait for it...'):
        result = MakeResume(name=name, job=job, content=content)
        st.success('Done!')

    st.write('## 생성된 이력서')
    st.divider()
    st.write(result);