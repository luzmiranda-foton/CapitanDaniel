import streamlit as st
from datetime import date

st.set_page_config(page_title="Mi Dashboard de Estudio", page_icon="🎓", layout="wide")

# --- LÓGICA DE DÍAS ---
fecha_examen = date(2026, 10, 3)
hoy = date.today()
dias_faltan = (fecha_examen - hoy).days

# --- SIDEBAR ---
with st.sidebar:
    st.title("📂 Menú Principal")
    st.info(f"⏳ **{dias_faltan} días** restantes para el gran examen.")

# --- CONTENIDO PRINCIPAL ---
st.title("🚀 ¡Bienvenido a tu Plan de Estudio, Capi Daniel✈️!")
st.write("Usa el menú de la izquierda para cambiar de materia.")

col1, col2, col3 = st.columns(3)
col1.metric("Días para el examen", f"{dias_faltan}")
col2.metric("Materias pendientes", "3")
col3.metric("Tu progreso actual", "25%")

st.image("IMG-20251017-WA0017.jpg"¡Mantén el enfoque amorcito, tu puedes!")
