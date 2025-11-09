import streamlit as st

st.set_page_config(
    layout="centered",
    page_title="About This App"
)   

st.title("About This App")

st.markdown("""
This Streamlit application is designed to provide users with an interactive interface to submit prompts and receive responses.
""")

with st.expander("How to use this App", expanded=True):
    st.write(""" 
    1. Enter your prompt in the text area provided on the main page.
    2. Click the "Submit" button to send your prompt.
    3. View the response generated based on your input.
""")    
