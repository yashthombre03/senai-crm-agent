from typing import TypedDict

class AgentState(TypedDict):

    email: str

    sender: str

    thread_id: str

    thread_history: str

    rag_context: str

    category: str

    sentiment: str

    urgency: str

    requires_human: bool

    reply: str
    action_taken: str