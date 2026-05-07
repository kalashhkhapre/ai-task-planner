from fastapi import FastAPI
from pydantic import BaseModel

from app.workflows.planner_graph import graph


class PlanRequest(BaseModel):
    goal: str


app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Planner Running"}


@app.post("/plan")
def plan(request: PlanRequest):
    result = graph.invoke({"goal": request.goal}) # type: ignore
    return result
