# 🧠 Terminal Chatbot using LangChain + OpenAI

This is a simple terminal-based chatbot built using [LangChain](https://www.langchain.com/) and OpenAI's GPT models. It demonstrates how to maintain chat history, use system instructions, and interact with a language model directly from the command line.

---

## 🚀 Features

- 💬 Interactive chat in terminal
- 🧠 Maintains conversation context
- ⚙️ Uses OpenAI's models
- 🔐 Secure API access via `.env`
- 📚 Good starting point for learning LangChain

---

## 🏗️ Tech Stack

- Python 3.8+
- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenAI API](https://platform.openai.com/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

---

## 📁 Project Structure

```
simple-chatbot/
├── app.py           # Main chatbot script
├── .env             # Stores OpenAI API key and model name
├── README.md        # Project documentation
```

---

## 🧪 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/simple-chatbot.git
cd simple-chatbot
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your `.env` file

Create a `.env` file in the root directory and add:

```
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL_NAME=your-choice-of-model
```

---

## 🧠 How It Works

- The app loads your API key and model from `.env`
- A system prompt defines the assistant’s personality
- Chat history is stored in memory and passed back to the model with every user query
- Use `exit` to quit the session

---

## 🖥️ Run the chatbot

```bash
python app.py
```

---

## 📝 Sample Conversation

```
You: What is the capital of France?
AI: The capital of France is Paris.
You: Who is the president?
AI: As of my knowledge cutoff in 2023, the president is Emmanuel Macron.
You: exit
```

---

## 📌 Notes

- The model is stateless by default, so we maintain the full chat history manually using LangChain's message schema.
- API usage costs are based on tokens used — keep track of your usage on OpenAI dashboard.