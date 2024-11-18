import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from Modules import VisualHandler
import base64

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",
)
if not st.session_state:
    VisualHandler.initial()
else:
    VisualHandler.custom_sidebar()
    VisualHandler.set_background(st.session_state.bg)

st.title("MBTI PERSONA")
def display_home(): # Task for Nguyen Dang Minh, Ninh Duy Tuan
    col1, col2 = st.columns([15,5])
    with col1:
        st.header("""Welcome to our website! \n Only 10 minutes to get a “freakishly accurate” description of who you are and why you do things the way you do.""")
    if st.button("Take the Test", key="test_button"):
        switch_page("Personality Test")
    st.markdown('</div>', unsafe_allow_html=True)
    #st.image('/Users/apple/Library/Mobile Documents/com~apple~CloudDocs/Downloads/Product-launching-plan.pptx', width=200)
    st.write('''41K+                     3M+
    \n Tests taken today
    \nTests taken in Vietnam
    1299M+
    \nTotal tests taken
    91.2%
    \nResults rated as accurate or very accurate''')
    col1, col3 = st.columns([1, 3])
    
    with col1:
        st.header("""PERSONALITY TYPES
    Understand others""") 
   # with col2:
      #  st.image('/Users/apple/Library/Mobile Documents/com~apple~CloudDocs/Downloads/Product-launching-plan.pptx', width=200) 
    with col3:
        st.write("""
    In our free type descriptions you’ll learn what really drives, inspires, and worries different personality types, helping you build more meaningful relationships.""")


display_home()
