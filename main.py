from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()

with open("q-vercel-python.json", "r") as f:
    all_data = json.load(f)

class MarksFilter(BaseModel):
    marks: List[int]

@app.post("/api")
def filter_data(names: List[str] = Query(...), marks_filter: MarksFilter = None):
    min_mark, max_mark = marks_filter.marks

    filtered = [
        entry for entry in all_data
        if entry["name"] in names and min_mark <= entry["marks"] <= max_mark
    ]
    return filtered
