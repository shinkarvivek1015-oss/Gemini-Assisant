from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## ----------------------- Page config -----------------------
st.set_page_config(
    page_title="Gemini Assistant",
    page_icon="🌈",
    layout="centered",
    initial_sidebar_state="expanded",
)

## ----------------------- Colorful CSS -----------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #fceabb 0%, #f8b5c1 30%, #a1c4fd 65%, #c2ffd8 100%);
        background-attachment: fixed;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Header */
    .app-header {
        text-align: center;
        padding: 1.4rem 1rem 1rem 1rem;
    }
    .app-header .badge {
        display: inline-block;
        background: linear-gradient(135deg, #ff6b6b, #f8961e, #f9c74f);
        font-size: 1.6rem;
        width: 56px;
        height: 56px;
        line-height: 56px;
        border-radius: 18px;
        margin-bottom: 0.6rem;
        box-shadow: 0 6px 18px rgba(255, 107, 107, 0.45);
    }
    .app-header h1 {
        font-size: 1.9rem;
        font-weight: 800;
        background: linear-gradient(90deg, #ff6b6b, #f9844a, #f9c74f, #90be6d, #43aa8b, #577590);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.15rem;
        letter-spacing: -0.01em;
        animation: rainbowShift 6s ease infinite;
    }
    @keyframes rainbowShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .app-header p {
        color: #5b5468;
        font-size: 0.92rem;
        margin-top: 0;
        font-weight: 500;
    }

    /* Chat message container card look */
    [data-testid="stChatMessage"] {
        padding: 0.5rem 0;
        animation: fadeIn 0.25s ease-in;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(6px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* User message: right-aligned, punchy gradient bubble */
    div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarUser"]) {
        display: flex;
        justify-content: flex-end;
    }
    div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarUser"]) div[data-testid="stChatMessageContent"] {
        background: linear-gradient(135deg, #6a5ff7, #9d7bff);
        color: white;
        border-radius: 18px;
        border-bottom-right-radius: 6px;
        padding: 0.75rem 1.15rem;
        max-width: 78%;
        box-shadow: 0 6px 16px rgba(106, 95, 247, 0.35);
        font-weight: 500;
    }

    /* Assistant message: colorful card, left-aligned */
    div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) div[data-testid="stChatMessageContent"] {
        background: rgba(255, 255, 255, 0.85);
        border: 1px solid rgba(255,255,255,0.6);
        border-radius: 18px;
        border-bottom-left-radius: 6px;
        padding: 0.75rem 1.15rem;
        max-width: 82%;
        color: #33302b;
        line-height: 1.6;
        box-shadow: 0 6px 16px rgba(0,0,0,0.08);
        backdrop-filter: blur(6px);
    }

    /* Avatars */
    [data-testid="stChatMessageAvatarUser"] {
        background: linear-gradient(135deg, #6a5ff7, #9d7bff) !important;
    }
    [data-testid="stChatMessageAvatarAssistant"] {
        background: linear-gradient(135deg, #ff6b6b, #f9c74f) !important;
    }

    /* Chat input bar */
    [data-testid="stChatInput"] {
        border-radius: 20px;
        border: 2px solid transparent;
        background: linear-gradient(#ffffff, #ffffff) padding-box,
                    linear-gradient(135deg, #ff6b6b, #6a5ff7, #43aa8b) border-box;
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
    }
    [data-testid="stChatInput"] textarea {
        color: #2d2a26;
        font-weight: 500;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffe8d6 0%, #ffd6e8 50%, #d6e8ff 100%);
        border-right: 2px solid rgba(255,255,255,0.5);
    }
    section[data-testid="stSidebar"] h3 {
        color: #3d3a45;
        font-weight: 700;
    }
    section[data-testid="stSidebar"] label {
        color: #4a4555 !important;
        font-weight: 600;
    }

    /* Sidebar button */
    section[data-testid="stSidebar"] .stButton > button {
        background: linear-gradient(135deg, #ff6b6b, #f9844a);
        color: white;
        border: none;
        border-radius: 14px;
        font-weight: 700;
        padding: 0.55rem 1rem;
        box-shadow: 0 5px 14px rgba(255, 107, 107, 0.4);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    section[data-testid="stSidebar"] .stButton > button:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 8px 20px rgba(249, 132, 74, 0.5);
    }

    /* Selectbox */
    [data-baseweb="select"] {
        border-radius: 12px !important;
    }

    /* Slider accent */
    .stSlider [data-baseweb="slider"] div div div {
        background: linear-gradient(90deg, #ff6b6b, #6a5ff7) !important;
    }

    /* Custom scrollbar */
    ::-webkit-scrollbar { width: 10px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #ff6b6b, #6a5ff7);
        border-radius: 10px;
    }

    hr { border-color: rgba(255,255,255,0.5); }
</style>
""", unsafe_allow_html=True)

## ----------------------- Sidebar settings -----------------------
with st.sidebar:
    st.markdown("### 🎨 Settings")

    model_choice = st.selectbox(
        "Model",
        ["gemini-3.6-flash"],
        index=0,
    )

    temperature = st.slider("Creativity (temperature)", 0.0, 1.0, 0.7, 0.05)

    system_instruction = st.text_area(
        "System instruction (optional)",
        placeholder="e.g. Answer concisely. Be friendly and clear.",
        height=90,
    )

    st.markdown("---")
    if st.button("🗑️ New chat", use_container_width=True):
        st.session_state.pop("chat", None)
        st.session_state.pop("chat_history", None)
        st.session_state.pop("chat_config", None)
        st.rerun()

## ----------------------- 🔑 AI FUNCTION: session / model setup -----------------------
current_config = (model_choice, temperature, system_instruction)

if (
    "chat" not in st.session_state
    or st.session_state.get("chat_config") != current_config
):
    model_kwargs = {
        "generation_config": genai.GenerationConfig(temperature=temperature),
    }
    if system_instruction.strip():
        model_kwargs["system_instruction"] = system_instruction.strip()

    model = genai.GenerativeModel(model_choice, **model_kwargs)
    st.session_state["chat"] = model.start_chat(history=[])
    st.session_state["chat_config"] = current_config

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

## ----------------------- Header -----------------------
st.markdown("""
<div class="app-header">
    <div class="badge">🌈</div>
    <h1>Gemini Assistant</h1>
    <p>Ask me anything ✨</p>
</div>
""", unsafe_allow_html=True)

## ----------------------- Render existing chat history -----------------------
for msg in st.session_state["chat_history"]:
    avatar = "🧑" if msg["role"] == "user" else "✨"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["text"])

## ----------------------- Chat input (sticky bottom, Enter-to-send) -----------------------
prompt = st.chat_input("Message Gemini...")

if prompt:
    # Show user's message immediately
    st.session_state["chat_history"].append({"role": "user", "text": prompt})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)

    # 🔑 AI FUNCTION: send the message to Gemini and stream the reply back
    with st.chat_message("assistant", avatar="✨"):
        placeholder = st.empty()
        full_reply = ""
        try:
            response = st.session_state["chat"].send_message(prompt, stream=True)
            for chunk in response:
                if chunk.text:
                    full_reply += chunk.text
                    placeholder.markdown(full_reply + "▌")
            placeholder.markdown(full_reply if full_reply else "*(no response)*")
        except Exception as e:
            full_reply = f"⚠️ Something went wrong: {e}"
            placeholder.markdown(full_reply)

    st.session_state["chat_history"].append({"role": "assistant", "text": full_reply})

## ----------------------- Empty state -----------------------
if not st.session_state["chat_history"]:
    st.markdown("""
    <div style="text-align:center; color:#6b6478; padding: 3rem 1rem; font-weight: 500;">
        💬 Start typing below to chat with Gemini.
    </div>
    """, unsafe_allow_html=True)