from fastapi import FastAPI, Query
from typing import List
import json

app = FastAPI()

with open("q-vercel-python.json", "r") as f:
    all_data = json.load(f)

@app.get("/api")
def filter_data(
    name: List[str] = Query(...),
    min_marks: int = Query(0),
    max_marks: int = Query(100)
):
    filtered = [
        entry for entry in all_data
        if entry["name"] in name and min_marks <= entry["marks"] <= max_marks
    ]
    return filtered
