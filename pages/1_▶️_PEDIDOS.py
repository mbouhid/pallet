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
        name = st.text_input('Nome do Cliente:', 'Cliente2')
        qtd = st.sidebar.number_input('Quantidade:', 100, step=100, help="Digitar a qtd de Pallets a serem produzidos")
        month_dlv = st.selectbox('Mês de entrega:', months, help="Mês de entrega dos Pallets ao cliente")
        with st.expander('Pallet120', expanded = True):
            for prod in sub_pallet120:
                if prod == '1200x90x15':
                    qtd1200 = qtd * 8
                    st.write(f'{prod}:', qtd1200)
                elif prod == '1000x90x18':
                    qtd1000 = qtd * 3
                    st.write(f'{prod}:', qtd1000)
                elif prod == '90x90x90':
                    qtd90 = qtd * 9
                    st.write(f'{prod}:', qtd90)
                elif prod == 'extra1200x90x15':
                    qtd1200ex = qtd * 3
                    st.write(f'{prod}:', qtd1200ex)
        #col1, col2 = st.columns(2)
        #with col1:
        submission = st.form_submit_button(label='Salvar')
        #with st.sidebar:
        #    clear = st.form_submit_button(label='Limpar')
        if submission == True:
            addData(name, month_dlv, 'Pallet120', qtd, qtd1200, qtd1000, qtd90, qtd1200ex)
            st.success('Guardado com sucesso!')
        #if clear == True:
        #    st.sidebar.success('Limpeza feita!')
def addData(a, b, c, d, e, f, g, h):
    cur.execute("""CREATE TABLE IF NOT EXISTS request(
                nome_cliente TEXT(50),
                mes_entrega TEXT(15),
                produto TEXT(50),
                qtd INTEGER(5),
                peca1200 INTEGER(6),
                peca1000 INTEGER(6),
                peca90 INTEGER(6),
                peca1200ex INTEGER(6));
                """)
    cur.execute("INSERT INTO request VALUES (?,?,?,?,?,?,?,?)", (a, b, c, d, e, f, g, h))
    conn.commit()
    #st.success('Successfully submitted')


form()


# Verificação da tabela criada
#query = """
#    select * from request
#    
#"""
#df = pd.read_sql_query(query, conn)
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