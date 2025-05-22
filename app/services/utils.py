# app/services/utils.py
import os
from langchain.vectorstores import FAISS

def save_faiss_index(index, path):
    index.save_local(path)

def load_faiss_index(path):
    return FAISS.load_local(path, embeddings=None)