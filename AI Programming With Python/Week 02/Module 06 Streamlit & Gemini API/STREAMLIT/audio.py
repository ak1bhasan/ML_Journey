import streamlit as st

st.title("Input your files (audio)", anchor = False)

st.divider()

# from directory

st.audio("audio/welcome.mp3", loop = True)

st.divider()



audio_files = st.file_uploader("Enter your audio", 
                 type = ['mp3', 'ogg', 'flac'])

print(type(audio_files))


if audio_files:
    st.audio(audio_files)
