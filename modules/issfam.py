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
    st.title("🏥 Ley del Instituto de Seguridad Social para las Fuerzas Armadas Mexicanas")

    usuario = st.session_state.get("usuario")

    if not usuario:
        st.warning("⚠️ Primero escribe tu nombre en la página principal.")
        st.stop()

    seccion_id = "issfam_parte1"
    dificultad = "🟠 Medio"

    progreso = cargar_progreso()

    st.markdown("## ISSFAM - Primera parte")
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
            "tipo": "multiple",
            "pregunta": "1. Selecciona prestaciones que se otorgan con arreglo a la Ley del ISSFAM. (Art. 18)",
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
            "pregunta": "2. ¿Quiénes tramitarán la afiliación del personal ante el Instituto? (Art. 19)",
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
            "pregunta": "4. ¿Qué es el Haber de Retiro según el Art. 21?",
            "correcta": "Haber de retiro es la prestación económica vitalicia a que tienen derecho los militares retirados en los casos y condiciones que fija esta Ley.",
            "opciones": [
                "Haber de retiro es una ayuda temporal por enfermedad.",
                "Haber de retiro es la prestación económica vitalicia a que tienen derecho los militares retirados en los casos y condiciones que fija esta Ley.",
                "Haber de retiro es un préstamo hipotecario.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "5. ¿Qué es la Pensión conforme al Art. 21?",
            "correcta": "Pensión es la prestación económica vitalicia a que tienen derecho los familiares de los militares en los casos y condiciones que fije esta Ley.",
            "opciones": [
                "Pensión es la prestación económica vitalicia a que tienen derecho los familiares de los militares en los casos y condiciones que fije esta Ley.",
                "Pensión es una beca escolar.",
                "Pensión es una compensación en una sola exhibición para el militar activo.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "6. ¿Qué es la Compensación conforme al Art. 21?",
            "correcta": "Compensación es la prestación económica a que tienen derecho los militares y sus familiares, en una sola exhibición, en los términos y condiciones que fije esta Ley.",
            "opciones": [
                "Compensación es una prestación médica permanente.",
                "Compensación es la prestación económica a que tienen derecho los militares y sus familiares, en una sola exhibición, en los términos y condiciones que fije esta Ley.",
                "Compensación es una vivienda otorgada gratuitamente.",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "7. Selecciona causas de retiro según el Art. 24 de la Ley del ISSFAM.",
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
            "pregunta": "8. ¿Cuál es la edad límite de los individuos de tropa para permanecer en activo? (Art. 25)",
            "correcta": "50 años.",
            "opciones": [
                "45 años.",
                "50 años.",
                "60 años.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "9. ¿Quedan exentos de impuestos los haberes de retiro, compensaciones y pensiones? (Art. 32)",
            "correcta": "Los haberes de retiro, compensaciones y pensiones quedan exentos de todo impuesto.",
            "opciones": [
                "Los haberes de retiro, compensaciones y pensiones quedan exentos de todo impuesto.",
                "Los haberes de retiro, compensaciones y pensiones pagan doble impuesto.",
                "Solo las pensiones quedan exentas, pero no los haberes de retiro.",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "10. Selecciona quiénes tienen derecho al 100% del haber de la jerarquía reconocida para efectos de retiro. (Art. 33)",
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
            "pregunta": "11. ¿Qué porcentaje corresponde al militar con 20 años de servicios para efectos de retiro? (Art. 35)",
            "correcta": "60%",
            "opciones": [
                "50%",
                "60%",
                "75%",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "12. ¿Qué ocurre con el porcentaje del haber de retiro después de 20 años de servicios? (Art. 35)",
            "correcta": "Aumenta progresivamente por cada año adicional de servicio.",
            "opciones": [
                "Aumenta progresivamente por cada año adicional de servicio.",
                "Disminuye por cada año adicional de servicio.",
                "Permanece siempre en 60%.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "13. ¿Cuál es el porcentaje máximo que puede alcanzarse por años de servicio? (Art. 35)",
            "correcta": "100%",
            "opciones": [
                "80%",
                "90%",
                "100%",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "14. ¿Quién cubre el pago de haberes de retiro, compensaciones y pensiones? (Art. 40)",
            "correcta": "El Instituto de Seguridad Social para las Fuerzas Armadas Mexicanas.",
            "opciones": [
                "El Instituto de Seguridad Social para las Fuerzas Armadas Mexicanas.",
                "Cada unidad militar.",
                "Únicamente la Secretaría de Hacienda.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "15. ¿Qué naturaleza tienen las prestaciones otorgadas por esta Ley?",
            "correcta": "Son prestaciones de seguridad social.",
            "opciones": [
                "Son prestaciones de seguridad social.",
                "Son premios militares discrecionales.",
                "Son sanciones administrativas.",
            ],
        },
    ]

    respuestas_usuario = {}

    with st.form("form_issfam"):
        for i, p in enumerate(preguntas):
            st.markdown(f"### {p['pregunta']}")

            if p["tipo"] == "radio":
                respuestas_usuario[i] = st.radio(
                    "Elige una respuesta:",
                    p["opciones"],
                    key=f"issfam_radio_{i}",
                )

            elif p["tipo"] == "multiple":
                respuestas_usuario[i] = st.multiselect(
                    "Selecciona una o varias respuestas:",
                    p["opciones"],
                    key=f"issfam_multi_{i}",
                )

            st.divider()

        enviar = st.form_submit_button("✅ Revisar respuestas")

    if enviar:
        aciertos = 0
        total = len(preguntas)

        st.markdown("## Resultados")

        for i, p in enumerate(preguntas):
            respuesta = respuestas_usuario[i]

            if p["tipo"] == "radio":
                if respuesta == p["correcta"]:
                    aciertos += 1
                    st.success(f"✅ Pregunta {i + 1}: Correcta")
                else:
                    st.error(f"❌ Pregunta {i + 1}: Incorrecta")
                    st.write(f"Respuesta correcta: **{p['correcta']}**")

            elif p["tipo"] == "multiple":
                if set(respuesta) == set(p["correctas"]):
                    aciertos += 1
                    st.success(f"✅ Pregunta {i + 1}: Correcta")
                else:
                    st.error(f"❌ Pregunta {i + 1}: Incorrecta")
                    st.write("Respuestas correctas:")
                    for correcta in p["correctas"]:
                        st.write(f"- {correcta}")

        porcentaje = round((aciertos / total) * 100)
        color, mensaje = obtener_color_dominio(porcentaje)

        st.markdown("## 📊 Dominio del tema")
        st.metric("Resultado", f"{porcentaje}%")
        st.write(f"Nivel: **{color}**")
        st.write(f"Comentario: **{mensaje}**")

        if usuario not in progreso:
            progreso[usuario] = {}

        progreso[usuario][seccion_id] = {
            "aciertos": aciertos,
            "total": total,
            "porcentaje": porcentaje,
            "color": color,
            "mensaje": mensaje,
            "dificultad": dificultad,
        }

        guardar_progreso(progreso)

        st.success("✅ Progreso guardado correctamente.")
