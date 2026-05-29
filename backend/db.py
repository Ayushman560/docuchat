import psycopg2
from pgvector.psycopg2 import register_vector
from dotenv import load_dotenv
import os

load_dotenv()

def get_conn():
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    register_vector(conn)
    return conn 