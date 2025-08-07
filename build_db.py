# build_db.py

# build_db.py

from app.loader import load_pdf
from app.splitter import split_docs
from app.embedder import get_embedder
from app.vectorstore import save_vectorstore
from app.config import DATA_DIR, VECTORSTORE_PATH

def main():
    print("Loading PDF...")
    documents = load_pdf(DATA_DIR)
    
    print("Splitting documents...")
    chunks = split_docs(documents)

    print("Loading embedder...")
    embedder = get_embedder()

    print("Saving vectorstore...")
    save_vectorstore(chunks, embedder, VECTORSTORE_PATH)

    print(" FAISS Vectorstore created!")

if __name__ == "__main__":
    main()




'''
from app.loader import load_pdf
from app.splitter import split_docs
from app.vectorstore import save_vectorstore

docs = load_pdf("data/e23076_uber-ars.pdf")
splits = split_docs(docs)
save_vectorstore(splits)
'''