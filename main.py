from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("q-vercel-python.json", "r") as f:
    all_data = json.load(f)

# Convert data to a lookup dictionary for fast access
data_dict = {entry["name"]: entry["marks"] for entry in all_data}

@app.get("/api")
def filter_data(
    name: Optional[List[str]] = Query(None),
    marks_min: int = Query(0),
    marks_max: int = Query(100)
):
    if name is None:
        marks = [
            mark for mark in data_dict.values()
            if marks_min <= mark <= marks_max
        ]
    else:
        marks = [
            mark if (mark := data_dict.get(n)) is not None and marks_min <= mark <= marks_max else None
            for n in name
        ]
    return {"marks": marks}
