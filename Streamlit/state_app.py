import streamlit as st
count = 0
if st.button("Click Counter"):
    count = count + 1
st.write("Count",count)

#count = st.session_state.count += 1
# st.write("Button Clicked:", st.session_state.count)

if "count" not in st.session_state:
    st.session_state.count = 0
if st.button("Add one more"):
    st.session_state.count += 1
st.write(st.session_state.count)