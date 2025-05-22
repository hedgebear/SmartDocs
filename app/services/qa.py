# app/services/qa.py
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from app.services.utils import load_faiss_index

FAISS_DIR = "vector_store"

llm = OpenAI(temperature=0)
chain = load_qa_chain(llm, chain_type="stuff")

def answer_question(doc_id: int, question: str) -> str:
    db = load_faiss_index(os.path.join(FAISS_DIR, f"doc_{doc_id}"))
    docs = db.similarity_search(question)
    return chain.run(input_documents=docs, question=question)