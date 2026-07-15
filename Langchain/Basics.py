# using langchain with chromadb
import os

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    collection_name="knowledge_base",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile",
)


print("Enter your documents.")
print("Type 'done' when finished.\n")

documents = []

while True:
    text = input("Document: ")
    if text.lower() == "done":
        break
    documents.append(Document(page_content=text))

if documents:
    vectorstore.add_documents(documents)
    print("\nDocuments stored successfully!\n")
else:
    print("\nNo documents added.\n")

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant.
Answer ONLY using the context below.

Context:
{context}

Question:
{question}

Answer:
""")

print("\nYou can now ask questions.")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ")
    if question.lower() == "exit":
        break
    docs = retriever.invoke(question)
    context = "\n\n".join(doc.page_content for doc in docs)
    chain = prompt | llm
    response = chain.invoke({
        "context": context,
        "question": question
    })
    print("\nAssistant:", response.content)
    print("-" * 60)