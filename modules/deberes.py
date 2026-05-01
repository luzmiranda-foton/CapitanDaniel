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
    st.title("Reglamento General de Deberes Militares")

    usuario = st.session_state.get("usuario")

    if not usuario:
        st.warning("⚠️ Primero escribe tu nombre en la página principal.")
        st.stop()

    seccion_id = "rgdm_parte1"
    dificultad = "🟢 Fácil"

    progreso = cargar_progreso()

    
    st.info(f"👤 Usuario: **{usuario}**")
    st.info(f"Dificultad del tema: {dificultad}")

    if usuario in progreso and seccion_id in progreso[usuario]:
        datos = progreso[usuario][seccion_id]
        st.success(
            f"Progreso guardado: {datos['color']} — "
            f"{datos['porcentaje']}% — {datos['mensaje']}"
        )

    preguntas = [

        {
            "tipo": "radio",
            "pregunta": "1. ¿Qué se entiende por deber militar según el Reglamento General de Deberes Militares?",
            "correcta": "Se entiende por deber, el conjunto de las obligaciones que a un militar impone su situación dentro del Ejército.",
            "opciones": [
                "Se entiende por deber, el conjunto de las obligaciones que a un militar impone su situación dentro del Ejército.",
                "Es únicamente obedecer órdenes sin cuestionar.",
                "Es solo cumplir horarios y guardias."
            ]
        },

        {
            "tipo": "radio",
            "pregunta": "2. ¿Cuál es la definición de disciplina según el Reglamento?",
            "correcta": "La disciplina es la norma a que los militares deben sujetar su conducta.",
            "opciones": [
                "La disciplina es la norma a que los militares deben sujetar su conducta.",
                "La disciplina es castigo constante.",
                "La disciplina es obedecer solo en campaña."
            ]
        },

        {
            "tipo": "radio",
            "pregunta": "3. ¿Qué exige el servicio de las armas según el epígrafe del Reglamento?",
            "correcta": "Que el militar lleve el cumplimiento del deber hasta el sacrificio.",
            "opciones": [
                "Que el militar lleve el cumplimiento del deber hasta el sacrificio.",
                "Que el militar obtenga beneficios personales.",
                "Que el militar evite toda responsabilidad."
            ]
        },

        {
            "tipo": "multiple",
            "pregunta": "4. Selecciona lo estrictamente prohibido al superior según el Art. 1°.",
            "correctas": [
                "Todo rigor innecesario",
                "Todo castigo no determinado por leyes o reglamentos",
                "Toda palabra ofensiva",
                "Todo ademán ofensivo"
            ],
            "opciones": [
                "Todo rigor innecesario",
                "Todo castigo no determinado por leyes o reglamentos",
                "Toda palabra ofensiva",
                "Todo ademán ofensivo",
                "Corregir faltas legales",
                "Dar instrucciones del servicio"
            ]
        },

        {
            "tipo": "radio",
            "pregunta": "5. ¿Cuál es el principio vital de la disciplina según el Art. 2°?",
            "correcta": "El deber de obediencia.",
            "opciones": [
                "El deber de obediencia.",
                "El castigo físico.",
                "La antigüedad."
            ]
        },

        {
            "tipo": "radio",
            "pregunta": "6. ¿Cómo deben cumplirse las órdenes según el Art. 3°?",
            "correcta": "Con exactitud e inteligencia, sin demoras ni murmuraciones.",
            "opciones": [
                "Con exactitud e inteligencia, sin demoras ni murmuraciones.",
                "Solo si convienen al subordinado.",
                "Con demora si no urgen."
            ]
        },

        {
            "tipo": "multiple",
            "pregunta": "7. ¿Qué órdenes están prohibidas según el Art. 4°?",
            "correctas": [
                "Las contrarias a las leyes y reglamentos",
                "Las que lastimen la dignidad de inferiores",
                "Las que constituyan delito"
            ],
            "opciones": [
                "Las contrarias a las leyes y reglamentos",
                "Las que lastimen la dignidad de inferiores",
                "Las que constituyan delito",
                "Las órdenes urgentes",
                "Las órdenes escritas"
            ]
        },

        {
            "tipo": "radio",
            "pregunta": "8. ¿Qué debe mantenerse rigurosamente según el Art. 5°?",
            "correcta": "La subordinación entre grado y grado de la jerarquía militar.",
            "opciones": [
                "La subordinación entre grado y grado de la jerarquía militar.",
                "La rivalidad entre grados.",
                "La competencia entre unidades."
            ]
        },

        {
            "tipo": "radio",
            "pregunta": "9. ¿Qué deben conocer los militares según el Art. 10?",
            "correcta": "Con minuciosidad las leyes militares y reglamentos relacionados con su situación.",
            "opciones": [
                "Con minuciosidad las leyes militares y reglamentos relacionados con su situación.",
                "Solo reglamentos internos de cocina.",
                "Únicamente órdenes verbales."
            ]
        },

        {
            "tipo": "radio",
            "pregunta": "10. ¿Qué se prohíbe según el Art. 11?",
            "correcta": "Toda conversación que manifieste tibieza en el servicio.",
            "opciones": [
                "Toda conversación que manifieste tibieza en el servicio.",
                "Hablar con superiores.",
                "Pedir instrucciones."
            ]
        },

        {
            "tipo": "radio",
            "pregunta": "11. ¿Cómo hará sus solicitudes el militar según el Art. 13?",
            "correcta": "Por los conductos regulares comenzando por su inmediato superior.",
            "opciones": [
                "Por los conductos regulares comenzando por su inmediato superior.",
                "Saltando toda jerarquía.",
                "Solo por redes sociales."
            ]
        },

        {
            "tipo": "multiple",
            "pregunta": "12. Según el Art. 19, al portar uniforme en vía pública deberán:",
            "correctas": [
                "Presentarse perfectamente aseados",
                "Usar cabello corto",
                "Mantener la cabeza erguida"
            ],
            "opciones": [
                "Presentarse perfectamente aseados",
                "Usar cabello corto",
                "Mantener la cabeza erguida",
                "Llevar manos en bolsillos",
                "Ir desabotonados"
            ]
        },

        {
            "tipo": "radio",
            "pregunta": "13. ¿Qué lugares no deben frecuentar según el Art. 21?",
            "correcta": "Cantinas, garitos y sitios de prostitución.",
            "opciones": [
                "Cantinas, garitos y sitios de prostitución.",
                "Bibliotecas militares.",
                "Campos de entrenamiento."
            ]
        },

        {
            "tipo": "radio",
            "pregunta": "14. ¿Qué obliga el Art. 22 respecto a la preparación?",
            "correcta": "Estudiar constantemente para desempeñar con eficiencia la misión.",
            "opciones": [
                "Estudiar constantemente para desempeñar con eficiencia la misión.",
                "Solo estudiar en ascensos.",
                "No estudiar después del grado inicial."
            ]
        },

        {
            "tipo": "radio",
            "pregunta": "15. ¿Qué prohíbe el Art. 36 respecto a elecciones?",
            "correcta": "Hacer presión moral o material para inclinar la opinión pública.",
            "opciones": [
                "Hacer presión moral o material para inclinar la opinión pública.",
                "Votar libremente.",
                "Actualizar credencial."
            ]
        }

    ]

    if "rgdm_respuestas" not in st.session_state:
        st.session_state.rgdm_respuestas = {}

    correctas = 0

    for i, p in enumerate(preguntas):

        key_respuesta = f"{usuario}_{seccion_id}_respuesta_{i}"
        key_confirmada = f"{usuario}_{seccion_id}_confirmada_{i}"

        st.markdown("---")
        st.markdown(f"### {p['pregunta']}")

        ya_confirmada = st.session_state.rgdm_respuestas.get(
            key_confirmada, False
        )

        if p["tipo"] == "radio":

            respuesta = st.radio(
                "Elige una opción:",
                p["opciones"],
                key=key_respuesta,
                disabled=ya_confirmada,
                index=None
            )

        else:

            respuesta = []
            st.write("Selecciona una o varias respuestas:")

            for j, opcion in enumerate(p["opciones"]):

                key_check = f"{usuario}_{seccion_id}_{i}_{j}"

                marcado = st.checkbox(
                    opcion,
                    key=key_check,
                    disabled=ya_confirmada
                )

                if marcado:
                    respuesta.append(opcion)

        if not ya_confirmada:

            if st.button(
                "Confirmar respuesta",
                key=f"btn_{usuario}_{i}"
            ):

                if len(respuesta) == 0 if p["tipo"] == "multiple" else respuesta is None:
                    st.warning("Selecciona respuesta primero.")
                else:
                    st.session_state.rgdm_respuestas[key_respuesta] = respuesta
                    st.session_state.rgdm_respuestas[key_confirmada] = True
                    st.rerun()

        else:

            respuesta_guardada = st.session_state.rgdm_respuestas.get(
                key_respuesta
            )

            if p["tipo"] == "radio":

                if respuesta_guardada == p["correcta"]:
                    st.success("✅ Correcto")
                    correctas += 1
                else:
                    st.error("❌ Incorrecto")
                    st.write(f"Respuesta correcta: **{p['correcta']}**")

            else:

                if set(respuesta_guardada) == set(p["correctas"]):
                    st.success("✅ Correcto")
                    correctas += 1
                else:
                    st.error("❌ Incorrecto")
                    st.write("Respuestas correctas:")
                    for x in p["correctas"]:
                        st.write(f"- {x}")

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
            st.success("✅ Sección aprobada.")
        else:
            st.warning("❌ No aprobaste.")

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

        for i, p in enumerate(preguntas):

            st.session_state.rgdm_respuestas.pop(
                f"{usuario}_{seccion_id}_confirmada_{i}",
                None
            )

            st.session_state.rgdm_respuestas.pop(
                f"{usuario}_{seccion_id}_respuesta_{i}",
                None
            )

            for j in range(len(p["opciones"])):
                st.session_state.pop(
                    f"{usuario}_{seccion_id}_{i}_{j}",
                    None
                )

        st.rerun()
