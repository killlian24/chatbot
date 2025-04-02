from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from langchain.vectorstores import Chroma
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.embeddings import OllamaEmbeddings

app = FastAPI()

app.mount("/", StaticFiles(directory="/app", html=True), name="static")

class Query(BaseModel):
    question: str

@app.post("/chat")
def chat(query: Query):
    db = Chroma(persist_directory="./chroma_db", embedding_function=OllamaEmbeddings(model="mistral"))
    retriever = db.as_retriever()
    qa = RetrievalQA.from_chain_type(llm=Ollama(model="mistral"), retriever=retriever)
    answer = qa.run(query.question)
    return {"answer": answer}
