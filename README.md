<h1 align="center">Sistema Controle de Pallet</h1>

<p align="center">Sistema web de cálculo de materiais e controle de estoque, que será utilizado na produção de pallets.</p>



Tabela de conteúdos
=================
<p align="center">
 <a href="#sobre">Sobre</a> •
 <a href="#objetivo">Objetivo</a> •
 <a href="#premissas">Premissas</a> •
 <a href="#tecnologias">Tecnologias</a> • 
 <a href="#solução">Solução</a> • 
 <a href="#utilizacao">Como instalar</a> • 
 <a href="#Lições_Aprendidas">Lições Aprendidas</a> • 
 <a href="#proximos_passos">Próximos Passos</a> • 
 <a href="#referências">Referências</a> • 
 <a href="#autor">Autor</a> • 
 <a href="#contribuidores">Contribuidores</a>  • 
 <a href="#licenc-a">Licença</a> • 
</p>

### Sobre

O sistema de controle de pallets servirá para controlar os pedidos de clientes, calculando a quantidade de material necessária para a produção dos pallets solicitados. O sistema fará, após o login, o controle de pedidos e estoque, cadastro de clientes, fornecedores e produtos, controle e monitoramento da produção e relatórios para ajudar na tomada da decisão. O sistema será escrito em Python + Pandas, guardará em banco de dados sqlite3 e utilizará a cloud do Streamlit para hospedar até que o cliente faça a validação. Após a aprovação, o sistema será migrado para o ambiente web do cliente. 


### Objetivo
Seguem algumas funcionalidades a serem criadas:

 1. Tela de login, com múltiplas regras de acordo com a hierarquia da empresa.
 2. Tela Pedidos: Cadastro do pedido, referenciando o tipo de pallet cadastrado a determinado cliente e cálculo dos materiais a serem gravados no banco de dados.
 3. Tela Produtos: Cadastro dos modelos de pallets e os materiais necessários para a produção.
 4. Tela Clientes: Cadastro do cliente ou fornecedor, referenciando o modelo do pallet ao cliente específico.
 5. Tela Produção: Dashboard dos produtos que estão sendo produzidos de acordo com a semana em andamento e a data de entrega (sinalização do prazo com verde/amarelo/vermelho)
 6. Tela Estoque: Cadastro dos materiais disponíveis para a produção de pallets.
 7. Tela Relatório: Lista de relatórios disponíveis:
     - Estoque: Quantidade de estoque de cada material disponível para a produção. Filtros: Tipo Material, Data de entrada
     - Pedidos Aprovados: Quantidade de pallets solicitados e aprovados para a produção, mostrando a quantidade de material necessária e se há no estoque ou não.
     
 
 
 
### Premissas

- Na limpeza dos dados:
   - Retirados os ID´s duplicados
   - Retirado o ID com número de quartos igual a 33 (possível erro de digitação)  
- Imóveis em bom estado foram considerados como condition igual 3 ou 4
- O crescimento anual foi calculado com o valor médio dos imóveis por ano, pois a base de dados só possuia o período de 13 meses.


### Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)

### Solução

- [HC_App_final_Streamlit.pdf](https://github.com/mbouhid/project_house_rocket/blob/main/hc_app_final_Streamlit.pdf)
- [HC_App_final_Streamlit_Menu.pdf](https://github.com/mbouhid/project_house_rocket/blob/main/hc_app_final_Streamlit_Menu.pdf)

### Como Instalar

Passo a passo de como rodar o modelo.

### Lições Aprendidas

- A base de dados tem que estar limpa
- As afirmações devem ser bem claras para que a solução da análise confirme ou não as hipóteses
- Nem toda afimação/hipótese tem solução ou será respondida
- Identificar claramente as premissas para alinhamento das expectativas
- Importante saber exatamente o que o cliente precisa.
- Identificar as necessidades mesmo que não esteja no pedido do cliente.


### Referências

[Kaggle](https://www.kaggle.com/)

[Github](https://github.com/)

[Comunidade Data Science](https://www.comunidadedatascience.com/)

[Blog Seja Um Data Scientist](https://medium.com/@meigarom/os-5-projetos-de-data-science-que-far%C3%A1-o-recrutador-olhar-para-voc%C3%AA-c32c67c17cc9)


### Autor

<img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/41192466?v=4" width="100px;" alt=""/>

[![Linkedin Badge](https://img.shields.io/badge/-MarcioBouhid-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/marciobouhid/)](https://www.linkedin.com/in/marciobouhid/) 


### Contribuidores

O projeto não teve contribuidores oficiais. A Comunidade Data Science foi consultada em determinados momentos.


### Licença

GNU General Public License v3.0

