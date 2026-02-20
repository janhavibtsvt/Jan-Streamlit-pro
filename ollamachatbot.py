import os
from langchain_community.llms import Ollama 
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

st.title("Langchain demo with Gemma model")
input_text=st.text_input("What is on your mind 🐼")

llm= Ollama(model="gemma2:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

st.write(chain.invoke({"question":input_text}))