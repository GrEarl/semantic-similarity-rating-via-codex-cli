from fastapi import FastAPI
import asyncio
import subprocess
import numpy as np
import polars as po


app = FastAPI()

@app.get("/")
async def top_page():
    return {"message": "Anything is in here...Now time"}

@app.post("/tasks")
async def task_generator():
    pass

async def task_compiler(task_id, llm_response, SSR_Model):
    pass
