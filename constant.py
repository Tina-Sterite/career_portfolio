import pandas as pd
import graphviz as graphviz

edu = [["Computer Science Transfer - Data Science","2025","Massasoit Community College","TBD"], 
       ["AI Powered Data Analytics","2024","Network Technology Academy Institute","TBD"],
       ["Specialized Studies Program, Business Intelligence and Data Warehousing",
      "2017",
      "University of California, Irvine Division of Continuing Education ",
      "4.0 GPA"]
      ]

info = {'name':'Tina Sterite', 
        'Brief':'My name is Tina Sterite. An innovative Business Intelligence Engineer with a passion for transforming complex data into actionable insights. With over 15 years of experience in data analytics, report development, and project management, I specialize in leveraging tools like Tableau, Alteryx, and SQL to drive business decisions. My expertise spans from traditional BI to cutting-edge AI-powered analytics, allowing me to bridge the gap between technical implementation and strategic business needs. As a lifelong learner currently pursuing further education in Data Science, committed to staying at the forefront of technology trends. My goal is to empower organizations through data-driven solutions, enhancing efficiency, visibility, and decision-making processes while facilitating collaboration and fostering an enthusiastic work environment.\n\nMy unique value lies in the ability to merge technical prowess with business applications and operations, driving impactful business decisions through comprehensive analysis and reporting. This proficiency extends across various industries, leveraging deep knowledge in Oracle SQL, PostgreSQL, and advanced BI tools to enhance data integrity and reporting capabilities. By streamlining processes and developing innovative solutions, my track record showcases a profound impact on operational efficiency, stakeholder visibility, and proactive issue resolution in a collaborative team environment.',
        'photo':{'path':'abc.jpg','width':150},
        "Mobile": "6178406565",
        "Email": "tsterite@gmail.com",
        "LinkedIn": "https://www.linkedin.com/in/tina-sterite/",
        "City": "East Bridgewater, MA",
        'edu':pd.DataFrame(edu,columns=['Qualification','Year','Institute','Score']),
        "Stackoverflow_flair": "<a href=\"https://www.linkedin.com/in/tina-sterite\"></a>",
                
        "skills": ["Aleryx",
                   "Oracle SQL",
                   "Tableau",
                   "Qualtrics",
                   "SQL Server Mgmt Studio",
                   "Python",
                   "SSRS",
                   "Streamlit",
                   "iCEDQ",
                   "DB2","Informatica","Azure DevOps","PowerBI","Azure Data Factory"]
        }
paper_info = {'name':['x','x'],'publication':['x','x'],'journal':['x','x'],'year':['2199','2199'],
              'role':['x','x'],'Summary':['x','x'],
              'file':['cover_letter.pdf','cover_letter.pdf'],
              'images':{'0':[{'path':'images/rpa1.PNG','caption':'Digitization pipeline','width':600}],
                        '1':[[{'path':'images/pr1.PNG','caption':'Capture seed words'},
                              {'path':'images/pr2.PNG','caption':'cluster words using seed words'},
                              {'path':'images/pr3.PNG','caption':'clean junk words'}],
                             [{'path':'images/hw1.PNG','caption':'Filter 1'},
                              {'path':'images/hw2.PNG','caption':'Filter 2'},
                              {'path':'images/hw3.PNG','caption':'Filter 3'}]]}}

skill_col_size = 3

embed_component= {'linkedin':"""
<div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="tina-sterite" data-version="v1">
    <a class="badge-base__link LI-simple-link" href="https://www.linkedin.com/in/tina-sterite?trk=profile-badge">Tina Sterite</a>
</div>
"""}