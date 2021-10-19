import streamlit as st
import pandas as pd
import plotly.express as px

# Texto
st.write("""
# Avaliação dos filmes

Por gênero do avaliador e ano de lançamento  
""")

# Cabeçalho da barra lateral
st.sidebar.header('Filtros')

# Load data
df = pd.read_csv('best_year.csv')

# Plot
fig = px.line(df, x="year", y=["rating_homens", "rating_mulheres"])

fig.update_layout(
    xaxis_title_text='ano do lançamento',
    yaxis_title_text='avaliação',
    bargap=0.1, 
    template='simple_white')

st.write(fig)

st.subheader('Dados')
st.write(df[['year', 'rating_homens', 'rating_mulheres']])
