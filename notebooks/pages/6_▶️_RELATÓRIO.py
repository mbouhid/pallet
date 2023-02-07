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
st.write(df)

# Filters
st.sidebar.multiselect(
    'Escolha um produto',
    list(df['nome_produto'].unique()), 
    default=list(df['nome_produto'].unique())
)

st.sidebar.multiselect(
    'Escolha os meses',
    months, 
)


df['qtd'] = df['qtd'].astype(int)
df_filtered = df[df['nome_produto'] == 'test2']
texto = 'A soma do test2 é : '
st.write(texto, df_filtered['qtd'].sum())

conn.close()