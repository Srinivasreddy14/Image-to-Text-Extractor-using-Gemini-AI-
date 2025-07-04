import streamlit as st # type: ignore
from PIL import Image # type: ignore
import google.generativeai as genai # type: ignore
import streamlit as st # type: ignore
import pathlib
import textwrap
import os
from dotenv import load_dotenv # type: ignore
load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=gemini_key)

model = genai.GenerativeModel('gemini-2.0-flash') # type: ignore
import os
from dotenv import load_dotenv # type: ignore
load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=gemini_key)

model = genai.GenerativeModel('gemini-2.0-flash')

# creating a function to get the response
def gemini_ai_response(input,image,prompt):
    if prompt != "":
        response = model.generate_content([input, image[0], prompt])
    else:
        response = model.generate_content([input, image[0]])
    
    return response.text

#creating a function read the image in byte data
def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


##initialize our streamlit app

st.set_page_config(page_title="Gemini LLM Application")

st.header("Multilanguage invoice extractor")

# File uploader
uploaded_file = st.file_uploader("upload the image...", type=["jpg", "jpeg", "png"])

# Text input
input = st.text_input("Enter your prompt here:")

# Display uploaded image
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Get the Answers")

input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """

## If ask button is clicked

if submit:
    image_data = input_image_setup(uploaded_file)
    response=gemini_ai_response(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)