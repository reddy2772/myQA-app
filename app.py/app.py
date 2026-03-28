import streamlit as st 
from langchain_community.llms import Ollama 
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser 

st.title("QA App with Gemma")

input_text = st.text_input("Ask your question:")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a useful assistant."),
    ("user", "Question: {question}")
])

llm = Ollama(model = "gemma:2b")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser 

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)