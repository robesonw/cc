# API Migration Notes

This frontend has been migrated from Base44 to REST API endpoints.

## Endpoint Mapping

- Base44 collections → `/api/{entity-slug}`
- GET collection → `GET /api/{entity-slug}?limit=&offset=&q=`
- GET item → `GET /api/{entity-slug}/{id}`
- CREATE → `POST /api/{entity-slug}`
- UPDATE → `PATCH /api/{entity-slug}/{id}`
- DELETE → `DELETE /api/{entity-slug}/{id}`

## Entity Slugs

Entity slugs should be in kebab-case (e.g., `recipe-items`, `user-profiles`).

## Payload Shapes

- For CREATE: Use the Create model (omit optional fields or send null when needed)
- For UPDATE: Use the Update model (partial updates)

## Usage

```typescript
import { apiClient } from './api/client';

// List items
const items = await apiClient.get('/api/recipes', { limit: 10, offset: 0 });

// Get single item
const item = await apiClient.get(`/api/recipes/${id}`);

// Create
const newItem = await apiClient.post('/api/recipes', { name: '...', ... });

// Update
const updated = await apiClient.patch(`/api/recipes/${id}`, { name: '...' });

// Delete
await apiClient.delete(`/api/recipes/${id}`);
```
