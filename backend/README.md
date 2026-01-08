# Generated Backend API

This is a generated FastAPI backend skeleton.

## Running the API

Using Docker Compose:
```bash
docker compose up --build
```

Using uvicorn directly:
```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

## API Endpoints

- `GET /api/health` - Health check endpoint

## Example API Usage

### Postgres Entity Example

```bash
# List entities
curl http://localhost:8080/api/user-link?limit=10&offset=0

# Create entity
curl -X POST http://localhost:8080/api/user-link \
  -H "Content-Type: application/json" \
  -d '{"user_id": "123", "target_id": "456"}'

# Get entity
curl http://localhost:8080/api/user-link/{id}

# Update entity
curl -X PUT http://localhost:8080/api/user-link/{id} \
  -H "Content-Type: application/json" \
  -d '{"user_id": "123", "target_id": "789"}'

# Delete entity
curl -X DELETE http://localhost:8080/api/user-link/{id}
```

### Mongo Entity Example

```bash
# List entities
curl http://localhost:8080/api/recipe?limit=10&offset=0&q=chicken

# Create entity
curl -X POST http://localhost:8080/api/recipe \
  -H "Content-Type: application/json" \
  -d '{"title": "Chicken Curry", "ingredients": [{"name": "chicken", "qty": 500}]}'

# Get entity
curl http://localhost:8080/api/recipe/{id}

# Update entity
curl -X PATCH http://localhost:8080/api/recipe/{id} \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Recipe"}'

# Delete entity
curl -X DELETE http://localhost:8080/api/recipe/{id}
```
