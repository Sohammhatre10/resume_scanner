import os
import json
import anthropic
import sys

# Put your Claude API key or replace with environment variable if needed
os.environ["ANTHROPIC_API_KEY"] = ""

def create_resume_with_claude(user_input):
    """
    Create a resume based on user-provided information using Claude and structure it into JSON format.

    Args:
    user_input (str): The user's input containing resume details.

    Returns:
    dict: Structured resume information in JSON format.
    """
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    
    # Defining the Claude prompt
    prompt = f"""
    You are a professional resume creator. Given the following details provided by a user, structure it in this JSON format:
    {{
        "name": "First Name Last Name",
        "phone_number": "Phone Number",
        "education": ["Education details"],
        "skills": ["Skill 1", "Skill 2", ...],
        "experience": ["Experience 1", "Experience 2", ...],
        "certifications": ["Certification 1", "Certification 2", ...]
    }}

    User Details: {user_input}
    """

    response = client.completions.create(
        model="claude-1",
        prompt=prompt,
        max_tokens_to_sample=1024,
        temperature=0.1
    )

    # Gets the response text
    response_text = response['completion']

    # Trying to parse the response into JSON
    try:
        json_output = json.loads(response_text)
    except json.JSONDecodeError:
        print("Error: The model output is not valid JSON. Raw output:", response_text)
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
    print(f"JSON data has been saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python claude_handler.py '<user_input>'")
        sys.exit(1)
    
    user_input = sys.argv[1]
    try:
        output = create_resume_with_claude(user_input)
        
        output_file = "generated_resume.json"
        
        save_json_to_file(output, output_file)
        
        print("Generated Resume Data:")
        print(json.dumps(output, indent=2))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
