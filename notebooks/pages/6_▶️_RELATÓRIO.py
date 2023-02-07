import sqlite3
import streamlit as st
import pandas as pd
from PIL import Image


st.title('RELATÓRIO')

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
    value=[0, 10000],
    min_value=0,
    max_value=10000,
    step=5)
linhas_selecionadas_max = df['qtd'] <=  qtde_slider_max
linhas_selecionadas_min = df['qtd'] >=  qtde_slider_min
df = df.loc[linhas_selecionadas_max & linhas_selecionadas_min, :]

### FILTRO POR CLIENTE ###
clientes = st.sidebar.multiselect("Selecione os clientes:", options=list(df["nome_cliente"].unique()), default=list(df["nome_cliente"].unique()))
linhas_selecionadas = df['nome_cliente'].isin(clientes)
df = df.loc[linhas_selecionadas, :]

st.write(df)
