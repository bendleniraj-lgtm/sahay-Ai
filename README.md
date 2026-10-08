# Sahay AI

Sahay AI is an intelligent assistant platform designed to provide personalized help and support through AI-powered conversations.

## Features

- 🤖 AI-powered conversational interface
- 💬 Natural language understanding and generation
- 🔧 Modular architecture for easy customization
- 📚 Knowledge base integration
- 🔐 Secure and private conversations
- ⚡ Fast response times

## Tech Stack

- **Backend:** Python with FastAPI
- **AI/ML:** LangChain, OpenAI API
- **Database:** PostgreSQL
- **Frontend:** React (TypeScript)
- **Deployment:** Docker, Kubernetes

## Project Structure

```
sahay-Ai/
├── backend/              # FastAPI backend application
│   ├── app/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── main.py
├── frontend/             # React TypeScript application
│   ├── src/
│   ├── public/
│   └── package.json
├── docs/                 # Documentation
├── tests/                # Test suite
├── docker-compose.yml    # Local development setup
├── .env.example          # Environment variables template
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- Docker & Docker Compose
- PostgreSQL 14+

### Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/bendleniraj-lgtm/sahay-Ai.git
   cd sahay-Ai
   ```

2. **Set up environment variables:**
   ```bash
   cp .env.example .env
   ```

3. **Start services with Docker:**
   ```bash
   docker-compose up -d
   ```

4. **Install backend dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

5. **Run backend:**
   ```bash
   python main.py
   ```

6. **Install frontend dependencies:**
   ```bash
   cd ../frontend
   npm install
   npm start
   ```

Backend API will be available at `http://localhost:8000`
Frontend will be available at `http://localhost:3000`

## Development

### Running Tests

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd ../frontend
npm test
```

### Code Quality

```bash
# Backend linting
python -m flake8 app/
python -m black app/

# Frontend linting
npm run lint
```

## API Documentation

API documentation is available at `http://localhost:8000/docs` (Swagger UI)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, email support@sahayai.com or open an issue on GitHub.
