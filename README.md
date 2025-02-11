# PDF Q&A with Retrieval-Augmented Generation (RAG)

This project implements a PDF Question & Answering application using Retrieval-Augmented Generation (RAG) architecture. It allows users to upload a PDF document and then ask questions about its content in a chat-like interface. The backend, built with FastAPI (`fastapi_api.py`), processes the PDF, creates a vector store index, and uses a retrieval chain to generate answers to user queries based on the PDF content. The frontend, built with Streamlit (`app.py`), provides an interactive user interface for uploading PDFs and engaging in a Q&A session with the document.

## Execution Flow and Instructions

To run this application, follow these steps to set up both the backend (FastAPI) and the frontend (Streamlit) components.  **Since all files are in the root directory, you will execute commands from the main repository directory.**

**1. Backend Setup (FastAPI):**

*   **Navigate to the root directory of your repository** (where `fastapi_api.py` is located).
*   **Ensure you have the necessary Python packages installed.** You'll need to install the dependencies for your FastAPI backend.  If you have a `requirements.txt` file in your repository, you can install them using pip:
    ```bash
    pip install -r requirements.txt
    ```
    *(If you don't have a `requirements.txt`, you'll need to create one listing dependencies like `fastapi`, `uvicorn`, `pydantic`, and any libraries used in `fastapi_api.py` for PDF processing, vector database, and RAG implementation such as Langchain, ChromaDB, etc.)*

*   **Run the FastAPI application:** Open your terminal, navigate to the root directory of your repository, and execute the following command to start the FastAPI server:
    ```bash
    uvicorn fastapi_api:app --reload --host 0.0.0.0 --port 8000
    ```
    This command starts the FastAPI application (`app` instance in `fastapi_api.py`) using Uvicorn, enables hot reloading for development, and binds it to host `0.0.0.0` and port `8000`.  The backend server should now be running at `http://127.0.0.1:8000`.

**2. Frontend Setup (Streamlit):**

*   **Ensure you are in the root directory of your repository** (where `app.py` is located).
*   **Ensure you have Streamlit installed.** If not, install it using pip:
    ```bash
    pip install streamlit
    ```
*   **Run the Streamlit application:** In the same directory, execute the following command in your terminal:
    ```bash
    streamlit run app.py
    ```
    Streamlit will automatically open your application in a new tab in your default web browser.  You should see the "PDF Q&A with Retrieval-Augmented Generation" application running.

**3. Using the Application:**

*   **Upload a PDF:** In the Streamlit application sidebar, use the "Upload a PDF file" file uploader to select and upload a PDF document.
*   **Processing:** Once you upload a PDF, the application will display "Uploaded File: \[Your PDF Name]" in the sidebar and automatically start processing the PDF in the backend. You'll see a "Processing PDF..." spinner.
*   **Success/Error Message:** Upon successful processing, you'll see a "PDF processed and index created successfully!" message in the sidebar. If there's an error, an error message will be displayed instead.
*   **Ask Questions:** In the main chat area, type your question in the "Enter your question here..." input box at the bottom and press Enter or click the send icon.
*   **View Responses:** Your question will appear in the chat interface, and after a short delay (while the backend generates the response), the answer from the RAG model will appear as a response from the "assistant".
*   **Continue the Conversation:** You can continue to ask more questions about the same PDF document in the chat interface. To ask questions about a different PDF, simply upload a new PDF file in the sidebar.

**Important Notes:**

*   **Backend URL:** Ensure that the `BACKEND_URL` variable in your `app.py` is correctly set to `"http://127.0.0.1:8000"` if your FastAPI backend is running locally on port 8000. Adjust it if you are running the backend on a different host or port.
*   **Error Handling:** The application includes basic error handling. Check the sidebar and the chat interface for error messages if something goes wrong during PDF processing or query answering.
*   **File Names:** This README refers to your Streamlit app as `app.py` and your FastAPI backend as `fastapi_api.py` based on the screenshot.  Ensure these filenames match your actual file names.
*   **Dependencies:** Make sure to install all necessary Python packages for both the frontend and backend as described in the setup steps.
*   **Vector Database Index:** The backend saves the vector database index to a directory named `vector_db_index` in the same directory as `fastapi_api.py`. Ensure that the backend has write permissions to this directory.


This revised README should be provide accurate flow of the project.  
