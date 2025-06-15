# Risk Analytics Dashboard - Architecture

This document summarizes the high level design for the Risk Analytics Dashboard. The system provides real-time monitoring of more than 30 risk indicators across eight business units.

## System Overview
- Frontend built with React and D3.js for rich visualizations.
- Backend implemented using FastAPI and WebSockets for real-time updates.
- Risk calculation engine processes data streamed through Kafka and stores results in a time series database.

## Main Components
```
Frontend (React + D3.js)
  - Dashboard Components
  - Real-time Charts
  - Alert Manager

API Layer (FastAPI)
  - Risk API
  - Metrics API
  - Alert API

Risk Calculation Engine
  - Indicator Calculator
  - Aggregation Engine
  - Alert Engine

Data Pipeline
  - Kafka Streams
  - Time Series Database
  - Historical Data Store
```

## Risk Indicator Framework
The platform covers eight risk categories (Operational, Financial, Compliance, Security, Reputational, Strategic, Technology, Vendor) and evaluates indicators using a normalized 0-100 scoring model with threshold-based alerts.

## Data Models
Key data structures are represented in `backend/app/models.py`.

## Running Locally
Follow the instructions in the project README to start the backend. The frontend folder contains a placeholder for future development.
