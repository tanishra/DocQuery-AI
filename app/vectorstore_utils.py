from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from typing import List
import torch

def create_faiss_index(texts: List[str]):
    # Choose GPU if available
    device = "cuda" if torch.cuda.is_available() else "cpu"

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2",
        model_kwargs={"device": device}  # Pass device here
    )

    # No need to access .client or .model manually now
    return FAISS.from_texts(texts, embeddings)

def retrive_relevant_docs(vectorstore: FAISS, query: str, k: int = 4):
    """
    Retrieve the top-k most similar documents from the FAISS vectorstore
    for a given query string.
    
    Args:
        vectorstore (FAISS): The FAISS vector store object.
        query (str): The search query.
        k (int, optional): Number of results to return. Defaults to 4.
        
    Returns:
        List: List of the top-k relevant documents.
    """
    return vectorstore.similarity_search(query, k=k)
