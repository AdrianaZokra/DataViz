import streamlit as st
from PIL import Image
import datetime
import os
import style
import toml
import warnings
import pandas as pd

st.set_page_config(layout="wide")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
style.set_style()
# Get the current directory of the Python script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Define the relative path to the resources folder
resources_dir = os.path.join(script_dir, "resources")
# Access a specific resource within the "resources" folder
logo_path = os.path.join(resources_dir,"logo.jpg")

warnings.filterwarnings('ignore')

#Ajout d'un logo
image = Image.open(logo_path)
col1,col2 = st.columns([0.05,0.95])
with col1:
  st.image(image,width=200)

# Date du jour
box_date = str(datetime.datetime.now().strftime("%d / %m / %Y"))
st.write(f":date: Date du jour : {box_date}")

# Centrer le titre
with col2:
    st.markdown("<h1 style='text-align: center;'>WELCOME !</h1>",unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>We are Data Insight Crew 😎 </h2>", unsafe_allow_html=True)

st.markdown("""<div style="text-align: justify;">
    🎤 "Un monde à +2 °C pourrait encore être assurable, un monde à 4 °C ne le serait certainement plus" - PDG d’AXA Henri de Castries
    </div>""",unsafe_allow_html=True)

st.markdown("",unsafe_allow_html=True)
st.markdown("""<div style="text-align: justify;">
     Nous sommes Data Insight Crew, une équipe de 5 actuaires.
</div>""",unsafe_allow_html=True)

st.markdown("""<div style="text-align: justify;">
     Cette année, dans le cadre du challenge Data Visualisation organisé par l’Institut des Actuaires, 
     notre équipe a mené une analyse sur l’impact des catastrophes naturelles sur l’immobilier en France, 
     avec la problématique suivante : Définition du capital sous risque et son évolution au cours du temps.
</div>""",unsafe_allow_html=True)

st.markdown("""<div style="text-align: justify;">
     En effet, en raison de ces risques naturels qui gagnent en intensité d'année en année, de plus en plus d’assureurs se désengagent. 
     Il devient, alors, de plus en plus difficile d’assurer contre ces évènements climatiques. 
     Pour notre étude, nous disposons de l’historique des catastrophes naturelles de 1985 à 2022. 
     Nous avons également à notre disposition les données foncières de 2019 à 2022.
     Nous avons décidé de nous focaliser uniquement sur les ventes de maisons et d’appartements.
     Les résultats que nous avons obtenus seront présentés sur cette page web.
</div>""",unsafe_allow_html=True)

st.markdown("",unsafe_allow_html=True)
st.markdown("""<div style="text-align: justify;">
     Bonne Lecture !
</div>""",unsafe_allow_html=True)