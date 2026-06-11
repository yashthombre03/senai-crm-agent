from langgraph.graph import StateGraph,END

from agent.state import AgentState

from agent.nodes import (
    rag_node,
    reply_node,
    decision_node,
    escalation_node
)

builder = StateGraph(
    AgentState
)

builder.add_node(
    "rag",
    rag_node
)

builder.add_node(
    "decision",
    decision_node
)

builder.add_node(
    "reply",
    reply_node
)

builder.add_node(
    "escalate",
    escalation_node
)

#Edges
builder.set_entry_point(
    "rag"
)

builder.add_edge(
    "rag",
    "decision"
)

#conditional routing
def route(state):

    if state["requires_human"]:

        return "escalate"

    return "reply"

builder.add_conditional_edges(
    "decision",
    route
)


builder.add_edge(
    "reply",
    END
)

builder.add_edge(
    "escalate",
    END
)

graph = builder.compile()