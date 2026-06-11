from rag.retriever import (
    search_knowledge_base
)

from agent.email_agent import (
    generate_reply
)

query = """
Do nonprofits receive discounts?
"""

docs = search_knowledge_base(
    query
)

context = "\n".join(
    doc.page_content
    for doc in docs
)


reply = generate_reply(
    email=query,
    thread_history="",
    context=context
)

print(reply)