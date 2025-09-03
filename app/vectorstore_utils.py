from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from typing import List
import torch

def create_faiss_index(texts: List[str]):
    # Auto-select device: GPU if available, else CPU
    device = "cuda" if torch.cuda.is_available() else "cpu"

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

    # Force full model load on correct device
    embeddings.client = embeddings.client.to(device)

    return FAISS.from_texts(texts, embeddings)


def retrive_relevant_docs(vectorstore: FAISS, query: str, k: int = 4):
    return vectorstore.similarity_search(query, k=k)


