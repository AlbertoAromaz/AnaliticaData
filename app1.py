import streamlit as st
import pandas as pd

def cargar_df():
    st.subheader("DataFrame Crudo:")
    df = pd.read_csv('GOOGLE_BASE_WINE_CHEESE_PROJECT - DATASET.csv')    
    st.dataframe(df)

if __name__ == '__main__':
    cargar_df()