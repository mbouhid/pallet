# Libraries
import pandas as pd
from PIL import Image
import streamlit as st



st.set_page_config( page_title='Clientes', layout='wide')

# Import dataset
df_raw = pd.read_csv( 'data/dfpronto.csv' )

df = df_raw.copy()


#=======================================================
#       BARRA LATERAL
#=======================================================


logo = Image.open( './img/pallet.webp')
st.sidebar.image( logo)

st.sidebar.markdown( """_______""" )

# FILTRO
st.sidebar.markdown( '## Average Price for Two' )

dollar_slider_min, dollar_slider_max = st.sidebar.slider( 
    'Select price limit:',
    value=[0.0, 755.0],
    min_value=0.0,
    max_value=755.0)

st.sidebar.markdown( """---""" )

st.sidebar.markdown( '## Countries' )

country = st.sidebar.multiselect( 
    'Select the country:',
    list(df['country'].unique()), 
    default=list(df['country'].unique()) )

st.sidebar.markdown( """---""" )

## Filtro de preço
linhas_selecionadas_max = df['dollar'] <=  dollar_slider_max
linhas_selecionadas_min = df['dollar'] >=  dollar_slider_min
df = df.loc[linhas_selecionadas_max & linhas_selecionadas_min, :]

# Filtro de país
linhas_selecionadas = df['country'].isin( country )
df = df.loc[linhas_selecionadas, :]




#====================================
#      LAYOUT LOCATIONS
#====================================
st.markdown("__________")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric('Table Booking', df['has_table_booking'].sum(), help="Restaurants that has table booking")

with col2:
    st.metric('Delivery Service', df['is_delivering_now'].sum(), help="Restaurants with delivery service")

with col3:
    st.metric('Online Service', df['has_online_delivery'].sum(), help="Restaurants that acept online requests")
       
with col4:
    meancity = df[['country', 'city']].groupby('country').nunique().reset_index()
    st.metric('Average Cities', meancity['city'].mean().round(2), help='Average Cities by Country')

st.markdown("__________")    
