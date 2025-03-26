import streamlit as st

if 'page' not in st.session_state:
    st.session_state.page = 'Iniciar sesión'

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def navigate(page):
    st.session_state.page = page

if st.session_state.page == 'Iniciar sesión':
    pass