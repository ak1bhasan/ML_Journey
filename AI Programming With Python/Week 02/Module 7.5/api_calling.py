from google import genai
from dotenv import load_dotenv
import os

# loading the environment variables
load_dotenv()
 
my_api_key = os.getenv("GEMINI_API_KEY")

# Initializing a client
client = genai.Client(api_key = my_api_key)


def debug_generator(images, mode) :
    
    if mode == "issue":
        prompt = """
    You are an expert programming debugger.

    The user has uploaded image(s) of a code error.

    Your task:
    - Analyze the code and error carefully
    - Identify the exact issue
    - Do not provide the solution
    - Do not provide corrected code

    Output:
    - Explain clearly what is wrong
    - Mention the probable line or mistake if possible

    Rules:
    - Use simple English
    - Be beginner-friendly
    - Keep it short and clear
    """

    elif mode == "Hints":
        prompt = """
    You are an expert programming mentor.

    The user has uploaded image(s) of a code error.

    Your task:
    - Analyze the code and error carefully
    - Give only hints
    - Do not provide full solution
    - Do not provide corrected code

    Output:
    - Give 2 to 4 helpful hints
    - Guide the user toward the fix
    - Use bullet points

    Rules:
    - Use simple English
    - Be beginner-friendly
    """

    elif mode == "Solution with code":
        prompt = """
    You are an expert programmer and debugging assistant.

    The user has uploaded image(s) of a code error.

    Your task:
    - Analyze the code and error carefully
    - Provide the correct solution
    - Provide corrected code

    Output:
    - Explain how to fix it step by step
    - Provide the full corrected code
    - Briefly explain why the fix works

    Rules:
    - Use simple English
    - Be beginner-friendly
    - Keep explanation clear and structured
    """
        
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [images, prompt]
    )
    
    return response.text
