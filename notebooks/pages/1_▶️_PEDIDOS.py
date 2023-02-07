# Libs
import sqlite3
import streamlit as st
import calendar
import pandas as pd

# Connect DB
conn = sqlite3.connect('pallet.db', check_same_thread=False)
cur = conn.cursor()


# Page Title
st.title('PEDIDOS')

# -Settings-
models = ['pallet100', 'pallet120']
sub_pallet120 = ['1200x90x15', '1000x90x18', '90x90x90', 'extra1200x90x15']
months = list(calendar.month_name[1:])



def form():
    st.write('Preencher com as informações para o cálculo')
    with st.form(key='Cálculo de materiais', clear_on_submit=True):
        name = st.text_input('Nome do Cliente:')
        col1, col2 = st.columns(2)
        with col1:
            qtd = st.sidebar.number_input('Quantidade:', 100, step=100)
        with col2:
            month_dlv = st.sidebar.selectbox('Mês de entrega:', months)
        with st.expander('Pallet120'):
            for prod in sub_pallet120:
                if prod == '1200x90x15':
                    st.write(f'{prod}:', qtd*8)
                elif prod == '1000x90x18':
                    st.write(f'{prod}:', qtd*3)
                elif prod == '90x90x90':
                    st.write(f'{prod}:', qtd*9)
                elif prod == 'extra1200x90x15':
                    st.write(f'{prod}:', qtd*3)
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
#st.write(df)

## Filters
#st.sidebar.multiselect(
#    'Escolha um produto',
#    list(df['nome_produto'].unique()), 
#    default=list(df['nome_produto'].unique())
#)
#
#st.sidebar.multiselect(
#    'Escolha os meses',
#    months, 
#)


#df['qtd'] = df['qtd'].astype(int)
#df_filtered = df[df['nome_produto'] == 'test2']
#texto = 'A soma do test2 é : '
#st.write(texto, df_filtered['qtd'].sum())

conn.close()