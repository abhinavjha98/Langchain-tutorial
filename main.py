import os
from decouple import config
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st

first_input_prompt = PromptTemplate(
        input_variables=['name'],
        template="Tell me about celebrity {name}",
)
#streamlit framework
OPEN_AI = config('OPENAI_KEY')

llm = OpenAI(openai_api_key=OPEN_AI,temperature=0.8)

LLMChain(llm=llm,prompt=first_input_prompt,verbose=True,output_key='title')



st.title("AJ LLM")
input_text = st.text_input("Search the topic you want")



if input_text:
    st.write(llm(input_text))



