from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama


def build_rag(pdf_path):

    # Load PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Split text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(documents)

    # Embeddings
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    # Vector database
    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    retriever = vectorstore.as_retriever()

    # LLM
    llm = ChatOllama(
        model="llama3.2:3b",
        temperature=0
    )

    return retriever, llm
