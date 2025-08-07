from app.vectorstore import load_vectorstore

def get_retriever(k=3):
    vectordb = load_vectorstore()
    return vectordb.as_retriever(search_kwargs={"k": k})
