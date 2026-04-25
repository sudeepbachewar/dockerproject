import streamlit as st
import random
import time

st.set_page_config(page_title="Love Trap 💘", layout="centered")

# Title
st.markdown("<h1 style='text-align:center;'>💘 Confess Your Love 💘</h1>", unsafe_allow_html=True)

# Session state for steps
if "step" not in st.session_state:
    st.session_state.step = 0

# Random funny button texts
funny_texts = [
    "I LOVE YOU ❤️",
    "Click me if you dare 😏",
    "Don't click this 👀",
    "Totally safe button 😇",
    "Free chocolate 🍫",
    "Last warning ⚠️",
]

button_text = random.choice(funny_texts)

# Step 0 - teasing phase
if st.session_state.step == 0:
    st.markdown("### Do you really want to confess something? 🤔")

    if st.button(button_text):
        st.session_state.step = 1
        st.rerun()

# Step 1 - fake loading
elif st.session_state.step == 1:
    st.markdown("### Processing your feelings... 💭")

    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

    st.session_state.step = 2
    st.rerun()

# Step 2 - prank reveal
elif st.session_state.step == 2:
    st.balloons()
    st.markdown(
        "<h2 style='text-align:center; color:red;'>let's have sex gauri 🫦</h2>",
        unsafe_allow_html=True
    )

    if st.button("Try again 😂"):
        st.session_state.step = 0
        st.rerun()
