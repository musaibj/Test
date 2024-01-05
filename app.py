import streamlit as st
from test import Generator

def main():
  st.title("Username Generator")

  first_name = st.text_input("Enter First Name")
  second_name = st.text_input("Enter Second Name")

  if st.button("Generate Usernames"):
    obj = Generator()
    usernames = obj.generate_username(first_name, second_name)

    st.subheader("Generated Usernames:")
    for username in usernames:
        st.write(username)

if __name__ == "__main__":
    main()
