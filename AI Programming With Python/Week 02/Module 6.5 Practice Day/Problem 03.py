from google import genai
import os 
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


st.title("Text Improving")
st.divider()


user_input = st.text_input("Write a sentence : ", )
client = genai.Client(api_key = api_key)


response = None

if st.button("Improved Version") :
    if user_input.strip() == "":
        st.warning("Please enter a prompt")
    else :
        prompt = f"Improve this sentence professionally : {user_input}"
        response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents =(prompt)
        )


if response is not None:
    st.subheader("Improved Version : ")
    st.success(response.text)
