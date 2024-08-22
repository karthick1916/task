import requests
import streamlit as st


API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def query(file):
        data = file.read()  
        response = requests.post(API_URL, headers=headers, data=data)
        return response.json()

up=st.file_uploader("uplode a image",type="jpg")
 
if st.button("click"):
    st.write(query(up))
   