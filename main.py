import streamlit as st
from datetime import date
import json
import os
import pandas as pd


RUTA_USUARIO = "data/usuario.json"
RUTA_PROGRESO = "data/progreso.json"


def cargar_usuario():
    try:
        with open(RUTA_USUARIO, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}


def guardar_usuario(nombre):
    os.makedirs("data", exist_ok=True)
    with open(RUTA_USUARIO, "w", encoding="utf-8") as f:
        json.dump({"usuario": nombre}, f, indent=4, ensure_ascii=False)


def cargar_progreso():
    try:
        with open(RUTA_PROGRESO, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}


st.set_page_config(
    page_title="Mi Dashboard de Estudio",
    page_icon="🎓",
    layout="wide"
)


datos_usuario_guardado = cargar_usuario()

if "usuario" not in st.session_state:
    st.session_state["usuario"] = datos_usuario_guardado.get("usuario", "")


fecha_examen = date(2026, 10, 3)
hoy = date.today()
dias_faltan = (fecha_examen - hoy).days


with st.sidebar:
    st.title("📂 Menú Principal")

    nombre = st.text_input(
        "👤 Ingresa tu nombre",
        value=st.session_state["usuario"],
        key="input_usuario"
    )

    if nombre.strip():
        st.session_state["usuario"] = nombre.strip()
        guardar_usuario(nombre.strip())

    st.info(f"⏳ **{dias_faltan} días** restantes para el gran examen.")


usuario = st.session_state.get("usuario", "")

if not usuario:
    usuario = "Invitado"


st.title(f"🚀 ¡Bienvenido a tu Plan de Estudio, {usuario}! ✈️")
st.write("Usa el menú de la izquierda para cambiar de materia.")


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


col1, col2, col3 = st.columns(3)

col1.metric("Días para el examen", f"{dias_faltan}")
col2.metric("Materias pendientes", materias_pendientes)
col3.metric("Tu progreso actual", f"{porcentaje_general}%")


st.image(
    "IMG-20251017-WA0017.jpg",
    caption="¡Mantén el enfoque amorcito, tú puedes!",
    use_container_width=True
)


st.markdown("---")
st.subheader("Dashboard de Progreso")

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

    st.subheader("Avance por sección")
    st.bar_chart(df.set_index("Sección")["Porcentaje"])

    st.subheader("Diagnóstico")

    for _, fila in df.iterrows():
        st.write(
            f"{fila['Estado']} **{fila['Sección']}** "
            f"({fila['Porcentaje']}%) | "
            f"Dificultad: {fila['Dificultad']}"
        )

else:
    st.info("Todavía no tienes progreso guardado. Ve a Legislación y completa una sección.")
