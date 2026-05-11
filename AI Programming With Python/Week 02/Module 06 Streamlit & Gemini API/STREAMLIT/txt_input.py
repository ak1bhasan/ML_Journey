import streamlit as st

# st.write("Hello World")

st.title(":world_map: My first Streaamlit Web apps", anchor = False)

st.header("Content 1", divider = True)
st.subheader("Content 1 Subheader")

st.text("Hello Wolrd")

st.markdown(":red[**Hello**] *world*")

st.markdown(":red-background[:orange[**Hello**] *world*]:world_map:")

a = 10
b = 20

st.write(a, b)