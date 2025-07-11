# Risk-Analytics-Dashboard

This repository contains a skeleton implementation of the Risk Analytics Dashboard project. It includes a FastAPI backend and a placeholder for the React frontend.

## Backend

The backend is built with **FastAPI** and uses Pydantic settings for
configuration. Copy `.env.example` to `.env` and adjust if needed. To run
the API locally:

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Run the test suite with:

```bash
cd backend
pytest
```

The API exposes simple endpoints under `/risk`, `/metrics`, and `/alerts`.

## Frontend

The frontend folder contains the starting point for a React application using TypeScript. Additional implementation is required to complete the dashboard.

## Documentation

See `docs/architecture.md` for the detailed architecture and design notes.
