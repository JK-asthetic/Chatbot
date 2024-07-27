import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai

# Configure the generative AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

# Define a function to generate a response from the model
def get_gemini_response(ques):
    resp = model.generate_content(ques)
    return resp.text

# Setting up the Streamlit app
st.set_page_config(
    page_title="Gemini Pro Q/A Project",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Setting up header
st.header("Gemini Q/A App")

# Initialize session state for history
if 'history' not in st.session_state:
    st.session_state.history = []

question = st.text_input("Ask a question: ")

if st.button("Submit"):
    response = get_gemini_response(question)
    
    # Save the interaction to history
    st.session_state.history.append((question, response))
    
    # Display the current interaction
    st.write("*User*:", question)
    st.write("*Bot*:", response)

# Display the history in the sidebar
with st.sidebar:
    st.header("History")
    if st.session_state.history:
        for i, (q, r) in enumerate(st.session_state.history):
            st.write(f"**Q{i + 1}:** {q}")
            st.write(f"**A{i + 1}:** {r}")
            st.write("---")
    else:
        st.write("No history yet.")
