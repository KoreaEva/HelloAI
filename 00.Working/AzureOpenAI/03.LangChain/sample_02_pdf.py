api_key = "2988febbc1c947b590b8294e3f24a33d"
api_base = "https://helloairad2.openai.azure.com/"
api_type = 'azure'
api_version = "2023-05-15"

import os
import openai
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS


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
from langchain.llms import AzureOpenAI
from langchain.chains import AnalyzeDocumentChain
from langchain.chains.summarize import load_summarize_chain

llm = AzureOpenAI(temperature=0,
                    openai_api_key=api_key,
                    openai_api_base=api_base,
                    openai_api_type=api_type,
                    openai_api_version=api_version,
                    deployment_name="devmodel",)
summary_chain = load_summarize_chain(llm, chain_type="map_reduce")
summarize_document_chain = AnalyzeDocumentChain(combine_docs_chain=summary_chain)

print('---------------------------------------------')
print(summarize_document_chain.run(raw_text))


from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import AzureChatOpenAI

model = AzureChatOpenAI(temperature=0,
                    openai_api_key=api_key,
                    openai_api_base=api_base,
                    openai_api_type=api_type,
                    openai_api_version=api_version,
                    deployment_name="devmodel2",)
qa_chain = load_qa_chain(model, chain_type="map_reduce")
qa_document_chain = AnalyzeDocumentChain(combine_docs_chain=qa_chain)


print(qa_document_chain.run(
    input_document = raw_text,
    question = "싱클레어를 괴롭힌 사람은?"
))
     