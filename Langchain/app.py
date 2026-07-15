from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    api_key=api_key ,
    model ="llama-3.3-70b-versatile",
)

# system = SystemMessage(
#     content="You are a helpful assistant. Always answer in 2-3 simple sentences using easy English."
# )
messages = [
    SystemMessage(
        content="You are a helpful assistant. Always answer in 2-3 simple sentences using easy English."
    )
]


# question = input("Ask : ")
# response = llm.invoke(question)
# print(response.content)

# questions = [
#     "What is AI?",
#     "What is Python?",
#     "What is LangChain?"
# ]

# for q in questions:
#     response = llm.invoke([
#         system,
#         HumanMessage(content=q)
#     ])
#     print("\nQuestion :", q)
#     print(response.content)

while True:
    question = input("You : ")
    
    if question.lower() == "exit":
        break
    
     # Save user message
    messages.append(HumanMessage(content=question))

    # Send entire conversation
    response = llm.invoke(messages)

    # response = llm.invoke([
    #     system,
    #     HumanMessage(content=question)
    #     ])
    
    
    print("\nQuestion :", question)
    print("AI:",response.content)

    messages.append(AIMessage(content=response.content))
    