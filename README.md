<p align="center">
  <img src="assets/banner.jpg" alt="Gemini Assistant Banner" width="100%"/>
</p>

<h1 align="center">🌈 Gemini Assistant</h1>

<p align="center">
  <strong>A smart, Gemini-powered AI chat assistant that helps you answer questions, solve problems, write content, learn new concepts, and get things done faster.</strong>
</p>

<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/></a>
  <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/></a>
  <a href="https://ai.google.dev/"><img src="https://img.shields.io/badge/Google%20Gemini-API-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Gemini"/></a>
  <a href="https://github.com/shinkarvivek1015-oss/Gemini-Assisant"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License"/></a>
  <a href="https://github.com/shinkarvivek1015-oss/Gemini-Assisant"><img src="https://img.shields.io/github/stars/shinkarvivek1015-oss/Gemini-Assisant?style=for-the-badge&color=gold" alt="Stars"/></a>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-demo">Demo</a> •
  <a href="#-project-structure">Structure</a> •
  <a href="#-getting-started">Getting Started</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-contributing">Contributing</a>
</p>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **Gemini AI Integration** | Powered by Google's latest Gemini Flash model for fast, intelligent responses |
| 💬 **Real-Time Streaming** | Responses stream progressively with a live typing cursor for a smooth experience |
| 🎨 **Beautiful UI** | Colorful gradient backgrounds, glassmorphism effects, custom chat bubbles & avatars |
| 📜 **Chat History** | Full conversation history maintained during each session |
| ⚙️ **Customizable Settings** | Adjust model selection, creativity (temperature), and system instructions via sidebar |
| 🆕 **New Chat** | Clear the conversation and start fresh with a single click |
| 🔒 **Secure API Key** | API key loaded securely from `.env` environment variables |
| 📱 **Responsive Design** | Centered layout with custom scrollbar and responsive sidebar |
| ✍️ **Custom System Prompts** | Guide the AI's behavior with optional system instructions |
| 🌀 **Smooth Animations** | Fade-in animations on chat messages, hover effects on buttons, and a rainbow-shifting header |

---

## 🎬 Demo

<p align="center">
  <img src="https://img.shields.io/badge/▶_Run_Locally-See_Getting_Started-blueviolet?style=for-the-badge" alt="Run Demo"/>
</p>

**What the chat interface looks like:**

```
┌─────────────────────────────────────────────────────────────┐
│                    🌈  Gemini Assistant                     │
│                     Ask me anything ✨                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                       🧑  What is quantum computing?        │
│                                                             │
│  ✨  Quantum computing is a type of computation that        │
│      harnesses quantum mechanical phenomena such as         │
│      superposition and entanglement to process              │
│      information in fundamentally new ways...               │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  💬  Message Gemini...                                      │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

The project contains **three evolutionary versions** of the chatbot, each building on the previous:

```
Gemini-Assistant/
│
├── 📄 chat.py          # v1 — Basic Q&A chatbot (foundation)
├── 📄 hat.py           # v2 — Enhanced UI with custom CSS & dark theme
├── 📄 qachat.py        # v3 — Full-featured assistant (recommended ⭐)
├── 📄 .env             # API key configuration (not tracked in git)
├── 📁 assets/          # Project assets (banner image, etc.)
│   └── 🖼️ banner.jpg   # README banner image
└── 📄 README.md        # You are here!
```

### 📝 File Breakdown

#### `chat.py` — The Foundation
> A minimal, functional Q&A chatbot to get started quickly.

- ✅ Basic Streamlit text input + button interface
- ✅ Sends questions to Gemini and displays streamed responses
- ✅ Maintains simple chat history with role labels

#### `hat.py` — Enhanced Experience
> Adds a polished dark-mode UI with custom CSS styling.

- ✅ **Dark gradient background** (purple → deep violet)
- ✅ **Custom chat bubbles** — gradient-colored user & glass-effect bot messages
- ✅ **Avatar icons** for user (🧑) and bot (🤖)
- ✅ Responsive two-column input layout with a "Send 🚀" button
- ✅ Smooth box-shadow and hover effects on buttons

#### `qachat.py` — The Complete Assistant ⭐
> The production-ready version with all bells and whistles.

- ✅ **Rainbow gradient background** with Poppins font
- ✅ **Sidebar settings panel** with:
  - Model selection dropdown
  - Temperature/creativity slider (0.0 → 1.0)
  - Custom system instruction text area
  - "New Chat" button to reset the conversation
- ✅ **Streamlit `st.chat_message`** — native chat UI components
- ✅ **`st.chat_input`** — sticky bottom input bar with Enter-to-send
- ✅ **Real-time streaming** with a live `▌` typing cursor
- ✅ **Error handling** — gracefully catches API errors
- ✅ **Dynamic model reconfiguration** — changes take effect instantly
- ✅ **Rainbow-animated header** with CSS `@keyframes`
- ✅ **Custom scrollbar** with gradient styling

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.9+** installed on your machine
- A **Google Gemini API key** (get one free at [Google AI Studio](https://aistudio.google.com/apikey))

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/shinkarvivek1015-oss/Gemini-Assisant.git
cd Gemini-Assisant
```

