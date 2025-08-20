from fastapi import FastAPI, Request
from src.wrapper import resume_wrapper
from typing import Any

app = FastAPI()

@app.post("/generate")
def handle_request(resume_data: dict[str, Any]):
    resume_wrapper(resume_data)
    return {"response":"resume generated successfully"}

@app.middleware("http")
async def request_logger(request: Request, call_next):
    print(f"{request.method} {request.url}")
    response = await call_next(request)
    return response
