import pandas as pd
import plotly_express as px
import geopandas as gpd
import plotly.graph_objects as go
import streamlit
import geopandas as gpd

#Les couleurs
color = 'lightblue'
color_map_inondation = "ice"
color_map_secheresse= "Peach"
color_discrete= "indianred"
palette="Viridis"
color_type_local=["coral","cornflowerblue"]
palette_secheresse="YlOrRd"
palette_innondation="Blues"

#Ressources drive

dataf_2022_url="https://drive.google.com/uc?id=1RjGM0ENl8WhKWsq6utgOsr2UFL04W1Uh"
data_sec_url="https://drive.google.com/uc?id=1--TcMwX_pnAh_-Lqby65sQRh6PtpSOhz"
data_inond_url="https://drive.google.com/uc?id=1-0WfkhLqpmtjTQj7k7wPgnhckKa93suf"
data_mouv_url="https://drive.google.com/uc?id=1-18Yod3G-fOpdWd33KVcUN9Te-gyDm_2"
data_url="https://drive.google.com/uc?id=15dmJK9ocvPvKvhIkyDWaygvfHVZd7tsa"
count_url="https://drive.google.com/uc?id=1-2Lz8CjPz3133Qb28uJNJZIkLLdaDnRQ"
df_in_sec_url="https://drive.google.com/uc?id=1-9hFcBH5rlW0MmO-kLRxPRwZmZ14ySn8"
Geo_REG_url="https://drive.google.com/uc?id=1CIshBgHezNQthzReeKcMqIdv9pUaZRHN"
Geo_DEP_url="https://drive.google.com/uc?id=1mvshQwYHPHSCikBHBFjNQyeRqRI11e3Q"


#import des bases
@streamlit.cache_data
def load_data():
    dataf_2022 = pd.read_csv(dataf_2022_url)
    data_sec = pd.read_csv(data_sec_url, low_memory=False)
    data_inond = pd.read_csv(data_inond_url)
    data_mouv= pd.read_csv(data_mouv_url)
    data=pd.read_csv(data_url)
    count=pd.read_csv(count_url)
    df_in_sec=pd.read_csv(df_in_sec_url)
    Geo_REG=gpd.read_file(Geo_REG_url)
    Geo_DEP=gpd.read_file(Geo_DEP_url)
    return {"dataf_2022": dataf_2022, "data_sec": data_sec, "data_inond": data_inond,
            "data_mouv": data_mouv, "data": data, "count": count,
            "df_in_sec": df_in_sec, "Geo_REG": Geo_REG, "Geo_DEP": Geo_DEP}


# Load the dictionary of DataFrames using the cached function
data_dict = load_data()

#fig 1 dans CAT NAT
fig = px.line(data_dict["dataf_2022"], x='Année', y='nombre de sinistres déclarés', color='type de catastrophe naturelle',
              line_group='type de catastrophe naturelle',
              title="Nombre de sinistres déclarés par type de catastrophe au cours du temps")
fig.update_traces(mode="markers+lines", hovertemplate=None)


#fig 2 dans CAT NAT
# Fonction pour calculer la durée moyenne
def calculate_average_duration(data_frame, start_year, end_year, event_type):
    # Filtrer les données pour le type d'événement spécifié et les années données
    filtered_data = data_frame[(data_frame["Année"] >= start_year) & (data_frame["Année"] <= end_year)]

    # Calculer la durée moyenne
    average_duration = filtered_data['nb_jours'].sum() / filtered_data['nb_jours'].count()

    print(f"Durée moyenne de {event_type} entre {start_year} et {end_year}: {average_duration:.2f} jours")

    return average_duration

# Calcul des durées moyennes pour chaque événement entre 2001-2010 et 2010-2022
durée_moyenne_inondation_01_10 = calculate_average_duration(data_dict["data_inond"], 2001, 2010, "Inondation")
durée_moyenne_sécheresse_01_10 = calculate_average_duration(data_dict["data_sec"], 2001, 2010, "Sécheresse")
durée_moyenne_mouv_01_10 = calculate_average_duration(data_dict["data_mouv"], 2001, 2010, "Mouvement de terrain")

