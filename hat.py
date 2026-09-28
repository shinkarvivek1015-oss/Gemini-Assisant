from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load gemini model and get response
model = genai.GenerativeModel("gemini-3.6-flash")

if 'chat' not in st.session_state:
    st.session_state['chat'] = model.start_chat(history=[])

def get_gemini_response(question):
    response = st.session_state['chat'].send_message(question, stream=True)
    return response

## ----------------------- Page config -----------------------
st.set_page_config(
    page_title="Gemini Chat",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed",
)

## ----------------------- Custom CSS -----------------------
st.markdown("""
<style>
    /* Overall app background */
    .stApp {
        background: linear-gradient(135deg, #1f1c2c 0%, #2d1b4e 45%, #4a1d6b 100%);
    }

    /* Hide default streamlit chrome */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Header banner */
    .app-header {
        text-align: center;
        padding: 1.8rem 1rem 1.2rem 1rem;
    }
    .app-header h1 {
        background: linear-gradient(90deg, #a78bfa, #f472b6, #60a5fa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.4rem;
        font-weight: 800;
        margin-bottom: 0;
    }
    .app-header p {
        color: #c9c3e0;
        font-size: 0.95rem;
        margin-top: 0.2rem;
    }

    /* Chat bubble container */
    .chat-row {
        display: flex;
        margin: 0.6rem 0;
        align-items: flex-start;
    }
    .chat-row.user {
        justify-content: flex-end;
    }
    .chat-row.bot {
        justify-content: flex-start;
    }
    .bubble {
        max-width: 75%;
        padding: 0.75rem 1.1rem;
        border-radius: 18px;
        font-size: 0.98rem;
        line-height: 1.45;
        box-shadow: 0 4px 14px rgba(0,0,0,0.25);
        word-wrap: break-word;
    }
    .bubble.user {
        background: linear-gradient(135deg, #7c3aed, #a855f7);
        color: white;
        border-bottom-right-radius: 4px;
    }
    .bubble.bot {
        background: rgba(255,255,255,0.08);
        color: #f1f0f7;
        border: 1px solid rgba(255,255,255,0.12);
        border-bottom-left-radius: 4px;
        backdrop-filter: blur(6px);
    }
    .avatar {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1rem;
        margin: 0 8px;
        flex-shrink: 0;
    }
    .avatar.user { background: #a855f7; }
    .avatar.bot { background: #f472b6; }

    /* Input box styling */
    .stTextInput > div > div > input {
        background-color: rgba(255,255,255,0.08);
        color: white;
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 12px;
        padding: 0.6rem 1rem;
    }
    .stTextInput > div > div > input::placeholder {
        color: #ccc;
    }

    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #7c3aed, #ec4899);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.55rem 1.6rem;
        font-weight: 600;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
        box-shadow: 0 4px 12px rgba(124,58,237,0.4);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(236,72,153,0.5);
    }

    /* Divider */
    hr {
        border-color: rgba(255,255,255,0.1);
    }
</style>
""", unsafe_allow_html=True)

## ----------------------- Header -----------------------
st.markdown("""
<div class="app-header">
    <h1>✨ Gemini LLM Chat</h1>
    <p>Ask anything — powered by Google's Gemini model</p>
</div>
""", unsafe_allow_html=True)

## ----------------------- Session state -----------------------
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

## ----------------------- Input row -----------------------
col1, col2 = st.columns([5, 1])
with col1:
    input_text = st.text_input(
        "Input",
        key="input",
        placeholder="Type your question here...",
        label_visibility="collapsed",
    )
with col2:
    submit = st.button("Send 🚀", use_container_width=True)

## ----------------------- Handle submission -----------------------
if submit and input_text:
    st.session_state['chat_history'].append(("user", input_text))

    response = get_gemini_response(input_text)
    bot_reply = ""
    for chunk in response:
        if chunk.text:
            bot_reply += chunk.text

    st.session_state['chat_history'].append(("bot", bot_reply))

## ----------------------- Render chat history -----------------------
if st.session_state['chat_history']:
    st.markdown("<hr>", unsafe_allow_html=True)

for role, text in st.session_state['chat_history']:
    if role == "user":
        st.markdown(f"""
        <div class="chat-row user">
            <div class="bubble user">{text}</div>
            <div class="avatar user">🧑</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-row bot">
            <div class="avatar bot">🤖</div>
            <div class="bubble bot">{text}</div>
        </div>
        """, unsafe_allow_html=True)

## ----------------------- Empty state -----------------------
if not st.session_state['chat_history']:
    st.markdown("""
    <div style="text-align:center; color:#9d97c4; padding: 2rem;">
        💬 Start the conversation by typing a message above.
    </div>
    """, unsafe_allow_html=True)