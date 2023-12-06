import streamlit as st
import CAT_NAT
import style
import os
from PIL import Image
import plotly_express as px

style.set_style()

script_dir = os.path.dirname(os.path.abspath(__file__))
resources_dir = os.path.join(script_dir, "resources")
legende_path = os.path.join(resources_dir, "legende.jpg")

## Adding tabs
tab1, tab2 , tab3= st.tabs(["Général","Sécheresse","Inondation"])

with tab1:
    with st.container():
        st.write(CAT_NAT.fig)
        with st.expander("Voir l'explication"):
           st.write("Sur les 4 années, Nord est le département ayant enregistrés le plus de transaction, tandis que Lozère est celui ayant enregistré le moins.")
    with st.container():
        st.write(CAT_NAT.fig2)
        with st.expander("Voir l'explication"):
           st.write("Sur les 4 années, Nord est le département ayant enregistrés le plus de transaction, tandis que Lozère est celui ayant enregistré le moins.")
    with st.container():
        st.write(CAT_NAT.fig3)
        with st.expander("Voir l'explication"):
           st.write("Sur les 4 années, Nord est le département ayant enregistrés le plus de transaction, tandis que Lozère est celui ayant enregistré le moins.")
#    with st.container():
#        st.write(CAT_NAT.fig4)
#        with st.expander("Voir l'explication"):
#            st.write("Sur les 4 années, Nord est le département ayant enregistrés le plus de transaction, tandis que Lozère est celui ayant enregistré le moins.")
with tab2:
    with st.container():
        st.write(CAT_NAT.fig5)
    with st.container():
        st.write(CAT_NAT.fig6)
