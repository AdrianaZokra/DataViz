# -*- coding: utf-8 -*-

import streamlit as st
import dvf_concat_trait
from PIL import Image
import datetime
import os

# Get the current directory of the Python script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to the resources folder
resources_dir = os.path.join(script_dir, "resources")

# Access a specific resource within the "resources" folder
logo_path = os.path.join(resources_dir,"logo.jpg")


#Adding logo
#st.set_page_config(layout="wide")
image = Image.open(logo_path)
col1,col2 = st.columns([0.05,0.95])

#Insertion de notre logo
with col1:
  st.image(image,width=200)

#Mettre un titre au centre de la page
with col2:
  st.markdown("<h1 style='text-align: center;'>WELCOME !</h1>", unsafe_allow_html=True)
  st.markdown("<h2 style='text-align: center;'>We are Data Insight Crew ; '> \:sunglasses: ' </h2>" , unsafe_allow_html = True)
#mettre la date du jour
box_date = str(datetime.datetime.now().strftime("%d / %m / %Y"))
st.write(f"Date du jour : {box_date}")


