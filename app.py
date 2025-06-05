import streamlit as st
import pandas as pd
import retrievalmodule 
from retrievalmodule import DocumentRetrievalChain
import os

st.set_page_config(layout='wide')

st.header("Website Query (concept)")

#URL uploader widget
url = st.text_input("Enter a website as resource to query")

process_url_clicked = st.sidebar.button("Process URL")
# Save file to desired location
if process_url_clicked:
    with st.spinner("Processing ..."):
        retrieval_chain_ob = DocumentRetrievalChain(url)
        retrieval_chain = retrieval_chain_ob.get_chain()
    
    question = st.text_input("Enter your question here", key="question")
    

    if question:
        with st.spinner("Thinking ..."):
            answer = retrieval_chain({"question":question}, return_only_outputs=True)
            answer = answer['answer']
            st.write(answer)
    

    