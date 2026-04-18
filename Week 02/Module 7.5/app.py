import streamlit as st
from api_calling import debug_generator
from PIL import Image

# title
st.title("AI Code Debugger")
st.markdown("Upload the image of your code error")

st.divider()


with st.sidebar :
    st.header("Controls")
    # image
    images = st.file_uploader(
        "Upload  the photos of your code",
        type = ["jpeg", "jpg", "png"],
        accept_multiple_files= True
    )
    
    pil_images = []
    if images :
        for img in images :
            pil_image = Image.open(img)
            pil_images.append(pil_image)
    
    if images :
        if len(images) > 3 :
            st.error("You can upload maximum 3 images only.")
        else :
            st.subheader("Uploaded Images")
            
            col = st.columns(len(images))
            for i, img in enumerate(images) :
                with col[i] :
                    st.image(img)
                    
    # Button
    debug_button = st.selectbox(
        "How you want to solve the problem",
        ("Hints", "Solution with code"),
        index = None
    )
    
    pressed = st.button("Click the button to initiate AI", type = "primary")
    
if pressed :
    if not images :
        st.error("You must upload 1 image")
    elif not debug_button :
        st.error("You must select an option")
    
    
    if images and debug_button :
        # issue
        if debug_button == "Hints" :
            with st.container(border = True) :
                st.subheader("The Issue :")
            
                with st.spinner("AI is finding the issue...") :
                    issue_result = debug_generator(pil_images, "issue")
                    st.markdown(issue_result)
        
            # Solution of issue
            with st.container(border = True) :
                st.subheader("The Solution")
                
                with st.spinner("Don't worry, AI is here to provide the solution...") :
                    solution_result = debug_generator(pil_images, debug_button)
                    st.markdown(solution_result)
                    
                    
        elif debug_button == "Solution with code" :
            with st.container(border = True) :
                st.subheader("The Issue :")
            
                with st.spinner("AI is finding the issue...") :
                    issue_result = debug_generator(pil_images, "issue")
                    st.markdown(issue_result)
        
            # Solution of issue
            with st.container(border = True) :
                st.subheader("The Solution")
                
                with st.spinner("Don't worry, AI is here to provide the solution...") :
                    solution_result = debug_generator(pil_images, debug_button)
                    st.markdown(solution_result)
                           



        