# Notes Creator

A vibe-coded desktop app to generate notes from YouTube video transcripts using AI.

## Features

- Fetches transcripts from YouTube videos.
- Uses AI to generate concise, well-structured notes.
- Supports multiple LLM providers: Gemini, OpenAI, and Anthropic.
- Simple and intuitive GUI.

## Requirements

- Python 3.11 or higher
- An API key for one of the supported LLM providers (Gemini, OpenAI, or Anthropic)

## How to Run Locally

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/notes-creator.git
    cd notes-creator
    ```

2.  **Install dependencies using uv:**

    ```bash
    uv pip install -e .
    ```

3.  **Set up your environment variables:**

    - Copy the `.env.example` file to a new file named `.env`:
      ```bash
      cp .env.example .env
      ```
    - Open the `.env` file and add your API key for the desired LLM provider.
    - Make sure to set the `LLM_PROVIDER` variable to the provider you are using (e.g., `LLM_PROVIDER=GEMINI`).

4.  **Run the application:**
    ```bash
    uv run notes-creator
    ```

## How to Use

1.  Launch the application.
2.  Paste a YouTube video URL into the input field.
3.  Click the "Generate Notes" button.
4.  The generated notes will appear in the text box below.
