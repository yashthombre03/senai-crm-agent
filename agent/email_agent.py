import os

from dotenv import load_dotenv
load_dotenv()

#LLM:
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

#Prompt:
from langchain_core.prompts import ChatPromptTemplate
from agent.prompts import EMAIL_ASSISTANT_PROMPT

prompt = ChatPromptTemplate.from_template(
    EMAIL_ASSISTANT_PROMPT
)

chain = prompt | llm

def generate_reply(
    email,
    thread_history,
    context
):

    response = chain.invoke({

        "email": email,

        "thread_history": thread_history,

        "context": context
    })

    return response.content