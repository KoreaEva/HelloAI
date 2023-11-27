import openai
import requests
from PIL import Image
from io import BytesIO
import streamlit as st

openai.api_type = "azure"
openai.api_base = "https://helloairaddalle.openai.azure.com/"
openai.api_version = "2023-06-01-preview"
openai.api_key = '8bec25dfe1a04e6da9fa7be8f1b2af1c'

prompt = st.text_input('Please input the prompt')
button_click = st.button('Create')

if(button_click):
    generation_response = openai.Image.create(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=2
    )

    image = Image.open(BytesIO(requests.get(generation_response["data"][0]["url"]).content))
    st.image(image, caption=prompt)

    #st.write(generation_response["data"][0]["url"])

