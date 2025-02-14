import os
from dotenv import load_dotenv
load_dotenv()


from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain import hub


groq_api_key = os.getenv('GROQ_API_KEY')
os.environ['HF_TOKEN'] = os.getenv('HUGGINGFACE_API_KEY')

def create_index(path, index_save_path='vector_db_index'):
    loader = PyPDFLoader(path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=250)
    final_docs = text_splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings(
        model_name = 'sentence-transformers/all-MiniLM-L6-v2',
    )
    vectorstore = FAISS.from_documents(final_docs, embeddings)
    #save the vectorstore
    vectorstore.save_local(index_save_path)

    return vectorstore

def load_index(index_path='vector_db_index'):
    try:
        embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
        vectorstore = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
        return vectorstore
    except FileNotFoundError:
        print(f"Error: Index file not found at {index_path}")
        return None  # Or raise the exception, depending on how you want to handle it
    except Exception as e:
        print(f"An error occurred while loading the index: {e}")
        return None
    

def load_llm():
    llm = ChatGroq(
        model='llama3-8b-8192',
        api_key = groq_api_key
    )
    return llm


#create a retrieval chain
def create_retrievalchain(vectorstore):
    #create retrieval qa chat prompt
    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

    #create a stuff documents chain
    combine_docs_chain = create_stuff_documents_chain(
        load_llm(),
        retrieval_qa_chat_prompt
        ) 
    #create a retrieval chain
    retrieval_chain = create_retrieval_chain(vectorstore.as_retriever(), combine_docs_chain)
    
    return retrieval_chain

# Function to generate a response using the retrieval chain
def generate_response(retrieval_chain, query):
    response = retrieval_chain.invoke({"input": query})
    return response['answer']
