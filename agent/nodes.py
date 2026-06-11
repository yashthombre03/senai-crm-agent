#NODE1
from backend.services.thread_service import (
    get_thread_history
)

def load_thread_node(state):

    print("Loading thread...")

    return state

#NODE2
from rag.retriever import (
    search_knowledge_base
)

def rag_node(state):

    docs = search_knowledge_base(
        state["email"]
    )

    context = "\n".join(
        doc.page_content
        for doc in docs
    )

    state["rag_context"] = context

    return state    

#Generate reply
from agent.email_agent import (
    generate_reply
)

def reply_node(state):

    response = generate_reply(

        email=state["email"],

        thread_history=state["thread_history"],

        context=state["rag_context"]
    )

    state["reply"] = response
    state["action_taken"] = "reply_generated"
    return state


#Decision Node
def decision_node(state):

    email = state["email"].lower()

    if (
        "lawsuit" in email
        or "legal" in email
        or "attorney" in email
    ):

        state["requires_human"] = True

    else:

        state["requires_human"] = False

    return state

#Human Escalation Node
def escalation_node(state):

    state["reply"] = (
        "Escalated to human support."
    )
    state["action_taken"] = "human_escalation"

    return state