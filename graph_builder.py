import graphviz as graphviz

graph = graphviz.Digraph()
graph.edge('9AM, start','check mails')
graph.edge('check mails','check Active Batch, Tableau, and Alteryx job runs')
graph.edge('check Active Batch, Tableau, and Alteryx job runs','resolve issues',label='If bug found')
graph.edge('resolve issues','10AM, attend scrum')
graph.edge('check Active Batch, Tableau, and Alteryx job runs','10AM, attend scrum')
graph.edge('10AM, attend scrum','work on assigned work')
graph.edge('work on assigned work','Tableau',label='usually')
graph.edge('work on assigned work','SQL Queries',label='Almost everyday')
graph.edge('EDA','SQL Queries')
graph.edge('SQL Queries','EDA')
graph.edge('work on assigned work','Data Modeling',label='seldom')
graph.edge('work on assigned work','Some meeting')
graph.edge('work on assigned work','Around 5PM')
graph.edge('Around 5PM','end')
graph.edge('Some meeting','end',label='If too long')
graph.edge('Some meeting','work on assigned work')