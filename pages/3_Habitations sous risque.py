import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import style
import geopandas as gpd
from streamlit_folium import folium_static


style.set_style()

#filtered_data = Methodes.filter_dataframe(data_NA, 1)
#st.map(filtered_data, latitude='Latitude', longitude='Longitude')


#Ressources drive

Geo_REG_url="https://drive.google.com/uc?id=1CIshBgHezNQthzReeKcMqIdv9pUaZRHN"
Geo_DEP_url="https://drive.google.com/uc?id=1mvshQwYHPHSCikBHBFjNQyeRqRI11e3Q"
nb_secheresse_url="https://drive.google.com/file/d/1NaMQ7rNmg5IN73uHAl74nK33dQpv0mgn"
nb_inondation_url="https://drive.google.com/file/d/1RWd7EHFIqLfzcgqIpcYPOuzVQaWsEgFa"
#import des bases
@st.cache_data
def load_data():
    Geo_REG=gpd.read_file(Geo_REG_url)
    Geo_DEP=gpd.read_file(Geo_DEP_url)
    nb_secheresse = pd.read_csv(nb_secheresse_url,usecols=['Code_dep', 'Nb_sec'])
    nb_inondation = pd.read_csv(nb_inondation_url,usecols=['Code_dep', 'Nb_in'])
    return {"Geo_REG": Geo_REG, "Geo_DEP": Geo_DEP,"nb_secheresse": nb_secheresse, "nb_inondation": nb_inondation}


data_dict = load_data()

columns_secheresse = ['Code_dep', 'Nb_sec']
columns_inondation = ['Code_dep', 'Nb_in']

# Carte FOLIUM
# Lecture du fichier
Geo = gpd.GeoDataFrame(data_dict["Geo_DEP"])
col3, col4 = st.columns((2))
with col3:
    st.markdown("<u>**Carte : Le cas de la sécheresse**</u>", unsafe_allow_html=True)
    # Creation de la carte de la france avec folium
    france_map = folium.Map(location=[46.6031, 1.7001], zoom_start=5)
    sec = folium.Choropleth(
        geo_data=Geo,
        name="choropleth",
        data=data_dict["nb_secheresse"],
        columns=columns_secheresse,
        key_on='feature.properties.Code_dep',
        fill_color="YlOrRd",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Départements les plus touchés par la sécheresse 1985-2022",
        popup=''
    ).add_to(france_map)
    sec.geojson.add_child(
        folium.features.GeoJsonTooltip(['Département'], labels=False)
    )
    # Afficher la carte dans Streamlit
    folium_static(france_map)
with col4:
    st.markdown("<u>**Carte : Le cas de l'inondation**</u>", unsafe_allow_html=True)
    # Creation de la carte de la france avec folium
    france_map = folium.Map(location=[46.6031, 1.7001], zoom_start=5)
    inondation = folium.Choropleth(
        geo_data=Geo,
        name="choropleth",
        data=data_dict["nb_inondation"],
        columns=columns_inondation,
        key_on='feature.properties.Code_dep',
        fill_color="Blues",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Départements les plus touchés par les inondations 1985-2022",
        popup=''
    ).add_to(france_map)
    inondation.geojson.add_child(
        folium.features.GeoJsonTooltip(['Département'], labels=False)
    )
    # Afficher la carte dans Streamlit
    folium_static(france_map)
