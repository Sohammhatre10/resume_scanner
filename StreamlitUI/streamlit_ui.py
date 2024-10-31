import streamlit as st
import json

# Model options for demo purposes
model_options = [
    "ChatOllamaResumeScanner", "ClaudeResumeScan", "GeminiResumeScan", 
    "GroqLlamaResumeScanner", "GroqMixtralResumeScanner", 
    "HuggingfaceTransformerResumeScanner", "LlamaCppResumeScan", 
    "MistralResumeScanner", "OllamaResumeScanner", "OpenAIResumeScanner"
]

# Function to simulate scanning a resume
def scan_resume(file, model):
    output = {
        "name": "John Doe",
        "phone_number": "+123456789",
        "education": ["BSc in Computer Science, University XYZ"],
        "skills": ["Python", "Java", "Machine Learning"],
        "experience": ["Software Engineer at Company ABC, 2020-2022"],
        "certifications": ["Certified Python Developer"]
    }
    return json.dumps(output, indent=2)

# Function to create a resume based on user input
def create_resume(name, phone, education, skills, experience, certifications, model):
    resume_data = {
        "name": name,
        "phone_number": phone,
        "education": education.split(","),
        "skills": skills.split(","),
        "experience": experience.split(","),
        "certifications": certifications.split(",")
    }
    return json.dumps(resume_data, indent=2)

# Streamlit Interface
st.title("Resume Scanner and Creator")

# Dropdown for selecting between Resume Scan and Resume Create
option = st.selectbox("Select Mode", ["Resume Scan", "Resume Create"])

# Model selection dropdown
model = st.selectbox("Select Model", model_options)

if option == "Resume Scan":
    # File uploader for Resume Scan mode
    file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])
    if file and st.button("Submit"):
        result = scan_resume(file, model)
        st.text_area("Result", result, height=200)
elif option == "Resume Create":
    # Input fields for Resume Create mode
    name = st.text_input("Name")
    phone = st.text_input("Phone Number")
    education = st.text_input("Education (comma-separated)")
    skills = st.text_input("Skills (comma-separated)")
    experience = st.text_input("Experience (comma-separated)")
    certifications = st.text_input("Certifications (comma-separated)")
    
    # Submit button for Resume Create mode
    if st.button("Submit"):
        result = create_resume(name, phone, education, skills, experience, certifications, model)
        st.text_area("Result", result, height=200)
