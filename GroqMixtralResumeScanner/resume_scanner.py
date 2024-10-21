import json
import sys
from PyPDF2 import PdfReader
import docx
from langchain.prompts import PromptTemplate
from groq import Groq

import os

client = Groq(
    api_key= "",
)



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

import re

import re

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
    # Create a prompt using the provided template
    prompt = PromptTemplate(template=template, input_variables=["text"])
    formatted_prompt = prompt.format(text=text)

    # Make the API call
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": formatted_prompt,
            }
        ],
        model="mixtral-8x7b-32768",
    )
    response = chat_completion.choices[0].message.content

    # Extract JSON data from the response using regular expressions
    json_match = re.search(r"\{.*\}", response, re.DOTALL)
    if json_match:
        json_text = json_match.group(0)
        # Further cleaning: remove trailing non-JSON text if any exists
        json_text = json_text.rsplit("}", 1)[0] + "}"
        try:
            json_output = json.loads(json_text)
        except json.JSONDecodeError:
            print("Error: The cleaned content is not valid JSON. Raw output:", json_text)
            json_output = {"error": "Failed to parse JSON"}
    else:
        print("Error: No valid JSON found in the response. Raw output:", response)
        json_output = {"error": "No valid JSON found"}

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