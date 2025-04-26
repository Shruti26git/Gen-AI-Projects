import streamlit as st
import google.generativeai as genai

# Configure the Gemini API
genai.configure(api_key="AIzaSyBY7sYPeOU0k8XhOsYWougRTXQCnft0bzY")

# Load the Gemini model
model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")

# Streamlit UI
st.set_page_config(page_title="Gemini AI Chat", layout="centered")
st.title("🧠 Gemini AI Chatbot")
st.markdown("Ask me anything!")

# Input box
user_prompt = st.text_area("Enter your question:", height=150)

# Submit button
if st.button("Generate Answer"):
    if user_prompt.strip() == "":
        st.warning("Please enter a question before submitting.")
    else:
        with st.spinner("Generating response..."):
            response = model.generate_content(user_prompt)
            st.markdown("### ✨ Response:")
            st.write(response.text)
