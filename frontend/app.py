import streamlit as st
import httpx

st.set_page_config(page_title="DocuChat", page_icon="📄")
st.title("DocuChat — RAG Document Q&A")

st.subheader("1. Upload a document")
uploaded = st.file_uploader("Choose a PDF or DOCX", type=["pdf", "docx"])
if uploaded:
    with st.spinner("Ingesting..."):
        res = httpx.post("http://localhost:8000/ingest",
                         files={"file": (uploaded.name, uploaded.getvalue())},
                         timeout=120)
    st.success(f"Done: {uploaded.name}") if res.status_code == 200 else st.error("Failed")

st.subheader("2. Ask a question")
question = st.text_input("Type your question")
if question:
    with st.spinner("Thinking..."):
        res = httpx.post("http://localhost:8000/query",
                         json={"question": question}, timeout=60)
    data = res.json()
    st.write(data["answer"])
    with st.expander("View sources"):
        for c in data["citations"]:
            st.caption(f"Doc: {c['doc']} | Chunk: {c['chunk']}") 