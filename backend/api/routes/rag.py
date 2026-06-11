from fastapi import APIRouter

from rag.retriever import (
    search_knowledge_base
)

router = APIRouter()

@router.get("/rag/search")
def rag_search(
    query: str
):

    docs = search_knowledge_base(
        query
    )

    return [
        doc.page_content
        for doc in docs
    ]