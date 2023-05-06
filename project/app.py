import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import lasio
import matplotlib.pyplot as plt

hide_footer = """<style>
footer {
  visibility: hidden;
}
</style>
"""

footer = """<style>
.footer {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  height:23px;
  background-color: white;
  color: black;
  text-align: center;
  align-items:center;
}
</style>
<div class="footer">
  <p>Developed with ❤️ by Sourav</p>
</div>
"""
st.markdown(hide_footer, unsafe_allow_html=True)
st.markdown(footer, unsafe_allow_html=True)

#st.set_page_config(page_title="Survey result")
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
    
    first_cols = st.selectbox(
    'choose first columns',
    (list(df.columns)),
    )
    second_cols = st.selectbox(
    'choose second column',
    (list(df.columns)),
    )
    st.write(second_cols)
    data1 = df[second_cols]
    data2=df[first_cols]

    if st.checkbox("click to see the plot"):
        fig = plt.figure(figsize=(2,5))
        plt.plot(data1,data2,'r')
        st.pyplot(fig,use_container_width=False)


    
    
    






    



    





    


