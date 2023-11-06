import os
import openai
from langchain.chat_models import ChatOpenAI
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS

# api_key = "2988febbc1c947b590b8294e3f24a33d"
# api_base = "https://helloairad2.openai.azure.com"
# api_type = 'azure'
# api_version = "1"

api_key = "8a8e7d4d1700468f9bcafc6f48a89216"
api_base = "https://helloairad.openai.azure.com"
api_type = 'azure'
api_version = "2023-05-15"

# chatModel = ChatOpenAI( openai_api_key=api_key,
#                         openai_api_base=api_base,
#                         api_type=api_type,
#                         api_version=api_version,
#                         engine="devmodel",
#                         temperature=2)

# print(chatModel.predict('hi'))


# PDF 파일을 읽어온다.
reader = PdfReader("Demian.pdf")

raw_text = ""

for i, page in enumerate(reader.pages):
  text = page.extract_text()

  if text:
    raw_text += text

raw_text = raw_text.replace("Downloaded from https://www.holybooks.com"," ")
print(raw_text[:1000])


# PDF의 전체 내용을 요약한다.
from langchain import OpenAI
from langchain.chains import AnalyzeDocumentChain
from langchain.chains.summarize import load_summarize_chain

#llm = OpenAI(temperature=0)

llm = ChatOpenAI( openai_api_key=api_key,
                        openai_api_base=api_base,
                        api_type=api_type,
                        api_version=api_version,
                        engine="devmodel",
                        temperature=2)

summary_chain = load_summarize_chain(llm, chain_type="map_reduce")
summarize_document_chain = AnalyzeDocumentChain(combine_docs_chain=summary_chain)

print(summarize_document_chain.run(raw_text))