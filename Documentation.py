import streamlit as st

st.set_page_config(page_title="Documentation", page_icon='./assets/phd.png', layout="centered", initial_sidebar_state="auto", menu_items=None)

st.title("Base de données des progammes média au Bénin")

st.subheader("Description")

st.markdown("""
            Cette plateforme web vous donne un accès à toute la base de données des programmes radio et TV diffusés (enregistrés) en République du Bénin.
            
            Pour y accéder, vous devez disposer d'un nom d'utilisateur et d'un mot de passe valide.
            """)

st.subheader("Fonctionnement")

st.markdown("""
            Cet outil vous permet d'obtenir la liste des programmes radio et TV diffusés (enregistrés) au Bénin en vous basant sur des mots-clés.
            
            Vous avez la possibilité de:
            * effectuer des recherches sur l'ensemble des émissions diffusées sur un support média,
            * effectuer des recherches sur les émissions ayant et/ou contenant un certain titre,
            * effectuer des recherches sur les émissions animées par une certaine personne. 
            """)