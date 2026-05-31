# Hybrid GraphRAG Enterprise Chatbot

Role-Based Secure Enterprise Knowledge Assistant

---

## Features

- Supabase Authentication
- Role-Based Access Control
- Neo4j Knowledge Graph
- GraphRAG Retrieval
- Ollama Local LLM Routing
- Gemini Cloud LLM Routing
- Secure JWT Validation
- Chat History Storage
- Admin Dashboard
- Streaming Responses

---

## Architecture

User
↓
Supabase Auth
↓
JWT Validation
↓
Role Verification
↓
Neo4j Graph Retrieval
↓
Sensitivity Check
↓
Ollama OR Gemini
↓
Response
↓
Supabase Chat Storage

---

## User Roles

Developer
- Architecture Docs
- Security Docs
- Internal Policies

Intern
- Training Material
- Learning Resources

Client
- Public Company Information

Admin
- Full Access

---

## Local Development

### Backend

cd backend

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload

---

### Frontend

cd frontend

npm install

npm run dev

---

### Ollama

Install Ollama

Pull Mistral

ollama pull mistral

Run

ollama serve

---

### Neo4j

Create AuraDB Instance

Copy URI

Update .env

---

### Supabase

Create Project

Enable Authentication

Create Roles Table

Configure JWT

---

## Deployment

Frontend:
- Vercel

Backend:
- Railway

Database:
- Supabase

Graph:
- Neo4j Aura

LLMs:
- Ollama + Gemini

---

## Security Flow

Authentication First

JWT Validation

Role Filtering

Sensitivity Filtering

LLM Routing

Response Logging

---

## Future Enhancements

Document Upload

Graph Auto Builder

Fine-Tuned Models

Audit Logs

Multi-Tenant Support