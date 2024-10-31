import gradio as gr
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

# Define the Gradio Interface
def main_interface(option, model, file=None, name="", phone="", education="", skills="", experience="", certifications=""):
    if option == "Resume Scan":
        if file is None:
            return "Please upload a file for scanning."
        return scan_resume(file, model)
    elif option == "Resume Create":
        return create_resume(name, phone, education, skills, experience, certifications, model)

# Building the Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("## Resume Scanner and Creator")
    
    # Dropdown for selecting between Resume Scan and Resume Create
    option = gr.Dropdown(["Resume Scan", "Resume Create"], label="Select Mode")
    
    # Model selection dropdown
    model = gr.Dropdown(model_options, label="Select Model")
    
    # File uploader for Resume Scan mode
    file_input = gr.File(label="Upload Resume (PDF or DOCX)", visible=False)
    
    # Input fields for Resume Create mode
    name = gr.Textbox(label="Name", visible=False)
    phone = gr.Textbox(label="Phone Number", visible=False)
    education = gr.Textbox(label="Education (comma-separated)", visible=False)
    skills = gr.Textbox(label="Skills (comma-separated)", visible=False)
    experience = gr.Textbox(label="Experience (comma-separated)", visible=False)
    certifications = gr.Textbox(label="Certifications (comma-separated)", visible=False)
    
    # Output display
    output = gr.Textbox(label="Result", interactive=False)

    # Function to update input field visibility based on mode selection
    def update_visibility(selected_option):
        if selected_option == "Resume Scan":
            return gr.update(visible=True), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)
        else:
            return gr.update(visible=False), gr.update(visible=True), gr.update(visible=True), gr.update(visible=True), gr.update(visible=True), gr.update(visible=True), gr.update(visible=True)

    # Update the interface elements based on dropdown selection
    option.change(
        update_visibility,
        inputs=[option],
        outputs=[file_input, name, phone, education, skills, experience, certifications]
    )
    
    # Submit button to trigger the main function
    submit = gr.Button("Submit")
    submit.click(
        main_interface,
        inputs=[option, model, file_input, name, phone, education, skills, experience, certifications],
        outputs=output
    )

# Launch the Gradio app
demo.launch()
