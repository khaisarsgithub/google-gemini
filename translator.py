# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Translator Application")

input=st.text_input("Input Content: ",key="input")
lang=st.text_input("Target Language: ",key="lang")


submit=st.button("Translate")

## If ask button is clicked

try:
  if submit:
      prompt = f"translate the sentences within the ``` into {lang} language  ```#{input}```"
      response=get_gemini_response(prompt)
      st.subheader("The Translation is: ")
      st.write(response)
except Exception as e:
   print(e)
   st.subheader("We are not available in the language you entered yet")