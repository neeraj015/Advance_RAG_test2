from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEndpoint
import streamlit as st

def get_llm(provider, temperature=0.3):
    if provider == "Groq":
        return ChatGroq(
            model_name="meta-llama/llama-4-maverick-17b-128e-instruct",
            temperature=temperature,
            groq_api_key=st.secrets["GROQQ_API_KEY"]
        )
    else:
        return HuggingFaceEndpoint(
            repo_id="mistralai/Mistral-7B-Instruct-v0.1",
            temperature=temperature,
            huggingfacehub_api_token=st.secrets["HUGGINGFACEHUB_API_TOKEN"]
        )
