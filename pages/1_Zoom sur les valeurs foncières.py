import streamlit as st
import dvf_concat_trait
import plotly as plt
import Methodes
import plotly_express as px
import style

style.set_style()

## Adding tabs
tab1, tab2, tab3 = st.tabs(["Département","Région","Valeurs foncières et Prix m2"])

with tab1:
    with st.container():
        st.write(dvf_concat_trait.fig)
        with st.expander("Voir l'explication"):
           st.write("Sur les 4 années, Nord est le département ayant enregistrés le plus de transaction, tandis que Lozère est celui ayant enregistré le moins.")
    with st.container():
        st.write(dvf_concat_trait.fig2)
        with st.expander("Voir l'explication"):
            st.write(
                "Paris est le département ayant enregistré le plus de vente d'appartements. "
                "Il est aussi le déparetement avec le moins d'achat de maison sur la même période. "
                "En effet, Paris est une ville densément peuplée avec une forte qui possèd un étalement "
                "horizontal pour loger toutes cette population.Nord est le département avec le plus de maison vendues toutes "
                "années confondues.")

with tab2:
    with st.container():
        st.write(dvf_concat_trait.fig3)
        with st.expander("Voir l'explication"):
           st.write("Un regroupement par région hisse l'Ile-De-France comme la région enregistrant le plus de transactions au niveau des maison,"
                    " la Nouvelle-Aquitaine au niveau des maisons.")
    with st.container():
        region = st.multiselect("Sélectionner la région", dvf_concat_trait.region_transactionTest['Région'].unique())
        if not region:
            df = dvf_concat_trait.region_transactionTest.copy()
        else:
            df = dvf_concat_trait.region_transactionTest[dvf_concat_trait.region_transactionTest["Région"].isin(region)]
        #st.write(dvf_concat_trait.fig4)
        st.write(px.bar(df, x='Département', y='Nombre',title='Nombre de vente par département filtré par région'))
    with st.container():
        type_local = st.multiselect("Sélectionner le type de local", dvf_concat_trait.region_transactionAnnee['Type local'].unique())
        if not type_local:
            df2 = dvf_concat_trait.region_transactionAnnee.copy()
        else:
            df2 = dvf_concat_trait.region_transactionAnnee[dvf_concat_trait.region_transactionAnnee["Type local"].isin(type_local)]
        # st.write(dvf_concat_trait.fig4)
        fig3= px.bar(df2, x='Région', y= 'Nombre',
             color='Type local',barmode='group',
             title= 'Nombre de ventes par région et type d'+ "'" + "habitation 2019-2022",
             color_discrete_sequence=["coral","cornflowerblue"],
             animation_frame="Annee",range_y=[0,120000])
        fig3.update_layout(sliders=[{"currentvalue": {"prefix": "Année="}}])
        fig3.update_layout(margin=dict(l=40, r=30, t=30, b=200))
        fig3['layout']['updatemenus'][0]['pad'] = dict(r=10, t=150)
        fig3['layout']['sliders'][0]['pad'] = dict(r=10, t=150, )
        st.write(fig3)

with tab3:
    with st.container():
        st.write(dvf_concat_trait.fig5)
        with st.expander("Voir l'explication"):
           st.write("On constate qu'il y a une augmentation du prix/m^2 au cours du temps aves la région d'Ile de france en tête sur toutes les années."
                    "Elle se trauiduit d'une par une augmentation du prix et une diminution de la surface"
                    "La Provence-Alpes-Côte d'Azur possède un prix/m^2 aussi élevé que celui d'Ile de france"
                    "Il peut exister des disparité importante entre les départements d'une même région (en Ile-De-France par exemple avec Paris) , donc le graphique donne surtout une approximation de ce prix.")
    #with st.container():
    #    st.write(dvf_concat_trait.fig6)
