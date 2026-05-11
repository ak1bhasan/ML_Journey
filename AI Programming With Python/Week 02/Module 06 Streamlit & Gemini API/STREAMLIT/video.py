import streamlit as st

st.title("Input your files (video)", anchor = False)

st.divider()


video_files = st.file_uploader("Enter your video", 
                 type = ['mp4', 'mkv'])

# print(type(video_files))

button = st.button("Click to upload")

if button :
    if video_files:
        st.video(video_files)
        st.success("Your file is uploaded successfully.")
    else :
        st.error("You must upload a file.")
        




