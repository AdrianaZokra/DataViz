import pandas as pd
import plotly_express as px
import geopandas as gpd


color = 'lightblue'
color_map = "Viridis"
palette = "Viridis"

data_sec = pd.read_csv(r"C:/documents A5_2023-2024/DataVizChallenge/Bases_output/data_sec.csv")
data_inond=pd.read_csv(r"C:/documents A5_2023-2024/DataVizChallenge/Bases_output/data_inond.csv")
Geo_DEP = gpd.read_file('C:/documents A5_2023-2024/DataVizChallenge/Resources/departements.geojson')
Geo_REG = gpd.read_file('C:/documents A5_2023-2024/DataVizChallenge/Resources/regions.geojson')

database = data_sec
variable = "nb_jours"
titre_variable = "nombre de secheresse"


#calcul de la moyenne de durée des sinitres par département
group_dep = database.groupby('Département')[variable].count()
group_dep = pd.DataFrame(data=group_dep)
group_dep = group_dep.rename(columns={"nb_jours": titre_variable})
group_dep = group_dep.reset_index()

carte1 = px.choropleth(group_dep, geojson=Geo_DEP.set_index(['code']), locations='Département', color=titre_variable,
                    color_continuous_scale=color_map,
                    projection="mercator"
                   )
carte1.update_geos(fitbounds="locations", visible=False)
carte1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#Par région
database = data_sec
variable = "nb_jours"
titre_variable = "Nombre de sécheresse"


group_reg = database.groupby( ['class','Région'])[variable].count()
group_reg = pd.DataFrame(data=group_reg)
group_reg = group_reg.rename(columns={"nb_jours": titre_variable})
group_reg = group_reg.reset_index()

carte2 = px.choropleth(group_reg, geojson=Geo_REG.set_index(['code']), locations='class', color=titre_variable,
                    color_continuous_scale=color_map,
                    projection="mercator",hover_data={'class': False, titre_variable: True, 'Région': True}
                   )
carte2.update_geos(fitbounds="locations", visible=False)
carte2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


