import streamlit as st
from datetime import date

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Mi Dashboard de Estudio", page_icon="🎓", layout="wide")

# --- LÓGICA DE DÍAS RESTANTES ---
# Cambia esta fecha por la de tu examen real
fecha_examen = date(2025, 6, 27) 
hoy = date.today()
dias_faltan = (fecha_examen - hoy).days

# --- MENÚ LATERAL ---
with st.sidebar:
    st.title("📂 Menú Principal")
    materia = st.radio(
        "Selecciona una materia:",
        ["🏠 Inicio", "📐 Matemáticas", "🐍 Python", "🧪 Química"]
    )
    st.divider()
    st.info(f"⏳ **{dias_faltan} días** restantes para el gran examen.")

# --- PÁGINA DE INICIO ---
if materia == "🏠 Inicio":
    st.title("🚀 ¡Bienvenido a tu Plan de Estudio, Daniel!")
    st.write("Selecciona una materia en el menú de la izquierda para comenzar a practicar.")
    
    # Métricas principales
    col1, col2, col3 = st.columns(3)
    col1.metric("Días para el examen", f"{dias_faltan}")
    col2.metric("Materias pendientes", "3")
    col3.metric("Tu progreso actual", "25%")
    
    st.image("https://images.unsplash.com/photo-1434030216411-0b793f4b4173?auto=format&fit=crop&q=80&w=1000", caption="¡Mantén el enfoque!")

# --- MATERIA: PYTHON ---
elif materia == "🐍 Python":
    st.title("🐍 Cuestionario de Python")
    st.write("Responde las preguntas y presiona el botón al final para ver tu nota.")

    with st.form("quiz_python"):
        # Pregunta 1
        q1 = st.selectbox(
            "1. ¿Cómo se define una función en Python?",
            ["function mi_func():", "def mi_func():", "void mi_func():", "create mi_func():"]
        )
        
        # Pregunta 2
        q2 = st.radio(
            "2. ¿Cuál de estos es un tipo de dato inmutable?",
            ["Lista (list)", "Diccionario (dict)", "Tupla (tuple)"]
        )
        
        # Pregunta 3
        q3 = st.text_input("3. Escribe el comando para imprimir 'Hola' en la pantalla:")

        enviar = st.form_submit_button("Finalizar y Calificar")

    if enviar:
        puntaje = 0
        
        # Calificar P1
        if q1 == "def mi_func():":
            puntaje += 1
            st.success("✅ Pregunta 1: ¡Correcto!")
        else:
            st.error("❌ Pregunta 1: Incorrecto. Se usa 'def'.")
            
        # Calificar P2
        if q2 == "Tupla (tuple)":
            puntaje += 1
            st.success("✅ Pregunta 2: ¡Correcto!")
        else:
            st.error("❌ Pregunta 2: Incorrecto. Las listas son mutables.")

        # Calificar P3
        if "print" in q3.lower() and ("hola" in q3.lower()):
            puntaje += 1
            st.success("✅ Pregunta 3: ¡Correcto!")
        else:
            st.error("❌ Pregunta 3: Incorrecto. El comando es print('Hola').")

        # Resultado final
        nota_final = (puntaje / 3) * 10
        st.subheader(f"📊 Tu calificación: {nota_final:.1f}/10")
        if nota_final >= 6:
            st.balloons()
            st.success("¡Felicidades, aprobaste!")
        else:
            st.warning("Necesitas repasar un poco más.")

# --- MATERIA: MATEMÁTICAS (Ejemplo vacío) ---
elif materia == "📐 Matemáticas":
    st.title("📐 Matemáticas")
    st.info("Esta sección aún no tiene cuestionarios. ¡Añade los tuyos en el código!")

# --- MATERIA: QUÍMICA ---
elif materia == "🧪 Química":
    st.title("🧪 Química")
    st.write("Cuestionario en construcción...")
