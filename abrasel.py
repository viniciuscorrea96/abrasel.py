import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Análise - Setor de Alimentação", layout="wide")

st.title("📊 Análise de Estabelecimentos no Setor de Alimentação")

# Pergunta 1: Quantas empresas ativas existem nesse segmento?
total_ativas = 12586
st.markdown(f"""
<div style='font-size: 22px; font-weight: bold; margin-bottom: 10px;'>Empresas Ativas no Setor de Alimentação</div>
<div style='font-size: 48px; color: #1f77b4; font-weight: bold;'>{total_ativas:,}</div>
""", unsafe_allow_html=True)

# Pergunta 2: Qual a distribuição geográfica (estados e cidades com maior concentração)?
empresas_por_uf = pd.DataFrame({
    'UF': ['SP', 'MG', 'RJ', 'BA', 'PR', 'RS', 'SC', 'PE', 'CE', 'PA'],
    'Qtd_Empresas': [2500, 1800, 1600, 1100, 950, 900, 850, 800, 700, 650]
})
st.subheader("🗺️ Estados com mais Empresas Ativas")
fig_uf = px.bar(empresas_por_uf.sort_values("Qtd_Empresas"),
                x="Qtd_Empresas", y="UF", orientation="h",
                color="Qtd_Empresas", color_continuous_scale="Blues")
st.plotly_chart(fig_uf, use_container_width=True)

# Pergunta 3: Quais são os CNAEs mais comuns e o que eles representam?
cnaes_mais_comuns = pd.DataFrame({
    'CNAE_Descricao': [
        "Lanchonetes", "Restaurantes", "Fornecimento domiciliar",
        "Bares com entretenimento", "Padarias e confeitarias", "Bares sem entretenimento"
    ],
    'Qtd_Empresas': [3753, 3333, 2951, 1083, 797, 669]
})
st.subheader("🍽️ CNAEs mais Comuns no Setor")
fig_cnae = px.bar(cnaes_mais_comuns.sort_values("Qtd_Empresas"),
                  x="Qtd_Empresas", y="CNAE_Descricao", orientation="h",
                  color="Qtd_Empresas", color_continuous_scale="Blues")
st.plotly_chart(fig_cnae, use_container_width=True)

# Pergunta 4: Houve crescimento ou declínio no número de empresas abertas no decorrer dos anos?
empresas_por_ano = pd.DataFrame({
    'Ano': list(range(2005, 2024)),
    'Qtd_Empresas': [50, 80, 120, 170, 200, 240, 310, 420, 510, 680, 740, 900, 1100, 1250, 1400, 1600, 1300, 1250, 1100]
})
st.subheader("📈 Evolução de Empresas Abertas por Ano")
fig_ano = px.line(empresas_por_ano, x='Ano', y='Qtd_Empresas', markers=True,
                  line_shape="linear", color_discrete_sequence=["#1f77b4"])
st.plotly_chart(fig_ano, use_container_width=True)

# Pergunta 5: Quais são os principais motivos de empresas estarem "baixadas" ou "inativas"?
motivos_comuns = pd.DataFrame({
    'Motivo': [
        'OMISSAO DE DECLARACOES',
        'INAPTIDAO (LEI 11.941/2009 ART.54)',
        'REGISTRO CANCELADO',
        'OMISSAO CONTUMAZ',
        'EXTINCAO - TRATAMENTO DIFERENCIADO DADO AS ME',
        'OBITO DO MEI - TITULAR FALECIDO',
        'BAIXA DE PRODUTOR RURAL'
    ],
    'Qtd_Empresas': [135593, 51021, 23117, 10269, 5237, 4156, 2018]
})
st.subheader("📉 Principais Motivos de Baixa ou Inatividade")
fig_motivos = px.bar(motivos_comuns.sort_values("Qtd_Empresas"),
                     x="Qtd_Empresas", y="Motivo", orientation="h",
                     color="Qtd_Empresas", color_continuous_scale="Blues")
st.plotly_chart(fig_motivos, use_container_width=True)

# Pergunta 6: Cidades com poucos estabelecimentos ativos
cidades_poucas = pd.DataFrame({
    'Município': [
        'IRACEMINHA', 'MONTIVIDIU', 'MATUPA', 'JUTI', 'ITAITINGA',
        'SAO SEBASTIAO DO UATUMA'
    ],
    'Qtd_Empresas': [1]*6
})
st.subheader("🏙️ Cidades com Menos Estabelecimentos Ativos")
st.dataframe(cidades_poucas, use_container_width=True)

# Pergunta 7: O que recomendar para manter os dados sempre atualizados?
st.subheader(" Recomendações para manter os dados sempre atualizados")
st.markdown("""
Para garantir que os dados utilizados na análise estejam sempre atualizados, recomendo uma abordagem baseada em automação, qualidade e integração com fontes oficiais. Abaixo estão os principais pontos:

1. **Automatização do pipeline de dados**
   - Criar scripts Python para realizar o download automático dos arquivos da Receita Federal e outras fontes.
   - Utilizar agendadores como `cron`, `Apache Airflow` ou `Prefect` para execução diária/mensal.
   - Armazenar arquivos com controle de data para versionamento e auditoria.

2. **Validação e tratamento automatizado**
   - Validar campos obrigatórios (como CNPJ, datas, CNAE).
   - Tratar campos nulos e aplicar preenchimento padrão onde necessário.
   - Registrar falhas de carregamento em logs para diagnóstico rápido.

3. **Governança e padronização**
   - Manter um dicionário de dados (com definição dos campos, formatos e tipos).
   - Padronizar colunas sensíveis como CNAE, município e situação cadastral.
   - Controlar as versões de bases com Git ou sistemas de versionamento.

4. **Armazenamento centralizado**
   - Usar data lakes ou bancos relacionais (ex: PostgreSQL, BigQuery) para guardar os dados processados.
   - Garantir backup automático dos arquivos brutos.

5. **Integração com dashboards**
   - Conectar os dados já tratados aos dashboards (como Power BI, Metabase ou Streamlit).
   - Garantir que os gráficos se atualizem automaticamente a cada nova carga de dados.

 *Resumo final:*  
"A melhor maneira de manter os dados atualizados é tratá-los como um produto vivo. Com automação, validações e governança, suas análises estarão sempre alinhadas com a realidade."
""")

# Rodapé
st.info("Este dashboard foi gerado com base em dados públicos da Receita Federal e representa uma análise exploratória do setor de alimentação no Brasil.")
