# Libs
import sqlite3
import streamlit as st
import calendar
import pandas as pd

# Connect DB
conn = sqlite3.connect('pallet.db', check_same_thread=False)
cur = conn.cursor()


st.title('RELATÓRIO')

months = list(calendar.month_name[1:])

# Verificação da tabela criada
query = """
    select * from pedido
    
"""
df = pd.read_sql_query( query, conn)
st.table(df)

# Filters
#st.sidebar.multiselect(
#    'Escolha um produto',
#    list(df['nome_produto'].unique()), 
#    default=list(df['nome_produto'].unique())
#)

st.sidebar.multiselect(
    'Escolha os meses',
    months, 
)


#====================================
#      LAYOUT LOCATIONS
#====================================
st.markdown("__________")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric('Pallet120', df['produto'].sum(), help="Quantidade Total de Pallets de acordo com o filtro")

with col2:
    st.metric('Delivery Service', df['is_delivering_now'].sum(), help="Restaurants with delivery service")

with col3:
    st.metric('Online Service', df['has_online_delivery'].sum(), help="Restaurants that acept online requests")
       
with col4:
    meancity = df[['country', 'city']].groupby('country').nunique().reset_index()
    st.metric('Average Cities', meancity['city'].mean().round(2), help='Average Cities by Country')

st.markdown("__________")    





df['qtd'] = df['qtd'].astype(int)
df_filtered = df[df['nome_produto'] == 'test2']
texto = 'A soma do test2 é : '
st.write(texto, df_filtered['qtd'].sum())

conn.close()