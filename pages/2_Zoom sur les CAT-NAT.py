import streamlit as st
import dvf_concat_trait
# # Ajout d'une sidebar
st.sidebar.header('Filtres')

## Adding tabs
tab1, tab2 = st.tabs(["Sécheresse","Inondation"])

def plot_section_1():
    with st.container():
        with tab1:
            st.header("Graphe")
            st.write(dvf_concat_trait.fig)
            with st.expander("Voir l'explication"):
                st.write("Le graphe ci-dessus représente ... *italique*")
        with tab2:
            st.header("Dataframe")
            st.write(dvf_concat_trait.departement_transaction)


def plot_section_2():
    st.write(dvf_concat_trait.fig2)

option = st.sidebar.selectbox('Quelle analyse souhaiteriez-vous voir?',('Département avec le plus de transaction','Prix au mètre carré'),index=None,
   placeholder="Selectionner une analyse...")

if option == 'Département avec le plus de transaction':
    plot_section_1()

elif option == 'Prix au mètre carré':
    plot_section_2()


