import streamlit as st
from utils import get_image_as_base64


def render_about():
    col1, col2 = st.columns([1, 2])

    #Load profile picture
    img_perfil = get_image_as_base64("assets/images/profile.png")

    #Render profile picture and name section
    col1.markdown(f"""
    <div style="display: flex; justify-content: center; margin-top: -20px;">
    <img src="data:image/png;base64,{img_perfil}" style="border-radius: 255px; width: 150px; height: 150px;">
    </div> <h4 style="text-align: center;margin-top: -1px;">Matheus Reis</h4>
    """, unsafe_allow_html=True
    ),

    #Render job title and skills section
    col2.markdown(
    """
    <div style="margin-top: 20px;">
        <p>
            <strong>Job title:</strong> IT Auditor - Mid-level at Banco BV
        </p>
        <p>
            <strong>Skills:</strong> Data Enthusiast | Python & SQL | Engineering Data Pipelines | Business-Oriented Tech Professional
        </p>
    </div>
    """,
    unsafe_allow_html=True,
),
    
    #Render e-mail and linkedin link section
    col2.markdown(
            """
            <div style="display: flex; align-items: center; gap: 10px;">
                <a href="mailto:matheusreissilva800@gmail.com" style="text-decoration: none; font-size: 14px;">
                    📩 <b>matheusreissilva800@gmail.com</b>
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        ),
    
    col2.markdown(
            """
            <div style="display: flex; align-items: center; gap: 10px;">
                <a href="https://www.linkedin.com/in/matheusreis-silva" target="_blank" style="text-decoration: none; font-size: 14px;">
                    🌐 <b>LinkedIn: Matheus Reis</b>
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        ),


    
    #Render 'About Me' section
    st.markdown("""
    <div style="margin-top: 100px;">
    </div>

    ### About Me
    I'm a tech professional with 4+ years of experience working with systems, data, and business controls. Over time, I’ve become increasingly passionate about transforming raw data into meaningful solutions — combining technical tools with analytical thinking to support smarter decisions.
    <br>
    Today, I’m focusing on building real-world data solutions: from ingestion and transformation to analysis and automation. My current goal is to deepen my skills in Data Engineering, Machine Learning, and Cloud Technologies, while contributing to impactful projects. 🚀
    """, unsafe_allow_html=True
    ),


    #Render qualifications section
    st.markdown("""
    <div style="margin-top: 100px;">
    </div>

    #### 💼 Qualifications

    <br>
                    
    🌍 **Languages:**
    + **Portuguese:** Native
    + **English:** Advanced (C2 - EF SET)

    <br>

    🛠️ **Technologies & Tools**: 
    + **Languages:** Python, SQL 
    + **Data Tools:** Pandas, NumPy, Scikit-Learn, Power BI
    + **Databases:** SQLite, PostgreSQL, SQL Server
    + **Automation & Engineering:** APIs, ETL, Airflow, Docker (in progress)
    + **Cloud:** Microsoft Azure (AZ-900 certified)
    + **Others:** Git/GitHub, Excel, Jupyter Notebooks, VS Code, Streamlit

    <br>


    📂 **Featured Projects**:
    + Building ETL pipelines with Python and SQL
    + Automating data collection from APIs
    + Creating dashboards to support decision-making
    + Experimenting with ML models for predictive tasks

                
    <br>

    📚 **Learning & Certifications**
    + 🎓**Postgraduate in:**
        + Database & Business Intelligence
        + Cloud IT Management

    <br>
                
    + 🏅 **Certifications:**
        + Microsoft Certified: Azure Fundamentals (AZ-900)
        + Lean Six Sigma Yellow Belt
        + EF SET English Certificate (C2 - Mastery)
                    
    """, unsafe_allow_html=True
    )
