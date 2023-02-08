# Libraries
import pandas as pd
import streamlit as st
from PIL import Image


st.set_page_config( page_title='Estoque', layout='wide')



# Page Title
st.title('ESTOQUE')

st.subheader('Página para atualização dos materiais que foram comprados '
             'e serão colocados no estoque para serem utilizados na '
             'produção futura.')

#=======================================================
#       BARRA LATERAL
#=======================================================


#logo = Image.open( './img/pallet.webp')
#st.sidebar.image( logo)