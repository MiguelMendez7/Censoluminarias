
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Simulación de datos del censo
censo = {
    "LED 100W": {"cantidad": 50, "tipo_medicion": "Medida"},
    "Vapor de Sodio 250W": {"cantidad": 30, "tipo_medicion": "Directa"},
    "Fluorescente 40W": {"cantidad": 20, "tipo_medicion": "Medida"},
}

# Función para mostrar los datos en tabla
def mostrar_censo():
    df = pd.DataFrame.from_dict(censo, orient="index")
    st.write("### Datos del Censo de Luminarias")
    st.dataframe(df)

# Función para graficar distribución de luminarias
def graficar_luminarias():
    tipos = list(censo.keys())
    cantidades = [datos["cantidad"] for datos in censo.values()]

    plt.figure(figsize=(10, 5))
    plt.barh(tipos, cantidades, color='skyblue')
    plt.xlabel("Cantidad de Luminarias")
    plt.ylabel("Tipo de Luminaria")
    plt.title("Distribución de Luminarias en el CENSO")
    st.pyplot(plt)

# Crear la interfaz web
st.title("Sistema de Gestión de Luminarias")
st.sidebar.header("Opciones")

opcion = st.sidebar.radio("Selecciona una opción:", ["Ver Censo", "Gráfico de Luminarias"])

if opcion == "Ver Censo":
    mostrar_censo()
elif opcion == "Gráfico de Luminarias":
    graficar_luminarias()
