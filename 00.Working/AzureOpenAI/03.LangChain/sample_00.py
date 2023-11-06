from langchain.chat_models import AzureChatOpenAI
from langchain.llms import AzureOpenAI
#from langchain.llms import OpenAI

# api_key = "8a8e7d4d1700468f9bcafc6f48a89216"
# api_base = "https://helloairad.openai.azure.com"
# api_type = 'azure'
# api_version = "2023-05-15"

api_key = "2988febbc1c947b590b8294e3f24a33d"
api_base = "https://helloairad2.openai.azure.com/"
api_type = 'azure'
#api_version = "2023-05-15"
api_version = "2023-05-15"

print('Call AzureOpenAI')
chatModel = AzureChatOpenAI( openai_api_key=api_key,
                        openai_api_base=api_base,
                        openai_api_type=api_type,
                        openai_api_version=api_version,
                        deployment_name="devmodel2",
                        temperature=2,
                        )

# llm = OpenAI( openai_api_key=api_key,
#                         openai_api_base=api_base,
#                         api_type=api_type,
#                         api_version=api_version,
#                         engine="devmodel",
#                         temperature=0)

print(chatModel.predict('I like USA'))
