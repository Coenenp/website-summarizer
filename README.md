# website-summarizer
Website analyzer using chatgpt


# Analyze Pico's About Section

This repository contains a Python project that automates the analysis of the "About" section of the website [https://picoconsult.com/](https://picoconsult.com/). The script uses an agent-driven framework with OpenAI's GPT-4 to:

1. Visit the website.
2. Locate the "About" section.
3. Analyze its content.
4. Provide:
   - A concise, engaging summary (100-155 characters).
   - Five relevant tags/topics to categorize the content.
5. Save the results as a Markdown file (`analysis.md`).

---

## Features

- Uses **asynchronous programming** with Python's `asyncio`.
- Integrates with **OpenAI's GPT-4** for natural language processing.
- Saves results in a well-structured Markdown file for easy sharing.
- Supports environment variables using `dotenv`.

---

## Project Structure

```
root/
├── .env               # Environment variables (API keys, etc.)
├── analysis.md        # Output file with analysis results
├── main.py            # Main script for running the agent
├── requirements.txt   # List of Python dependencies
└── description.md     # Project description
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/analyze-pico-about.git
   cd analyze-pico-about
   ```

2. Create a Python virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your `.env` file with necessary environment variables (e.g., OpenAI API key):
   ```env
   OPENAI_API_KEY=your-openai-api-key
   ```

---

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. The agent will perform the following tasks:
   - Visit the website [https://picoconsult.com/](https://picoconsult.com/).
   - Locate the "About" section.
   - Analyze its content.
   - Generate a summary and propose tags.
   - Save the results to `analysis.md`.

---

## Output Example

The output file `analysis.md` will look like this:

```
# Analysis

## URL
https://picoconsult.com/

## Proposed Summary
(Populated by the script: A short summary of the "About" section.)

## Proposed Topics
- Topic 1
- Topic 2
- Topic 3
- Topic 4
- Topic 5
```

---
