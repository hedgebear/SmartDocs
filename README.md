# 📄 SmartDocs API

**SmartDocs** é uma API desenvolvida com **FastAPI** que permite o upload de documentos e a realização de **perguntas com IA** baseadas no conteúdo desses documentos. A inteligência artificial é integrada com **LangChain**, **OpenAI** e **FAISS** para indexação vetorial e busca semântica eficiente.

---

## 🚀 Funcionalidades

- Upload de documentos `.txt` via API.
- Indexação automática dos documentos em uma base vetorial com FAISS.
- Consultas em linguagem natural (perguntas) respondidas com base no conteúdo do documento.
- Uso de modelos da OpenAI via LangChain.
- Banco de dados PostgreSQL para gerenciamento dos documentos enviados.
- Estrutura modular com rotas separadas para upload e consulta.

---

## 🧱 Tecnologias Utilizadas

- **Python 3.10**
- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL**
- **FAISS (Facebook AI Similarity Search)**
- **LangChain**
- **OpenAI API**
- **Docker**

---

## 📦 Estrutura do Projeto

```bash
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
```

---

## ⚙️ Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/hedgebear/SmartDocs.git
cd smartdocs
```

### 2. Defina sua chave da OpenAI
Crie um arquivo `.env` ou defina diretamente no terminal:
```bash
export OPENAI_API_KEY="sua-chave-openai"
```

### 3. Configure seu banco de dados PostgreSQL

Altere a string de conexão no arquivo `app/database.py`:
```python
DATABASE_URL = "postgresql://user:password@localhost/smartdocs"
```

Crie o banco e as tabelas:
```bash
# Usando o SQLAlchemy diretamente (ou Alembic se configurado)
python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"
```

### 4. Execute com Docker
```bash
docker build -t smartdocs .
docker run -d -p 8000:8000 -e OPENAI_API_KEY=sua-chave smartdocs
```

### 5. Teste a API
Acesse: [http://localhost:8000/docs](http://localhost:8000/docs)

Você verá a documentação interativa da API com Swagger.

---

## 🧠 Como Funciona a IA

- Os arquivos `.txt` enviados são divididos em pedaços com LangChain.
- Cada pedaço é transformado em vetores semânticos com embeddings da OpenAI.
- Os vetores são armazenados localmente usando FAISS.
- Ao receber uma pergunta, os vetores mais relevantes são buscados.
- A resposta é gerada com base nesses trechos e entregue via LLM da OpenAI.

---

## ✅ Exemplos de Uso

### Upload de Documento
`POST /upload/`  
Arquivo: `documento.txt`

### Fazer Pergunta
`POST /query/`  
Body:
```json
{
  "document_id": 1,
  "question": "Qual o propósito do documento?"
}
```

---

## 📌 Requisitos

- Conta na [OpenAI](https://platform.openai.com/)
- Docker ou Python 3.10+
- PostgreSQL 12+

---

## 📚 Extensões Futuras

- Suporte a múltiplos formatos (PDF, DOCX).
- Autenticação e autorização com OAuth2.
- Dashboard com Streamlit ou React.
- Indexação assíncrona e escalável.

---

## 🧑‍💻 Autor

Projeto pessoal mantido por Lucas Fernandes Mosqueira.

Sinta-se à vontade para contribuir ou sugerir melhorias!

