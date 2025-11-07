from fastapi import FastAPI
import asyncio
import subprocess

app = FastAPI()

@app.get("/")
async def top_page():
    return {"message": "Anything is in here...Now time"}

