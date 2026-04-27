import streamlit as st
import joblib
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Clasificador IRIS", page_icon="🌸")

st.title("🌸 Clasificador de Flores IRIS")
st.markdown("Prueba tus modelos entrenados de **KNN** y **SVM**.")

# Sidebar para selección de modelo y parámetros
st.sidebar.header("Configuración")
tipo_modelo = st.sidebar.selectbox(
    "Selecciona el modelo:",
    ("K-Nearest Neighbors (KNN)", "Support Vector Machine (SVM)")
)

# Cargar el modelo seleccionado
def cargar_modelo(nombre_archivo):
    return joblib.load(nombre_archivo)

if tipo_modelo == "K-Nearest Neighbors (KNN)":
    modelo = cargar_modelo('modelo_iris_knn.pkl')
else:
    modelo = cargar_modelo('modelo_iris_svm.pkl')

# Entrada de datos (Slidars basados en las características del dataset IRIS)
st.subheader("Entrada de Características")
col1, col2 = st.columns(2)

with col1:
    sepal_l = st.slider("Largo del Sépalo (cm)", 4.0, 8.0, 5.4)
    sepal_w = st.slider("Ancho del Sépalo (cm)", 2.0, 4.5, 3.4)

with col2:
    petal_l = st.slider("Largo del Pétalo (cm)", 1.0, 7.0, 1.3)
    petal_w = st.slider("Ancho del Pétalo (cm)", 0.1, 2.5, 0.2)

# Botón de predicción
if st.button("Clasificar"):
    # Preparar los datos
    features = np.array([[sepal_l, sepal_w, petal_l, petal_w]])
    
    # Realizar predicción
    prediccion = modelo.predict(features)
    
    # Mapeo de nombres de especies
    especies = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
    resultado = especies.get(prediccion[0], "Desconocido")
    
    st.success(f"La predicción del modelo es: **Iris-{resultado}**")
    
    # Mostrar probabilidades si el modelo lo permite
    if hasattr(modelo, "predict_proba"):
        st.write("### Probabilidades:")
        probs = modelo.predict_proba(features)
        for i, esp in especies.items():
            st.write(f"{esp}: {probs[0][i]*100:.2f}%")
