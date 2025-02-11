from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from rag_backend import create_index, load_index, create_retrievalchain, generate_response
import os

app = FastAPI()

# Pydantic model for the query request
class QueryRequest(BaseModel):
    query: str

# Endpoint to upload a file and create the vector store index
@app.post("/upload-and-process")
async def upload_and_process(file: UploadFile = File(...)):
    try:
        # Save the uploaded file temporarily
        file_path = f"temp_{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())

        # Create the index and save it to disk
        index_save_path = "vector_db_index"
        create_index(file_path, index_save_path)

        # Clean up the temporary file
        os.remove(file_path)

        return {"message": "File processed and index created successfully", "index_path": index_save_path}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to handle user queries
@app.post("/query")
async def query(request: QueryRequest):
    try:
        # Load the index
        index_path = "vector_db_index"
        vectorstore = load_index(index_path)
        if vectorstore is None:
            raise HTTPException(status_code=404, detail="Index not found. Please upload a file first.")

        # Create the retrieval chain
        retrieval_chain = create_retrievalchain(vectorstore)

        # Generate the response
        response = generate_response(retrieval_chain, request.query)
        return {"response": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)