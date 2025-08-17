import os
import openai
import anthropic
from google import genai
from typing import Protocol

class LLMClient(Protocol):
    """A protocol for LLM clients to generate notes."""
    def generate_notes(self, transcript: str) -> str:
        ...

class GeminiClient:
    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)

    def generate_notes(self, transcript: str) -> str:
        prompt = f"Please summarize the following transcript into concise, well-structured notes:\n\n{transcript}"
        response = self.client.models.generate_content(
            model='gemini-1.5-flash',
            contents=prompt
        )
        return response.text or ""

class OpenAIClient:
    def __init__(self, api_key: str):
        self.client = openai.OpenAI(api_key=api_key)

    def generate_notes(self, transcript: str) -> str:
        prompt = f"Please summarize the following transcript into concise, well-structured notes:\n\n{transcript}"
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        content = response.choices[0].message.content
        return content or ""

class AnthropicClient:
    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)

    def generate_notes(self, transcript: str) -> str:
        prompt = f"Please summarize the following transcript into concise, well-structured notes:\n\n{transcript}"
        response = self.client.messages.create(
            model="claude-2.1",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        text_parts = [block.text for block in response.content if block.type == 'text']
        return "".join(text_parts)

def get_llm_client() -> LLMClient:
    """
    Factory function to get the appropriate LLM client based on the environment variable.
    """
    provider = os.getenv("LLM_PROVIDER", "GEMINI").upper()

    if provider == "GEMINI":
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")
        return GeminiClient(api_key=api_key)
    
    elif provider == "OPENAI":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables.")
        return OpenAIClient(api_key=api_key)

    elif provider == "ANTHROPIC":
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables.")
        return AnthropicClient(api_key=api_key)
        
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")

def generate_notes_with_llm(transcript: str) -> str:
    """
    Generates notes from a transcript using the selected LLM.
    """
    try:
        client = get_llm_client()
        return client.generate_notes(transcript)
    except Exception as e:
        return f"Error generating notes: {e}"
