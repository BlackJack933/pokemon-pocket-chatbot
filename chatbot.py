# Terminal Chatbot — OpenAI API
#
# A conversational chatbot that runs in the terminal.
# Maintains a sliding memory window of 20 messages and tracks token costs.
#
# Model : gpt-4o-mini
# Pricing: $0.60 / 1M prompt tokens | $0.15 / 1M completion tokens

from openai import OpenAI
import os
from dotenv import load_dotenv

# --- 1. Setup ---
# Load API key from .env and initialise the OpenAI client
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- 2. State ---
# System prompt stored as a variable to avoid duplication
system_prompt = {"role": "system", "content": "You are a helpful assistant."}
memory = [system_prompt]  # Full conversation history (used for storage only)
totale = 0                # Cumulative cost in USD
response = None           # Initialised to None to handle early exit safely

# --- 3. Chat Loop ---
while True:

    user_input = input("User: ")

    # Exit on quit command — print usage stats only if at least one call was made
    if user_input.lower() in ["exit", "quit"]:
        print("Arrivederci")
        if response is not None:
            print(response.usage)
            print(f"Hai speso {totale}$ ")
        break

    # Append user message to full history
    memory.append({"role": "user", "content": user_input})

    # Build the context window: system prompt + last 20 messages
    # Keeps costs low and avoids hitting the context limit on long conversations
    messages = [system_prompt] + memory[-20:]

    # Call the API
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    # Append assistant reply to full history
    memory.append({"role": "assistant", "content": response.choices[0].message.content})

    print(response.choices[0].message.content, "\n")

    # --- 4. Cost Tracking ---
    # Price per single token = price per million / 1_000_000
    totale += (response.usage.completion_tokens * 0.00000015) + \
              (response.usage.prompt_tokens * 0.0000006)
