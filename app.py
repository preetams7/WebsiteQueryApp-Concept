import streamlit as st
import pandas as pd
import retrievalmodule 
from retrievalmodule import DocumentRetrievalChain
import os

st.set_page_config(layout='wide')

st.header("Website Query (concept)")

# File uploader widget
url = st.file_uploader("Enter a website as resource to query")



# Save file to desired location
if url is not None:
    
    question = st.text_input("Enter your question here", key="question")
    retrieval_chain_ob = DocumentRetrievalChain(url)
    retrieval_chain = retrieval_chain_ob.get_chain()

    if question:
        with st.spinner("Thinking ..."):
            answer = retrieval_chain({"question":question}, return_only_outputs=True)
            answer = answer['answer']
            st.write(answer)
    

    