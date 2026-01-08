# Generated Backend


# Culinary Compass - Full Stack Application

This is a monorepo containing the backend and frontend for Culinary Compass.

## Structure

- `/backend` - FastAPI backend application
- `/frontend` - React/Vite frontend application
- `/migrator-artifacts` - Migration artifacts and documentation

## Development Setup

### Prerequisites

- Docker and Docker Compose
- Node.js 18+ and npm
- Python 3.11+ (if running backend locally)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Start the backend services:
   ```bash
   docker compose up --build
   ```

   This will start:
   - API server at `http://localhost:8081`
   - PostgreSQL on port `5433`
   - MongoDB on port `27018`

3. Verify the backend is running:
   ```bash
   curl http://localhost:8081/health
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Create a `.env` file (copy from `.env.example`):
   ```bash
   cp .env.example .env
   ```

4. Start the development server:
   ```bash
   npm run dev
   ```

   The frontend will be available at `http://localhost:5173`

### Running Everything

1. In one terminal, start the backend:
   ```bash
   cd backend && docker compose up
   ```

2. In another terminal, start the frontend:
   ```bash
   cd frontend && npm run dev
   ```

## Environment Variables

### Frontend

- `VITE_API_BASE_URL` - Base URL for the API (default: `http://localhost:8081`)

See `frontend/.env.example` for more details.

## API Documentation

Once the backend is running, API documentation is available at:
- Swagger UI: `http://localhost:8081/docs`
- ReDoc: `http://localhost:8081/redoc`

## Testing

### Backend Smoke Test

```bash
cd backend
docker compose up -d
sleep 5  # Wait for services to start
curl http://localhost:8081/health
```

### Frontend Smoke Test

1. Start backend (see above)
2. Start frontend: `cd frontend && npm run dev`
3. Open `http://localhost:5173` in your browser
4. Verify the frontend loads and can connect to the backend
