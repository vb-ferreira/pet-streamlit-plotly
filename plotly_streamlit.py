import streamlit as st
import pandas as pd
import plotly.express as px

# Line chart
# # Texto
# st.write("""
# # Avaliação dos filmes

# Por gênero do avaliador e ano de lançamento  
# """)

# # Cabeçalho da barra lateral
# st.sidebar.header('Filtros')

# # Load data
# df = pd.read_csv('best_year.csv')

# # Plot
# fig = px.line(df, x="year", y=["rating_homens", "rating_mulheres"])

# fig.update_layout(
#     xaxis_title_text='ano do lançamento',
#     yaxis_title_text='avaliação',
#     bargap=0.1, 
#     template='simple_white')

# st.write(fig)

# st.subheader('Dados')
# st.write(df[['year', 'rating_homens', 'rating_mulheres']])


# ---


# Animated bar charts
# Load data
df = pd.read_csv('patho_acumulada.csv', sep=";")
#st.write(df)

# Texto
st.write("""
# Tipos de exame
### _frequência acumululada_
### (1981-1991)  
# """)


fig = px.bar(df, x="exame", y="frequencia", color="exame",
  animation_frame="ano", animation_group="exame", range_y=[0,100])

st.write(fig)
#fig.show()
