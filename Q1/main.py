from fastapi import FastAPI, HTTPException ,status
from pydantic import BaseModel,Field
app = FastAPI()

class problem(BaseModel):
    id : int
    title : str
    url : str
    difficulty : str
    tags : list[str]
id = 0

@app.get("/")
async def root():
    return {"message" : "Hello World"}

@app.get("/health")
async def health():
    return {"status" : "ok"}

problist = []

@app.post("/problems")
async def problems(data : problem):
    global id
    id = id + 1
    data.id = id
    title = data.title
    url = data.url
    tag = data.tags
    difficulty = data.difficulty
    problist.append(data)
    return{
        "id" : id,
        "title" : title,
        "url" : url,
        "difficulty" : difficulty,
        "tags" : tag,
        "solved" : False,
        "created_at" : "2026-09-15T10:00:00"
    }

class Response(BaseModel):
    data: list[dict] = Field(default_factory=list)
    
@app.get("/problems", response_model=Response)
async def get_problems(
    difficulty: str | None = None,
    tag: str | None = None,
    solved: bool | None = None
):
    response = Response()

    for data in problist:
        if difficulty is not None and data.difficulty != difficulty:
            continue

        if tag is not None and tag not in data.tags:
            continue

        response.data.append(data.model_dump())

    return response

@app.get("/problems/{problemid}")
async def get_problem(problemid : int):
    for data in problist:
        if data.id == problemid : 
            return data
    return HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Problem not found"
    )
# {
#   "id": 1,
#   "title": "Two Sum",
#   "url": "https://leetcode.com/problems/two-sum/",
#   "difficulty": "easy",
#   "tags": ["array", "hash-map"],
#   "solved": false,
#   "created_at": "2026-09-15T10:00:00"
# }

