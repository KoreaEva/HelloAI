import os
import openai
from dotenv import load_dotenv
load_dotenv()


#openai.api_key = "8a8e7d4d1700468f9bcafc6f48a89216"
openai.api_base = "https://helloairad.openai.azure.com/"
openai.api_type = 'azure'
openai.api_version = "2023-05-15"


response = openai.ChatCompletion.create(
    engine="devmodel", # engine = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": " 이력서를 작성해 주세요"}
#        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
#        {"role": "user", "content": "Do other Azure AI services support this too?"}
    ]
)

print(response)
print(response['choices'][0]['message']['content'])