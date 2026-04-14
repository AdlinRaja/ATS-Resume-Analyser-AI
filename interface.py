import streamlit as st 

from analysis import analyze_resume

st.set_page_config('AI Resume Analyzer',page_icon='👨‍💻')

st.title("AI POWERED Resume Analyzer 🧑🏻‍💻֎🇦🇮🧠")
st.header(':blue[AI POWERED Resume Analyzer by uploading resume and job description] 🤖🇦🇮 ')

st.subheader(':red[This page helps you to compare the resume with JD and provide ATS score, SWOT and probablity of selection]🎲')

st.sidebar.subheader('Drop your resume here 👇')

pdf_doc=st.sidebar.file_uploader('Upload your file hear 📤',type=['pdf'])

st.sidebar.markdown('Designed by Adlin Raja')
st.sidebar.markdown('Git hub : ')

job_des=st.text_area('Paste the JD here',max_chars=15000)

submit=st.button('Get Results 🎯')

if submit:
    with st.spinner('loading ⌛'):
        analyze_resume(pdf_doc,job_des)