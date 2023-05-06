import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import lasio

st.set_page_config(page_title="Survey result")
st.header("Ensure column contain GR DEPTH")
st.subheader('Upload File')

def get_data(uploaded_file):
    df = pd.DataFrame()
    if uploaded_file:
        type=uploaded_file.type
        
        if type=='text/csv':
            df = pd.read_csv(uploaded_file)
            
        if type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            df = pd.read_excel(uploaded_file,engine='openpyxl')
    return df



uploaded_file = st.file_uploader('Choose any Well log File',type=['las','xlsx','csv','text'])

df=get_data(uploaded_file)

if uploaded_file:
    if st.checkbox("click to show/hide data"):
        st.dataframe(df)

    if st.checkbox("click to show/hide columns"):
        st.write(df.columns)




    



    





    


