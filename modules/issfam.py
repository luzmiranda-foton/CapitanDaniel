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
    st.title("Ley del Instituto de Seguridad Social para las Fuerzas Armadas Mexicanas")

    usuario = st.session_state.get("usuario")

    if not usuario:
        st.warning("Primero escribe tu nombre en la página principal.")
        st.stop()

    seccion_id = "Ley del ISSFAM"
    dificultad = "🟠 Medio"

    progreso = cargar_progreso()

    st.markdown("## ISSFAM - Primera parte")
    st.info(f"👤 Usuario: **{usuario}**")
    st.info(f" Dificultad del tema: **{dificultad}**")

    if usuario in progreso and seccion_id in progreso[usuario]:
        datos = progreso[usuario][seccion_id]
        st.success(
            f"Progreso guardado: {datos['color']} — "
            f"{datos['porcentaje']}% — {datos['mensaje']}"
        )

    preguntas = [
        {
            "tipo": "multiple",
            "pregunta": " Selecciona prestaciones que se otorgan con arreglo a la Ley del ISSFAM. (Art. 18)",
            "correctas": [
                "Haber de retiro",
                "Pensión",
                "Compensación",
                "Pagas de defunción",
                "Ayuda para gastos de sepelio",
                "Fondo de trabajo",
                "Fondo de ahorro",
                "Seguro de vida",
                "Seguro colectivo de retiro",
                "Servicio médico integral",
                "Vivienda",
                "Beca de manutención",
                "Beca escolar",
                "Beca especial",
            ],
            "opciones": [
                "Haber de retiro",
                "Pensión",
                "Compensación",
                "Pagas de defunción",
                "Ayuda para gastos de sepelio",
                "Fondo de trabajo",
                "Fondo de ahorro",
                "Seguro de vida",
                "Seguro colectivo de retiro",
                "Servicio médico integral",
                "Vivienda",
                "Beca de manutención",
                "Beca escolar",
                "Beca especial",
                "Licencia para portar armas",
                "Ascenso automático",
                "Nombramiento político",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": " ¿Quiénes tramitarán la afiliación del personal ante el Instituto? (Art. 19)",
            "correcta": "Las Secretarías de la Defensa Nacional y de Marina.",
            "opciones": [
                "Las Secretarías de la Defensa Nacional y de Marina.",
                "Únicamente la Secretaría de Hacienda.",
                "Los propios militares de forma individual.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "3. ¿Qué es el Retiro según el Art. 21 de la Ley del ISSFAM?",
            "correcta": "Retiro es la facultad que tiene el Estado y que ejerce por conducto de las Secretarías de la Defensa Nacional y de Marina para separar del activo a los militares al ocurrir alguna de las causales previstas en esta Ley.",
            "opciones": [
                "Retiro es una sanción disciplinaria temporal.",
                "Retiro es la facultad que tiene el Estado y que ejerce por conducto de las Secretarías de la Defensa Nacional y de Marina para separar del activo a los militares al ocurrir alguna de las causales previstas en esta Ley.",
                "Retiro es una licencia voluntaria sin prestaciones.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": " ¿Qué es el Haber de Retiro según el Art. 21?",
            "correcta": "Haber de retiro es la prestación económica vitalicia a que tienen derecho los militares retirados en los casos y condiciones que fija esta Ley.",
            "opciones": [
                "Haber de retiro es una ayuda temporal por enfermedad.",
                "Haber de retiro es la prestación económica vitalicia a que tienen derecho los militares retirados en los casos y condiciones que fija esta Ley.",
                "Haber de retiro es un préstamo hipotecario.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": " ¿Qué es la Pensión conforme al Art. 21?",
            "correcta": "Pensión es la prestación económica vitalicia a que tienen derecho los familiares de los militares en los casos y condiciones que fije esta Ley.",
            "opciones": [
                "Pensión es la prestación económica vitalicia a que tienen derecho los familiares de los militares en los casos y condiciones que fije esta Ley.",
                "Pensión es una beca escolar.",
                "Pensión es una compensación en una sola exhibición para el militar activo.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": " ¿Qué es la Compensación conforme al Art. 21?",
            "correcta": "Compensación es la prestación económica a que tienen derecho los militares y sus familiares, en una sola exhibición, en los términos y condiciones que fije esta Ley.",
            "opciones": [
                "Compensación es una prestación médica permanente.",
                "Compensación es la prestación económica a que tienen derecho los militares y sus familiares, en una sola exhibición, en los términos y condiciones que fije esta Ley.",
                "Compensación es una vivienda otorgada gratuitamente.",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": " Selecciona causas de retiro según el Art. 24 de la Ley del ISSFAM.",
            "correctas": [
                "Llegar a la edad límite que fija el artículo 25 de esta Ley",
                "Quedar incapacitado en acción de armas o como consecuencia de las lesiones recibidas en ella",
                "Quedar incapacitado en otros actos del servicio o como consecuencia de ellos",
                "Quedar incapacitado en actos fuera del servicio, conforme a lo establecido en los artículos 174 y 183 de esta Ley",
                "Estar imposibilitado para el desempeño de las obligaciones militares por enfermedad que dure más de seis meses",
                "Solicitarlo después de haber prestado por lo menos veinte años de servicios",
            ],
            "opciones": [
                "Llegar a la edad límite que fija el artículo 25 de esta Ley",
                "Quedar incapacitado en acción de armas o como consecuencia de las lesiones recibidas en ella",
                "Quedar incapacitado en otros actos del servicio o como consecuencia de ellos",
                "Quedar incapacitado en actos fuera del servicio, conforme a lo establecido en los artículos 174 y 183 de esta Ley",
                "Estar imposibilitado para el desempeño de las obligaciones militares por enfermedad que dure más de seis meses",
                "Solicitarlo después de haber prestado por lo menos veinte años de servicios",
                "Cambiar de domicilio particular",
                "Solicitar vacaciones",
                "Reprobar un curso interno",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": " ¿Cuál es la edad límite de los individuos de tropa para permanecer en activo? (Art. 25)",
            "correcta": "50 años.",
            "opciones": ["45 años.", "50 años.", "60 años."],
        },
        {
            "tipo": "radio",
            "pregunta": " ¿Quedan exentos de impuestos los haberes de retiro, compensaciones y pensiones? (Art. 32)",
            "correcta": "Los haberes de retiro, compensaciones y pensiones quedan exentos de todo impuesto.",
            "opciones": [
                "Los haberes de retiro, compensaciones y pensiones quedan exentos de todo impuesto.",
                "Los haberes de retiro, compensaciones y pensiones pagan doble impuesto.",
                "Solo las pensiones quedan exentas, pero no los haberes de retiro.",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": " Selecciona quiénes tienen derecho al 100% del haber de la jerarquía reconocida para efectos de retiro. (Art. 33)",
            "correctas": [
                "Los militares incapacitados en acción de armas o a consecuencia de lesiones recibidas en ella",
                "Los militares incapacitados en otros actos del servicio o como consecuencia de ellos",
            ],
            "opciones": [
                "Los militares incapacitados en acción de armas o a consecuencia de lesiones recibidas en ella",
                "Los militares incapacitados en otros actos del servicio o como consecuencia de ellos",
                "Los militares que soliciten vacaciones",
                "Los militares que cambien de domicilio particular",
                "Los militares que reprueben un curso interno",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": " ¿Qué porcentaje corresponde al militar con 20 años de servicios para efectos de retiro? (Art. 35)",
            "correcta": "60%",
            "opciones": ["50%", "60%", "75%"],
        },
        {
            "tipo": "radio",
            "pregunta": " ¿Qué ocurre con el porcentaje del haber de retiro después de 20 años de servicios? (Art. 35)",
            "correcta": "Aumenta progresivamente por cada año adicional de servicio.",
            "opciones": [
                "Aumenta progresivamente por cada año adicional de servicio.",
                "Disminuye por cada año adicional de servicio.",
                "Permanece siempre en 60%.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": " ¿Cuál es el porcentaje máximo que puede alcanzarse por años de servicio? (Art. 35)",
            "correcta": "100%",
            "opciones": ["80%", "90%", "100%"],
        },
        {
            "tipo": "radio",
            "pregunta": " ¿Quién cubre el pago de haberes de retiro, compensaciones y pensiones? (Art. 40)",
            "correcta": "El Instituto de Seguridad Social para las Fuerzas Armadas Mexicanas.",
            "opciones": [
                "El Instituto de Seguridad Social para las Fuerzas Armadas Mexicanas.",
                "Cada unidad militar.",
                "Únicamente la Secretaría de Hacienda.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": " ¿Qué naturaleza tienen las prestaciones otorgadas por esta Ley?",
            "correcta": "Son prestaciones de seguridad social.",
            "opciones": [
                "Son prestaciones de seguridad social.",
                "Son premios militares discrecionales.",
                "Son sanciones administrativas.",
            ],
        },
    ]

    if "issfam_respuestas" not in st.session_state:
        st.session_state.issfam_respuestas = {}

    correctas = 0

    for i, p in enumerate(preguntas):
        key_respuesta = f"{usuario}_{seccion_id}_respuesta_{i}"
        key_confirmada = f"{usuario}_{seccion_id}_confirmada_{i}"

        st.markdown("---")
        st.markdown(f"### {i + 1}. {p['pregunta']}")

        ya_confirmada = st.session_state.issfam_respuestas.get(key_confirmada, False)

        if p["tipo"] == "radio":
            respuesta = st.radio(
                "Elige una opción:",
                p["opciones"],
                key=key_respuesta,
                disabled=ya_confirmada,
                index=None,
            )

        elif p["tipo"] == "multiple":
            st.write("Selecciona una o varias respuestas:")

            respuesta = []

            for j, opcion in enumerate(p["opciones"]):
                key_checkbox = f"{usuario}_{seccion_id}_pregunta_{i}_opcion_{j}"

                marcada = st.checkbox(
                    opcion,
                    key=key_checkbox,
                    disabled=ya_confirmada,
                )

                if marcada:
                    respuesta.append(opcion)

        if not ya_confirmada:
            if st.button("Confirmar respuesta", key=f"btn_{usuario}_{seccion_id}_{i}"):
                if p["tipo"] == "radio" and respuesta is None:
                    st.warning("Selecciona una respuesta primero.")
                elif p["tipo"] == "multiple" and len(respuesta) == 0:
                    st.warning("Selecciona al menos una respuesta.")
                else:
                    st.session_state.issfam_respuestas[key_respuesta] = respuesta
                    st.session_state.issfam_respuestas[key_confirmada] = True
                    st.rerun()

        else:
            respuesta_guardada = st.session_state.issfam_respuestas.get(key_respuesta)

            if p["tipo"] == "radio":
                if respuesta_guardada == p["correcta"]:
                    st.success("✅ Correcto")
                    correctas += 1
                else:
                    st.error("❌ Incorrecto")
                    st.write(f"Respuesta correcta: **{p['correcta']}**")

            elif p["tipo"] == "multiple":
                if set(respuesta_guardada) == set(p["correctas"]):
                    st.success("✅ Correcto")
                    correctas += 1
                else:
                    st.error("❌ Incorrecto")
                    st.write("Respuestas correctas:")
                    for correcta in p["correctas"]:
                        st.write(f"- {correcta}")

    total = len(preguntas)
    porcentaje = int((correctas / total) * 100)

    st.markdown("---")
    st.write(f"Resultado actual: **{correctas}/{total}**")
    st.progress(porcentaje / 100)

    color, mensaje = obtener_color_dominio(porcentaje)

    st.markdown(f"### Tu dominio actual: {color}")
    st.write(mensaje)

    if st.button("Finalizar sección"):
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
        for i, p in enumerate(preguntas):
            st.session_state.issfam_respuestas.pop(
                f"{usuario}_{seccion_id}_confirmada_{i}", None
            )
            st.session_state.issfam_respuestas.pop(
                f"{usuario}_{seccion_id}_respuesta_{i}", None
            )

            if p["tipo"] == "radio":
                st.session_state.pop(
                    f"{usuario}_{seccion_id}_respuesta_{i}", None
                )

            elif p["tipo"] == "multiple":
                for j in range(len(p["opciones"])):
                    st.session_state.pop(
                        f"{usuario}_{seccion_id}_pregunta_{i}_opcion_{j}", None
                    )

        st.rerun()
