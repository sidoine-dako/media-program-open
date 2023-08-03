import pandas as pd
import streamlit as st

import warnings
warnings.filterwarnings('ignore')
    

st.set_page_config(page_title="Recherche de programme", page_icon='./assets/phd.png', layout="wide", initial_sidebar_state="auto", menu_items=None)

    
st.header('Recherche des programmes média au Bénin')
# Import the data
link_url = st.secrets['url']

@st.cache_data(ttl="1d",show_spinner=False)
def import_data(url,sheet_name):
    data = pd.read_excel(io=url,sheet_name=sheet_name)
    return data

df_program = import_data(url=link_url,sheet_name="program")
df_medium = import_data(url=link_url,sheet_name="medium")

# Create the buttons and text box to set up the research
col_Medium, col_Text = st.columns([3,15])
with col_Medium:
    sel_Medium = st.multiselect(label='Media',options=df_medium['MedType'].unique(),default=df_medium['MedType'].unique(),help='Veuillez choisir un média')
with col_Text:
    sel_Support = st.multiselect(label='Support',options=df_medium.loc[df_medium['MedType'].isin(sel_Medium),'MedSup'].unique(),
                                 default=df_medium.loc[df_medium['MedType'].isin(sel_Medium),'MedSup'].unique())
    
text_search = st.text_input(label='Mots-clés',placeholder='Entrez ici les mots-clés pour effectuer votre recherche',
                help='Veuillez séparer les mots-clés par des points-virgules (;)')

df_complete = df_program.merge(right=df_medium,on="MedSup")
df_complete_process = df_complete.dropna(axis='columns',how='all')

df_complete_process = df_complete_process.loc[(df_complete_process['MedType'].isin(sel_Medium)) & (df_complete_process['MedSup'].isin(sel_Support))]
mask_medium = df_complete_process['MedSup'].str.contains(text_search,case=False)
mask_program = df_complete_process['ProgName'].str.contains(text_search,case=False)
df_complete_process = df_complete_process.loc[mask_medium | mask_program]
df_complete_process.drop(columns=['ProgAnim','MedFreq','MedCouv'],inplace=True)
df_complete_process = df_complete_process[["MedType","MedSup","ProgName","ProgLang","ProgDay","StartHour","EndHour"]]
df_complete_process.columns = ["Média",'Nom du support',"Nom de l'émission",'Langue',"Jour de diffusion", "Heure de début","Heure de fin"]

col_Df, _,col_stat= st.columns([15,3,5])
col_Df.dataframe(df_complete_process)
col_stat.metric(label="Nbre de Support",value=df_complete_process["Nom du support"].unique().shape[0])