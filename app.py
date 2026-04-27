import streamlit as st
import pandas as pd
import joblib
import os

# Configuración de la página
st.set_page_config(page_title="Clasificador de Iris", page_icon="🌸")

st.title("🌸 Clasificador de Flores Iris")
st.markdown("""
Esta aplicación permite probar modelos entrenados para predecir la especie de una flor Iris 
basándose en sus medidas morfológicas.
""")

# Sidebar para la selección del modelo y parámetros
st.sidebar.header("Configuración")

# Selección del modelo
modelo_choice = st.sidebar.selectbox(
    "Selecciona el modelo:",
    ("KNN (K-Nearest Neighbors)", "SVM (Support Vector Machine)")
)

# Cargar el modelo seleccionado
def cargar_modelo(nombre_archivo):
    if os.path.exists(nombre_archivo):
        return joblib.load(nombre_archivo)
    else:
        st.error(f"Archivo {nombre_archivo} no encontrado en el repositorio.")
        return None

if modelo_choice == "KNN (K-Nearest Neighbors)":
    model = cargar_modelo("modelo_iris_knn.pkl")
else:
    model = cargar_modelo("modelo_iris_svm.pkl")

# Inputs de usuario
st.sidebar.subheader("Medidas de la flor (cm)")
sepal_length = st.sidebar.slider("Largo del Sépalo", 4.0, 8.0, 5.4)
sepal_width = st.sidebar.slider("Ancho del Sépalo", 2.0, 4.5, 3.4)
petal_length = st.sidebar.slider("Largo del Pétalo", 1.0, 7.0, 1.3)
petal_width = st.sidebar.slider("Ancho del Pétalo", 0.1, 2.5, 0.2)

# Crear un DataFrame con la entrada
input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                         columns=['sepal length (cm)', 'sepal width (cm)', 
                                  'petal length (cm)', 'petal width (cm)'])

# Predicción
if model is not None:
    st.subheader("Resultado de la Predicción")
    
    if st.button("Clasificar"):
        prediction = model.predict(input_data)
        
        # Mapeo de especies (asumiendo orden estándar de Scikit-learn)
        especies = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
        resultado = especies.get(prediction[0], prediction[0])
        
        st.success(f"La especie predicha es: **Iris {resultado}**")
        
        # Mostrar probabilidades si el modelo lo permite
        if hasattr(model, "predict_proba"):
            st.write("---")
            st.write("**Probabilidades por clase:**")
            probabilidades = model.predict_proba(input_data)
            df_probs = pd.DataFrame(probabilidades, columns=["Setosa", "Versicolor", "Virginica"])
            st.bar_chart(df_probs.T)
else:
    st.warning("Por favor, asegúrate de que los archivos .pkl estén en la raíz del repositorio.")
