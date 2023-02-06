# Libs

import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect('pallet.db', check_same_thread=False)
cur = conn.cursor()



# Page Title
st.title('PEDIDOS')


def form():
    st.write('Preencher com as informações para o cálculo')
    with st.form(key='Cálculo de materiais', clear_on_submit=True):
        name = st.text_input('Nome do Produto:')
        qtd = st.text_input('Quantidade:')
        col1, col2 = st.columns(2)
        with col1:
            submission = st.form_submit_button(label='Salvar')
        with col2:
            clear = st.form_submit_button(label='Limpar')
        if submission == True:
            addData(name, qtd)
            st.success('Guardado com sucesso!')
        if clear == True:
            st.success('Limpeza feita!')

def addData(a, b):
    cur.execute("""CREATE TABLE IF NOT EXISTS pedido(nome_produto TEXT(50), qtd INTEGER(5));""")
    cur.execute("INSERT INTO pedido VALUES (?,?)", (a, b))
    conn.commit()
    st.success('Successfully submitted')


form()


# Verificação da tabela criada
query = """
    select * from pedido
    
"""

df = pd.read_sql_query( query, conn)
st.write(df)

st.sidebar.multiselect(
    'Escolha um produto',
    list(df['nome_produto'].unique()), 
    default=list(df['nome_produto'].unique())
)


df['qtd'] = df['qtd'].astype(int)
df_filtered = df[df['nome_produto'] == 'test2']
texto = 'A soma do test2 é : '
st.write(texto, df_filtered['qtd'].sum())

conn.close()