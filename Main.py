# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
from helper_function.utility import check_password # <--- This is the helper function that we have created 🆕
from logics.customer_query_handler import process_user_message

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()

 
# endregion <--------- Streamlit App Configuration --------->

st.title("Streamlit App")

form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Enter your prompt here", height=200)

if form.form_submit_button("Submit"):
    st.toast(f"User Input Submitted - {user_prompt}")
    response, course_details = process_user_message(user_prompt)
    st.write(response)
    st.divider()
    df = pd.DataFrame(course_details)
    st.write(df)
    print(f"User Input is {user_prompt}")