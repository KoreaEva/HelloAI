import openai

openai.api_key = "e835aefd70124e6b80915bb4d2a722c8"
openai.azure_endpoint = "https://llmlab-openai-001.openai.azure.com/"
openai.api_type = 'azure'
openai.api_version = "2023-05-15"

#   MakeResume function
def MakeResume(name, job, content):
    resume = openai.chat.completions.create(
    model="dev-gpt-35-turbo", # engine = "deployment_name".
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

print('안녕하세요 반갑습니다. AI 이력서 생성기 입니다.')

# st.write('먼저 여러분의 이름을 입력하세요')
name = input('이름을 입력해 주세요: ')

if(name):
    print(name + '님 환영합니다.')

job = input('여러분들의 직업을 입력하세요 ex)회사원,소프트웨어 개발자,군인,크리에이터,작가\n')

if(job):
    print(job)

content = input('본인의 이력을 쓰세요:\n')
print(content)

input('엔터키를 입력하면 이력서를 생성합니다.\n')

print('Wait for it...')

result = MakeResume(name=name, job=job, content=content)

print('## 생성된 이력서')
print(result)