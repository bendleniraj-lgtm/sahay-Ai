# Sahay AI

Sahay AI is a starter full-stack application for an AI assistant platform. This repository includes a FastAPI backend and a React frontend, with Docker support for local development.

## Stack

- Backend: Python, FastAPI, Uvicorn
- Frontend: React, Vite
- Database: PostgreSQL
- Dev workflow: Docker Compose

## Project structure

```text
sahay-Ai/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   └── main.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── src/
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
├── .env.example
├── .gitignore
├── docker-compose.yml
├── README.md
└── LICENSE
```

## Prerequisites

- Docker and Docker Compose
- Node.js 18+
- Python 3.11+

## Local development

1. Copy environment variables:

```bash
cp .env.example .env
```

2. Start all services:

```bash
docker-compose up --build
```

This starts:

- Backend: http://localhost:8000
- Frontend: http://localhost:5173
- PostgreSQL: localhost:5432

## Run manually without Docker

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0
```

## API endpoints

- GET `/` - API welcome message
- GET `/api/health` - Health check
- POST `/api/chat` - Example AI chat endpoint

## Notes

This is a starter scaffold intended to be extended with real AI logic, auth, database models, and deployment configuration.
