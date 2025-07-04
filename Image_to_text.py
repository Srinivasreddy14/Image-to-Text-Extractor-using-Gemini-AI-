import streamlit as st # type: ignore
from PIL import Image # type: ignore
import google.generativeai as genai # type: ignore
import os
from dotenv import load_dotenv # type: ignore
load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=gemini_key)

model = genai.GenerativeModel('gemini-2.0-flash')

def gemini_ai_response(prompt,image):
    if prompt!="":
       response = model.generate_content([prompt,image])
    else:
       response = model.generate_content(image)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Image to Text With Gemini Ai")

st.header("Gemini LLM Application")

# File uploader
uploaded_file = st.file_uploader("upload the image...", type=["jpg", "jpeg", "png"])

# Text input
input_prompt = st.text_input("Enter your prompt here:")

# Display uploaded image
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Get the Answers")

## If ask button is clicked

if submit:
    
    response=gemini_ai_response(input_prompt,image)
    st.subheader("The Response is")
    st.write(response)

