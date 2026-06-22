---

# Pokémon TCG Pocket Chatbot

A terminal-based conversational assistant designed to help new players discover and understand Pokémon Trading Card Game Pocket.

## Project Overview

This is the Phase 2 implementation of a progressively built chatbot project. In this phase, the assistant relies entirely on **prompt engineering** to guide and inform new players about the game's mechanics, card types, and core systems.

The project will expand across future phases:
- **Phase 3**: RAG, web scraping, and SQL database for dynamic knowledge updates
- **Phase 4**: Frontend interface

## Techniques Applied

- **Few-shot prompting**: Four example exchanges included in the system prompt to shape response style and tone
- **Chain of Thought**: Structured two-step response format (solution → follow-up question) to guide the user progressively

## Features

- Conversational loop with persistent session memory (sliding window of last 20 messages)
- Graceful exit via `exit` or `quit` commands
- API error handling with `try/except` to prevent crashes
- Responses grounded in a static knowledge base covering 16 core topics about TCG Pocket

## Tech Stack

- Python 3
- OpenAI API (`gpt-4o-mini`)
- `python-dotenv` for environment variable management

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install openai python-dotenv
   ```
3. Create a `.env` file in the root directory:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
4. Run the chatbot:
   ```bash
   python main.py
   ```

## Usage

```
User: What is Pokémon TCG Pocket?
Assistant: Pokémon TCG Pocket is a free-to-play mobile app...

User: exit
Exiting the assistant. Goodbye!
```

## Project Structure

```
pokemon-pocket-chatbot/
├── main.py
├── .env
├── .gitignore
└── README.md
```

---
