from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class problem(BaseModel):
    title : str
    url : str
    difficulty : str
    tags : list[str]


@app.get("/")
async def root():
    return {"message" : "Hello World"}

@app.get("/health")
async def health():
    return {"status" : "ok"}

@app.post("/problems")
async def problems(data : problem):
    title = data.title
    url = data.url
    return{
        "id" : 1,
        "title" : "Two Sum",
        "url" : "https://leetcode.com/problems/two-sum/",
        "difficulty" : "easy",
        "tags" : ["array","hash-map"],
        "solved" : False,
        "created_at" : "2026-09-15T10:00:00"
    }

# {
#   "id": 1,
#   "title": "Two Sum",
#   "url": "https://leetcode.com/problems/two-sum/",
#   "difficulty": "easy",
#   "tags": ["array", "hash-map"],
#   "solved": false,
#   "created_at": "2026-09-15T10:00:00"
# }

