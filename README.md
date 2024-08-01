# Portfolio builder

A streamlit based webapp deployed at [here](https://careerportfolio-6wrrnxu5eweqtgjmqtqsja.streamlit.app/)

## Contents

- LinkedIn Badge : [how to create one for your profile?](https://www.linkedin.com/pulse/how-create-linkedin-badge-your-website-amy-wallin/). Integrated using streamlit component
- (not used in this app) Stackoverflow Flair : [how to add a stackoverflow flair?](https://meta.stackexchange.com/questions/10497/how-do-i-put-my-stackoverflow-user-flair-on-my-blogger-blog). Integrated using streamlit component
- Career Snapshot: Built using [streamlit_timeline](https://pypi.org/project/streamlit-timeline/)
- Skills & Tools: Used streamlit buttons & columns features
- Education : Plotly(library for visualization) table
- (not used in this app) Research Paper detailed brief description : streamlit images, streamlit metrics, streamlit expander & plotly.express grouped barplot
- (not used in this app) Achievements : streamlit markdown (great to embed HTML codes)
- (not used in this app) Medium profile : Basic web scrapping. Profile preview generated using [pixelpoint's medium widget](https://medium-widget.pixelpoint.io/)
- Daily routine : [Graphviz library](https://pypi.org/project/graphviz/)
- (not used in this app) ML models integrated : Vanilla & Cycle GAN built using tensorflow

## Files description
* N/A cyclegan/ : weights for cyclegan model used for image translation
* N/A vanilla_gan/ : weights for vanilla gan used
* images/ : images used for research paper section
* pdf/ : pdfs available for downloading on portfolio
* constant.py : File with all static data used. 
* N/A cycle.py : cycle_gan models 
* N/A vanilla_gan.py: vanilla_gan models
* requirements.txt : requirements file generated using [pipreqs](https://pypi.org/project/pipreqs/)
* graph_builder.py : Daily routine graph using graphviz
* timeline.json : Json file used by streamlit_timeline for career snapshot

## How to deploy using Streamlit?
* Once confirm your app runds fine on localhost. Check using 
```
streamlit run streamlit_app.py 
```
* Create requirements.txt. 
* Push repo to github.
* Sign in https://streamlit.io/ using the same mail as for github account where code is pushed (for ease)
* Fill in the info & click deploy on the ![Deployment screen](https://user-images.githubusercontent.com/31255225/147195886-a7f69e07-ac50-4fe4-af3f-48e953c983fa.PNG) 





