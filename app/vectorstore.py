import os
from langchain_community.vectorstores import FAISS
from app.config import DB_FAISS_PATH
from app.embedder import get_embedder


from langchain.vectorstores import FAISS

def save_vectorstore(chunks, embedder, path):
    db = FAISS.from_documents(chunks, embedder)
    db.save_local(path)


''''
def save_vectorstore(splits):
    embedder = get_embedder()
    vectordb = FAISS.from_documents(splits, embedder)
    vectordb.save_local(DB_FAISS_PATH)
'''
def load_vectorstore():
    embedder = get_embedder()
    return FAISS.load_local(DB_FAISS_PATH, embedder, allow_dangerous_deserialization=True)
