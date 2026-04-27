import streamlit as st
import random

# Función para generar una nueva ecuación y guardarla en el estado de la sesión
def generar_ecuacion():
    a = random.randint(1, 10)
    x_real = random.randint(-10, 10)
    b = random.randint(-20, 20)
    c = a * x_real + b
    
    # Formatear el signo para que se vea natural (ej: 3x - 5 = 10 en lugar de 3x + -5 = 10)
    signo = "+" if b >= 0 else "-"
    ecuacion_str = f"{a}x {signo} {abs(b)} = {c}"
    
    st.session_state.ecuacion = ecuacion_str
    st.session_state.respuesta = x_real

# Inicializar el estado de la sesión si es la primera vez que se carga la app
if 'ecuacion' not in st.session_state:
    generar_ecuacion()

# Interfaz de usuario
st.set_page_config(page_title="Reto de Ecuaciones", page_icon="🧮")
st.title("🧮 Reto de Ecuaciones de Primer Grado")
st.write("Encuentra el valor exacto de **x** en la siguiente ecuación:")

# Mostrar la ecuación actual
st.header(st.session_state.ecuacion)

# Entrada del usuario
respuesta_usuario = st.number_input("Ingresa tu respuesta (x):", step=1)

# Crear columnas para los botones
col1, col2 = st.columns(2)

with col1:
    if st.button("✅ Verificar respuesta"):
        if respuesta_usuario == st.session_state.respuesta:
            st.success("¡Correcto! Eres un genio de las matemáticas.")
            st.balloons()  # Animación de éxito
        else:
            st.error("Respuesta incorrecta. ¡Sigue intentando!")
            st.snow()  # Animación de fallo (opcional, puedes quitarla si prefieres)

with col2:
    if st.button("🔄 Generar nueva ecuación"):
        generar_ecuacion()
        st.rerun() # Recarga la app para mostrar la nueva ecuación
