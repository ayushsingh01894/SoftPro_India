from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful AI assistant. Keep answers short and friendly. and keep message in 1.5.36    3"
        ),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ]
)


chain = prompt | llm | StrOutputParser()

history = []

print("Groq Conversation Chatbot")
print("Type 'exit' to stop.")

while True:

    user_input = input("\nYou : ")
    if user_input.lower() == "exit":
        print("\nGood Bye!")
        break

    response = chain.invoke(
        {
            "history": history,
            "input": user_input
        }
    )
    print("Bot :", response)
    # Save Conversation
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=response))


print("\nConversation History:\n")

for message in history:
    if isinstance(message, HumanMessage):
        print(f"Human : {message.content}")
    elif isinstance(message, AIMessage):
        print(f"AI    : {message.content}")


"""
InMemoryChatMessageHistory
RunnableWithMessageHistory

"""