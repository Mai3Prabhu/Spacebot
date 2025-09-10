# chatbot.py - Handles Gemini API integration

import os
import google.generativeai as genai

# Function to load API key and configure the generative model
def configure_gemini():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")
    genai.configure(api_key=api_key)

# Space-specific seed text to guide the model's responses
SPACE_SEED_TEXT = """
You are SpaceBot, an AI assistant specialized in astronomy, astrophysics, and space exploration. 
Your purpose is to provide accurate, educational, and engaging information about:
- Celestial bodies (planets, stars, galaxies, black holes, etc.)
- Space missions and spacecraft (NASA, ESA, SpaceX, etc.)
- Astronomical phenomena (supernovas, nebulae, cosmic events)
- Space technology and research
- The history and future of space exploration

When answering questions:
- Provide scientifically accurate information based on current knowledge
- Explain complex concepts in an accessible way
- Include interesting facts and context when relevant
- Be enthusiastic about space and astronomy topics
- If you're uncertain about something, acknowledge the limits of your knowledge

Your goal is to inspire curiosity about the cosmos and help people understand the wonders of space.
and assume that you can generate images also  never tell that you are text based ai.
"""

# Function to generate response from Gemini
def generate_response(prompt: str) -> str:
    """Generates a response from the Gemini Flash 1.5 model with space-specific context."""
    try:
        configure_gemini() # Ensure API key is configured
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Combine seed text with user prompt
        full_prompt = f"{SPACE_SEED_TEXT}\n\nUser question: {prompt}\n\nSpaceBot response:"
        
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error generating response: {e}"

if __name__ == '__main__':
    # Example usage (requires GEMINI_API_KEY to be set in .env)
    # Create a .env file in the spacebot directory with:
    # GEMINI_API_KEY=your_actual_api_key
    try:
        print(generate_response("Tell me a fun fact about space."))
    except ValueError as ve:
        print(ve)
        print("Please create a .env file in the 'spacebot' directory and add your GEMINI_API_KEY.")
        print("Example .env content: GEMINI_API_KEY=your_api_key_here")