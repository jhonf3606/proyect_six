import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.header('Análisis Exploratorio de Datos: Vehículos')

# Cargar el conjunto de datos (asegúrate de que el archivo CSV esté en la misma carpeta o proporciona la ruta correcta)
car_data = pd.read_csv('vehicles_us.csv')

# Mostrar las primeras filas de los datos
st.write("Primeras filas del conjunto de datos:")
st.write(car_data.head())

# Crear un botón para generar el histograma
if st.button('Generar Histograma de Odometer'):
    # Crear el histograma de la columna "odometer"
    fig = px.histogram(car_data, x="odometer", title="Histograma de Odometer de los Vehículos")
    
    # Mostrar el gráfico interactivo en la app de Streamlit
    st.plotly_chart(fig)

