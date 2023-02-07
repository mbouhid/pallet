# Libraries
import pandas as pd
import streamlit as st
from PIL import Image


st.set_page_config( page_title='Produção', layout='wide')



# Page Title
st.title('PRODUÇÃO')

st.subheader('Página para colocar a quantidade de material '
             'que será utilizado na produção dos pedidos e '
             'a retirada do estoque.')

#=======================================================
#       BARRA LATERAL
#=======================================================


logo = Image.open( './img/pallet.webp')
st.sidebar.image( logo)


