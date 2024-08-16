import streamlit as st
from constant import *
import numpy as np
import pandas as pd
from PIL import Image
from streamlit_timeline import timeline
import plotly.express as px
import plotly.figure_factory as ff
import requests
import re
import plotly.graph_objects as go
import io
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
from graph_builder import *
from streamlit_player import st_player

# Set page configuration
st.set_page_config(page_title="Tina Sterite's Portfolio", layout="wide", page_icon='👩🏻‍🔬')
# Custom CSS to change the sidebar button font size
custom_css = """
<style>
    .st-emotion-cache-1lxzorm.ef3psqc12 {
        font-size: .9rem !important; /* Adjust font size as needed */
        padding: 3px 5px !important; /* Adjust padding as needed */
        width: 200px; /*this one is controlling button width */
    }
    .st-emotion-cache-187vdiz.e1nzilvr4 {
        font-size: .9rem !important; /* Adjust font size as needed */
        padding: 3px 5px !important; /* Adjust padding as needed */
        width: 200px; 
    }
    .st-emotion-cache-1dfdf75.e1f1d6gn2 {
        font-size: .9rem !important; /* Adjust font size as needed */
        padding: 3px 5px !important; /* Adjust padding as needed */
        width: 200px; /*this one adjusted font for Visit my LinkedIn Page*/
    }
    .element-container.st-emotion-cache-nmzwn.e1f1d6gn4 {
        font-size: .9rem !important; /* Adjust font size as needed */
        padding: 3px 5px !important; /* Adjust padding as needed */
        width: 200px; /*this one adjusted font for */
    }
    .st-emotion-cache-uzeiqp.e1nzilvr4 {
        font-size: .9rem !important; /* Adjust font size as needed */
         /*this one adjusted the "about me" section.. the width did but the font doesn't seem affected.. actually linkedin page looks affected*/
    }
    .row-widget.stDownloadButton {
        padding: 10px !important; /* Example style */
        width: 200px;
        font-size: .9rem; 
    } 
    .eyeqlp52 st-emotion-cache-1u2dcfn.ex0cdmw0 {
        font-size: .9rem !important; /* Adjust font size as needed */
        padding: 3px 5px !important; /* Adjust padding as needed */
        width: 200px; /*this one adjusted font for  - font doesn't appear to affect anything*/ 
    }
</style>
 """

 # Inject the custom CSS into the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)

# Sidebar content
st.sidebar.image("images/profile_pic.jpeg", caption="Tina Sterite", width=200)


# Sidebar contact and resume download
st.sidebar.caption('Wish to connect?')
#contact
st.sidebar.write('📧: tsterite@gmail.com')
#linkedIn
st.sidebar.markdown("""
<div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="tina-sterite" data-version="v1">
    <a class="badge-base__link LI-simple-link" href="https://www.linkedin.com/in/tina-sterite?trk=profile-badge">Visit my LinkedIn Page</a>
</div>
""", unsafe_allow_html=True)
#linkedIn recommendations
st.sidebar.markdown('<a href="https://www.linkedin.com/in/tina-sterite/details/recommendations/" target="_blank">Visit my LinkedIn Recommendations</a>', unsafe_allow_html=True)
pdfFileObj = open('pdfs/Resume_DSterite.pdf', 'rb')
st.sidebar.download_button('Download resume', pdfFileObj, file_name='Resume_DSterite.pdf', mime='application/pdf')
pdf_url = open('pdfs/common_screening_q_and_a.pdf', 'rb')
#screening questions - answered
st.sidebar.download_button('Pre-screening Questions - Answered', pdf_url, file_name='common_screening_q_and_a.pdf', mime='application/pdf')
st.sidebar.image("images/PCEP.png", caption="PCEP - Certified Entry-Level Python Programmer", width=150)



# About me section
st.subheader('About me')
st.write(info['Brief'])

# Career snapshot
st.subheader('Career snapshot')
with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        start = "2023-12-31"
        end = "1993-08-01"
        timeline(data, height=400)

# Skills & Tools section
st.subheader('Skills & Tools ⚒️')
def skill_tab():
    rows, cols = divmod(len(info['skills']), skill_col_size)
    if cols:
        rows += 1
    skills = iter(info['skills'])
    for _ in range(rows):
        columns = st.columns(skill_col_size)
        for index in range(skill_col_size):
            try:
                skill = next(skills)
                columns[index].button(skill)
            except StopIteration:
                break

with st.spinner(text="Loading section..."):
    skill_tab()

# Education section
st.subheader('Education 📖')

# fig = go.Figure(data=[go.Table(
#     header=dict(values=list(info['edu'].columns),
#                 fill_color='paleturquoise',
#                 align='left',height=50,font_size=20),
#     cells=dict(values=info['edu'].transpose().values.tolist(),
#                fill_color='lavender',
#                align='left',height=40,font_size=15))])

# fig.update_layout(width=750, height=400)
# st.plotly_chart(fig)

df = info['edu']

# Display the DataFrame as a table using Streamlit
#st.style.hide_index()
st.dataframe(df,hide_index=True)

# Daily routine as Data Scientist
st.subheader('Daily routine as Business Intelligence Engineer')
st.graphviz_chart(graph)


    
    
