import streamlit as st
# from auth import authenticator
st.set_page_config(page_title='Attendance System',layout='wide')



with st.spinner("Initializing face recognition components"):
    import face_rec


st.header('Attendance System using Face Recognition')

st.success('Model loaded sucesfully')
st.success('Redis db sucessfully connected')



