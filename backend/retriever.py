import cohere, os
from backend.db import get_conn
from dotenv import load_dotenv

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def retrieve_and_answer(query: str, top_k: int = 5):
    resp = co.embed(texts=[query], model="embed-english-v3.0",
                    input_type="search_query")
    query_emb = resp.embeddings[0]
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT content, doc_name, page_num, chunk_index,
               1 - (embedding <=> %s::vector) AS score
        FROM documents ORDER BY score DESC LIMIT %s
    """, (query_emb, top_k))
    results = cur.fetchall()
    docs = [{"text": r[0]} for r in results]
    answer = co.chat(message=query, documents=docs)
    citations = [{"doc": r[1], "page": r[2], "chunk": r[3]} for r in results]
    return {"answer": answer.text, "citations": citations} 