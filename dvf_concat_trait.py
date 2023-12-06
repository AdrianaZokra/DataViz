import pandas as pd
import plotly_express as px
import streamlit as st
import Methodes


#Ressources drive
departement_transaction_url="https://drive.google.com/uc?id=1wbQ8urZTfpFUO5cyujnzpQBko49xBxjg"
departement_transactionAnnee_url="https://drive.google.com/uc?id=1H3Z4BsYRbKesVRWiix2htB802qIx-g2r"
region_transactionAnnee_url="https://drive.google.com/uc?id=1dG_qbJX2Wzo8I6vYEIMTwszDr9JTerXP"
moyenne_region_url="https://drive.google.com/uc?id=1iZSQeb_QPzsSywSyGLQsBrCv5wmbQ-Ex"
region_transactionTest_url="https://drive.google.com/uc?id=1J5bGiIAJn5jX6qULnS4d2ZWKcLtXFTRx"


#Les couleurs
color = 'lightblue'
color_map_inondation = "ice"
color_map_secheresse= "Peach"
color_discrete= "indianred"
palette="Viridis"
color_type_local=["coral","cornflowerblue"]

#import des bases
departement_transaction = pd.read_csv(departement_transaction_url)
departement_transactionAnnee = pd.read_csv(departement_transactionAnnee_url)
region_transactionAnnee = pd.read_csv(region_transactionAnnee_url)
region_transactionTest= pd.read_csv(region_transactionTest_url)
moyenne_region= pd.read_csv(moyenne_region_url)

#dvf= pd.read_csv(r"resources/dvf.csv")


#1er graphe dans valeurs foncières
fig= px.bar(departement_transaction, x= "Département",y= "Nombre",title= "Nombre de ventes par département")

#2e graphe dans valeurs foncières
fig2 = px.bar(departement_transactionAnnee, x='Département', y= 'Nombre',
             color='Type local',barmode='group',
             title ='Nombre de ventes par département et type d'+ "'" + "habitation 2019-2022",
             color_discrete_sequence=["coral","cornflowerblue"],
             animation_frame="Annee",range_y=[0,30000])

fig2.update_layout(sliders=[{"currentvalue": {"prefix": "Année="}}])

fig2.update_layout(margin=dict(l=40, r=30, t=30, b=200))
fig2['layout']['updatemenus'][0]['pad']=dict(r= 10, t= 150)
fig2['layout']['sliders'][0]['pad']=dict(r= 10, t= 150,)
fig2.update_xaxes(title='Départements')
title='Nombre de ventes par département et type d'+"'" + "habitation 2019-2022"


# 3e graphe dans les valeurs foncières
fig3 = px.bar(region_transactionAnnee, x='Région', y= 'Nombre',
             color='Type local',barmode='group',
             title= 'Nombre de ventes par région et type d'+ "'" + "habitation 2019-2022",
             color_discrete_sequence=["coral","cornflowerblue"],
             animation_frame="Annee",range_y=[0,120000])

fig3.update_layout(sliders=[{"currentvalue": {"prefix": "Année="}}])
fig3.update_layout(margin=dict(l=40, r=30, t=30, b=200))
fig3['layout']['updatemenus'][0]['pad']=dict(r= 10, t= 150)
fig3['layout']['sliders'][0]['pad']=dict(r= 10, t= 150,)

#4e graphe dans les valeurs foncières
#dans la page 1

#5e graphe dans valeurs foncieres

fig5= px.scatter(moyenne_region,x ='Surface_reelle',
           y='Valeur fonciere',
          size="PrixM2_moyenne",
          color='Région',
          facet_col='Type local',
          animation_frame="Annee",range_y=[0,400000],
          symbol='Région',
          title= 'Évolution du Prix/m^2 au cours du temps')

fig5.update_xaxes(title='Surface réelle')
fig5.update_yaxes(title='Valeur foncière')
fig5.update_layout(sliders=[{"currentvalue": {"prefix": "Année="}}])

#6e graphe dans valeurs foncieres
#fig6 = px.treemap(dvf, path=['Région','Département'], values=['Valeur fonciere'],
#                     height=700, title='Somme des valeurs foncières')
#fig6.data[0].textinfo = 'label+text+value'

