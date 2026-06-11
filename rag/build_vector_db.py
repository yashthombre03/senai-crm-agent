import os

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)
from langchain_community.vectorstores import Chroma
from langchain_huggingface import (
    HuggingFaceEmbeddings
)
#Load Documents
documents = []

folder = "knowledge_base"

for filename in os.listdir(folder):

    if filename.endswith(".md"):

        loader = TextLoader(
            os.path.join(folder, filename),
            encoding="utf-8"
        )

        documents.extend(
            loader.load()
        )

#Chunk Documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(
    documents
)

#Create Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


#Create ChromeDB
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="rag/chroma_db"
)



print(
    f"Stored {len(chunks)} chunks"
)