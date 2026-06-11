from agent.graph import graph
result = graph.invoke({

    "email":
    #"Do nonprofits receive discounts?",
    "My attorney will contact you regarding this lawsuit.",

    "sender":
    "alice@test.com",

    "thread_id":
    "thread_001",

    "thread_history": "",

    "rag_context": "",

    "category": "",

    "sentiment": "",

    "urgency": "",

    "requires_human": False,

    "reply": ""
})

print(
    result["reply"]
)