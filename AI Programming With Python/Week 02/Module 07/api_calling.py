from google import genai
from dotenv import load_dotenv
from gtts import gTTS
import os, io

# loading the environment variable
load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

# initializing a client

client = genai.Client(api_key = my_api_key)


# note generator
def note_generator(images) :
    
    prompt = """
    You are an intelligent academic assistant.

    Read all uploaded images carefully and combine the information from all of them.

    #### Summary
    - Summarize the notes in max 100 words
    - Use simple English

    #### Key Points
    - Write 5-7 important bullet points
    - Include important terms, definitions, and code logic from all images

    Rules:
    - Use proper Markdown
    - No extra explanation
    - Do not ignore any clear image
    - If some text is blurry or unreadable, focus on the readable parts only
    """
    
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = images + [prompt]
    )
    
    return response.text


def audio_trancription(text) :
    speech = gTTS(text, lang = 'en', slow = False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer


def quiz_generator(image, difficulty) :
    prompt = f"""
    You are an intelligent academic assistant.

    Your task is to generate a quiz only from the uploaded note image.

    Difficulty Level: {difficulty}

    Follow these difficulty rules:
    - Easy: simple recall questions
    - Medium: understanding-based questions
    - Hard: conceptual and tricky questions

    Generate:
    - 3 MCQ questions
    - 2 short questions
    - 1 answer section

    STRICT OUTPUT FORMAT:

    #### MCQ Questions
    1. Question text
    A) Option 1
    B) Option 2
    C) Option 3
    D) Option 4

    2. Question text
    A) Option 1
    B) Option 2
    C) Option 3
    D) Option 4

    3. Question text
    A) Option 1
    B) Option 2
    C) Option 3
    D) Option 4

    #### Short Questions
    1. Question text
    2. Question text

    #### Answers
    - MCQ Answers: 1-A, 2-C, 3-B
    - Short Answers:
    1. brief answer
    2. brief answer

    Rules:
    - Only use information visible in the image
    - Do not use outside knowledge
    - Do not include explanations
    - Do not add any introduction or closing text
    - Do not add markdown except the exact headings shown above
    - Keep the formatting clean and exact
    """
    
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [image, prompt]
    )
    
    return response.text

    