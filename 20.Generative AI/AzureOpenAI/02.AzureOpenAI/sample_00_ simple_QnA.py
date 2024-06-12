import openai

openai.api_key = "e835aefd70124e6b80915bb4d2a722c8"
openai.azure_endpoint = "https://llmlab-openai-001.openai.azure.com/"
openai.api_type = 'azure'
openai.api_version = "2023-05-15"

query = input('궁금한 내용을 입력하세요: ')

result = openai.chat.completions.create(
        model="dev-gpt-35-turbo", # engine = "deployment_name".
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": query + "가 뭐니"}  
            ]
    )

print(result.choices[0].message.content)