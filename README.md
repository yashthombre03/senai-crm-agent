# SenAI CRM Agent

An AI-powered CRM Email Intelligence System built using FastAPI, LangGraph, Groq, ChromaDB, and Streamlit.

The system ingests incoming customer emails, maintains conversation threads, performs sentiment analysis and intent classification, retrieves company knowledge using RAG, generates AI-assisted responses, and escalates critical cases to human support.

---

# Features

## Email Ingestion

- Accept incoming emails through REST APIs
- Store emails in SQLite database
- Prevent duplicate message ingestion

## Contact Management

- Automatically create and track contacts
- Maintain customer communication history

## Thread Management

- Group emails into conversation threads
- Track thread history for contextual understanding

## Sentiment Analysis

- Detect customer sentiment
- Positive
- Neutral
- Negative

## Email Classification

Classifies emails into categories such as:

- Billing
- Complaint
- Feature Request
- General Inquiry

## Retrieval-Augmented Generation (RAG)

- Stores company knowledge base in ChromaDB
- Retrieves relevant policy and documentation
- Supplies context to the AI agent

## LangGraph Agent Workflow

Agent performs:

1. Classification
2. Sentiment Analysis
3. Escalation Check
4. Knowledge Retrieval
5. Response Generation

## Human Escalation

Automatically escalates:

- Legal threats
- Security incidents
- High-risk emails

## Audit Logging

Tracks every agent decision for transparency and debugging.

## Interactive Dashboard

Built using Streamlit.

Provides:

- Email Analytics
- Thread Viewer
- Email Inspector
- AI Actions
- Escalation Monitoring
- Sentiment Distribution
- Category Distribution
- Audit Logs

---

# Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- SQLite

## AI & Agent Framework

- LangGraph
- LangChain
- Groq

## RAG

- ChromaDB
- HuggingFace Embeddings

## Frontend

- Streamlit

---

# Project Structure

```text
SenAI CRM Agent
│
├── backend
│   ├── api
│   ├── database
│   ├── models
│   ├── schemas
│   └── services
│
├── agent
│   ├── graph.py
│   ├── nodes.py
│   └── state.py
│
├── rag
│   ├── build_vectorstore.py
│   ├── retriever.py
│   └── knowledge_base.txt
│
├── simulator
│   └── replay_emails.py
│
├── frontend
│   └── dashboard.py
│
├── chroma_db
│
├── requirements.txt
│
└── README.md
```

---

# System Architecture

```text
Email Dataset
      │
      ▼
Replay Simulator
      │
      ▼
FastAPI Ingestion
      │
      ▼
Contact Management
      │
      ▼
Thread Management
      │
      ▼
Classification
      │
      ▼
Sentiment Analysis
      │
      ▼
LangGraph Agent
      │
 ┌────┴─────────┐
 ▼              ▼
RAG       Human Escalation
 ▼
Groq LLM
      │
      ▼
Actions Table
      │
      ▼
Audit Logs
      │
      ▼
Streamlit Dashboard
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd senai-crm-agent
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# Build Vector Database

```bash
python rag/build_vectorstore.py
```

---

# Create Database

```bash
python backend/database/create_db.py
```

---

# Replay Email Dataset

```bash
python simulator/replay_emails.py
```

---

# Run Backend

```bash
uvicorn backend.api.main:app --reload
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# Run Dashboard

```bash
streamlit run frontend/dashboard.py
```

---

# API Endpoints

## Email Ingestion

```http
POST /api/ingest
```

## Contacts

```http
GET /contacts
```

## Threads

```http
GET /threads/{thread_id}
```

## Sentiment Analytics

```http
GET /analytics/sentiment
```

## RAG Query

```http
POST /rag/query
```

## Actions

```http
GET /actions
```

## Audit Logs

```http
GET /audit
```

---

## Documentation

Additional project documentation can be found in the `docs/` directory:

- Architecture Diagram (`docs/architecture.md`)
- ER Diagram (`docs/er_diagram.md`)
- OpenAPI Specification (`docs/openapi.json`)
- Database Schema (`docs/schema.sql`)