import google.generativeai as genai
import os
import streamlit as st

# Get API for the model

key = os.getenv('GOOGLE_API_KEY')

# Configure the model

genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-2.5-flash-lite')

#Create a frontend UI
st.title('Simple Text Generation')
st.header('This is to test the Gemini Model as application')
prompt = st.text_input('Write your prompt here', max_chars=10000)
if prompt:
    response = model.generate_content(prompt)
    st.write(response.text)