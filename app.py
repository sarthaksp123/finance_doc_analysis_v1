import streamlit as st
import tempfile

from rag_pipeline import build_rag

st.set_page_config(
    page_title="Finance Doc Chat",
    layout="wide"
)

st.title("📄 Finance Document Chat (RAG)")

# -----------------------------
# Session state (for memory)
# -----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "qa_ready" not in st.session_state:
    st.session_state.qa_ready = False

if "retriever" not in st.session_state:
    st.session_state.retriever = None

if "llm" not in st.session_state:
    st.session_state.llm = None


# -----------------------------
# PDF Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file and not st.session_state.qa_ready:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        pdf_path = tmp_file.name

    with st.spinner("Processing document..."):
        retriever, llm = build_rag(pdf_path)
        st.session_state.retriever = retriever
        st.session_state.llm = llm
        st.session_state.qa_ready = True

    st.success("Document ready!")


# -----------------------------
# Clear Chat Button
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("🧹 Clear Chat"):
        st.session_state.chat_history = []

with col2:
    if st.button("🗑 Reset Document"):
        st.session_state.chat_history = []
        st.session_state.qa_ready = False
        st.session_state.retriever = None
        st.session_state.llm = None
        st.rerun()


# -----------------------------
# Chat Display
# -----------------------------
st.subheader("Chat History")

chat_container = st.container()

with chat_container:
    for q, a in st.session_state.chat_history:
        st.markdown(f"**🧑 You:** {q}")
        st.markdown(f"**🤖 AI:** {a}")
        st.markdown("---")


# -----------------------------
# Input Box
# -----------------------------
if st.session_state.qa_ready:

    question = st.text_input("Ask a question")

    if st.button("Send 🚀") and question.strip() != "":

        retriever = st.session_state.retriever
        llm = st.session_state.llm

        with st.spinner("Thinking..."):

            docs = retriever.get_relevant_documents(question)

            context = "\n\n".join(
                [d.page_content for d in docs]
            )

            prompt = f"""
You are a helpful assistant answering questions based on a financial document.

Context:
{context}

Question:
{question}
"""

            response = llm.invoke(prompt)
            answer = response.content

        # Append to history
        st.session_state.chat_history.append((question, answer))

        # Rerun to update UI
        st.rerun()
