# Libs
import sqlite3
import calendar
import pandas as pd
from PIL import Image
import streamlit as st


st.title('RELATÓRIO')

# Connect DB
conn = sqlite3.connect('pallet.db', check_same_thread=False)
cur = conn.cursor()

query = """
    select * from request
"""
df = pd.read_sql_query(query, conn)
conn.close()

### BARRA LATERAL ###

st.sidebar.markdown( '## Produtos' )

produtos = st.sidebar.multiselect(
    'Selecione os produtos:',
    list(df['produto'].unique()),
    default=list(df['produto'].unique()) )
linhas_selecionadas = df['produto'].isin(produtos)
df = df.loc[linhas_selecionadas, :]


st.sidebar.write("---")

### FILTRO POR QUANTIDADE DE PALLETS ###

qtde_slider_min, qtde_slider_max = st.sidebar.slider(
    'Selecione a quantidade desejada:',
    value=[0, 5000],
    min_value=0,
    max_value=5000,
    step=5)
linhas_selecionadas_max = df['qtd'] <=  qtde_slider_max
linhas_selecionadas_min = df['qtd'] >=  qtde_slider_min
df = df.loc[linhas_selecionadas_max & linhas_selecionadas_min, :]

### FILTRO POR MÊS ###
mes = st.sidebar.multiselect(
    "Selecione os Meses:",
    options=list(df["mes_entrega"].unique()),
    default=list(df["mes_entrega"].unique()))
linhas_selecionadas = df['mes_entrega'].isin(mes)
df = df.loc[linhas_selecionadas, :]

### FILTRO POR CLIENTE ###
clientes = st.sidebar.multiselect(
    "Selecione os clientes:",
    options=list(df["nome_cliente"].unique()),
    default=list(df["nome_cliente"].unique()))
linhas_selecionadas = df['nome_cliente'].isin(clientes)
df = df.loc[linhas_selecionadas, :]


#====================================
#      LAYOUT LOCATIONS
#====================================
st.markdown("__________")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric('Pallets Totais', df['qtd'].sum(), help="Pallets totais")

with col2:
    st.metric('Peça 1200', df['peca1200'].sum(), help="Qtd peça madeira 1200mm")

with col3:
    st.metric('Peça 1000', df['peca1000'].sum(), help="Qtd peça madeira 1000mm")

with col4:
    st.metric('Peça 90', df['peca90'].sum(), help="Qtd peça madeira 90mm")

with col5:
    st.metric('Peça 1200 extra', df['peca1200ex'].sum(), help="Qtd peça madeira 1200mm extra")


st.markdown("__________") 



st.table(df)