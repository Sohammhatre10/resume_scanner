from openai import OpenAI
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

client = OpenAI()



# Initialize the OpenAI model with your API key
def llm(prompt):
    return client.chat.completions.create(
    model="gpt-4o",  # Use a chat model
    messages=[
        {"role": "system", "content": "You are a resume generator."},
        {"role": "user", "content": prompt}
    ]
)