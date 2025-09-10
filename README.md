# SpaceBot: Your Cosmic Companion 🚀
## Project Description
SpaceBot is an interactive, AI-powered chatbot designed to be your personal guide to the cosmos. Built with Streamlit, it leverages Google's Gemini model to provide accurate and engaging information on a wide range of space-related topics, from celestial bodies to historical missions. This application goes a step further by integrating with the NASA API to display relevant images when you ask for them. Just ask a question, and let SpaceBot take you on a journey through the universe!

## Features
- Intelligent Q&A: Get detailed and accurate information about space and astronomy, powered by the Gemini 1.5 Flash model.

- NASA Image Integration: The chatbot automatically detects image-related queries and fetches stunning visuals from the NASA Image and Video Library.

- Interactive Interface: A user-friendly chat interface built with Streamlit makes it easy to ask questions and view responses.

- Custom Persona: SpaceBot is configured with a specific persona to provide enthusiastic and educational responses about the cosmos.

## Technologies Used
- Python: The core programming language.

- Streamlit: For creating the interactive web application interface.

- Google Generative AI (genai): For accessing the Gemini 1.5 Flash model.

- Requests: For making API calls to the NASA Image and Video Library.

- python-dotenv: To securely load API keys from a .env file.

## Getting Started
**Prerequisites**

- Python 3.8+

- A Google Gemini API Key

- A NASA API Key (for image functionality)

**Installation**

Clone the repository to your local machine:
```
Bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
**Create a virtual environment (recommended):**
```
Bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**Install the required dependencies:**
```
Bash

pip install -r requirements.txt
```

**Configuration**

Create a file named .env in your project's root directory.

Add your API keys to the .env file:
```
GEMINI_API_KEY=your_gemini_api_key_here
NASA_API_KEY=your_nasa_api_key_here
Replace your_gemini_api_key_here and your_nasa_api_key_here with your actual keys.
```
**Running the Application**

Ensure your virtual environment is active.

Run the application from your terminal:
```
Bash

streamlit run app.py
```

Your default web browser will automatically open and display the application.

**Usage**
Type your question into the chat input field at the bottom of the page.

- To get text-based answers: Ask questions like "What is a black hole?" or "Tell me about the Voyager 1 probe."

- To get images: Include keywords like image, picture, or photo in your query, for example: "Show me an image of the Orion Nebula." The app will display up to three relevant images from NASA's archive.

## Project Structure

- app.py: The main Streamlit application file. It handles the user interface, manages chat history, and routes user requests.

- chatbot.py: Contains the logic for interacting with the Google Gemini API. It defines the SpaceBot persona and generates text-based responses.

- nasa.py: Handles all interactions with the NASA API, specifically for searching and fetching image data.

- requirements.txt: Lists all Python libraries required to run the project.

- .env: (Hidden) Stores your API keys and other sensitive environment variables.

## Credits
- Google Gemini API: For powering the conversational AI.

- NASA Image and Video Library API: For providing the stunning visuals of space.








