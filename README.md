<div align="center">
  <h1>🧠 Quarry</h1>
  <p><strong>Premium AI Knowledge Infrastructure & Document Intelligence Platform</strong></p>

  <p>
    <a href="https://fastapi.tiangolo.com/"><img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI" /></a>
    <a href="https://www.postgresql.org/"><img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" /></a>
    <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" /></a>
    <img src="https://img.shields.io/badge/Security-JWT_Auth-success?style=for-the-badge" alt="Security" />
  </p>
</div>

---

## 🌟 Overview

**Quarry** is a production-grade AI Knowledge Infrastructure Platform engineered to process, store, and semantically retrieve document data at scale. 

It solves the foundational challenge of building scalable **Agentic workflows** by providing a robust, high-performance pipeline for document ingestion, dense vector embedding, and semantic search. Our vision is to evolve Quarry into a comprehensive ecosystem natively supporting hybrid search, advanced AI agents, and deep observability.

---

## ⚡️ Key Features

* **🔒 Enterprise Security**: Secure user authentication and authorization pipelines powered by JSON Web Tokens (JWT).
* **📄 Scalable Ingestion**: High-throughput PDF and document upload architecture.
* **⚙️ Intelligent Processing**: Automated text extraction combined with smart chunking strategies.
* **🧠 Vector Embeddings**: State-of-the-art dense vector representations using advanced transformer models.
* **🔍 Semantic Retrieval**: High-performance semantic search engine to surface the most contextually relevant data.

---

## 🏗️ Architecture

Quarry is architected upon strict **Domain-Driven Design** principles to ensure absolute maintainability and clean separation of concerns:

* **🌐 API Layer**: Lightning-fast endpoints built on `FastAPI` for routing, strict validation, and seamless serialization.
* **🛠️ Service Utilities**: Modular and decoupled pipelines for PDF parsing, text chunking, and vector embedding.
* **🗃️ Data Access**: `SQLAlchemy` ORM powering reliable relational mapping and efficient database sessions.
* **💾 Persistence**: `PostgreSQL` engine managing complex, robust relationships between Users, Documents, and Embedded Chunks.

---

## 🧰 Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **FastAPI** | High-performance async web framework |
| **PostgreSQL** | Primary relational database |
| **SQLAlchemy** | Object-Relational Mapping (ORM) |
| **JWT** | Secure token-based authentication |
| **Pydantic** | Strict data validation & serialization |
| **PyMuPDF** | Advanced PDF parsing & extraction |
| **Sentence Transformers**| Dense vector embedding generation |

---

## 📂 Project Structure

```text
app/
├── api/          # Route handlers & API endpoints
├── db/           # Database engine & session dependencies
├── models/       # SQLAlchemy ORM schemas
├── schemas/      # Pydantic data validation models
├── utils/        # Core AI, chunking, and security logic
└── main.py       # Application entrypoint
```

---

## 🚀 Quick Start

> [!IMPORTANT]
> Ensure you have Python 3.9+ and PostgreSQL installed locally before proceeding.

**1. Clone & Navigate**
```bash
git clone https://github.com/x2ankit/quarry.git
cd quarry
```

**2. Virtual Environment Setup**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: `venv\Scripts\activate`
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Database Initialization**
```bash
# Ensure your local PostgreSQL instance is running
python create_tables.py
```

**5. Launch the Engine**
```bash
uvicorn app.main:app --reload
```
*API Documentation will be instantly available at `http://localhost:8000/docs`.*

---

## 🔐 Environment Variables

Create a `.env` file at the root of your project:

```env
# Database Configuration
DATABASE_URL=postgresql://user:password@localhost:5432/quarry

# Security Keys
SECRET_KEY=your_cryptographic_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 🗺️ API Overview

| Endpoint | Description |
| :--- | :--- |
| `POST /api/auth/*` | Registration, login, and JWT generation |
| `POST /api/upload` | Secure ingestion of PDF documents |
| `GET /api/documents` | Management and inspection of processed data |
| `POST /api/chat` | Semantic search and contextual retrieval queries |
| `GET /health` | System readiness and health probes |

---

## 🔮 Roadmap

### Quarry v2 — Knowledge Retrieval Foundation

**✅ Completed**
- [x] Authentication Pipeline
- [x] Document Upload Service
- [x] Embedding Generation
- [x] Semantic Retrieval

**🚀 Upcoming**
- [ ] Redis Caching Layer
- [ ] Native `pgvector` Integration
- [ ] Hybrid Search Capabilities
- [ ] Neural Reranking
- [ ] Evaluation Frameworks
- [ ] Agentic Workflows
- [ ] Deep Observability

---

## 📊 Development Status

Quarry is currently in **active development**, accelerating towards the highly anticipated v2 milestone. The foundational infrastructure for processing and retrieval is battle-tested, while advanced caching, hyper-scale search capabilities, and production deployment mechanisms are actively being engineered.

---

<div align="center">
  <i>Engineered for scale. Built for the future of AI.</i>
</div>
