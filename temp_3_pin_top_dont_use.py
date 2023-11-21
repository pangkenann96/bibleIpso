import streamlit as st

# Pre-refined variable
name = "John Doe"

# Streamlit app
def main():
    # Setting the top bar text
    st.set_page_config(page_title="My Streamlit App", page_icon=":world_map:")

    # Concatenating the greeting
    greeting = f"Hello {name}"

    # Displaying the top bar text
    st.markdown(f"<h1 style='text-align: center;'>{greeting}</h1>", unsafe_allow_html=True)

    # Rest of the app content
    st.write("Welcome to my Streamlit app!")
    st.write("Feel free to explore.")

if __name__ == '__main__':
    main()