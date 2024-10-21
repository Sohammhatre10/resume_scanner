import json
import sys
from PyPDF2 import PdfReader
import docx
from ollama import Client
import os
import re

def extract_text_from_pdf(file_path):
    """
    Extract text content from a PDF file.

    Args:
    file_path (str): Path to the PDF file.

    Returns:
    str: Extracted text from the PDF.
    """
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file_path):
    """
    Extract text content from a DOCX file.

    Args:
    file_path (str): Path to the DOCX file.

    Returns:
    str: Extracted text from the DOCX.
    """
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def analyze_resume(text):
    """
    Analyze the given resume text and structure it into JSON format.

    Args:
    text (str): The resume text to analyze.

    Returns:
    dict: Structured resume information in JSON format.
    """
    template = """
    You are a professional resume scanner. Given the following resume text, extract the most relevant information and structure it in this JSON format:
    {{
        "name": "First Name Last Name",
        "phone_number": "Phone Number",
        "education": ["Education details"],
        "skills": ["Skill 1", "Skill 2", ...],
        "experience": ["Experience 1", "Experience 2", ...],
        "certifications": ["Certification 1", "Certification 2", ...]
    }}

    Resume Text: {text}
    """

    ollama_url      = os.getenv("OLLAMA_URL", "localhost")
    ollama_port     = os.getenv("OLLAMA_PORT", "11434")
    ollama_model    = os.getenv("OLLAMA_MODEL", "llama3.2")
    ollama_ssl      = os.getenv("OLLAMA_SSL", False)
    ollama_protocol = "https" if ollama_ssl else "http"

    prompt = template.format(text=text)
    client = Client(host=f'{ollama_protocol}://{ollama_url}:{ollama_port}')
    response = client.chat(model=ollama_model, messages=[
      {
        'role': 'user',
        'content': prompt,
      },
    ])

    response = extract_json_string_from_text(response['message']['content'])
    try:
        json_output = json.loads(response)
    except json.JSONDecodeError:
        print("Error: The model output is not valid JSON. Raw output:", response)
        json_output = {"error": "Failed to parse JSON"}

    return json_output

def process_resume(file_path):
    """
    Process a resume file and extract structured information.

    Args:
    file_path (str): Path to the resume file (PDF or DOCX).

    Returns:
    dict: Structured resume information in JSON format.

    Raises:
    ValueError: If the file format is not supported.
    """
    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        text = extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Only PDF and DOCX are allowed.")

    structured_output = analyze_resume(text)
    return structured_output

def save_json_to_file(data, output_file):
    """
    Save JSON data to a file.

    Args:
    data (dict): JSON data to save.
    output_file (str): Path to the output file.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"JSON data has been saved to {output_file}")

def extract_json_string_from_text(text):
    """
    Extract JSON string pattern from text

    Args:
    text (str): input text

    Returns:
    str: First JSON pattern found in text input, if no JSON was found then return the input
    """
    json_pattern = r'\{.*\}'

    matches = re.findall(json_pattern, text, re.DOTALL)

    json_objects = []
    for match in matches:
        json_objects.append(match)

    return json_objects[0] if len(json_objects) > 0 else text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_resume_file>")
        sys.exit(1)

    resume_file = sys.argv[1]
    try:
        output = process_resume(resume_file)

        output_file = os.path.splitext(resume_file)[0] + "_analysis.json"

        save_json_to_file(output, output_file)

        print("Analyzed Resume Data:")
        print(json.dumps(output, indent=2))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
