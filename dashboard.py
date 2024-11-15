import streamlit as st
from main import dados
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title("Dashboard de Dados de Países (2000-2023)")

# FILTROS
st.sidebar.header("Filtros")
anos = st.sidebar.slider("Selecione o intervalo de anos", min_value=int(dados['ano'].min()), max_value=int(dados['ano'].max()), value=(2000, 2023))
paises = st.sidebar.multiselect("Selecione os países", options=dados['pais'].unique(), default=dados['pais'].unique())

dados_filtrados = dados[(dados['ano'] >= anos[0]) & (dados['ano'] <= anos[1]) & (dados['pais'].isin(paises))]

st.dataframe(dados_filtrados)

# PARTE MAIS DAHORA, GRAFICOS DE LINHA
st.header("Gráficos de Indicadores")

# Dicionário de mapeamento para indicadores legíveis (para os gráficos também)
indicadores_map = {
    "Pib em Trilhões de Dólares": 'pib_em_trilhoes_usd',
    "Pib per Capita (USD)": 'pib_per_capita_usd',
    "População em Milhões": 'populacao_milhoes',
    "Expectativa de Vida": 'expectativa_de_vida',
    "Taxa de Inflação": 'taxa_de_inflacao',
    "Taxa de Desemprego": 'taxa_desemprego',
    "Taxa de Criminalidade": 'taxa_criminalidade',
    "Gasto com Saúde per Capita (USD)": 'gasto_com_saude_per_capita',
    "Proporção de Médicos para Paciente": 'proporcao_de_medico_para_paciente',
    "Gasto Militar (Bilhões de USD)": 'gasto_militar_bilhoes_usd',
    "Número de Militares Ativos": 'numero_militares_ativos',
    "Índice de Igualdade de Gênero": 'indice_igualdade_genero',
    "Taxa de Pobreza": 'taxa_pobreza',
    "Índice de Percepção de Corrupção": 'indice_percepcao_corrupcao',
    "Índice de Liberdade de Imprensa": 'indice_liberdade_imprensa',
    "Taxa de Participação Votação": 'taxa_participacao_votacao',
    "Taxa de Crescimento Populacional": 'taxa_de_crescimento_populacional',
    "População Urbana": 'populacao_urbana'
}
#INDICADOR
indicador_legivel = st.selectbox(
    "Selecione o indicador para o gráfico",
    options=list(indicadores_map.keys())
)
#GRAFICO DE INDICADOR POR ANO

indicador = indicadores_map[indicador_legivel]
dados_sorted = dados_filtrados.sort_values(by="ano")
fig_line = px.line(
    dados_sorted,
    x="ano",
    y=indicador,
    color="pais",
    hover_name="pais"
)
fig_line.update_xaxes(type="linear")
st.plotly_chart(fig_line)

# GRAFICO DE DISPERSÃO LIBERADE DE IMPRESA VS PERCEPCAO DE CORRUPCAO
dados_filtrados_scatter = dados_filtrados[['pais', 'ano', 'indice_liberdade_imprensa', 'indice_percepcao_corrupcao']]
fig_scatter = px.scatter(
    dados_filtrados_scatter,
    x="indice_liberdade_imprensa",
    y="indice_percepcao_corrupcao",
    color="pais",
    hover_name="pais",
    title="Liberdade de Imprensa VS Percepção de Corrupção"
)
st.plotly_chart(fig_scatter)

# GRAFICO DE BARRA POR PAISES
st.header("Distribuição de Dados por País")
indicadores_map2 = {
    "Pib em Trilhões de Dólares": 'pib_em_trilhoes_usd',
    "Pib per Capita (USD)": 'pib_per_capita_usd',
    "População em Milhões": 'populacao_milhoes',
    "Expectativa de Vida": 'expectativa_de_vida',
    "Taxa de Inflação": 'taxa_de_inflacao',
    "Taxa de Desemprego": 'taxa_desemprego',
    "Taxa de Criminalidade": 'taxa_criminalidade',
    "Gasto com Saúde per Capita (USD)": 'gasto_com_saude_per_capita',
    "Proporção de Médicos para Paciente": 'proporcao_de_medico_para_paciente',
    "Gasto Militar (Bilhões de USD)": 'gasto_militar_bilhoes_usd',
    "Número de Militares Ativos": 'numero_militares_ativos',
    "Índice de Igualdade de Gênero": 'indice_igualdade_genero',
    "Índice de Percepção de Corrupção": 'indice_percepcao_corrupcao',
    "Índice de Liberdade de Imprensa": 'indice_liberdade_imprensa',
    "População Urbana": 'populacao_urbana'
}
#INDICADOR
indicador_legivel2 = st.selectbox(
    "Selecione o indicador para o gráfico",
    options=list(indicadores_map2.keys())
)
#GRAFICO DE INDICADOR POR ANO

indicador2 = indicadores_map[indicador_legivel2]
fig_bar = px.bar(dados_filtrados, x="pais", y=indicador2)
st.plotly_chart(fig_bar)

indicadores_media_map = {
    "Pib em Trilhões de Dólares": 'pib_em_trilhoes_usd',
    "Pib per Capita (USD)": 'pib_per_capita_usd',
    "Gasto com Saúde per Capita (USD)": 'gasto_com_saude_per_capita'
}

#RESUMO FINAL DAS METRICAS SELECIONADAS
st.header("Métricas Resumidas")
indicator_legivel = st.selectbox(
    "Selecione o indicador para as métricas",
    options=list(indicadores_media_map.keys())
)
indicator = indicadores_media_map[indicator_legivel]

st.write(f"Média do {indicator_legivel}: ${dados_filtrados[indicator].mean():.2f}")
st.write(f"Valor Máximo do {indicator_legivel}: ${dados_filtrados[indicator].max():.2f}")
st.write(f"Valor Mínimo do {indicator_legivel}: ${dados_filtrados[indicator].min():.2f}")
