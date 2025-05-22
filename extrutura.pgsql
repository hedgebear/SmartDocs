app/
├── main.py                 # Inicialização da aplicação FastAPI
├── models.py               # Modelo de documento (ORM)
├── schemas.py              # Schemas Pydantic para validação
├── database.py             # Conexão com o banco de dados
├── routes/
│   ├── upload.py           # Rota para upload de documentos
│   └── query.py            # Rota para perguntas
├── services/
│   ├── embedding.py        # Indexação de documentos com embeddings
│   ├── qa.py               # Consulta e resposta com LLM
│   └── utils.py            # Utilitários para salvar/carregar índices
uploads/                    # Pasta onde os arquivos são salvos
vector_store/              # Índices vetoriais gerados por documento
requirements.txt
Dockerfile
README.md
