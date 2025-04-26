import streamlit as st
import PIL.Image
import google.generativeai as genai

# Configure the Gemini API (replace with your actual API key)
genai.configure(api_key="AIzaSyBY7sYPeOU0k8XhOsYWougRTXQCnft0bzY")

# Load the Gemini model
model = genai.GenerativeModel('models/gemini-2.5-flash-preview-04-17')

st.set_page_config(page_title="Image-to-Text with Gemini", layout="centered")
st.title("🧠 Image-to-Text using Gemini AI")
st.markdown("Upload an image and let Gemini generate the content.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = PIL.Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Generating content..."):
        response = model.generate_content(image)
        if hasattr(response, "text"):
            st.markdown("### 📄 Extracted Text")
            st.markdown(response.text)
        else:
            st.error("Failed to generate content.")
