from langchain_community.vectorstores import Chroma

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

#load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

#load chromaDB
vectorstore = Chroma(
    persist_directory="rag/chroma_db",
    embedding_function=embeddings
)

#retriever
retriever = vectorstore.as_retriever(   
    search_kwargs={
        "k": 1         #return top 3 matching chunks
    }
)


def search_knowledge_base(
    query
):

    docs = retriever.invoke(
        query
    )

    return docs