api_key = "2988febbc1c947b590b8294e3f24a33d"
api_base = "https://helloairad2.openai.azure.com/"
api_type = 'azure'
api_version = "2023-05-15"

from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader('Demian.pdf')
pages = loader.load_and_split()

print(pages[3])


from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False
)

texts = text_splitter.split_documents(pages)

print(texts[5])

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

embeddings_model = OpenAIEmbeddings(
                                        openai_api_key=api_key,
                                        openai_api_base=api_base,
                                        openai_api_type=api_type,
                                        openai_api_version=api_version,
                                        deployment="devmodel_emb"
                                    )

db = Chroma.from_documents(texts, embeddings_model)