import json
import sys
import os
from groq import Groq
from langchain.prompts import PromptTemplate

# Initialize Groq client
client = Groq(api_key="your_api_key_here")

def get_user_input(prompt):
    """
    Helper function to get input from the user.

    Args:
    prompt (str): The prompt message for user input.

    Returns:
    str: User input text.
    """
    return input(prompt).strip()

def create_resume_with_groq():
    """
    Gather user inputs, send them to Groq's Mixtral model to generate a structured resume.

    Returns:
    dict: Structured resume information in JSON format.
    """
    # Gather information from the user
    name = get_user_input("Enter your full name: ")
    phone_number = get_user_input("Enter your phone number: ")

    print("\nEnter your education details. Type 'done' when finished.")
    education = []
    while True:
        edu_detail = get_user_input("Education (e.g., 'BSc in Computer Science, University Name, Year'): ")
        if edu_detail.lower() == "done":
            break
        education.append(edu_detail)

    print("\nEnter your skills. Type 'done' when finished.")
    skills = []
    while True:
        skill = get_user_input("Skill (e.g., 'Python, Java'): ")
        if skill.lower() == "done":
            break
        skills.append(skill)

    print("\nEnter your work experience. Type 'done' when finished.")
    experience = []
    while True:
        exp = get_user_input("Experience (e.g., 'Software Engineer at Company, Year'): ")
        if exp.lower() == "done":
            break
        experience.append(exp)

    print("\nEnter your certifications. Type 'done' when finished.")
    certifications = []
    while True:
        cert = get_user_input("Certification (e.g., 'Certified Python Developer'): ")
        if cert.lower() == "done":
            break
        certifications.append(cert)

    # Structure user input into a prompt template
    template = """
    You are a resume generator. Given the following details, create a structured resume in JSON format:
    {{
        "name": "{name}",
        "phone_number": "{phone_number}",
        "education": {education},
        "skills": {skills},
        "experience": {experience},
        "certifications": {certifications}
    }}
    """
    prompt = PromptTemplate(template=template, input_variables=["name", "phone_number", "education", "skills", "experience", "certifications"])
    formatted_prompt = prompt.format(
        name=name,
        phone_number=phone_number,
        education=education,
        skills=skills,
        experience=experience,
        certifications=certifications
    )

    # Make the API call to the Groq client
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

    # Parse JSON response
    try:
        json_output = json.loads(response)
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON response from model.")
        json_output = {"error": "Failed to parse JSON"}

    return json_output

def save_json_to_file(data, output_file):
    """
    Save JSON data to a file.

    Args:
    data (dict): JSON data to save.
    output_file (str): Path to the output file.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"\nJSON data has been saved to {output_file}")

if __name__ == "__main__":
    try:
        # Create resume data through Groq's model
        resume_data = create_resume_with_groq()
        
        # Specify output file name
        output_file = "resume_generated.json"
        
        # Save resume data to JSON file
        save_json_to_file(resume_data, output_file)
        
        print("\nGenerated Resume Data:")
        print(json.dumps(resume_data, indent=2))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
