# DocuChat — RAG-Based Document Q&A

An intelligent document Q&A system powered by Retrieval-Augmented Generation (RAG) that lets you upload PDF or DOCX files and ask natural language questions, receiving accurate answers with source citations.

## Demo
Upload any PDF or DOCX → Ask a question → Get an AI-powered answer with the exact document, page, and chunk it came from.

## Features
- Upload PDF and DOCX documents via a clean web interface
- Ask natural language questions about your documents
- Get citation-backed answers showing document name and chunk
- Semantic search using vector embeddings for accurate retrieval
- Fast vector similarity search with PostgreSQL + pgvector
- RESTful API backend with FastAPI
- Interactive Streamlit frontend

## How It Works
1. Upload a PDF or DOCX file through the Streamlit UI
2. Document is parsed and split into semantic chunks
3. Each chunk is embedded using Cohere embeddings
4. Embeddings are stored in PostgreSQL with pgvector
5. User asks a question — it gets embedded the same way
6. Top 5 most similar chunks are retrieved from the database
7. Cohere LLM generates an answer grounded in those chunks
8. Answer is displayed with source citations

## Tech Stack
- Python
- FastAPI
- Streamlit
- LangChain
- Cohere Embeddings
- PostgreSQL + pgvector
- pypdf
- python-dotenv
- httpx

## Project Structure
