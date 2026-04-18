import streamlit as st
from api_calling import note_generator, audio_trancription, quiz_generator
from PIL import Image

# title
st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note summary and Quizzes")

st.divider()


with st.sidebar :
    st.header("Controls")
    
    # images
    images = st.file_uploader(
        "Upload the photos of your note",
        type = ["jpeg", "jpg", "png"],
        accept_multiple_files = True
    )
    
    pil_images = []
    for img in images :
        pil_img = Image.open(img)
        pil_images.append(pil_img)
    
    
    if images :
        if len(images) > 3 :
            st.error("Upload at max 3 images.")
        else :
            st.subheader("Uploaded images")
            
            col = st.columns(len(images))
            
            for i, img in enumerate(images) :
                with col[i] :
                    st.image(img)
    
    
    # Difficulty
    selected_option = st.selectbox(
        "Enter the difficulty of your quiz",
        ("Easy", "Medium", "Hard"), 
        index = None
    )

    pressed = st.button("Click the button to initiate AI", type = "primary")
    

if pressed :
    if not images :
        st.error("You must upload 1 image")
    
    elif not selected_option :
        st.error("You must select a difficulty")
        

    if images and selected_option :
    
        # note
    
        with st.container(border = True) :
            st.subheader("Your Note : ")
            
            # the portion will be replaced by API call
            
            with st.spinner("AI is writing notes for you...") :
                generate_notes = note_generator(pil_images)
                st.markdown(generate_notes)
    
        # Audio Transcript
        
        with st.container(border = True) :
            st.subheader("Audio Transcription")
            
            # the portion will be replaced by API call
            with st.spinner("AI is generating audio for you...") :
                # clearing the markdown
                generate_notes = generate_notes.replace("#", "")
                generate_notes = generate_notes.replace("*", "")
                generate_notes = generate_notes.replace("`", "")
                generate_notes = generate_notes.replace("_", "")
                generate_notes = generate_notes.replace(">", "")
                generate_notes = generate_notes.replace("\n- ", "\n")
                generate_notes = generate_notes.replace("•", "")
                generate_notes = generate_notes.replace("\n", " ")
                generate_notes = generate_notes.replace("  ", " ")
                generate_notes = generate_notes.strip()

                audio_transcript = audio_trancription(generate_notes)
                st.audio(audio_transcript) 
        
        # Quiz
        
        with st.container(border = True) :
            st.subheader(f"Quiz ({selected_option} Level)")
            with st.spinner("AI is generating quiz for you...") :
                # the portion will be replaced by API call
                quizzess = quiz_generator(pil_images, selected_option)
                st.markdown(quizzess) 