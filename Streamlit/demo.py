import streamlit as st
import pandas as pd
import time

# -----------------------
# Page Title
# -----------------------
st.title("🎓 Student Dashboard")
st.header("Welcome to Streamlit Demo")
st.subheader("Fill your details")

# -----------------------
# Sidebar
# -----------------------
st.sidebar.title("Menu")
page = st.sidebar.radio("Select Page", ["Home", "Profile", "Result"])

# -----------------------
# Home Page
# -----------------------
if page == "Home":

    st.text("This is a Streamlit Widget Demo.")
    st.write("Using different Streamlit components.")

    # Form
    with st.form("student_form"):
        name = st.text_input("Enter Name")
        age = st.number_input("Enter Age", 10, 100)
        gender = st.radio("Gender", ["Male", "Female", "Other"])
        course = st.selectbox(
            "Select Course",
            ["Python", "Data Science", "AI", "Web Development"]
        )

        skills = st.multiselect(
            "Skills",
            ["Python", "Java", "C++", "SQL", "Machine Learning"]
        )

        about = st.text_area("About Yourself")

        agree = st.checkbox("I agree to Terms & Conditions")

        submit = st.form_submit_button("Submit")

    if submit:
        st.success("Form Submitted Successfully!")
        st.write("### Student Information")
        st.write("Name:", name)
        st.write("Age:", age)
        st.write("Gender:", gender)
        st.write("Course:", course)
        st.write("Skills:", skills)
        st.write("About:", about)

# -----------------------
# Profile Page
# -----------------------
elif page == "Profile":

    tabs = st.tabs(["Upload", "Media", "Progress"])

    with tabs[0]:
        file = st.file_uploader("Upload a File")

        if file:
            st.success("File Uploaded!")

    with tabs[1]:
        st.image(
            "https://picsum.photos/400/200",
            caption="Sample Image"
        )

        #st.audio("sample.mp3")

        st.video(
            "https://youtu.be/c35fpGWqXnk?si=x3xaPjjpv0SNDC50"
        )

    with tabs[2]:

        if st.button("Start Progress"):
            progress = st.progress(0)

            with st.spinner("Loading..."):
                for i in range(101):
                    time.sleep(0.02)
                    progress.progress(i)

            st.success("Completed!")

# -----------------------
# Result Page
# -----------------------
elif page == "Result":

    data = {
        "Subject": ["Python", "Math", "AI"],
        "Marks": [90, 85, 95]
    }

    df = pd.DataFrame(data)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Marks", 270)

    with col2:
        st.metric("Percentage", "90%")

    st.dataframe(df)

    st.table(df)

    st.info("Excellent Performance!")
    st.warning("Keep practicing.")
    st.error("No errors found. (Demo)")

# -----------------------
# Session State Example
# -----------------------
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Click Counter"):
    st.session_state.count += 1

st.write("Button Clicked:", st.session_state.count)

# -----------------------
# Cache Example
# -----------------------
@st.cache_data
def square(n):
    return n * n

num = st.slider("Choose Number", 1, 20)

st.write("Square =", square(num))

# -----------------------
# Download Button
# -----------------------
csv = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6]
}).to_csv(index=False)

st.download_button(
    "Download CSV",
    csv,
    file_name="data.csv",
    mime="text/csv"
)

# -----------------------
# Chat Example
# -----------------------
if prompt := st.chat_input("Ask something..."):
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        st.write(f"You said: {prompt}")

        