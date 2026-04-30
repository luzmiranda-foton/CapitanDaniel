import streamlit as st
from datetime import date
import json
import pandas as pd

st.set_page_config(
    page_title="Mi Dashboard de Estudio",
    page_icon="🎓",
    layout="wide"
)

# ----------------------------
# FUNCIONES
# ----------------------------
def cargar_progreso():
    try:
        with open("data/progreso.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

# ----------------------------
# LÓGICA DE DÍAS
# ----------------------------
fecha_examen = date(2026, 10, 3)
hoy = date.today()
dias_faltan = (fecha_examen - hoy).days

# ----------------------------
# SIDEBAR
# ----------------------------
with st.sidebar:
    st.title("📂 Menú Principal")

    nombre = st.text_input("👤 Ingresa tu nombre")

    if nombre:
        st.session_state["usuario"] = nombre

    st.info(f"⏳ **{dias_faltan} días** restantes para el gran examen.")

# ----------------------------
# USUARIO ACTUAL
# ----------------------------
usuario = st.session_state.get("usuario", "Invitado")

# ----------------------------
# CONTENIDO PRINCIPAL
# ----------------------------
st.title(f"🚀 ¡Bienvenido a tu Plan de Estudio, {usuario}! ✈️")
st.write("Usa el menú de la izquierda para cambiar de materia.")

# ----------------------------
# CARGAR PROGRESO
# ----------------------------
progreso = cargar_progreso()

porcentaje_general = 0
materias_pendientes = 3

if usuario in progreso and len(progreso[usuario]) > 0:
    datos_usuario = progreso[usuario]

    total_porcentajes = 0

    for seccion, datos in datos_usuario.items():
        total_porcentajes += datos["porcentaje"]

    porcentaje_general = int(total_porcentajes / len(datos_usuario))
    materias_pendientes = max(0, 3 - len(datos_usuario))

# ----------------------------
# MÉTRICAS
# ----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Días para el examen", f"{dias_faltan}")
col2.metric("Materias pendientes", materias_pendientes)
col3.metric("Tu progreso actual", f"{porcentaje_general}%")

# ----------------------------
# IMAGEN
# ----------------------------
st.image(
    "IMG-20251017-WA0017.jpg",
    caption="¡Mantén el enfoque amorcito, tú puedes!",
    use_container_width=True
)

# ----------------------------
# DASHBOARD DE PROGRESO
# ----------------------------
st.markdown("---")
st.subheader("📊 Dashboard de Progreso")

if usuario in progreso and len(progreso[usuario]) > 0:

    filas = []

    for seccion, datos in progreso[usuario].items():
        filas.append({
            "Sección": seccion,
            "Porcentaje": datos["porcentaje"],
            "Puntaje": datos["puntaje"],
            "Total": datos["total"],
            "Estado": datos["color"],
            "Dificultad": datos["dificultad"]
        })

    df = pd.DataFrame(filas)

    st.dataframe(df, use_container_width=True)

    st.subheader("📈 Avance por sección")
    st.bar_chart(df.set_index("Sección")["Porcentaje"])

    st.subheader("🎯 Diagnóstico")

    for _, fila in df.iterrows():
        st.write(
            f"{fila['Estado']} **{fila['Sección']}** "
            f"({fila['Porcentaje']}%) | "
            f"Dificultad: {fila['Dificultad']}"
        )

else:
    st.info("Todavía no tienes progreso guardado. Ve a Legislación y completa una sección.")
