<div align="center">
  <h1>🧠 Quarry</h1>
  <p><strong>Knowledge Infrastructure Platform for Retrieval, Agents, and Production AI Systems</strong></p>

  <p>
    <a href="https://fastapi.tiangolo.com/"><img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI" /></a>
    <a href="https://www.postgresql.org/"><img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" /></a>
    <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" /></a>
    <img src="https://img.shields.io/badge/Security-JWT_Auth-success?style=for-the-badge" alt="Security" />
  </p>
</div>

---

## 🎯 Why Quarry Exists

Building reliable generative AI applications requires robust document ingestion, consistent chunking strategies, and low-latency semantic retrieval. Existing off-the-shelf vector database wrappers often couple infrastructure too tightly with orchestration logic. 

Quarry decouples these concerns, providing a dedicated, API-first service exclusively for document intelligence and vector retrieval. This architectural separation guarantees that engineering teams retain complete control over their RAG (Retrieval-Augmented Generation) pipelines and multi-tenant data isolation.

---

## 🏗️ Design Principles

- **API-First**: All system capabilities are exposed via strict, statically-typed REST endpoints.
- **Stateless Orchestration**: The API layer remains stateless; all state is durably persisted, allowing horizontal scalability.
- **Deterministic Processing**: Document chunking and embedding pipelines must yield predictable, testable outputs.
- **Relational Integrity First**: Before introducing specialized vector indexes, relational mapping (User -> Document -> Chunk) is enforced via a standard RDBMS to ensure strict access control and data integrity.

---

## 🚀 Current Capabilities

Quarry v1 is a functional, single-node document retrieval engine. It provides the core end-to-end pipeline required to securely upload a document, extract its text, compute dense vector representations, and query the resulting index.

* **🔒 Authentication**: Stateless, JWT-based bearer token authentication.
* **📄 Document Ingestion**: Synchronous PDF parsing and text extraction.
* **⚙️ Text Processing**: Deterministic sliding-window chunking logic.
* **🧠 Vector Generation**: In-memory dense embedding computation using local transformer models.
* **🔍 Semantic Search**: Similarity matching against processed chunks for contextual retrieval.

---

## 🔮 Future Vision

Quarry will evolve from a synchronous, single-node API into a distributed, highly observable infrastructure component capable of supporting asynchronous ingestion pipelines, hybrid search workloads, and autonomous agents at enterprise scale.

### Planned Stack Evolution
- **Caching & Queues**: Introduction of Redis for rate limiting and asynchronous task queues (e.g., Celery) to handle massive document ingestion workloads.
- **Vector Indexing**: Native `pgvector` integration, migrating from basic similarity search to optimized HNSW/IVFFlat indexes.
- **Observability**: Implementation of OpenTelemetry for distributed tracing, Prometheus for metrics, and Grafana for dashboards.
- **Deployment**: Containerization via Docker, orchestration via Kubernetes (Helm), and infrastructure as code via Terraform.

---

## 🏛️ System Architecture

```mermaid
graph TD
    Client[Client Application] -->|Auth Token| API[FastAPI Gateway]
    Client -->|PDF Upload| API
    Client -->|Search Query| API
    
    subgraph Core Services
        API -->|Raw File| PDFParser[PDF Extraction Service]
        PDFParser -->|Extracted Text| Chunker[Chunking Engine]
        Chunker -->|Text Chunks| Embedder[Embedding Pipeline]
        Embedder -->|Dense Vectors| Retrieval[Retrieval Service]
    end
    
    subgraph Persistence Layer
        API --> DB[(PostgreSQL)]
        Embedder --> DB
        Retrieval --> DB
    end
```

---

## ⚙️ Technology Stack

| Domain | Technologies | Purpose |
| :--- | :--- | :--- |
| **API & Routing** | FastAPI, Pydantic | High-performance async routing and strict data validation |
| **Data & Persistence** | PostgreSQL, SQLAlchemy | Relational datastore and Object-Relational Mapping |
| **Security** | python-jose, passlib | JWT cryptographic verification and password hashing |
| **Document Intelligence**| PyMuPDF, sentence-transformers | PDF parsing, text extraction, and dense vector generation |

---

## 🗺️ Quarry Evolution

### Quarry v1 — Foundation
✅ JWT Authentication  
✅ PostgreSQL  
✅ PDF Upload  
✅ Embedding Generation  
✅ Semantic Retrieval  

### Quarry v2 — Performance
⬜ Redis  
⬜ pgvector  
⬜ Docker  
⬜ Testing  

### Quarry v3 — Intelligence
⬜ LLM Integration  
⬜ Streaming  
⬜ Cost Tracking  

### Quarry v4 — Production RAG
⬜ Hybrid Search  
⬜ Reranking  
⬜ Evaluation  

---

## 🛠️ Local Development Setup

**1. Environment Setup**
```bash
git clone https://github.com/x2ankit/quarry.git
cd quarry
python -m venv venv
source venv/bin/activate  # Windows: `venv\Scripts\activate`
pip install -r requirements.txt
```

**2. Configuration**
Define your environment variables in a root `.env` file:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/quarry
SECRET_KEY=your_cryptographic_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**3. Database Initialization**
Generate the relational schemas against your local PostgreSQL instance:
```bash
python create_tables.py
```

**4. Server Execution**
Launch the ASGI server:
```bash
uvicorn app.main:app --reload
```
*API Documentation and OpenAPI spec available at `http://localhost:8000/docs`.*
