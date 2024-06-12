import openai

openai.api_key = "e835aefd70124e6b80915bb4d2a722c8"
openai.azure_endpoint = "https://llmlab-openai-001.openai.azure.com/"
openai.api_type = 'azure'
openai.api_version = "2023-05-15"

print('안녕하세요 반갑습니다. AI 시인 입니다.')

name = input('작가명을 입력해 주세요: ')

if(name):
    print(name + '님 환영합니다.')

subject = input('시의 주제를 입력하세요: ')

if(subject):
    print(subject)

content = input('추가로 하고 싶은 이야기를 쓰세요: ')

input('엔터키를 누르면 시를 생성합니다')

print('Wait for it...')

result = openai.chat.completions.create(
        model="dev-gpt-35-turbo", # engine = "deployment_name".
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "작가의 이름은 " + name},
            {"role": "user", "content": "시의 주제는 " + subject},
            {"role": "user", "content": "상세 내용은" + content + '이다'},
            {"role": "user", "content": "시를 생성해줘"}        
            ]
    )


print('## ChatGPT가 생성한 시')
print(result.choices[0].message.content)