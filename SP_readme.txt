===============================
FINANCE DOC RAG PROJECT
===============================

Project Path:
/Users/sarthakpradhan/llm/project_financedocanalysis

-------------------------------
WHAT THIS PROJECT DOES
-------------------------------
This is a local AI system that allows you to:

1. Upload a PDF (financial documents, reports, etc.)
2. Ask questions about the document
3. Get AI-generated answers using a local LLM (no API needed)

It uses:
- Streamlit (UI)
- LangChain (RAG pipeline)
- FAISS (vector database)
- Ollama (local LLM runtime)
- Llama 3.2 3B model
- Nomic embeddings

-------------------------------
HOW TO RUN THE PROJECT
-------------------------------

STEP 1: Go to project folder
cd /Users/sarthakpradhan/llm/project_financedocanalysis

STEP 2: Activate virtual environment
source venv/bin/activate

STEP 3: Start Ollama (VERY IMPORTANT)
In a separate terminal:
ollama serve

STEP 4: Ensure models are installed
ollama pull llama3.2:3b
ollama pull nomic-embed-text

STEP 5: Run Streamlit app
streamlit run app.py

Then open browser link shown in terminal.

-------------------------------
HOW TO USE THE APP
-------------------------------

1. Upload a PDF file
   (Example: earnings report, financial statement, research paper)

2. Wait for processing to complete

3. Type a question like:
   - What is the revenue growth?
   - Summarize this document
   - What are the key risks?
   - What are the main financial highlights?

4. Click "Send"

5. View answer in chat section

-------------------------------
FEATURES
-------------------------------

- PDF upload
- Document chunking
- Vector search (FAISS)
- Local embeddings (nomic-embed-text)
- Local LLM inference (llama3.2:3b)
- Chat-style Q&A interface
- Session-based chat history
- Clear chat & reset document buttons

-------------------------------
PROJECT STRUCTURE
-------------------------------

project_financedocanalysis/
│
├── app.py                # Streamlit UI
├── rag_pipeline.py      # RAG logic (retrieval + LLM)
├── venv/                # Python environment (DO NOT PUSH)
├── requirements.txt     # dependencies

-------------------------------
IMPORTANT NOTES
-------------------------------

- Make sure Ollama is running before starting app
- Use Python 3.11 if possible for stability
- Do NOT commit venv/ to GitHub
- First run may take time due to model loading

-------------------------------
TROUBLESHOOTING
-------------------------------

Problem: "Ollama not found"
Fix: Install from https://ollama.com and restart terminal

Problem: Streamlit not running
Fix: python -m streamlit run app.py

Problem: Slow responses
Fix: First run is slow due to model loading (normal)

-------------------------------
END OF FILE
-------------------------------
