import streamlit as st
import json
import os


RUTA_PROGRESO = "data/progreso.json"


def cargar_progreso():
    try:
        with open(RUTA_PROGRESO, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}


def guardar_progreso(data):
    os.makedirs("data", exist_ok=True)
    with open(RUTA_PROGRESO, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def obtener_color_dominio(porcentaje):
    if porcentaje >= 80:
        return "🟢 Verde", "Lo dominas bien"
    elif porcentaje >= 60:
        return "🟠 Naranja", "Vas regular, conviene repasar"
    else:
        return "🔴 Rojo", "Falta estudiar esta parte"


def show():
    st.title("📘 Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos")

    usuario = st.session_state.get("usuario")

    if not usuario:
        st.warning("⚠️ Primero escribe tu nombre en la página principal.")
        st.stop()

    seccion_id = "disciplina_parte1"
    dificultad = "🟢 Facil"

    progreso = cargar_progreso()

    st.markdown("## Primera parte")
    st.info(f"👤 Usuario: **{usuario}**")
    st.info(f"🔥 Dificultad del tema: **{dificultad}**")

    if usuario in progreso and seccion_id in progreso[usuario]:
        datos = progreso[usuario][seccion_id]
        st.success(
            f"Progreso guardado: {datos['color']} — "
            f"{datos['porcentaje']}% — {datos['mensaje']}"
        )

    preguntas = [
        {
            "pregunta": "¿Cuál es el objeto de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos? (Art. 1°)",
            "correcta": "La presente Ley tiene por objeto preservar la disciplina militar como principio de orden y obediencia que regula la conducta de los individuos que integran el Ejército y Fuerza Aérea Mexicanos. Sus disposiciones son de observancia obligatoria para todos los militares que integran el Ejército y Fuerza Aérea Mexicanos de conformidad con su Ley Orgánica.",
            "opciones": [
                "Regular únicamente los ascensos y recompensas del personal militar.",
                "La presente Ley tiene por objeto preservar la disciplina militar como principio de orden y obediencia que regula la conducta de los individuos que integran el Ejército y Fuerza Aérea Mexicanos. Sus disposiciones son de observancia obligatoria para todos los militares que integran el Ejército y Fuerza Aérea Mexicanos de conformidad con su Ley Orgánica.",
                "Establecer exclusivamente las reglas de retiro y seguridad social militar.",
            ],
        },
        {
            "pregunta": "¿Qué exige el servicio de las armas según el Art. 1° Bis?",
            "correcta": "El servicio de las armas exige que el militar lleve el cumplimiento del deber hasta el sacrificio y que anteponga al interés personal, el respeto a la Constitución Política de los Estados Unidos Mexicanos, la soberanía de la Nación, la lealtad a las instituciones y el honor del Ejército y Fuerza Aérea Mexicanos.",
            "opciones": [
                "El servicio de las armas exige únicamente obedecer órdenes administrativas.",
                "El servicio de las armas exige que el militar lleve el cumplimiento del deber hasta el sacrificio y que anteponga al interés personal, el respeto a la Constitución Política de los Estados Unidos Mexicanos, la soberanía de la Nación, la lealtad a las instituciones y el honor del Ejército y Fuerza Aérea Mexicanos.",
                "El servicio de las armas permite anteponer el interés personal cuando no exista orden directa.",
            ],
        },
        {
            "pregunta": "¿Qué debe observar el militar conforme al Art. 2°?",
            "correcta": "El militar debe observar buen comportamiento, para que el pueblo deposite su confianza en el Ejército y Fuerza Aérea y los considere como la salvaguarda de sus derechos.",
            "opciones": [
                "El militar debe observar buen comportamiento, para que el pueblo deposite su confianza en el Ejército y Fuerza Aérea y los considere como la salvaguarda de sus derechos.",
                "El militar debe actuar solo conforme a sus intereses personales.",
                "El militar debe evitar relacionarse con la sociedad civil en todo momento.",
            ],
        },
    ]

    if "disciplina_respuestas" not in st.session_state:
        st.session_state.disciplina_respuestas = {}

    correctas = 0

    for i, p in enumerate(preguntas):
        key_respuesta = f"{usuario}_{seccion_id}_respuesta_{i}"
        key_confirmada = f"{usuario}_{seccion_id}_confirmada_{i}"

        st.markdown("---")
        st.markdown(f"### {i + 1}. {p['pregunta']}")

        ya_confirmada = st.session_state.disciplina_respuestas.get(key_confirmada, False)

        respuesta = st.radio(
            "Elige una opción:",
            p["opciones"],
            key=key_respuesta,
            disabled=ya_confirmada,
            index=None
        )

        if not ya_confirmada:
            if st.button("Confirmar respuesta", key=f"btn_{usuario}_{i}"):
                if respuesta is None:
                    st.warning("Selecciona una respuesta primero.")
                else:
                    st.session_state.disciplina_respuestas[key_confirmada] = True
                    st.rerun()
        else:
            respuesta_guardada = st.session_state.get(key_respuesta)

            if respuesta_guardada == p["correcta"]:
                st.success("✅ Correcto")
                correctas += 1
            else:
                st.error("❌ Incorrecto")

    total = len(preguntas)
    porcentaje = int((correctas / total) * 100)

    st.markdown("---")
    st.write(f"Resultado actual: **{correctas}/{total}**")
    st.progress(porcentaje / 100)

    color, mensaje = obtener_color_dominio(porcentaje)

    st.markdown(f"### Tu dominio actual: {color}")
    st.write(mensaje)

    if st.button("📊 Finalizar sección"):
        if porcentaje >= 70:
            aprobado = True
            st.success("✅ Sección aprobada. Puedes avanzar al siguiente nivel.")
        else:
            aprobado = False
            st.warning("❌ No aprobaste. Te recomiendo repetir esta sección.")

        if usuario not in progreso:
            progreso[usuario] = {}

        progreso[usuario][seccion_id] = {
            "aprobado": aprobado,
            "puntaje": correctas,
            "total": total,
            "porcentaje": porcentaje,
            "color": color,
            "mensaje": mensaje,
            "dificultad": dificultad
        }

        guardar_progreso(progreso)
        st.success("💾 Progreso guardado.")

    if st.button("🔄 Reiniciar intento"):
        for i in range(total):
            st.session_state.disciplina_respuestas.pop(
                f"{usuario}_{seccion_id}_confirmada_{i}", None
            )
            st.session_state.pop(
                f"{usuario}_{seccion_id}_respuesta_{i}", None
            )
        st.rerun()
