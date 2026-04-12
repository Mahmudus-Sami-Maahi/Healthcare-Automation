# app.py
import os
import pandas as pd
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Set your Groq API key
os.environ["Your Model"] = "Your API Key"

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
- Specialization: [Insert Designation]
- Department: [Insert Department]
- Hospital: [Insert Hospital]
- Address: [Insert Address]
- Booking Time: [Insert Booking Time]
- Available Time: [Insert Available Time]

Rules:
1. Only use the dataset below.
2. If multiple doctors match, list all in the same format.
3. If nothing is found, say exactly: "No matching doctor found."
4. If the question is not related to medical or doctors, reply exactly: "I am a medical bot. I do not know other information."

5. Match user intent intelligently using keywords:

General Mapping:
- "heart", "chest pain" → Cardiology / Cardiologist
- "kidney", "urine" → Nephrology
- "skin", "rash", "acne" → Dermatology
- "bone", "joint", "fracture" → Orthopedic
- "child", "baby" → Pediatrics
- "mental", "depression", "anxiety" → Psychiatry
- "hormone", "diabetes", "thyroid" → Endocrinology
- "cancer", "tumor" → Oncology
- "ear", "nose", "throat", "sinus" → ENT

Newly Added:
- "eye", "vision", "blur", "eye pain" → Ophthalmology / Eye Specialist
- "head", "headache", "migraine", "brain" → Neurology / Neurologist
- "stroke", "seizure" → Neurology
- "fever", "infection" → General Physician / Internal Medicine
- "stomach", "gas", "ulcer", "liver" → Gastroenterology
- "lung", "breathing", "asthma" → Pulmonology
- "pregnancy", "women", "period" → Gynecology
- "teeth", "dental" → Dentistry

6. Search across:
- Doctor Name
- Designation (Specialization)
- Department
- Hospital
- Address
- Booking Time
- Available Time

7. Prefer exact matches, but allow partial and keyword-based matching.
8. Do not generate or assume any data outside the dataset.

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