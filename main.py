from fastapi import FastAPI, Query
from typing import List
import json

app = FastAPI()

with open("q-vercel-python.json", "r") as f:
    all_data = json.load(f)

@app.get("/api")
def filter_data(
    name: List[str] = Query(...),
    marks_min: int = Query(0),
    marks_max: int = Query(100)
):
    marks = [
        entry["marks"] for entry in all_data
        if entry["name"] in name and marks_min <= entry["marks"] <= marks_max
    ]
    return {"marks": marks}
