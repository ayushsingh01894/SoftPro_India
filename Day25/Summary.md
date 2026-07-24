# Day 25 – LangChain Agents (Complete Notes)
## Step 1 — Why ReAct Agent?
### Day 23 me kya kiya tha?
Tumne khud tool-calling loop likha tha.
Flow:

```text
User
   ↓
Model
   ↓
Tool Call?
   ↓
Yes
   ↓
Run Tool
   ↓
Tool Result
   ↓
Model
   ↓
Final Answer
```

Code kuch aisa tha:

```python
while True:
    ai = model.invoke(messages)
    if ai.tool_calls:
        run_tool()
    else:
        break
```

Ye pura loop tumne khud likha.

---

## Problem
Har project me ye loop dobara likhna padega.
---

## LangChain Solution
Sirf ek line
```python
agent = create_agent(
    model,
    tools
)
```

Bas.
Ye internally wahi loop bana deta hai.
---

## Is loop ka naam
**ReAct**
```
Reason
↓
Act
↓
Observe
↓
Reason
↓
Answer
```

---
# Step 2 — First Agent

Ab humne

```python
ChatGroq()
```
banaya.
Fir

```python
TOOLS=[
add,
multiply
]
```

Fir

```python
agent=create_agent(
model,
TOOLS
)
```

Ab

```python
agent.invoke(...)
```

kar sakte hain.

---

## invoke()

```python
result=agent.invoke(
{
"messages":[
("human","2+4")
]
}
)
```

Ye agent ko chalata hai.

---

### Output

Agent sirf answer nahi deta.

Poora conversation return karta hai.

```
HumanMessage

↓

AIMessage

↓

ToolMessage

↓

AIMessage
```

Final answer

```python
result["messages"][-1]
```

---

# Step 3 — Inside the Loop

Ab tak

sirf

```text
Answer
```

dikh raha tha.

Ab

```
Reason

↓

Tool Call

↓

Tool Result

↓

Answer
```

dekhna tha.

Isliye use kiya

```python
agent.stream(
stream_mode="updates"
)
```

---

### stream()

Ye realtime updates deta hai.

Jaise

```
Model

↓

Tool

↓

Model

↓

Tool

↓

Model
```

---

Example

```
Tool Call

↓

multiply

↓

42

↓

add

↓

142

↓

Answer
```

---

## stream() vs invoke()

### invoke()

Ek hi baar

Final answer

```
Answer
```

---

### stream()

Har step

```
Reason

↓

Act

↓

Observe

↓

Answer
```

---

# Step 4 — System Prompt

Ab tak

Agent sirf

Model + Tools

tha.

Ab

System Prompt add hua.

```python
create_agent(

model,

tools,

system_prompt=...
)
```

---

System Prompt

Agent ka

Rules

Persona

Behaviour

define karta hai.

Example

```
You are StudyBot.
Always use calculator.
Never guess.
```

---

Ab Agent ko personality mil gayi.

---

# Step 5 — Memory

Ab tak

Har invoke

blank tha.

```
Hi

↓

My name is Ali

↓

What's my name?

↓

I don't know
```

---

Solution

MemorySaver

```python
MemorySaver()
```

---

Agent

```python
agent=create_agent(

...

checkpointer=MemorySaver()

)
```

---

Ab

Thread ID

```python
config={

"configurable":{

"thread_id":"student-1"

}

}
```

---

Invoke

```python
agent.invoke(

...

config=config
)
```

---

Ab

```
Hi

↓

My name is Ali

↓

What's my name?

↓

Ali
```

---

Kyun?

Memory restore hui.

---

Different Thread

```
student-1

↓

Ali

```

```
student-2

↓

Blank
```

---

Har thread

alag memory.

---

# Step 6 — SoftBot

Sab combine.

```
Model

+

Tools

+

System Prompt

+

Memory

+

Streaming

=

SoftBot
```

---

Tools

```
Calculator

Search Handbook

Word Count
```

---

System Prompt

```
You are SoftBot.

Always use calculator.

Always use handbook.

Never guess.
```

---

Memory

```
MemorySaver()
```

---

Streaming

```
agent.stream()
```

---

Trace

```
How I got this

↓

Tool Call

↓

Tool Result

↓

Answer
```

---

# @tool

Normal function

```
def add():
```

LLM nahi dekh sakta.

---

Decorator

```
@tool
```

Ab

LLM use kar sakta hai.

---

Example

```python
@tool
def add(a,b):

return a+b
```

---

# create_agent()

Ye sabse important function hai.

Ye internally banata hai

```
Model

↓

Reason

↓

Tool Call

↓

Tool

↓

Observation

↓

Model

↓

Answer
```

