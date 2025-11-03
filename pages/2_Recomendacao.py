import streamlit as st
import pandas as pd
import random

# Carregar dados dos filmes

filmes = pd.read_csv('filmes.csv',sep=",")

# Título da página
st.title("🎲 Me Sugira um Filme!")

# Filtros para sugestão
col1, col2 = st.columns(2)

with col1:
    genero = st.selectbox(
        "Gênero:",
        ["Qualquer"] + sorted(filmes['Genre'].unique().tolist())
    )

with col2:
    nota_minima = st.slider(
        "Nota mínima:",
        min_value=float(filmes['Rating'].min()),
        max_value=float(filmes['Rating'].max()),
        value=8.0
    )

# Botão para gerar sugestão
if st.button("🎯 Sugerir Filme Aleatório", type="primary"):
    # Aplicar filtros
    filmes_filtrados = filmes[filmes['Rating'] >= nota_minima]
    
    if genero != "Qualquer":
        filmes_filtrados = filmes_filtrados[filmes_filtrados['Genre'] == genero]
    
    if len(filmes_filtrados) > 0:
        # Escolher filme aleatório
        filme_sugerido = filmes_filtrados.sample(1).iloc[0]
        
        # Mostrar sugestão
        st.success("🎉 Aqui está sua sugestão!")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(filme_sugerido['Image URL'], use_container_width=True)
        
        with col2:
            st.header(filme_sugerido['Title'])
            st.write(f"**Ano:** {filme_sugerido['Year']}")
            st.write(f"**Nota:** ⭐ {filme_sugerido['Rating']}")
            st.write(f"**Duração:** ⏱️ {filme_sugerido['Duration']}")
            st.write(f"**Gênero:** 🎭 {filme_sugerido['Genre']}")
            st.write(f"**Posição no Ranking:** #{filme_sugerido['Rank']}")
            
            st.markdown(f"[🔗 Ver no IMDb]({filme_sugerido['IMDb URL']})")
    else:
        st.warning("❌ Não encontrei filmes com esses critérios. Tente ajustar os filtros!")