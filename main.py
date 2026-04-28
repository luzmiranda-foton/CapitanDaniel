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
        ["🏠 Inicio", "Manual 1", "Manual 2", "Manual 3 ", "Legislacion"]

    )
    st.divider()
    st.info(f"⏳ **{dias_faltan} días** restantes para el gran examen.")

# --- PÁGINA DE INICIO ---
if materia == "🏠 Inicio":
    st.title("🚀 ¡Bienvenido a tu Plan de Estudio, Capi Daniel✈️!")
    st.write("Selecciona una materia en el menú de la izquierda para comenzar a practicar.")
    
    # Métricas principales
    col1, col2, col3 = st.columns(3)
    col1.metric("Días para el examen", f"{dias_faltan}")
    col2.metric("Materias pendientes", "3")
    col3.metric("Tu progreso actual", "25%")
    
    st.image("https://images.unsplash.com/photo-1434030216411-0b793f4b4173?auto=format&fit=crop&q=80&w=1000", caption="¡Mantén el enfoque, tu puedes amorcito!")
elif materia == "legislacion":
    try:
        st.switch_page("Pages/legislacion.py")
    except:
        st.switch_page("pages/legislacion.py")


