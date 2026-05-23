import streamlit as st
import pandas as pd
 
st.title(" Mini Análisis de Datos")

archivo = st.file_uploader("Sube un archivo (CSV o Excel)", type=["csv", "xlsx"]) 

if archivo:
    name = archivo.name.lower()
    if name.endswith(".csv"):
        df = pd.read_csv(archivo)
    else:
        df = pd.read_excel(archivo)

    st.subheader("Vista previa")
    st.dataframe(df.head())

    st.subheader("Estadísticas")
    st.write(df.describe())

    num_cols = df.select_dtypes("number").columns
    if len(num_cols) > 0:
        col = st.selectbox("Columna para graficar", num_cols)
        st.bar_chart(df[col])
    else:
        st.info("No hay columnas numéricas para graficar")
else:
    st.info("Sube un archivo CSV o Excel para empezar")
