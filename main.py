import streamlit as st
from datetime import date

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Mi Dashboard de Estudio", page_icon="🎓", layout="wide")

# --- LÓGICA DE DÍAS RESTANTES ---
# Cambia esta fecha por la de tu examen real
fecha_examen = date(2026, 10, 3) 
hoy = date.today()
dias_faltan = (fecha_examen - hoy).days

# --- MENÚ LATERAL ---
with st.sidebar:
    st.title("📂 Menú Principal")
    materia = st.radio(
        "Selecciona una materia:",
        ["🏠 Inicio", "📐 Matemáticas", "🐍 Python", "🧪 Química", "📜 Legislación Militar"]

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
elif materia == "📜 Legislación Militar":
    st.switch_page("pages/2_Legislacion_Militar.py")

