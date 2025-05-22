# app/routes/query.py
from fastapi import APIRouter
from app.schemas import QueryRequest, QueryResponse

router = APIRouter()

@router.post("/", response_model=QueryResponse)
def query_document(data: QueryRequest):
    # Simulando resposta de IA - a lógica real usará embeddings e LLM
    return QueryResponse(answer=f"Resposta simulada para: '{data.question}' no doc {data.document_id}")
