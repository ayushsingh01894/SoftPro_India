# LangChain 
AI applications banane ke liye reusable building blocks provide karta hai.

it's not LLM it's Framework
# Jaise
Flask
↓
Web Apps
# Waise hi
LangChain
↓
LLM Apps

                LangChain

                     │

        ┌────────────┼────────────┐

        ▼            ▼            ▼

      Groq        OpenAI      Ollama

        │            │            │

        └────────────┼────────────┘

                     ▼

                  Output
    
LangChain kisi ek model se tied nahi ha

1. withut langchain
# you write yourself

question = input()
prompt = f"""
Question:
{question}
"""
response = groq.chat.completions.create(...)
answer = response.choices[0].message.content
print(answer)

2. With Langchain

response = llm.invoke(question)
print(response.content)

# Real Architecture
          User
            │
            ▼
     PromptTemplate
            │
            ▼
          Model
            │
            ▼
     Output Parser
            │
            ▼
         Response
Har component ek alag class hota hai.
Aur ye hi LangChain ka beauty hai.

# ----------------------------
Ab tak tum function-based programming kar rahe the.
Ab hum component-based AI engineering karenge.
Example:
Instead of
def ask():
    ...

# Hum banayenge
PromptTemplate
↓
LLM
↓
Parser
↓
Chain
Ye reusable hoga.
Isi wajah se bade AI systems maintain karna easy hota hai.

# --------------------------------------------------------------------------------------------------
Lesson 2 — Installation + First LangChain Program
-------------------------------------------------
1.  — Install Libraries
pip install langchain
Fir
pip install langchain-groq
Aur
pip install python-dotenv
Verify
pip list

---------------------------------
Manual
Groq Client
↓
API
------------------------
LangChain
ChatGroq
↓
API
--------------------------------------
# llm.involve()
Actual working
invoke()
↓
Prompt Banana --> Messages Banana --> Groq API
--> Response --> AIMessage Object --> Return

# AIMessage
# Question
Output string kyu nahi hai?
Dekho.
print(type(response))
# Output
<class 'AIMessage'>
Interesting.

-------------------------------------------------
# LangChain Message System
Ye LangChain ki backbone hai

# Pehle Ek Question
Tumne abhi ye likha tha.
<response = llm.invoke("Hello")

# Question.
Ye string kiske paas ja rahi hai?
Internally LangChain isko convert karta hai.
HumanMessage("Hello")
Tumhe dikhta nahi.
Automatically hota hai.

-------------------------------------------------
# LangChain Messages Kya Hain?

LLM sirf text nahi dekhta. Wo roles bhi dekhta hai.

# Example

ChatGPT me.

Systez
↓
You are a helpful AI.
↓
User
↓
What is Python?
↓
Assistant
↓
Python is...
Ye teen alag messages hain.

----------------------------------------------
# Message Types
Message	                      Role
SystemMessage	              AI ko instructions
HumanMessage	              User ka message
AIMessage	                  AI ka reply

Bas ye 3 sabse important hain.
<how work>

# Visualization
System
↓
You are an AI Teacher.
──────────────────────
Human
↓
What is Python?
──────────────────────
AI
↓
Python is...

------------------------------------------------
------ Import -------
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

Ye imports almost har LangChain project me use honge.

# Visualization
Human
↓
What is AI?
↓
LLM
↓
Answer
------------------------------------------
# SystemMessage - Ye AI ka behavior control karta hai.
from langchain_core.messages import (
    SystemMessage,
    HumanMessage
)
messages = [
    SystemMessage(
        content="You are a Python Teacher."
    ),
    HumanMessage(
        content="Explain List."
    )
]
response = llm.invoke(messages)
print(response.content)

----------------------------------------
# AIMessage

Suppose pehle conversation hui.

User
↓
Hello

AI
↓
Hello!

Ye bhi save karna padta hai.
messages = [
    HumanMessage(
        content="Hello"
    ),
    AIMessage(
        content="Hello! How can I help you?"
    ),
    HumanMessage(
        content="What is Python?"
    )
]
response = llm.invoke(messages)
print(response.content)

Observe.
Ab AI ko previous conversation bhi pata hai.

-----------------------------------------------
# LCEL (LangChain Expression Language)
Sabse Pehle Question
Abhi tak hum kya kar rahe the?
response = llm.invoke("What is AI?")
print(response.content)

# Simple.
Ab suppose tumhe ye karna hai.

Question
↓
Prompt Banana
↓
LLM
↓
Output Parse
↓
Print

# Without LCEL
prompt = create_prompt(question)
response = llm.invoke(prompt)
answer = response.content
print(answer)
Har step manually.
-----------------------
# LCEL Kya Hai? ---> LCEL ek syntax hai jisse hum multiple LangChain components ko ek pipeline me connect karte hain.

# Visualization

Prompt
↓
LLM
↓
Parser

# LCEL me
prompt | llm | parser
<Ye | operator Python ka normal OR operator nahi hai.>
LangChain ne isko overload kiya hai.

-------------------------------------------------

# Without LCEL
prompt = ...
response = llm.invoke(prompt)
answer = parser.invoke(response)
print(answer)

# With LCEL
chain = prompt | llm | parser
answer = chain.invoke(question)

<from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()
chain = llm | parser
response = chain.invoke("Hello")
print(response)>

<from langchain_core.output_parsers import StrOutputParser
Ye LLM ke output ko simple string me convert karta hai.>>
  
-----------------------------------------------
------------------------------------------------

# Prompt Templates
# Definition
PromptTemplate ek reusable prompt hota hai jisme variables hote hain.

from langchain_core.prompts import PromptTemplate

# ------------- Real Life Example

# Suppose tumhare paas ek Resume Template hai.

Name : ______

Age : ______

College : ______

