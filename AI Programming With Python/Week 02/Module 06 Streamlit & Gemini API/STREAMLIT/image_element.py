import streamlit as st

st.title("Input your files (image)", anchor = False)

st.divider()

# Storage
st.image("images/linear_regression.jpeg")

# url
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUT2jLYoIC9Lg65AVA5KhEUdJdWFm0-vznZg&s")


st.divider()

images = st.file_uploader("Enter your image (at max 2)", 
                 type = ['jpeg', 'jpg', 'png'],
                 accept_multiple_files = True)

print(type(images))

if images :
    if len(images) > 2 :
        st.warning("You uploaded 3 photos.")
    col = st.columns(len(images))
    for i, per_image in enumerate(images) :
        with col[i] :
            st.image(per_image)