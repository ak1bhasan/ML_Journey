from google import genai
import os 
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


st.title("Generate Response")
st.divider()


user_input = st.text_input("Write a prompt : ")
client = genai.Client(api_key = api_key)

response = None

if st.button("Generate") :
    if user_input.strip() == "":
        st.warning("Please enter a prompt")
    else :
        response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = user_input
        )

if response is not None :
    st.markdown(response.text)

