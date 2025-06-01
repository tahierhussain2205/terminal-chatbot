from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI model name from environment variable
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME", "gpt-3.5-turbo")

# Initialize the OpenAI Chat model
llm = ChatOpenAI(model=OPENAI_MODEL_NAME)

# Stores the full conversation history as a list of messages
conversation_history = []

# Define the system prompt to set the behavior of the AI
system_prompt = SystemMessage(content="You are a helpful AI assistant.")
conversation_history.append(system_prompt)

# Begin interactive chat loop
while True:
    # Take user input
    user_input = input("You: ")

    # Allow user to exit the loop
    if user_input.lower() == "exit":
        break

    # Add the user message to the conversation history
    conversation_history.append(HumanMessage(content=user_input))

    # Invoke the model with the full conversation history
    model_response = llm.invoke(conversation_history)

    # Extract and print the AI's response
    ai_reply = model_response.content
    print(f"AI: {ai_reply}")

    # Add the AI's response to the conversation history
    conversation_history.append(AIMessage(content=ai_reply))
