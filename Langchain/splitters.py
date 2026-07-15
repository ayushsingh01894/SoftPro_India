from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
 
POLICY = """
LangChain is a framework for developing applications powered by language models.
It provides tools for document loading, text splitting, embeddings, vector stores,
retrieval, and chains.
RecursiveCharacterTextSplitter splits text recursively using a list of separators
until the desired chunk size is reached.
""".strip()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10,
    separators=["\n\n", "\n", " ", ""]
)

chunks = text_splitter.split_text(POLICY)

for i, chunk in enumerate(chunks, start=1):
    print(f"Chunk {i}:")
    print(chunk)
    print("-" * 40)


docs = [
    Document(
        page_content="""
        LangChain helps build LLM applications.
        RecursiveCharacterTextSplitter is commonly used to split long documents.
        """,
        metadata={"source": "dummy.txt"}
    )
]

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10
)

split_docs = text_splitter.split_documents(docs)

for doc in split_docs:
    print(doc.page_content)
    print(doc.metadata)
    print("-" * 30)