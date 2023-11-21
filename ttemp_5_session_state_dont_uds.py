import streamlit as st

# Function to initialize session state
def initialize_session_state():
    if 'selected_row' not in st.session_state:
        st.session_state.selected_row = None

# Initialize session state
initialize_session_state()

# Display the selected row
st.write('Selected Row:', st.session_state.selected_row)

# Update the selected row
selected_row = st.number_input('Select a row', min_value=0, max_value=10, key='selected_row_input')

if selected_row is not None:
    st.session_state.selected_row = selected_row

# Display the updated selected row
st.write('Updated Selected Row:', st.session_state.selected_row)