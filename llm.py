from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

# Load environment variables from a .env file
load_dotenv()

# Ensure the required environment variable is set
if "MODEL_NAME" not in os.environ:
    raise ValueError("Environment variable 'MODEL_NAME' is not set. Please add it to your .env file.")

# Initialize the ChatGroq model
llm = ChatGroq(model_name=os.environ["MODEL_NAME"], temperature=0.4)

# Function to invoke the LLM and return the response content
def invoke_llm(message):
    try:
        response = llm.invoke(message)
        return response.content
    except Exception as e:
        print(f"Error invoking LLM: {e}")
        return None
