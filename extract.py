# app.py
import streamlit as st
import pandas as pd
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import os

# Set your Groq API key
os.environ["GROQ_API_KEY"] = "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"

# -------------------------------
# 1. Load CSV Data
# -------------------------------
@st.cache_data
def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df.to_string(index=False)

csv_file = "doctors_data.csv"
data_text = load_csv(csv_file)

# -------------------------------
# 2. Initialize LLM
# -------------------------------
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

# -------------------------------
# 3. Prompt Template
# -------------------------------
template = """
You are a helpful medical assistant. Your job is to find doctor information from the dataset below.

Format:
- Doctor Name: [Insert Name]
- Department: [Insert Department]
- Hospital: [Insert Hospital]
- Address: [Insert Address]

Rules:
1. Only use the dataset below.
2. If multiple doctors match, list all.
3. If nothing found, say: "No matching doctor found."
4. If the question is not related to medicine, reply: "I am a medical bot. I do not know other information."
5. Search doctor department based on the user question keywords, for example: "kidney" should match "nephrology".

Dataset:
{data}

User question:
{question}

Answer:
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | llm

# -------------------------------
# 4. Streamlit Chatbot UI
# -------------------------------
st.title("🩺 Evercare Hospital Doctor Chatbot")

# Initialize session state for assistant messages only
if "assistant_messages" not in st.session_state:
    st.session_state.assistant_messages = []

# User input
user_input = st.text_input("Type your question here...", "")

if st.button("Send") and user_input:
    with st.spinner("Searching..."):
        response = chain.invoke({
            "question": user_input,
            "data": data_text
        })
        assistant_msg = response.content

    # Save assistant message only
    st.session_state.assistant_messages.append(assistant_msg)

# Display assistant messages only
for msg in st.session_state.assistant_messages:
    st.markdown(f"**Assistant:** {msg}")