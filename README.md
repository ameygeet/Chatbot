# Chatbot

# 🤖 Groq-Powered Chatbot

An intelligent, real-time chatbot powered by [Groq's ultra-fast LLM API](https://console.groq.com/) and built using [Streamlit](https://streamlit.io/). It uses Meta's LLaMA 4 Scout model to generate accurate and conversational responses in a clean, user-friendly interface.

---

## ✨ Features

- ⚡ **Ultra-Fast Responses** – Powered by Groq’s LPU-based low-latency API
- 🧠 **Smart Chat Memory** – Maintains conversation history in session
- 💬 **Styled Chat UI** – Beautiful layout using Streamlit + custom CSS
- 🛠️ **Fully Customizable** – Easy to tweak model, styling, and logic
- 🔐 **Secure Key Handling** – API key is managed via `.env` file

---

## 📁 Folder Structure

```
project/
├── chatbot.py         # Main app code
├── .env               # API key environment file
├── style.css          # Chat styling (UI customizations)
└── README.md          # Project documentation
```

---

## 🧰 Prerequisites

- Python 3.9 or higher
- Groq account & API key
- Installed Python packages:
  - `streamlit`
  - `groq`
  - `python-dotenv`

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/groq-chatbot.git
cd groq-chatbot
```

### 2. Install Required Packages

```bash
pip install streamlit groq python-dotenv
```

### 3. Add Your Groq API Key

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🚀 Usage

Start the chatbot app using:

```bash
streamlit run chatbot.py
```

This will open your browser where you can interact with the chatbot.

---

## 🧠 Model Configuration

The chatbot uses the following model from Groq:

- **Model**: `meta-llama/llama-4-scout-17b-16e-instruct`
- **Temperature**: `0.7`

These can be customized in `chatbot.py`.

---

## 🎨 Custom Styling

The `style.css` file contains custom CSS to control:

- Background and message bubble colors
- Font styles and sizes
- Layout spacing

You can modify it to suit your design preferences.

---

## ❓ Troubleshooting

| Issue                     | Solution                                                                 |
|--------------------------|--------------------------------------------------------------------------|
| `GROQ_API_KEY` not found | Ensure `.env` file exists and contains the correct key                   |
| Slow or no response       | Verify your internet and Groq API key; try restarting the Streamlit app |
| Model not found error    | Make sure the model name is valid on Groq's platform                     |

---

## 📸 Preview

*(You can insert a screenshot here)*  
Example:
```
+-----------------------------------+
| 💬 Ask Me Anything                |
|-----------------------------------|
| 🧑: Hello!                        |
| 🤖: Hi! How can I assist today?   |
+-----------------------------------+
```

---

## 🤝 Contributing

Pull requests are welcome! If you’d like to add new features, enhance the UI, or fix bugs, feel free to fork the repo and submit a PR.

---

## 📄 License

This project is licensed under the **MIT License**.  
You’re free to use, modify, and distribute it with attribution.

---

## 🙏 Credits

- [Groq](https://groq.com/) – For high-performance inference
- [Meta AI](https://ai.meta.com/) – For the LLaMA model family
- [Streamlit](https://streamlit.io/) – For the interactive UI framework

---

> Built with ❤️ using Groq + Streamlit  
> Created by [Your Name](https://github.com/yourusername)