Har student ke liye same format.
Sirf blanks fill hote hain.
# PromptTemplate bhi exactly yehi karta hai.

# Without PromptTemplate
question = "What is Python?"

prompt = f"""
You are a teacher.
Question:

{question}
"""
# With PromptTemplate
prompt = PromptTemplate.from_template(

"""
You are a teacher.
Question:
{question}
"""
)

Fir

prompt.invoke(
    {
        "question":"What is Python?"
    }
)
Automatically
You are a teacher.
Question:
What is Python?
ban jayega.
-------------------------------------------------
# code 

<from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template(
"""
You are an AI Teacher.
Question:
{question}
"""
)
formatted_prompt = prompt.invoke(
    {
        "question":"What is Machine Learning?"
    }
)
print(formatted_prompt.text)>

---------------------------------------------------------------------------------------------------------------------------------------------------
<<<ChatPromptTemplate>>>

Agar PromptTemplate "single message" hai,
to ChatPromptTemplate "complete conversation" hai.

<<<Import
    ↓
Load API Key
    ↓
Create LLM
    ↓
Create Prompt
    ↓
Create Parser
    ↓
Create Chain
    ↓
Create Empty History
    ↓
Take User Input
    ↓
Save HumanMessage
    ↓
Invoke Chain
    ↓
Print Response
    ↓
Save AIMessage
    ↓
Repeat>>>

---------------------------------------------------------------------------------------------------------------------------------------------------
<<<Partial Variables>>>
Partial Variables wo variables hote hain jo ek baar set hote hain aur baad me automatically use hote rehte hain.
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a {role}. Answer in {language}."
    ),
    (
        "human",
        "{question}"
    )
]).partial(
    role="Python Teacher",
    language="English"
)
# only Answer
response = chain.invoke({
    "question": "Explain List"
})

---------------------------------------------------------------------------------------------------------------------------------------------------
<<<Lesson 4 — FewShotPromptTemplate>>>

# Pehle Problem
Suppose tum AI se puchte ho:
Convert this sentence into SQL
Find all employees.
Kabhi sahi answer aata hai.
Kabhi galat.
Kyu?
Kyuki AI ko format nahi pata.
 
# ------------------ Solution
AI ko pehle examples dikhao.
Jaise teacher bachche ko sikhata hai.

Example 1
English:
Find all students.
SQL:
SELECT * FROM students;
---------------------
Example 2
English:
Find all employees.
SQL:
SELECT * FROM employees;
---------------------
Now

English:
Find all customers.

SQL:
?
Ab AI pattern samajh gaya.
Ye hi Few-Shot Prompting hai.

---------------------------------
<LangChain Support
Import
from langchain_core.prompts import FewShotPromptTemplate

--------------------------------------------
<<<<<Example selector>>>>>
Problem
Abhi humne FewShotPromptTemplate banaya.
Examples

examples = [
    {"input":"2+2","output":"4"},
    {"input":"3+3","output":"6"},
    {"input":"5+5","output":"10"}
]
Suppose ab examples ho gaye

50
Still okay.

Suppose
5000 examples

To?
Kya prompt me 5000 examples bhejoge?

❌ Impossible.
<Reason
    Token limit
    Slow
    Expensive

Solution

# Example Selector
Example Selector automatically sirf best examples choose karta hai.

# Real Life Example

Exam chal raha hai.
Teacher bolta hai
    "Polynomial solve karo."
Kya teacher Algebra ki sari book dega?
❌
Sirf
Polynomial wale examples.
Exactly Example Selector.

# Visualization

             1000 Examples
                    │
                    ▼
          Example Selector
                    │
         Chooses Best 3 Examples
                    │
                    ▼
                 Prompt
                    │
                    ▼
                   LLM

<<<Types of Example Selectors>>>
LangChain me bahut selectors hain.

Sabse important:

✅ LengthBasedExampleSelector
✅ SemanticSimilarityExampleSelector ⭐⭐⭐⭐⭐

Baaki bhi hain, lekin ye do sabse useful hain.

1️⃣ LengthBasedExampleSelector
Ye sirf length dekhta hai.
Example
Token Limit = 100
Agar examples zyada ho rahe hain.
To automatically kuch hata dega.

2️⃣ SemanticSimilarityExampleSelector ⭐⭐⭐⭐⭐
Ye sabse important hai.
Ye embeddings use karta hai.
Observe.
Examples

Example 1
Translate English to Hindi
----------------
Example 2
Write SQL Query
----------------
Example 3
Python Function
----------------
User
↓
Translate "Good Morning"

Question.
Kaunsa example useful?
Obviously
Translate English to Hindi
Ye selector automatically ye choose karega

<<<pip install chromadb>>>

>>>>  FewShotPromptTemplate → Jab examples kam ho (5–10) aur sabhi examples har request me bhejne ho.
>>>>>  LengthBasedExampleSelector → Jab examples zyada ho aur prompt size control karna ho.
>>>>>  SemanticSimilarityExampleSelector → Jab examples bahut zyada ho (1000+), aur har input ke liye sirf relevant examples bhejne ho. Ye production systems me sabse common approach hai.

<<<<Output Parsers>>>>
LangChain Output Parser Types

Module 3 me hum ye sab padhenge:

1. StrOutputParser ✅ AIMessage → String
2. JsonOutputParser ✅ JSON --> Dict
3. PydanticOutputParser ✅ json -> validation objects
4. CommaSeparatedListOutputParser ✅
5. RetryOutputParser ✅
6. OutputFixingParser✅ Invalid Output → Valid Output
7. Structured Output✅


⭐ Golden Rule

Agar output sirf display karna hai
➡️ StrOutputParser
Agar JSON chahiye
➡️ JsonOutputParser
Agar production-grade validation chahiye
➡️ PydanticOutputParser