---

# invoke()

Ek request bhejna.

```python
agent.invoke(...)
```

Return

```
messages
```

---

# stream()

Live updates

```
Model

↓

Tool

↓

Model

↓

Tool

↓

Answer
```

---

# MemorySaver()

Conversation save karta hai.

---

# thread_id

Conversation ka naam.

```
student-1
```

alag

```
student-2
```

alag.

---

# system_prompt

Agent ka behaviour.

```
Friendly

Professional

Doctor

Teacher

StudyBot
```

Sab yahi decide karta hai.

---

# ReAct

Sabse important concept.

```
Reason

↓

Act

↓

Observe

↓

Reason

↓

Answer
```

Ye har Agent ka heart hai.

---

# Day 25 Summary

```
Step 1

Manual Loop

↓

Step 2

create_agent()

↓

Step 3

stream()

↓

Step 4

system_prompt

↓

Step 5

MemorySaver

↓

Step 6

Complete AI Assistant
```

---

## Yaad rakhne layak 10 important points

1. **`@tool`** kisi normal Python function ko AI tool bana deta hai.
2. **`create_agent(model, tools)`** automatic ReAct loop create karta hai.
3. **ReAct = Reason → Act → Observe → Answer.**
4. **`agent.invoke()`** ek request chala kar final conversation return karta hai.
5. **`agent.stream(..., stream_mode="updates")`** har intermediate step live dikhata hai.
6. **`system_prompt`** agent ki personality aur rules define karta hai.
7. **Model khud decide karta hai** kaunsa tool use karna hai; tumhe `if/else` routing nahi likhni padti.
8. **`MemorySaver()`** conversation history persist karta hai.
9. **`thread_id`** alag-alag conversations ko isolate karta hai.
10. **Final SoftBot** = Model + Tools + System Prompt + Memory + Streaming (trace) = ek conversational AI assistant.



====================================================================================================================================================================================================================

Bilkul. Agar tum interview ya project ke liye padh rahe ho, to alag-alag examples yaad karne ki zarurat nahi hai. Ek hi **complete code** se saare concepts samajh lo. Main isi approach se samjhata hoon.

---

# LangChain Agent – Complete Theory

## Pehle AI Model kaise kaam karta tha?

Sirf LLM tha.

```text
User
   ↓
LLM
   ↓
Answer
```

Example:

```text
User:
2 + 4
```

LLM:

```text
6
```

Ye simple question tha.

---

Ab maan lo user poochta hai:

```text
What is 25 multiplied by 4?
```

Hum chahte hain AI calculator use kare.

LLM khud Python function nahi chala sakta.

Isliye tools introduce hue.

---

# Tool kya hota hai?

Tool ek normal Python function hai.

Example

```python
def calculator(a, b):
    return a + b
```

Ye sirf Python function hai.

LLM ise dekh bhi nahi sakta.

Isliye hum likhte hain

```python
@tool
def calculator(a, b):
    return a + b
```

`@tool` LangChain ko batata hai:

> "Ye function AI use kar sakta hai."

Ab ye AI ka toolbox ban gaya.

---

# Model aur Tool ka relation

Ab AI ke paas toolbox hai.

```text
LLM

↓

Calculator

↓

Search

↓

Database

↓

Weather
```

Lekin problem hai.

AI ko kaise pata chale ki tool kab use karna hai?

---

# ReAct

Isi problem ko solve karta hai.

ReAct ka matlab:

```text
Reason

↓

Act

↓

Observe

↓

Answer
```

Example:

User:

```text
What is 25 × 4?
```

---

## Reason

Model sochta hai.

```text
Ye maths ka question hai.
Calculator use karna chahiye.
```

---

## Act

Tool call karta hai.

```python
calculator(
a=25,
b=4,
op="mul"
)
```

---

## Observe

Tool result deta hai.

```text
100
```

---

## Final Answer

LLM bolta hai

```text
25 multiplied by 4 is 100.
```

Ye poora ReAct cycle hai.

---

# create_agent()

Ab socho agar ye loop tum khud likho.

```python
while True:

    ai = model.invoke()

    if ai.tool_calls:

        tool()

    else:

        break
```

Har project me same code.

LangChain ne bola:

Ye sab hum kar dete hain.

Sirf likho

```python
agent = create_agent(
model,
tools
)
```

Bas.

Ye internally poora loop bana deta hai.

---

# Ab complete code dekhte hain

Ye line dekho

```python
model = ChatGroq(
model="llama-3.3-70b-versatile"
)
```

Iska matlab

AI brain bana.

Abhi sirf brain hai.

Iske paas memory nahi.

