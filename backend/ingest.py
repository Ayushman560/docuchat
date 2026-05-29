from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import cohere, os
from backend.db import get_conn
from dotenv import load_dotenv

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def ingest_file(file_path: str, doc_name: str):
    reader = PdfReader(file_path)
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)

    resp = co.embed(texts=chunks, model="embed-english-v3.0",
                    input_type="search_document")
    embeddings = resp.embeddings

    conn = get_conn()
    cur = conn.cursor()
    for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
        cur.execute(
            "INSERT INTO documents (content, embedding, doc_name, chunk_index)"
            " VALUES (%s, %s, %s, %s)", (chunk, emb, doc_name, i))
    conn.commit()
    cur.close() 