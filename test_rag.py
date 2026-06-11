from rag.retriever import (
    search_knowledge_base
)

results = search_knowledge_base(
    "nonprofit discount"
)

for doc in results:

    print("\n")
    print(doc.page_content)