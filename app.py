# app.py - Main application file for SpaceBot

import streamlit as st
import chatbot
import nasa
import os
import re
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

IMAGE_KEYWORDS = ["image", "show me", "picture", "photo", "visualize", "see" , "images" , "pictures" , "photos"]

def contains_image_request(text):
    """Check if the user prompt requests an image."""
    return any(kw in text.lower() for kw in IMAGE_KEYWORDS)

def extract_search_query(prompt):
    """Basic keyword-based NLP to extract search-worthy phrases."""
    # For now, a simple fallback to the full prompt
    # Could be enhanced using spaCy or GPT extraction
    return re.sub(r'[^\w\s]', '', prompt).strip()

def display_image_results(images):
    """Display NASA image results in columns."""
    cols = st.columns(len(images))
    for i, img_data in enumerate(images):
        with cols[i]:
            st.image(img_data["image_url"], caption=img_data["title"], use_column_width=True)
            with st.expander("Description"):
                st.markdown(img_data.get("description", "No description available."))

def show_user_message(message):
    with st.chat_message("user"):
        st.markdown(message)

def show_assistant_message(response_text, images=None):
    with st.chat_message("assistant"):
        st.markdown(response_text)
        if images:
            st.write("🔭 NASA Images:")
            display_image_results(images)

def main():
    st.set_page_config(page_title="SpaceBot", page_icon="🚀", layout="wide")
    st.title("🪐 SpaceBot")
    st.caption("Your friendly guide to the cosmos, powered by Gemini and NASA.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if "images" in msg:
                display_image_results(msg["images"])

    user_question = st.chat_input("Ask SpaceBot about the universe...")

    if user_question:
        st.session_state.messages.append({"role": "user", "content": user_question})
        show_user_message(user_question)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    gemini_response = chatbot.generate_response(user_question)
                except Exception as e:
                    gemini_response = "❌ Sorry, I encountered an error generating the response."
                    st.error(str(e))

                assistant_msg = {"role": "assistant", "content": gemini_response}
                st.markdown(gemini_response)

                # If image-related, trigger NASA image search
                if contains_image_request(user_question):
                    st.info("Searching NASA's image archive...")
                    query = extract_search_query(user_question)
                    try:
                        nasa_images = nasa.search_nasa_images(query=query)
                        if nasa_images:
                            assistant_msg["images"] = nasa_images[:3]
                            display_image_results(assistant_msg["images"])
                        else:
                            st.warning("No images found for this topic.")
                    except Exception as e:
                        st.error(f"NASA API error: {e}")

        st.session_state.messages.append(assistant_msg)

if __name__ == "__main__":
    # Ensure Gemini API key is present
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key or gemini_api_key == "your_actual_api_key":
        st.error("🚨 GEMINI_API_KEY is not set correctly.")
        st.info("Create a `.env` file and set `GEMINI_API_KEY=your_key_here`.")
        st.stop()

    try:
        chatbot.configure_gemini()
    except Exception as e:
        st.error(f"Gemini configuration error: {e}")
        st.stop()

    main()
