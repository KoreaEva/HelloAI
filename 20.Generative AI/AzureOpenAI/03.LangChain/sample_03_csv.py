
api_key = "2988febbc1c947b590b8294e3f24a33d"
api_base = "https://helloairad2.openai.azure.com/"
api_type = 'azure'
api_version = "2023-05-15"

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/kairess/toy-datasets/master/titanic.csv")

print(df.head())

from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain.agents import AgentType
from langchain.llms import AzureOpenAI
agent = create_pandas_dataframe_agent(AzureOpenAI(temperature=0,
                                        openai_api_key=api_key,
                                        openai_api_base=api_base,
                                        openai_api_type=api_type,
                                        openai_api_version=api_version,
                                        deployment_name="devmodel"),
                                    df=df,
                                    #AgentType=AgentType.OPENAI_FUNCTIONS,
                                    verbose=True)
                                    #agent_type=AgentType.OPENAI_FUNCTIONS)

#print(agent.run('how many rows are there'))
print(agent.run('What is the average age of passengers?'))
#print(agent.run('행이 몇 개지?'))
#print(agent.run('승객들의 평균 연령은?'))
#print(agent.run('여자 승객들의 평균 연령은?'))
#print(agent.run('객실 등급과 성별에 따른 생존자 수를 계산해줘'))


#langchain_experimental.agents.create_pandas_dataframe_agent