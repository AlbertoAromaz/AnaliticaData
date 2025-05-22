import streamlit as st
from PIL import Image 
from app1 import cargar_df
from app2 import graficos

img = Image.open("perfil-del-usuario.png")
st.set_page_config(page_title='Mi APP', page_icon=img, layout="wide"
                   , initial_sidebar_state="collapsed")

def página_principal():
    st.title("Modelo predictivo para recomendaciones de maridaje vinícola basado en técnicas de Machine Learning e interpretación de modelos")
    st.write("¡Bienvenido a la aplicación de demostración!")
    st.write("Usa el menú de la izquierda para navegar entre las páginas.")

st.sidebar.title("Navegación")    
pagina = st.sidebar.selectbox("Selecciona una página", ["Página Principal", 
                                                        "DataFrame", 
                                                        "Gráficos",
                                                        "Conócenos"])

if pagina == "Página Principal":
    página_principal()
elif pagina == "DataFrame":
    cargar_df()
elif pagina == "Gráficos":
    graficos()
else:
    st.subheader("Conócenos")
    nombre = "Alberto Z."
    st.text(f"Hola, Soy {nombre}, esto es Analitica de Datos y Sistemas Predictivos.")



