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

    seccion_id = "Disciplina del ejercito y fuerza aerea"
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
            "pregunta": "Lee el siguiente texto:\n\nLa presente Ley tiene por objeto preservar la disciplina militar como principio de orden y obediencia que regula la conducta de los individuos que integran el Ejército y Fuerza Aérea Mexicanos. Sus disposiciones son de observancia obligatoria para todos los militares que integran el Ejército y Fuerza Aérea Mexicanos de conformidad con su Ley Orgánica.\n\n¿A qué ley o artículo pertenece?",
            "correcta": "Artículo 1° de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
            "opciones": [
                "Artículo 1° de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
                "Artículo 3° de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
                "Artículo 14 de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
            ],
        },
        {
            "pregunta": "Lee el siguiente texto:\n\nEl servicio de las armas exige que el militar lleve el cumplimiento del deber hasta el sacrificio y que anteponga al interés personal, el respeto a la Constitución Política de los Estados Unidos Mexicanos, la soberanía de la Nación, la lealtad a las instituciones y el honor del Ejército y Fuerza Aérea Mexicanos.\n\n¿A qué ley o artículo pertenece?",
            "correcta": "Artículo 1° Bis de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
            "opciones": [
                "Artículo 1° Bis de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
                "Artículo 5° de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
                "Artículo 17 de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
            ],
        },
        {
            "pregunta": "¿Qué debe observar el militar conforme al Art. 2° de la Ley de Disciplina?",
            "correcta": "El militar debe observar buen comportamiento, para que el pueblo deposite su confianza en el Ejército y Fuerza Aérea y los considere como la salvaguarda de sus derechos.",
            "opciones": [
                "El militar debe observar buen comportamiento, para que el pueblo deposite su confianza en el Ejército y Fuerza Aérea y los considere como la salvaguarda de sus derechos.",
                "El militar debe obedecer solamente a sus superiores inmediatos.",
                "El militar debe evitar el contacto con la población civil.",
            ],
        },
        {
            "pregunta": "Lee el siguiente texto:\n\nLa disciplina en el Ejército y Fuerza Aérea es la norma a que los militares deben ajustar su conducta; tiene como bases la obediencia, y un alto concepto del honor, de la justicia y de la moral, y por objeto, el fiel y exacto cumplimiento de los deberes que prescriben las leyes y reglamentos militares.\n\n¿A qué ley o artículo pertenece?",
            "correcta": "Artículo 3° de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
            "opciones": [
                "Artículo 3° de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
                "Artículo 4° de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
                "Artículo 18 de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
            ],
        },
        {
            "pregunta": "¿Cuál es la base fundamental del Ejército y Fuerza Aérea Mexicanos según el Art. 3° Bis?",
            "correcta": "La disciplina es la base fundamental del Ejército y Fuerza Aérea Mexicanos, los cuales existen primordialmente para defender los intereses de la Patria y preservar su vida institucional.",
            "opciones": [
                "La disciplina es la base fundamental del Ejército y Fuerza Aérea Mexicanos, los cuales existen primordialmente para defender los intereses de la Patria y preservar su vida institucional.",
                "La obediencia al mando civil es la base fundamental del Ejército y Fuerza Aérea Mexicanos.",
                "La jerarquía es la base fundamental del Ejército y Fuerza Aérea Mexicanos.",
            ],
        },
        {
            "pregunta": "¿Qué exige la disciplina entre el superior y el subalterno? (Art. 4°)",
            "correcta": "La disciplina exige respeto y consideraciones mutuas entre el superior y el subalterno, la infracción de esta norma de conducta se castigará de conformidad con las leyes y reglamentos militares.",
            "opciones": [
                "La disciplina exige respeto y consideraciones mutuas entre el superior y el subalterno, la infracción de esta norma de conducta se castigará de conformidad con las leyes y reglamentos militares.",
                "La disciplina exige obediencia exclusiva del subalterno hacia el superior.",
                "La disciplina exige trato preferencial únicamente al superior.",
            ],
        },
        {
            "pregunta": "Lee el siguiente texto:\n\nEl militar debe proceder de un modo legal, justo y enérgico en el cumplimiento de sus obligaciones, a fin de obtener la estimación y obediencia de sus subalternos. Es deber del superior educar y dirigir a los individuos que la Nación pone bajo su mando.\n\n¿A qué ley o artículo pertenece?",
            "correcta": "Artículo 5° de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
            "opciones": [
                "Artículo 5° de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
                "Artículo 7° de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
                "Artículo 42 de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
            ],
        },
        {
            "pregunta": "¿Qué facultad tiene el superior en caso de extrema necesidad en actos del servicio? (Art. 6°)",
            "correcta": "En caso de extrema necesidad en actos del servicio, el superior podrá servirse de sus armas o de la fuerza a su mando para obtener obediencia a sus órdenes o mantener la disciplina.",
            "opciones": [
                "En caso de extrema necesidad en actos del servicio, el superior podrá servirse de sus armas o de la fuerza a su mando para obtener obediencia a sus órdenes o mantener la disciplina.",
                "En caso de extrema necesidad en actos del servicio, el superior deberá suspender el mando.",
                "En caso de extrema necesidad en actos del servicio, el superior deberá retirarse del lugar.",
            ],
        },
        {
            "pregunta": "¿De qué es responsable el superior respecto a las tropas que tiene a su mando? (Art. 7°)",
            "correcta": "El superior será responsable del orden en las tropas que tuviere a su mando, así como del cumplimiento de las obligaciones del servicio, sin que pueda disculparse en ningún caso con la omisión y descuido de sus subalternos.",
            "opciones": [
                "El superior será responsable del orden en las tropas que tuviere a su mando, así como del cumplimiento de las obligaciones del servicio, sin que pueda disculparse en ningún caso con la omisión y descuido de sus subalternos.",
                "El superior solo será responsable de sus actos personales.",
                "El superior podrá disculparse con la omisión de sus subalternos.",
            ],
        },
        {
            "pregunta": "¿Qué prohíbe el Art. 14 de la Ley de Disciplina respecto a las órdenes que puede dar el militar?",
            "correcta": "Queda estrictamente prohibido al militar dar órdenes cuya ejecución constituya un delito; el militar que las expida y el subalterno que las cumpla, serán responsables conforme al Código de Justicia Militar.",
            "opciones": [
                "Queda estrictamente prohibido al militar dar órdenes cuya ejecución constituya un delito; el militar que las expida y el subalterno que las cumpla, serán responsables conforme al Código de Justicia Militar.",
                "Queda permitido al militar dar órdenes cuya ejecución constituya falta administrativa.",
                "Solo será responsable el subalterno que las cumpla.",
            ],
        },
        {
            "pregunta": "¿Qué se entiende por actos del servicio según el Art. 15 de la Ley de Disciplina?",
            "correcta": "Debe entenderse por actos del servicio, los prescritos por las leyes, reglamentos y disposiciones de observancia general que dicte la Superioridad.",
            "opciones": [
                "Debe entenderse por actos del servicio, los prescritos por las leyes, reglamentos y disposiciones de observancia general que dicte la Superioridad.",
                "Debe entenderse por actos del servicio únicamente los realizados en combate.",
                "Debe entenderse por actos del servicio solo los ordenados por escrito.",
            ],
        },
        {
            "pregunta": "Lee el siguiente texto:\n\nQueda estrictamente prohibido al militar en servicio activo, inmiscuirse en asuntos políticos, directa o indirectamente, salvo aquel que disfrute de licencia que así se lo permita en términos de lo dispuesto por las leyes; así como pertenecer al estado eclesiástico o desempeñarse como ministro de cualquier culto religioso, sin que por ello pierda los derechos que le otorga la Constitución Política de los Estados Unidos Mexicanos.\n\n¿A qué ley o artículo pertenece?",
            "correcta": "Artículo 17 de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
            "opciones": [
                "Artículo 17 de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
                "Artículo 18 de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
                "Artículo 43 de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
            ],
        },
        {
            "pregunta": "¿Qué obligación tiene el militar respecto al saludo? (Art. 18)",
            "correcta": "El militar está obligado a saludar a sus superiores y a los de su misma jerarquía, conforme se prescriben los reglamentos, así como a corresponder el saludo de sus subalternos.",
            "opciones": [
                "El militar está obligado a saludar a sus superiores y a los de su misma jerarquía, conforme se prescriben los reglamentos, así como a corresponder el saludo de sus subalternos.",
                "El militar está obligado únicamente a saludar a sus superiores inmediatos.",
                "El saludo militar será opcional fuera del servicio.",
            ],
        },
        {
            "pregunta": "Lee el siguiente texto:\n\nEl militar que tenga alguna queja en relación con las disposiciones superiores o las obligaciones que le impone el servicio, podrá acudir ante el superior inmediato para la solución de sus demandas y, en caso de no ser debidamente atendido, podrá llegar por rigurosa escala, hasta el Presidente de la República, si es necesario.\n\n¿A qué ley o artículo pertenece?",
            "correcta": "Artículo 42 de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
            "opciones": [
                "Artículo 42 de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
                "Artículo 14 de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
                "Artículo 7° de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
            ],
        },
        {
            "pregunta": "Lee el siguiente texto:\n\nTodo militar que infrinja la presente Ley, así como algún precepto reglamentario, se hará acreedor a un correctivo disciplinario, de acuerdo con su jerarquía en el Ejército y Fuerza Aérea y, si la magnitud de su falta constituye un delito, quedará sujeto a lo dispuesto por el Código de Justicia Militar.\n\n¿A qué ley o artículo pertenece?",
            "correcta": "Artículo 43 de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
            "opciones": [
                "Artículo 43 de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
                "Artículo 17 de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
                "Artículo 3° de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos",
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

        ya_confirmada = st.session_state.disciplina_respuestas.get(
            key_confirmada, False
        )

        respuesta = st.radio(
            "Elige una opción:",
            p["opciones"],
            key=key_respuesta,
            disabled=ya_confirmada,
            index=None,
        )

        if not ya_confirmada:
            if st.button(
                "Confirmar respuesta",
                key=f"btn_{usuario}_{seccion_id}_{i}",
            ):
                if respuesta is None:
                    st.warning("Selecciona una respuesta primero.")
                else:
                    st.session_state.disciplina_respuestas[key_respuesta] = respuesta
                    st.session_state.disciplina_respuestas[key_confirmada] = True
                    st.rerun()

        else:
            respuesta_guardada = st.session_state.disciplina_respuestas.get(
                key_respuesta
            )

            if respuesta_guardada == p["correcta"]:
                st.success("✅ Correcto")
                correctas += 1
            else:
                st.error("❌ Incorrecto")
                st.write(f"Respuesta correcta: **{p['correcta']}**")

    total = len(preguntas)
    porcentaje = int((correctas / total) * 100)

    st.markdown("---")
    st.write(f"Resultado actual: **{correctas}/{total}**")
    st.progress(porcentaje / 100)

    color, mensaje = obtener_color_dominio(porcentaje)

    st.markdown(f"### Tu dominio actual: {color}")
    st.write(mensaje)

    if st.button("📊 Finalizar sección"):
        aprobado = porcentaje >= 70

        if aprobado:
            st.success("✅ Sección aprobada. Puedes avanzar al siguiente nivel.")
        else:
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
            "dificultad": dificultad,
        }

        guardar_progreso(progreso)
        st.success("Progreso guardado.")

    if st.button("🔄 Reiniciar intento"):
        for i in range(total):
            st.session_state.disciplina_respuestas.pop(
                f"{usuario}_{seccion_id}_confirmada_{i}",
                None,
            )
            st.session_state.disciplina_respuestas.pop(
                f"{usuario}_{seccion_id}_respuesta_{i}",
                None,
            )
            st.session_state.pop(
                f"{usuario}_{seccion_id}_respuesta_{i}",
                None,
            )

        st.rerun()
