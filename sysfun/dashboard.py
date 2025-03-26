#importar as Bibliotecas
import pandas as pd
import streamlit as st 
import plotly.express as px 
import sqlite3


#Conectar ao banco de Dados
conexao = sqlite3.connect("db.sqlite3")

#Ler os dados da tabela 

dados = pd.read_sql("""Select * from cadfun_funcionarios""",conexao)

##Streamlit##

#Configuração PAgina do Streamlit
st.set_page_config(
    page_title="Dashboard",
    page_icon=":bar_chart:",
    layout="wide"
)

#Configurou Coluna e linha para demostração do graficos

col1,col2 = st.columns(2) # Primeira linha com  2 coluna
col3,col4,col5 = st.columns(3) # Segunda linha com 3 colunas

#Grafico 1 - Coluna 1,1
#Histrograma de Idade

with col1:
    st.title("Histograma")
    fig = px.histogram(dados, x='idade', nbins=10)
    st.plotly_chart(fig)

#Grafico 2 - Coluna 1,2
#Boxplot

with col2:
    st.title("Departamento X Salario")
    fig2 = px.box(dados, x='departamento_id', y='salario')
    st.plotly_chart(fig2)

#Grafico 3 - Coluna 2,1
#Pizza ou Torta
with col3:
     st.title("Ativos e Inativos")
#    fig3 = px.pie(dados, names='ativo')
#    st.plotly_chart(fig3)

#Grafico 4 - coluna 2,2
#Grafico de Barra - Contagem funcionarios
with col4:
    st.title("Contagem Funcionarios por Departamento")
    qtd_funcionarios = dados['departamento_id'].value_counts().reset_index()
    qtd_funcionarios.columns = ['departamento_id','qtd_funcionarios']
    fig4 = px.bar(qtd_funcionarios, x='departamento_id',y='qtd_funcionarios')
    st.plotly_chart(fig4)

#Grafico 5 - Coluna 2,3
#Grafico de Dispersão ou POntos
with col5:
    st.title("Salario x Idade")
    fig5 = px.scatter(dados, x='idade', y='salario')
    st.plotly_chart(fig5)