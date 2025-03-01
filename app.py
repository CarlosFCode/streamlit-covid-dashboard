import pandas as pd
import plotly.express as px
import streamlit as st

# Carregar os dados
@st.cache_data
def load_data():
    data = pd.read_csv('covid_dashboard/owid-covid-data.csv')
    return data

df = load_data()

# Título do aplicativo
st.title('Dashboard de Análise de COVID-19')

# Descrição
st.write("""
Este dashboard permite visualizar dados de COVID-19 em diferentes países.
Use os filtros abaixo para explorar os dados.
""")

# Filtro de país
paises = df['location'].unique()
pais_selecionado = st.selectbox('Selecione um país', paises)
# Filtro de métricas
metricas = {
    "Casos": 'new_cases',
    'Mortes': 'new_deaths',
    'Vacinações': 'new_vaccinations'
}
metrica_selecionada = st.selectbox('Selecione uma métrica: ', list(metricas.keys()))

# Dados filtrados
dados_filtrados = df[df['location'] == pais_selecionado]

fig = px.line(
    dados_filtrados,
    x="date",
    y=metricas[metrica_selecionada],
    title=f"{metrica_selecionada} em {pais_selecionado}"
)

st.plotly_chart(fig)

# Estatísticas resumidas
total_casos = dados_filtrados['new_cases'].sum()
total_mortes = dados_filtrados['new_deaths'].sum()
total_vacinacoes = dados_filtrados['new_vaccinations'].sum()

st.write(f"**Total de Casos:** {total_casos:,}")
st.write(f"**Total de Mortes:** {total_mortes:,}")
st.write(f"**Total de Vacinações:** {total_vacinacoes:,}")