from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma
from strapi_loader import fetch_strapi_content

texts = fetch_strapi_content()
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.create_documents(texts)

embeddings = OllamaEmbeddings(model="mistral")
db = Chroma.from_documents(docs, embeddings, persist_directory="./chroma_db")
db.persist()
