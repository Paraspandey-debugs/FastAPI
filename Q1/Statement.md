**Target API to build:** `CP Problem Tracker API` — a personal API to log competitive programming problems you attempt.

**First PS: CP Problem Tracker API v0 — In-Memory CRUD**

### Background
You solve CP problems and want to track them: title, link, difficulty, tags, solved status. Build a REST API for this. No DB yet. Store everything in a Python dict/list.

### Functional requirements
1. `GET /health`  
   Returns `200` with `{"status": "ok"}`

2. `POST /problems`  
   Body:
   ```json
   {
     "title": "Two Sum",
     "url": "https://leetcode.com/problems/two-sum/",
     "difficulty": "easy",
     "tags": ["array", "hash-map"]
   }
   ```
   Returns `201` with:
   ```json
   {
     "id": 1,
     "title": "Two Sum",
     "url": "https://leetcode.com/problems/two-sum/",
     "difficulty": "easy",
     "tags": ["array", "hash-map"],
     "solved": false,
     "created_at": "2026-09-15T10:00:00"
   }
   ```

3. `GET /problems`  
   Returns list of all problems.  
   Optional query filters:
   - `?difficulty=easy`
   - `?tag=array`
   - `?solved=false`

4. `GET /problems/{problem_id}`  
   Returns one problem or `404`.

5. `PATCH /problems/{problem_id}`  
   Partial update. Example: change title, difficulty, tags, or solved.  
   Returns updated problem or `404`.

6. `DELETE /problems/{problem_id}`  
   Returns `204` on success, `404` if not found.

7. `POST /problems/{problem_id}/solve`  
   Marks `solved: true`. Returns updated problem or `404`.

### Data model constraints
- `id`: int or UUID
- `title`: string, min length 1
- `url`: string / `HttpUrl`
- `difficulty`: enum: `easy`, `medium`, `hard`
- `tags`: list of strings, default `[]`
- `solved`: bool, default `false`
- `created_at`: datetime

### Rules
- In-memory only. No database.
- Use FastAPI + Pydantic only.
- Must expose auto docs at `/docs`.
- Use correct HTTP status codes.
- Validation errors should return `422`.

### Acceptance test
Run:
```bash
uvicorn main:app --reload
```

Then check:
```bash
curl localhost:8000/health
curl localhost:8000/docs
curl -X POST localhost:8000/problems -H "Content-Type: application/json" -d '{"title":"Two Sum","url":"https://leetcode.com/problems/two-sum/","difficulty":"easy","tags":["array","hash-map"]}'
curl localhost:8000/problems
curl "localhost:8000/problems?difficulty=easy&tag=array"
curl localhost:8000/problems/1
curl -X POST localhost:8000/problems/1/solve
curl -X DELETE localhost:8000/problems/1
```

Also test:
- Creating with empty title → `422`
- Getting missing ID → `404`
- Invalid difficulty → `422`

### Google these as you build
- FastAPI first steps
- FastAPI path parameters
- FastAPI query parameters
- FastAPI request body
- Pydantic BaseModel
- Pydantic Field
- Python Enum in FastAPI
- FastAPI HTTPException
- FastAPI status codes
- FastAPI response_model
- FastAPI APIRouter
- FastAPI TestClient

