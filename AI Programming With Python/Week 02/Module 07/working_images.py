import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

from PIL import Image

# loading the environment variable
load_dotenv()


my_api_key = os.getenv("GEMINI_API_KEY")

# initializing a client

client = genai.Client(api_key = my_api_key)

# images
images = st.file_uploader(
        "Upload the photos of your note",
        type = ["jpeg", "jpg", "png"],
        accept_multiple_files = True
    )


# print(type(images))

if images :
    pil_images = []
    for img in images :
        pil_img = Image.open(img)
        pil_images.append(pil_img)
        
        
    prompt = """
    You are an intelligent academic assistant.
    ## 📌 Summary
    - Summarize the note in max 150 words
    - Use simple English

    ## 🧠 Key Points
    - 5-7 important bullet points

    Rules:
    - Use proper Markdown
    - No extra explanation
    """
    
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [pil_images, prompt]
    )
    
    st.markdown(response.text)