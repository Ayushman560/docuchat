from fastapi import FastAPI, UploadFile, File
from backend.ingest import ingest_file
from backend.retriever import retrieve_and_answer
import shutil

app = FastAPI()

@app.get("/")
def root():
    return {"status": "DocuChat API running"}

@app.post("/ingest")
async def ingest(file: UploadFile = File(...)):
    path = f"/tmp/{file.filename}"
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    ingest_file(path, file.filename)
    return {"status": "ingested", "file": file.filename}

@app.post("/query")
async def query(body: dict):
    return retrieve_and_answer(body["question"]) 