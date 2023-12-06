import streamlit as st
import CAT_NAT
import dvf_concat_trait
from PIL import Image
import pandas as pd
import Methodes
import folium
from streamlit_folium import st_folium

import style

style.set_style()

## Adding tabs and columns, and filters
#tab1, tab2 = st.tabs(["Évènements sécheresse","Évènements inondation"])
col1,col2 = st.columns(2)
#data_NA = CAT_NAT.data_sec.dropna(subset=['Latitude'])
#data_NA = data_NA.dropna(subset=['Longitude'])
#data_NA_inond=CAT_NAT.data_inond.dropna(subset=['Latitude'])
#data_NA_inond=data_NA_inond.dropna(subset=['Longitude'])




#filtered_data = Methodes.filter_dataframe(data_NA, 1)
#st.map(filtered_data, latitude='Latitude', longitude='Longitude')

#filtered_data2 = Methodes.filter_dataframe(data_NA_inond, 2)
#st.map(filtered_data2, latitude='Latitude', longitude='Longitude')

# Create a Folium map centered around France
#france_map = folium.Map(location=[46.6031, 1.7001], zoom_start=6)
#st_data = st_folium(france_map, width=725)

#def tab_secheresse():
#    st.header("Pour les évènements sécheresse")
#    with st.container():
#        with col1:
#            # st.write(CAT_NAT.carte1)
#            filtered_data = filter_dataframe(data_NA, 1)
#            st.map(filtered_data, latitude='Latitude', longitude='Longitude')

#def tab_inondation():
#    st.header("Pour les évènements inondation")
#    with st.container():
#        with col1:
#            # st.write(CAT_NAT.carte1)
#           filtered_data2 = filter_dataframe(data_NA_inond, 2)
#            st.map(filtered_data2, latitude='Latitude', longitude='Longitude')

#choix=st.selectbox("Sélectionnez le type d'événement:",('Évènements sécheresse','Évènements inondation'),index=None,
#   placeholder="Selectionner une analyse...")

#if choix == 'Évènements sécheresse':
#    tab_secheresse()

#elif choix == 'Évènements inondation':
#    tab_inondation()


def create_tabs(df1: pd.DataFrame, df2: pd.DataFrame):
    with st.container():
        with st.expander("Sélectionnez le type d'événement"):
            tabs = st.tabs(["Évènements sécheresse", "Évènements inondation"])
            if tabs == "Évènements sécheresse":
                with tabs == "Évènements sécheresse":
                    st.header("Pour les évènements sécheresse")
                    with st.container():
                        with col1():
                            filtered_data = Methodes.filter_dataframe(df1, 1)
                            st.map(filtered_data, latitude='Latitude', longitude='Longitude')

            elif tabs == "Évènements inondation":
                st.header("Pour les évènements inondation")
                with st.container():
                    with col1():
                        filtered_data2 = Methodes.filter_dataframe(df2, 2)
                        st.map(filtered_data2, latitude='Latitude', longitude='Longitude')

#create_tabs(data_NA,data_NA_inond)


