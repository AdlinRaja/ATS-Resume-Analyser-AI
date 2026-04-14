import os
import streamlit as st 
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai

key=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)

from pdf import extract_text # method in pdf.py file

model=genai.GenerativeModel('gemini-2.5-flash-lite')

def analyze_resume(pdf_doc,job_des):
    if pdf_doc is not None:
        pdf_text=extract_text(pdf_doc)
        st.write('Text extracted Scuessfully ✅️')
    else:
        st.warning('Error !! Upload the file in pdf format !📤 ')

    ats_score=model.generate_content(f''' Compare the given pdf {pdf_text} and given job description {job_des}
                                     and provide ATS score on scale of 1-100
                                     Generate the results in bullet points(Maximum 5 points)''')
    
    probablity=model.generate_content(f''' Compare the given pdf {pdf_text} and given job description {job_des}
                                     and provide the probablity to get shortlisted,
                                     Generate the results in bullet points(Maximum 5 points)''')
    
    improvement=model.generate_content(f''' Compare the given pdf {pdf_text} and given job description {job_des}
                                     and provide the areas to improve the resume to be a good fit also look for skills 
                                     and give skills missed to add. 
                                     Generate the results in bullet points(Maximum5 points)''')
    
    swot=model.generate_content(f''' Compare the given pdf {pdf_text} and given job description {job_des}
                                     and provide the SWOT analysis of it
                                     Generate the results in bullet points(Maximum5 points)''')
    
    good_fit=model.generate_content(f''' Compare the given pdf {pdf_text} and given job description {job_des}
                                     and check if i am a good fit for this role,
                                     give results like (Bad,good,need improvement,best fit) on the basis of good fit,
                                     If it is bad or need improvement give key word to include to improve the resume
                                     Generate the results in bullet points(Maximum 5 points)''')
    
    suggessions=model.generate_content(f''' Compare the given pdf {pdf_text} and given job description {job_des}
                                     and provide some points which would be a good value addition to the resume,
                                     also suggest a better professional summary/objective or work experience summary after carefully
                                     considering the existing ones so the originallity is not lost
                                     Generate the results in bullet points''')
    
    job_suggessions=model.generate_content(f''' Analyze the given pdf {pdf_text}
                                     and provide best 5 jobs available for the profile 
                                     Generate the results with job title, company name, work location, expected industry range salary''')
    
    return{st.write(ats_score.text),
           st.write(probablity.text),
           st.write(improvement.text),
           st.write(swot.text),
           st.write(good_fit.text),
           st.write(suggessions.text),
           st.write(job_suggessions.text)}