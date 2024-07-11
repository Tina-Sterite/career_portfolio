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
st.set_page_config(page_title="Mehul Gupta's Portfolio", layout="wide", page_icon='👨‍🔬')

# Sidebar content
st.sidebar.markdown(info['Stackoverflow_flair'], unsafe_allow_html=True)

# Header and book announcement
st.header("My Debut book on Generative AI is out !!")
st.info("LangChain in your Pocket: Beginner's Guide to Building Generative AI Applications using LLMs")

# Display book image
st.image('images/book.png')

# Book details and purchase links
with st.expander("Book details"):
    st.image('images/amazon.png')
    st.markdown(book_details, unsafe_allow_html=True)

with st.expander("How to buy?"):
    for platform, link in books.items():
        st.markdown(f"""<a href="{link}"><b><u>{platform}</b></u></a>""", unsafe_allow_html=True)

# About me section
st.subheader('About me')
st.write(info['Brief'])

# Career snapshot
st.subheader('Career snapshot')
with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)

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
fig = go.Figure(data=[go.Table(
    header=dict(values=list(info['edu'].columns),
                fill_color='paleturquoise',
                align='left', height=65, font_size=20),
    cells=dict(values=[info['edu'][col].tolist() for col in info['edu'].columns],
               fill_color='lavender',
               align='left', height=40, font_size=15))])

fig.update_layout(width=750, height=400)
st.plotly_chart(fig)

# Research Papers section
st.subheader('Research Papers 📝')
def plot_bar():
    st.info('Comparing Brute Force approach with the algorithms')
    temp1 = rapid_metrics.loc[['Brute-Force_Printed', 'printed'], :].reset_index().melt(id_vars=['category'], value_vars=['precision', 'recall', 'f1_score'], var_name='metrics', value_name='%').reset_index()
    temp2 = rapid_metrics.loc[['Brute-Force_Handwritten', 'handwritten'], :].reset_index().melt(id_vars=['category'], value_vars=['precision', 'recall', 'f1_score'], var_name='metrics', value_name='%').reset_index()
    
    cols = st.columns(2)
    fig1 = px.bar(temp1, x="metrics", y="%", color="category", barmode='group')
    cols[0].plotly_chart(fig1, use_container_width=True)
    
    fig2 = px.bar(temp2, x="metrics", y="%", color="category", barmode='group')
    cols[1].plotly_chart(fig2, use_container_width=True)

def paper_summary(index):
    st.markdown(f'<h5><u>{paper_info["name"][index]}</h5>', unsafe_allow_html=True)
    st.caption(paper_info['role'][index])
    st.caption(f"{paper_info['journal'][index]} , {paper_info['publication'][index]} , {paper_info['year'][index]}")
    with st.expander('Detailed description'):
        with st.spinner(text="Loading details..."):
            st.write(paper_info['Summary'][index])
            pdfFileObj = open(f'pdfs/{paper_info["file"][index]}', 'rb')
            st.download_button('Download paper', pdfFileObj, file_name=paper_info['file'][index], mime='application/pdf')

paper_summary(0)
paper_summary(1)

# Achievements section
st.subheader('Achievements 🥇')
achievement_list = ''.join([f'<li>{item}</li>' for item in info['achievements']])
st.markdown(f'<ul>{achievement_list}</ul>', unsafe_allow_html=True)

# Medium Profile section
st.subheader('Medium Profile ✍️')
st.markdown(f"""<a href="{info['Medium']}">Access full profile here</a>""", unsafe_allow_html=True)

# YouTube section
st.subheader('Youtube ▶️')
st.markdown(f"""<a href="{info['youtube_url']}">Access channel here</a>""", unsafe_allow_html=True)

# Daily routine as Data Scientist
st.subheader('Daily routine as Data Scientist')
st.graphviz_chart(graph)

# Sidebar contact and resume download
st.sidebar.caption('Wish to connect?')
st.sidebar.write('📧: mehulgupta2016154@gmail.com')
pdfFileObj = open('pdfs/mehul_gupta_resume.pdf', 'rb')
st.sidebar.download_button('Download resume', pdfFileObj, file_name='mehul_gupta_resume.pdf', mime='application/pdf')