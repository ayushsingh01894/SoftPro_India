# Runnable

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)

# 1. RunnableLambda: any function becomes a chain step
word_count = RunnableLambda(lambda s: len(s.split()))
print("RunnableLambda word_count.invoke('one two three') =>", word_count.invoke("one two three"))
print()

analyze = RunnableParallel(
    upper=RunnableLambda(str.upper),
    words=RunnableLambda(lambda s: len(s.split())),
    chars=RunnableLambda(len),
)
print("RunnableParallel runs all branches on one input:")
print(" ", analyze.invoke("langchain is fun"))
print()

keep_and_shout = RunnableParallel(
    original=RunnablePassthrough(),          # the input, untouched
    shout=RunnableLambda(str.upper),         # a transformed copy
)
print("RunnablePassthrough keeps the input while you add to it:")
print(" ", keep_and_shout.invoke("hello"))
print()

def fake_retriever(question: str) -> str:
    """Pretend this searched a vector store and returned the best chunk."""
    return "Refunds are processed within 5-7 business days to the original payment method."

prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer ONLY from this context:\n{context}"),
    ("human", "{question}"),
])

rag_inputs = {
    "context": RunnableLambda(fake_retriever),   # question -> retrieved text
    "question": RunnablePassthrough(),           # question -> itself, unchanged
}
rag_prompt_chain = rag_inputs | prompt           # add "| model | parser" for the real thing

built = rag_prompt_chain.invoke("How long do refunds take?")
print("The classic RAG wiring, built offline (question -> filled prompt):")
for m in built.to_messages():
    print(f"  [{m.type:>6}] {m.content}")
print()

print("Add '| model | parser' to rag_prompt_chain and you have a full RAG chain.")
print("Same three runnables (Lambda/Parallel/Passthrough) wire up most real pipelines.")