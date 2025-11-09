import streamlit as st
import json
import pandas as pd

st.set_page_config(
    layout="centered",
    page_title="Course Details"
)   

st.title("Course Details")  

filepath = './data/courses-full.json'
# filepath = 'courses-full.json'

with open(filepath, 'r') as file:
    json_string = file.read()
    dict_of_courses = json.loads(json_string)

df = pd.DataFrame.from_dict(dict_of_courses, orient='index').reset_index()
df.index += 1

st.write("Here are the details of the courses available:",
         df
            )