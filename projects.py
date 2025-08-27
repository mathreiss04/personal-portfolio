import streamlit as st
from streamlit_elements import elements, mui 
from utils import get_image_as_base64


#Function to render project cards
def render_projects():
    st.title("Welcome to project section! 🚀")
    st.markdown('<div style="height: 100px;"></div>', unsafe_allow_html=True)

    #Load projects
    projects = [
        {
            "image": get_image_as_base64("assets/images/spotify.png"),
            "title": "🎵 Spotify Artist Explorer",
            "date": "2025/Aug",
            "description": "The Spotify Artist Explorer is an interactive web application built with Streamlit that allows users to explore artist information from the Spotify platform.",
            "link":"https://spotify-artist-explorer.streamlit.app"
        },
]

    #Render projects (cards) in columns
    col1, col2, col3 = st.columns([1, 1, 1])
    for i, project in enumerate(projects):
        current_col = [col1, col2, col3][i % 3]
        with current_col:
            with elements(f"project_card_{i}"):
                 #Card construction, size and color configuration
                with mui.Card(sx={"maxWidth": 700, "margin": "16px auto", "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.1)"}):

                    #Card title
                    with mui.CardContent():
                         mui.Typography(project['title'], variant='h6', component='div')

                        #Card image
                    mui.CardMedia(
                        component="img",
                        height="300",
                        image=f"data:image/png;base64,{project['image']}",
                        alt=project['title']
                        )
                        
                    with mui.CardContent():
                        mui.Typography(project["date"], color="text.secondary", variant="body2")
                        mui.Typography(project["description"], variant="body2", sx={"marginTop": "8px"})

                    #Card actions (buttons)
                    with mui.CardActions():
                        mui.Button("Learn More", href=project["link"], size="small", target="_blank")
                        mui.IconButton(mui.icon.Favorite())



