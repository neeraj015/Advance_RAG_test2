from langchain_huggingface import HuggingFaceEmbeddings
from app.config import EMBEDDING_MODEL_NAME

def get_embedder():
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