durée_moyenne_inondation_10_22 = calculate_average_duration(data_dict["data_inond"], 2010, 2022, "Inondation")
durée_moyenne_sécheresse_10_22 = calculate_average_duration(data_dict["data_sec"], 2010, 2022, "Sécheresse")
durée_moyenne_mouv_10_22 = calculate_average_duration(data_dict["data_mouv"], 2010, 2022, "Mouvement de terrain")

# Création d'un histograme
event_types = ['Inondation', 'Sécheresse', 'Mouvement de terrain']
average_durations_01_10 = [durée_moyenne_inondation_01_10, durée_moyenne_sécheresse_01_10,  durée_moyenne_mouv_01_10]
average_durations_10_22 = [durée_moyenne_inondation_10_22, durée_moyenne_sécheresse_10_22, durée_moyenne_mouv_10_22]

fig2 = go.Figure()

# Ajout des barres pour la période 2001-2010
fig2.add_trace(go.Bar(x=event_types, y=average_durations_01_10, name='2001-2010', marker_color=color_type_local[0]))

# Ajout des barres pour la période 2010-2022r
fig2.add_trace(go.Bar(x=event_types, y=average_durations_10_22, name='2010-2022', marker_color=color_type_local[1]))

fig2.update_layout(barmode='group', title='Durée moyenne des événements météorologiques entre 2001-2010 et 2010-2022',
                  xaxis_title='Types d\'événements',
                  yaxis_title='Durée moyenne (jours)')


#fig 3 sur CAT NAT
fig3 = px.bar(data_dict["count"], x='Annee', y=['nb_innondation', 'nb_secheresse'],
             labels={'value': 'Nombre d\'événements', 'variable': 'Type'},
             title='Evolution',
             barmode='group')

#fig 4 sur CAT NAT
fig4 = px.bar(data_dict["df_in_sec"], x='Région', y=['nb_innondation', 'nb_secheresse'], hover_name="Annee",
             animation_frame='Annee', barmode='group', text_auto=True)
fig4.update_layout(
    title="Nombre d'innondations et de sécheresses par région au fil du temps",
    yaxis=dict(range=[data_dict["df_in_sec"]['nb_innondation'].min(), data_dict["df_in_sec"]['nb_innondation'].max()])
)


#fig 5 sur CAT NAT
df_counts = data_dict["data_sec"].groupby("Année")["cod_nat_catnat"].count().reset_index(name="Nombre")
fig5 = px.bar(df_counts, x="Année", y="Nombre",
             title='Nombre d\'évenement de sécheresse par année', color_discrete_sequence=[color])

fig5.update_layout(
    xaxis_title="Année",
    yaxis_title="Nombre",  title_x=0.5
)

# fig 6 sur CAT NAT

variable = "cod_nat_catnat"
titre_variable = "Nombre de sécheresse"

group_reg = data_dict["data_sec"].groupby(['class', "Région" ])[variable].count()
group_reg = pd.DataFrame(data=group_reg)
group_reg = group_reg.rename(columns={"cod_nat_catnat": titre_variable})
group_reg = group_reg.reset_index()

variable = "cod_nat_catnat"
titre_variable = "Nombre de sécheresse"

fig6 = px.choropleth(group_reg, geojson=data_dict["Geo_REG"].set_index(['code']), locations='class', color=titre_variable,
                    color_continuous_scale=palette_secheresse,
                    projection="mercator",
                    hover_data={'class': False, titre_variable: True, 'Région': True}
                   )

fig6.update_geos(fitbounds="locations", visible=False)

fig6.update_layout( title=f"{titre_variable} par région", margin={"r":0,"t":0,"l":0,"b":0})


def figGet():
    return fig