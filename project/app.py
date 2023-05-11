import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import lasio
import matplotlib.pyplot as plt




st.set_page_config(
    page_title="Well Log Data Analysis",
    page_icon="https://th.bing.com/th/id/OIP.L1NZgqUFgDKqy1uAwf2-9AHaHa?pid=ImgDet&rs=1",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    },

)



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


    
    
    






    



    





    


