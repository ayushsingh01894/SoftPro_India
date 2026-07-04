import streamlit as st

st.title('Way to show content')
st.header("1.Text")
st.write("st.write prints plain text and support : **Markdown**")
st.code("def greet(name):\n return f'hi {name}")
st.divider()
st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("This is a header with a divider", divider="gray")
st.header("These headers have rotating dividers", divider=True)
st.header("One", divider=True)
st.header("Two", divider=True)
st.header("Three", divider=True)
st.header("Four", divider=True)


st.header("Pandas used : red[Example]")
import pandas as pd

students = pd.DataFrame({
    "ID": [101, 102, 103],
    "Name": ["Alice", "Bob", "Charlie"],
    "Marks": [85, 90, 78]
})

st.subheader("Students Data")
st.dataframe(students)

student = {
    "id": 101,
    "name": "Alice",
    "age": 20,
    "course": "Python"
}

st.json(student)

st.success("Sucess")
st.info("info")
st.warning("Warning")
st.error("Error")


# Widgets functions

name = st.text_input("Enter your name ? ", "")
st.write("Name:", name)

age = st.number_input("Enter your age", min_value=1, max_value=100)
st.write(age)

city = st.text_input("Enter your city ? ", "")
st.write("Name:", city)

marks = st.slider("Select Marks", 0, 100, 50)
st.write(marks)

if st.button("Click Me"):
    st.success("Button Clicked!")

agree = st.checkbox("I Agree")
if agree:
    st.write("Thank you!")

gender = st.radio("Select Gender", ["Male", "Female", "Other"])
st.write(gender)

course = st.selectbox(
    "Choose Course",
    ["Python", "Java", "C++"]
)
st.write(course)

skills = st.multiselect(
    "Select Skills",
    ["Python", "SQL", "Java", "AI"]
)
st.write(skills)

feedback = st.text_area("Feedback")
st.write(feedback)

file = st.file_uploader("Upload a File", max_upload_size=20)
if file:
    st.success("File Uploaded Successfully!")

date = st.date_input("Select Date")
st.write(date)

time = st.time_input("Select Time")
st.write(time)

color = st.color_picker("Choose Color")
st.write(color)

message = st.chat_input("Type your message")
if message:
    st.write(message)

st.write(f"Hii **{name or 'Friends'}** , Age: {age} ,  City: {city}")


#---------------------------------------------------------

bill = st.number_input("Bill Amount (Rs)", min_value=0.0 , value=500.0,step=50.0)
tip_persent = st.slider("Tip %", 0,30,10)
tip = bill * tip_persent/100
total = bill + tip
st.metric("Total to pay",f"Rs {total:.2f}")
st.divider()

