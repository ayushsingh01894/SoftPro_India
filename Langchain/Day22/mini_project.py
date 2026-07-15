import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

load_dotenv()

# Fake Knowledge Base
knowledge_base = {
    "refund": "Refunds are processed within 5-7 business days.",
    "cancel": "Orders can be cancelled within 24 hours.",
    "support": "You can contact support at support@company.com."
}

# Fake Retriever
def retrieve(question: str):
    q = question.lower()

    if "refund" in q:
        return knowledge_base["refund"]
    elif "cancel" in q:
        return knowledge_base["cancel"]
    elif "support" in q or "contact" in q:
        return knowledge_base["support"]

    return "No information found."

retriever = RunnableLambda(retrieve)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful customer support assistant.\n"
        "Use ONLY the given context.\n\n"
        "Context:\n{context}"
    ),
    ("human", "{question}")
])

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough(),
    }
    | prompt
    | llm
    | StrOutputParser()
)

question = input("Ask: ")
response = chain.invoke(question)

print("\nAnswer:")
print(response)