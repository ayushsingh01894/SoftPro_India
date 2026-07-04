import streamlit as st

st.title("Layout a page")
st.sidebar.header("Setting")

model = st.sidebar.selectbox("Model",["llama","OpenAi","Gemini"])

temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=2.0,
    value=0.7,
    step=0.1
)

st.write(f"Selected Model: **{model}**  &  Selected Tempreture: **{temperature}** ")

st.header("Cols puts things side by side")
col1,col2,col3,col4 = st.columns(4)
with col1:
    st.write("Col 1 Content")
    st.metric("User",1234,"+120")
with col2:
    st.write("Col 2 Content")
    st.metric("Active today",12,"-120")
with col3:
    st.write("Col 3 Content")
    st.metric("Signups",34,"+12")
with col4:
    st.write("Col 4 Content")
    st.metric("Login user",34,"-12")

#----------------------------------------------

st.title("Tabs Example")
tab1, tab2, tab3 ,tab4 = st.tabs(["Home", "Profile", "Settings","Summary"])

with tab1:
    st.header("Home")
    st.write("Welcome to the Home page.")

with tab2:
    st.header("Profile")
    name = st.text_input("Enter your name")
    st.write("Name:", name)

with tab3:
    st.header("Settings")
    dark_mode = st.checkbox("Enable Dark Mode")
    st.write("Dark Mode:", dark_mode)

with tab4:
    st.header("Summary")
    st.write("Hey")

st.header("Expender hide long or optional content")
with st.expander("Click to see content"):
    st.code(
        "Your are a helpful content",
        language="text"
    )

with st.expander("Click to see content"):
    st.write("You are a helpful content")
    st.code(
        """def greet(name):
        return f"Hello, {name}"
        """,
        language="python"
    )

show_debug = st.sidebar.checkbox("Show debug info")
if show_debug:
    st.warning("debug mode is on")
    st.json({"mode":model,"temperature":temperature})