import streamlit as st

st.title("Input your information", anchor = False)

st.divider()

name = st.text_input("Enter your name : ")

print(type(name))
# st.write(f"Your name is {name}")


st.divider()

age = st.number_input("Enter your age : ", value = None, placeholder = "Type your age...")

pressed = st.button("Enter to confirm", type = "primary")

selected = st.selectbox("Choose your profession", 
             ("Student", "Employee", "Businessman"),
             index = None,
             accept_new_options = True)

print(type(selected))
st.write("You selected ", selected)

# password = st.text_input("Enter your pass : ", type = "password")

# print(type(password))
# st.write(f"Your password {password}")
