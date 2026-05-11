# AI Code Debugger

An AI-powered Streamlit app that helps developers understand and fix code errors by analyzing screenshots of error messages.

## 🚀 Live Demo

[🔗 Live App](https://aidebug.streamlit.app/)

## Features

- Upload up to 3 images of code errors
- AI analyzes the error from screenshots
- Detects and explains the issue clearly
- Provides helpful hints without revealing the full solution
- Generates a full solution with corrected code
- Beginner-friendly explanations
- Clean and interactive UI using Streamlit

## Tech Stack

- Python
- Streamlit
- Google Gemini API (GenAI)
- PIL (Python Imaging Library)

## Project Structure
```text
📁 AI Code Debugger App
├── app.py              
├── api_calling.py      
├── requirements.txt
└── README.md
```

## How It Works

1. Upload one or more images containing code errors.
2. Images are processed and sent to the Gemini API.
3. Based on the selected mode, the app provides either hints or a full solution.
4. Output is displayed in two sections:
   - **The Issue**
   - **The Solution**

## Modes

### Hints Mode

- Explains the issue
- Provides hints only
- Helps users think through the fix themselves

### Solution with Code Mode

- Explains the issue
- Provides step-by-step solutions
- Shows corrected code
- Gives a clear explanation of why the fix works
