import streamlit as st
import strongPasswordGenerator
import pyperclip

st.set_page_config(page_title="Strong Password Generator")
st.title("Strong Password Generator")
st.subheader("Let's generate it!")

if st.button("Generate and Copy"):
    generated_password = strongPasswordGenerator.generate_strong_password()
    #st.text_input("Generated password:", value=generated_password, disabled=True)
    st.write("**Generated password:**", generated_password)
    pyperclip.copy(generated_password)
    st.success("Password copied to clipboard")