**2. Create a virtual environment (recommended)**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install streamlit google-generativeai python-dotenv
```

**4. Configure your API key**

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY="your-google-gemini-api-key-here"
```

> ⚠️ **Never commit your `.env` file!** Add it to `.gitignore` to keep your API key safe.

**5. Run the application**

```bash
# Run the full-featured version (recommended)
streamlit run qachat.py

# Or try the other versions
streamlit run hat.py
streamlit run chat.py
```

The app will open automatically in your browser at `http://localhost:8501` 🎉

---

## 💡 Usage

### Basic Chatting
Simply type your question in the input bar at the bottom and press **Enter**. The AI will respond with a streaming, real-time answer.

### Adjusting Settings (qachat.py)
Open the **sidebar** (click `>` on the top-left) to:

| Setting | What It Does |
|---------|-------------|
| **Model** | Choose which Gemini model to use |
| **Temperature** | `0.0` = focused & deterministic, `1.0` = creative & varied |
| **System Instruction** | Set a persona or behavior guide (e.g., *"Be concise and professional"*) |
| **New Chat** | Clears all history and starts a fresh conversation |

### Example Prompts
```
💡 "Explain machine learning like I'm 5"
📝 "Write a professional email to reschedule a meeting"
💻 "Debug this Python code: [paste code]"
🎯 "Create a study plan for learning React in 30 days"
🧮 "Solve this equation step by step: 3x² + 5x - 2 = 0"
```

---

## 🛠️ Tech Stack

<p align="center">

| Technology | Purpose |
|-----------|---------|
| <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" /> | Core programming language |
| <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" /> | Web application framework & UI |
| <img src="https://img.shields.io/badge/Google_Gemini-4285F4?style=flat-square&logo=google&logoColor=white" /> | AI model API for intelligent responses |
| <img src="https://img.shields.io/badge/python--dotenv-ECD53F?style=flat-square&logo=python&logoColor=black" /> | Secure environment variable management |
| <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" /> | Custom styling, gradients & animations |

</p>

---

## 🏗️ Architecture

```mermaid
flowchart LR
    A[🧑 User] -->|Types message| B[Streamlit UI]
    B -->|Sends prompt| C[Google Gemini API]
    C -->|Streams response| B
    B -->|Displays in chat bubble| A
    B -->|Saves to| D[Session State]
    D -->|Loads history| B

    style A fill:#6a5ff7,stroke:#333,color:#fff
    style B fill:#FF4B4B,stroke:#333,color:#fff
    style C fill:#4285F4,stroke:#333,color:#fff
    style D fill:#43aa8b,stroke:#333,color:#fff
```

---

## 🔧 Configuration

| Environment Variable | Required | Description |
|---------------------|----------|-------------|
| `GOOGLE_API_KEY` | ✅ Yes | Your Google Gemini API key from [AI Studio](https://aistudio.google.com/apikey) |

### Model Parameters (adjustable in sidebar)

| Parameter | Default | Range | Description |
|-----------|---------|-------|-------------|
| `temperature` | `0.7` | `0.0 – 1.0` | Controls randomness. Lower = more focused, higher = more creative |
| `system_instruction` | *empty* | Free text | Optional persona/behavior instructions for the AI |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Ideas for Contributions
- 🖼️ Add image/file upload support
- 💾 Save/load conversation history to file
- 🌙 Add dark/light theme toggle
- 📊 Add token usage statistics
- 🔗 Multi-turn context management improvements

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

<p align="center">
  <a href="https://github.com/shinkarvivek1015-oss">
    <img src="https://img.shields.io/badge/GitHub-shinkarvivek1015--oss-181717?style=for-the-badge&logo=github" alt="GitHub"/>
  </a>
</p>

---

<p align="center">
  <strong>⭐ If you found this project helpful, please give it a star!</strong>
</p>

<p align="center">
  Made with ❤️ and powered by Google Gemini
</p>
