from fastapi import FastAPI, Query
from typing import List, Optional
import json

app = FastAPI()

with open("q-vercel-python.json", "r") as f:
    all_data = json.load(f)

@app.get("/api")
def filter_data(
    name: Optional[List[str]] = Query(None),
    marks_min: int = Query(0),
    marks_max: int = Query(100)
):
    marks = [
        entry["marks"] for entry in all_data
        if (name is None or entry["name"] in name) and marks_min <= entry["marks"] <= marks_max
    ]
    return {"marks": marks}
