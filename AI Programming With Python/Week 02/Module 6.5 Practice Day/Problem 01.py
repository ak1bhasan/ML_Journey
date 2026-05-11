import streamlit as st

st.title("Calculator")

st.divider()

a = st.number_input("Enter a number : ", value = None)
b = st.number_input("Enter another number : ", value = None)

operation = st.selectbox("Choose operation", 
                         ("+", "-", "*", "/"))

result = 0
if st.button("Calculate"):
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        if b != 0:
            result = a / b
        else :
            st.error("Can not divide by zero.")
            result = None
        

if result is not None :
    st.success(f"Result : {result}")
    