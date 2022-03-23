import streamlit as st
import pandas as pd

df = pd.read_csv("C:/Users/STEFA/Desktop/github/Dados_Servidores_CE_Streamlit/datasets/format.csv",index_col=False)
st.dataframe(df)

#st.write("hello")