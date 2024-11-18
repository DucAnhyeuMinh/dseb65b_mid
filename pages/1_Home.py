import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from Modules import VisualHandler
import base64

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="collapsed",
)

VisualHandler.set_background('./home/background.webp')
VisualHandler.custom_sidebar()
st.title("MBTI PERSONA")
def display_home(): # Task for Nguyen Dang Minh, Ninh Duy Tuan
    col1, col2 = st.columns([15,5])
    with col1:
        st.header("""Welcome to our website! \n Only 10 minutes to get a “freakishly accurate” description of who you are and why you do things the way you do.""")
    st.markdown("""
        <style>
        .test-button {
        color: white;
        font-size: 5px;
        padding: 40px 15px;
        border-radius: 20px;
        border: none;
        cursor: pointer;
        display: inline-block;
        font-family: Arial, sans-serif;
        text-align: center;
        }
        .background {
        width: 10%;
        height: 10vh;
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative;
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown('<div class="background">', unsafe_allow_html=True)
    if st.button("Take the Test", key="test_button"):
        switch_page("Personality Test")
    st.markdown('</div>', unsafe_allow_html=True)
    #st.image('/Users/apple/Library/Mobile Documents/com~apple~CloudDocs/Downloads/Product-launching-plan.pptx', width=200)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.markdown('<div style="text-align: left; font-size: 25px;">144K+ </div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: left; font-size: 15rx;">Tests taken today </div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div style="text-align: center; font-size: 25px;">25K+</div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: center; font-size: 15px;">Tests taken in VietNam </div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div style="text-align: right; font-size: 25px;">1000K+</div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: right; font-size: 15px;">Total tests taken </div>', unsafe_allow_html=True)
    st.header("""PERSONALITY TYPES
                  
    Understand others""") 
   # with col2:
      #  st.image('/Users/apple/Library/Mobile Documents/com~apple~CloudDocs/Downloads/Product-launching-plan.pptx', width=200) 
    
    st.write("""
    In our free type descriptions you’ll learn what really drives, inspires, and worries different personality types, helping you build more meaningful relationships.""")

display_home()