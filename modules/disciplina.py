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
    dificultad = "🟢 Fácil"

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
            "pregunta": "¿Qué exige el servicio de las armas según la Ley de Disciplina?",
            "correcta": "El servicio de las armas exige que el militar lleve el cumplimiento del deber hasta el sacrificio y que anteponga al interés personal, el respeto a la Constitución Política de los Estados Unidos Mexicanos, la soberanía de la Nación, la lealtad a las instituciones y el honor del Ejército y Fuerza Aérea Mexicanos.",
            "opciones": [
                "Buscar beneficios personales.",
                "El servicio de las armas exige que el militar lleve el cumplimiento del deber hasta el sacrificio y que anteponga al interés personal, el respeto a la Constitución Política de los Estados Unidos Mexicanos, la soberanía de la Nación, la lealtad a las instituciones y el honor del Ejército y Fuerza Aérea Mexicanos.",
                "Cumplir solo órdenes administrativas."
            ]
        },
        {
            "pregunta": "Lee el texto: “La disciplina es la base fundamental del Ejército y Fuerza Aérea Mexicanos...” ¿A qué ley pertenece?",
            "correcta": "Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
            "opciones": [
                "Ley Federal de Armas de Fuego y Explosivos",
                "Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
                "Ley del ISSFAM"
            ]
        },
        {
            "pregunta": "¿Qué debe observar el militar conforme al Art. 2°?",
            "correcta": "El militar debe observar buen comportamiento, para que el pueblo deposite su confianza en el Ejército y Fuerza Aérea y los considere como la salvaguarda de sus derechos.",
            "opciones": [
                "El militar debe observar buen comportamiento, para que el pueblo deposite su confianza en el Ejército y Fuerza Aérea y los considere como la salvaguarda de sus derechos.",
                "El militar debe evitar contacto con civiles.",
                "El militar debe actuar solo en campaña."
            ]
        },
        {
            "pregunta": "Lee el texto: “Queda estrictamente prohibido al militar dar órdenes cuya ejecución constituya un delito...” ¿Qué artículo es?",
            "correcta": "Artículo 14",
            "opciones": [
                "Artículo 6",
                "Artículo 14",
                "Artículo 42"
            ]
        },
        {
            "pregunta": "¿Qué exige la disciplina entre superior y subalterno?",
            "correcta": "La disciplina exige respeto y consideraciones mutuas entre el superior y el subalterno, la infracción de esta norma de conducta se castigará de conformidad con las leyes y reglamentos militares.",
            "opciones": [
                "Solo obediencia del subalterno.",
                "La disciplina exige respeto y consideraciones mutuas entre el superior y el subalterno, la infracción de esta norma de conducta se castigará de conformidad con las leyes y reglamentos militares.",
                "No exige trato especial."
            ]
        },
        {
            "pregunta": "Lee el texto: “El militar está obligado a saludar a sus superiores...” ¿Qué tema regula?",
            "correcta": "El saludo militar",
            "opciones": [
                "El saludo militar",
                "Las quejas militares",
                "Los ascensos"
            ]
        },
        {
            "pregunta": "¿De qué es responsable el superior respecto a sus tropas?",
            "correcta": "El superior será responsable del orden en las tropas que tuviere a su mando, así como del cumplimiento de las obligaciones del servicio, sin que pueda disculparse en ningún caso con la omisión y descuido de sus subalternos.",
            "opciones": [
                "Solo responde por sí mismo.",
                "El superior será responsable del orden en las tropas que tuviere a su mando, así como del cumplimiento de las obligaciones del servicio, sin que pueda disculparse en ningún caso con la omisión y descuido de sus subalternos.",
                "Puede culpar siempre a sus subalternos."
            ]
        },
        {
            "pregunta": "Lee el texto: “Debe entenderse por actos del servicio...” ¿Qué artículo es?",
            "correcta": "Artículo 15",
            "opciones": [
                "Artículo 15",
                "Artículo 18",
                "Artículo 43"
            ]
        },
        {
            "pregunta": "¿Cuál es el objeto de esta ley?",
            "correcta": "La presente Ley tiene por objeto preservar la disciplina militar como principio de orden y obediencia que regula la conducta de los individuos que integran el Ejército y Fuerza Aérea Mexicanos. Sus disposiciones son de observancia obligatoria para todos los militares que integran el Ejército y Fuerza Aérea Mexicanos de conformidad con su Ley Orgánica.",
            "opciones": [
                "Regular únicamente ascensos.",
                "La presente Ley tiene por objeto preservar la disciplina militar como principio de orden y obediencia que regula la conducta de los individuos que integran el Ejército y Fuerza Aérea Mexicanos. Sus disposiciones son de observancia obligatoria para todos los militares que integran el Ejército y Fuerza Aérea Mexicanos de conformidad con su Ley Orgánica.",
                "Regular retiros."
            ]
        },
        {
            "pregunta": "Lee el texto: “Queda estrictamente prohibido al militar en servicio activo, inmiscuirse en asuntos políticos...” ¿Qué tema regula?",
            "correcta": "Participación política del militar",
            "opciones": [
                "Participación política del militar",
                "Uso de armas",
                "Ascensos"
            ]
        },
        {
            "pregunta": "¿Qué consecuencias tiene infringir la Ley de Disciplina?",
            "correcta": "Todo militar que infrinja la presente Ley, así como algún precepto reglamentario, se hará acreedor a un correctivo disciplinario, de acuerdo con su jerarquía en el Ejército y Fuerza Aérea y, si la magnitud de su falta constituye un delito, quedará sujeto a lo dispuesto por el Código de Justicia Militar.",
            "opciones": [
                "Solo una advertencia verbal.",
                "Todo militar que infrinja la presente Ley, así como algún precepto reglamentario, se hará acreedor a un correctivo disciplinario, de acuerdo con su jerarquía en el Ejército y Fuerza Aérea y, si la magnitud de su falta constituye un delito, quedará sujeto a lo dispuesto por el Código de Justicia Militar.",
                "Ninguna."
            ]
        },
        {
            "pregunta": "Lee el texto: “podrá acudir ante el superior inmediato... hasta el Presidente de la República...” ¿Qué artículo es?",
            "correcta": "Artículo 42",
            "opciones": [
                "Artículo 18",
                "Artículo 42",
                "Artículo 7"
            ]
        },
        {
            "pregunta": "¿Cómo debe proceder el militar en el cumplimiento de sus obligaciones?",
            "correcta": "El militar debe proceder de un modo legal, justo y enérgico en el cumplimiento de sus obligaciones, a fin de obtener la estimación y obediencia de sus subalternos. Es deber del superior educar y dirigir a los individuos que la Nación pone bajo su mando.",
            "opciones": [
                "Proceder libremente.",
                "El militar debe proceder de un modo legal, justo y enérgico en el cumplimiento de sus obligaciones, a fin de obtener la estimación y obediencia de sus subalternos. Es deber del superior educar y dirigir a los individuos que la Nación pone bajo su mando.",
                "Delegar todo."
            ]
        },
        {
            "pregunta": "Lee el texto: “En caso de extrema necesidad en actos del servicio...” ¿Qué artículo es?",
            "correcta": "Artículo 6",
            "opciones": [
                "Artículo 6",
                "Artículo 14",
                "Artículo 43"
            ]
        },
        {
            "pregunta": "¿En qué consiste la disciplina en el Ejército y Fuerza Aérea?",
            "correcta": "La disciplina en el Ejército y Fuerza Aérea es la norma a que los militares deben ajustar su conducta; tiene como bases la obediencia, y un alto concepto del honor, de la justicia y de la moral, y por objeto, el fiel y exacto cumplimiento de los deberes que prescriben las leyes y reglamentos militares.",
            "opciones": [
                "Es opcional.",
                "Solo aplica en guerra.",
                "La disciplina en el Ejército y Fuerza Aérea es la norma a que los militares deben ajustar su conducta; tiene como bases la obediencia, y un alto concepto del honor, de la justicia y de la moral, y por objeto, el fiel y exacto cumplimiento de los deberes que prescriben las leyes y reglamentos militares."
            ]
        }
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
        st.success("Progreso guardado.")

    if st.button("🔄 Reiniciar intento"):
        for i in range(total):
            st.session_state.disciplina_respuestas.pop(
                f"{usuario}_{seccion_id}_confirmada_{i}", None
            )
            st.session_state.pop(
                f"{usuario}_{seccion_id}_respuesta_{i}", None
            )
        st.rerun()
