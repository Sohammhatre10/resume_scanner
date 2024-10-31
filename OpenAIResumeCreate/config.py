from langchain.llms import OpenAI
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# Access the API key from the environment variable
api_key = os.getenv("API_KEY")


# Initialize the OpenAI model with your API key
llm = OpenAI(api_key=api_key, model="text-davinci-003")  # Adjust model if needed