Tools nahi.

Rules nahi.

---

Fir

```python
@tool
def calculator(...):
```

Calculator ban gaya.

---

Fir

```python
@tool
def search_handbook(...):
```

Dusra tool.

---

Fir

```python
TOOLS = [
calculator,
search_handbook,
word_count
]
```

Ye toolbox hai.

Jaise carpenter ke paas toolbox hota hai.

---

Fir

```python
SYSTEM_PROMPT = """
You are SoftBot...
"""
```

Ye agent ki personality hai.

Agar system prompt hata do

AI normal ChatGPT jaisa ban jayega.

Prompt lagane ke baad

Ye SoftBot ban gaya.

---

Fir

```python
agent=create_agent(
model=model,
tools=TOOLS,
system_prompt=SYSTEM_PROMPT,
checkpointer=MemorySaver()
)
```

Ye sabse important line hai.

Is ek line me

### Brain

```text
ChatGroq
```

*

### Toolbox

```text
Calculator

Search

Word Count
```

*

### Rules

```text
System Prompt
```

*

### Memory

```text
MemorySaver
```

=

Complete AI Agent

---

# MemorySaver

Agar ye na ho

```text
Hi

↓

My name is Ali

↓

What's my name?

↓

I don't know
```

Kyunki har invoke naya hota hai.

---

MemorySaver

Har chat save karta hai.

```python
checkpointer=MemorySaver()
```

---

Fir

```python
config={
"configurable":{
"thread_id":"student-1"
}
}
```

Ye conversation ka naam hai.

---

Same thread

```text
student-1

↓

Hi

↓

My name is Ali

↓

What's my name?

↓

Ali
```

---

Dusra thread

```text
student-2

↓

What's my name?

↓

I don't know
```

---

# run_turn()

Ye function sab kuch chalata hai.

```python
def run_turn(question):
```

Input

User ka question.

---

Fir

```python
agent.stream(...)
```

Ye invoke bhi karta hai

Aur

Live updates bhi deta hai.

---

Example

User

```text
What is 25 × 4?
```

---

Stream

Step 1

```text
Thinking...
```

---

Step 2

```text
Calling calculator
```

---

Step 3

```text
Calculator returned 100
```

---

Step 4

```text
Answer
```

---

Ye sab stream me milta hai.

---

Code

```python
if getattr(last,"tool_calls",None):
```

Iska matlab

Kya model ne tool call kiya?

Agar haan

Trace me add karo.

---

Fir

```python
ToolMessage
```

Aaya.

Matlab

Tool chal gaya.

Result mila.

Usko trace me save karo.

---

Fir

```python
elif last.content:
```

Final answer.

Usko answer variable me save kar do.

---

Return

```python
return answer,trace
```

---

Main loop

```python
while True:
```

Infinite chatbot.

---

Input

```python
question=input()
```

---

Agent

```python
answer,trace=run_turn(question)
```

---

Print

```python
SoftBot:
```

---

Print

```python
How I got this
```

Ye stream ka output hai.

---

# Agar user pooche

```text
What is the semester fee?
```

Flow

```text
User

↓

SoftBot

↓

Reason

↓

Fees question

↓

search_handbook

↓

Result

↓

Answer
```

---

Agar user bole

```text
2500 × 4
```

Flow

```text
User

↓

Reason

↓

Math

↓

Calculator

↓

10000

↓

Answer
```

---

Agar bole

```text
Count words

Hello everyone welcome to AI
```

Flow

```text
Reason

↓

word_count

↓

5

↓

Answer
```

---

# Architecture (Sab kuch ek diagram me)

```text
                 User
                   │
                   ▼
            ChatGroq Model
                   │
                   ▼
            create_agent()
                   │
   ┌───────────────┼────────────────┐
   │               │                │
   ▼               ▼                ▼
Calculator   Search Handbook   Word Count
   │               │                │
   └───────────────┼────────────────┘
                   ▼
            Tool Result
                   ▼
             MemorySaver
                   ▼
          Final AI Response
                   ▼
               User
```

## Is poore chapter ka ek sentence me summary

**LangChain Agent ek intelligent controller hai jo LLM, Tools, Memory aur System Prompt ko jodkar ReAct (Reason → Act → Observe → Answer) loop ke through user ke liye sahi tool choose karta hai, uska result observe karta hai, memory maintain karta hai aur final natural-language answer deta hai.**

Agar tum ye flow samajh gaye, to Day 25 ka core concept samajh gaye. Iske baad LangGraph padhna kaafi aasaan ho jata hai, kyunki LangGraph isi agent workflow ko aur flexible aur customizable bana deta hai.
