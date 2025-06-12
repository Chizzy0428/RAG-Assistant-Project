import streamlit as st
import os
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import tempfile

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="PDF RAG Assistant", layout="wide")
st.title("PDF Question Answering Assistant")

uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if uploaded_files and openai_api_key:
    with st.spinner("Loading and indexing your documents..."):
        all_docs = []
        for uploaded_file in uploaded_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.read())
                loader = PyMuPDFLoader(tmp_file.name)
                all_docs.extend(loader.load())

        # Split text into chunks
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        split_docs = splitter.split_documents(all_docs)

        # Vector store
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        vectorstore = FAISS.from_documents(split_docs, embeddings)

        # QA Chain
        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
        llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0)
        qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)

    st.success("Documents ready. Ask your question below.")

    query = st.text_input("Ask a question about your documents")
    if query:
        with st.spinner("Generating answer..."):
            result = qa_chain({"query": query})
            st.markdown(f"### Answer:\n{result['result']}")

            st.markdown("###  Source Snippets:")
            for i, doc in enumerate(result["source_documents"], start=1):
                snippet = doc.page_content.strip().replace("\n", " ")[:500]
                st.markdown(f"**Source {i}:** {snippet}...")

else:
    if not openai_api_key:
        st.warning("Please set your OpenAI API key in a `.env` file or via `os.environ['OPENAI_API_KEY']`.")
