from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from typing import List

def create_faiss_index(texts: List[str]) :
    embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-mpnet-base-v2",model_kwargs={"torch_dtype": "auto", "low_cpu_mem_usage": False})
    return FAISS.from_texts(texts, embeddings)


def retrive_relevant_docs(vectorstore: FAISS, query: str, k: int = 4):
    return vectorstore.similarity_search(query, k=k)


