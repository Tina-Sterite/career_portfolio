import pandas as pd
import graphviz as graphviz

edu = [ ["AI Powered Data Analytics","2024","Network Technology Academy Institute","TBD"],
       ["Specialized Studies Program, Business Intelligence and Data Warehousing",
      "2017",
      "University of California, Irvine Division of Continuing Education ",
      "4.0 GPA"]
      ]

info = {'name':'Tina Sterite', 
        'Brief':'My name is Tina Sterite and I have 8 years of experience working in the business intelligence and data space, and over 20 years in the IT space.  My wide range of experience in the IT and data spaces, collaboration across teams (business and IT) experience, as well as my technical aptitude will be a great value to your team.\n\n I have 8 years working with Tableau, Alteryx, SSRS (5yr) and writing SQL to create data sources for reporting and creating the reports themselves.  I have also had exposure to Power BI and Azure Data Factory.\n\nIn addition to curating the data sources for reporting; I’ve worked extensively over the years with data warehouse and application development teams to either create, locate, or correct data from source systems for reporting purposes.  I have experience working with team members across the globe and have made many friends in these colleagues.\n\nCurrently, I am enrolled in an AI Powered Data Analytics course with NTAi.  I have obtained the PCEP certification and am currently working on various Python projects using VS Code, Copilot, and REST APIs.  I’m excited to bring these new skills to the table.\n\nI LOVE what I do and would love the opportunity to bring my talent to your team and to expand and grow within your team.  Please feel free to connect!',
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