# app/services/embedding.py
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from app.services.utils import save_faiss_index

embeddings = OpenAIEmbeddings()
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)

FAISS_DIR = "vector_store"

import os
os.makedirs(FAISS_DIR, exist_ok=True)

def index_document(doc_id: int, file_path: str):
    loader = TextLoader(file_path)
    documents = loader.load()
    chunks = text_splitter.split_documents(documents)
    db = FAISS.from_documents(chunks, embeddings)
    save_faiss_index(db, os.path.join(FAISS_DIR, f"doc_{doc_id}"))