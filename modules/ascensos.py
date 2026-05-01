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
    st.title("Ley de Ascensos y Recompensas del Ejército y Fuerza Aérea Mexicanos")

    usuario = st.session_state.get("usuario")

    if not usuario:
        st.warning("⚠️ Primero escribe tu nombre en la página principal.")
        st.stop()

    seccion_id = "ascensos_parte1"
    dificultad = "🟠 Medio"

    progreso = cargar_progreso()

    st.markdown("## Primera parte")
    st.info(f"👤 Usuario: **{usuario}**")
    st.info(f"Dificultad del tema: **{dificultad}**")

    if usuario in progreso and seccion_id in progreso[usuario]:
        datos = progreso[usuario][seccion_id]
        st.success(
            f"Progreso guardado: {datos['color']} — "
            f"{datos['porcentaje']}% — {datos['mensaje']}"
        )

    preguntas = [
        {
            "tipo": "radio",
            "pregunta": "1. ¿Qué regula la Ley de Ascensos y Recompensas? (Art. 1°)",
            "correcta": "Regula los ascensos y las recompensas de los militares pertenecientes al Ejército y Fuerza Aérea Mexicanos.",
            "opciones": [
                "Regula los ascensos y las recompensas de los militares pertenecientes al Ejército y Fuerza Aérea Mexicanos.",
                "Regula únicamente las pensiones militares.",
                "Regula solo la disciplina militar.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "2. ¿A quién corresponde la aplicación de la Ley de Ascensos y Recompensas? (Art. 1°)",
            "correcta": "Al Presidente de los Estados Unidos Mexicanos y a la Secretaría de la Defensa Nacional.",
            "opciones": [
                "Al Presidente de los Estados Unidos Mexicanos y a la Secretaría de la Defensa Nacional.",
                "Únicamente a los comandantes de unidad.",
                "Al Congreso de la Unión exclusivamente.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "3. ¿Qué se entiende por Ascenso según el Art. 2° fracción VIII?",
            "correcta": "Ascenso es el acto de mando mediante el cual es conferido al militar un grado superior en el orden jerárquico dentro de la escala que fija la Ley Orgánica.",
            "opciones": [
                "Ascenso es el acto de mando mediante el cual es conferido al militar un grado superior en el orden jerárquico dentro de la escala que fija la Ley Orgánica.",
                "Ascenso es una recompensa económica temporal.",
                "Ascenso es una licencia otorgada por buen comportamiento.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "4. ¿Qué se entiende por Recompensas según el Art. 2° fracción IX?",
            "correcta": "Son las condecoraciones, menciones honoríficas, distinciones y citaciones que se otorgan para premiar heroísmo, capacidad profesional, servicios a la Patria o hechos meritorios.",
            "opciones": [
                "Son las condecoraciones, menciones honoríficas, distinciones y citaciones que se otorgan para premiar heroísmo, capacidad profesional, servicios a la Patria o hechos meritorios.",
                "Son únicamente aumentos de sueldo.",
                "Son castigos administrativos por faltas menores.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "5. ¿Quiénes son militares según el Art. 2° fracción XII?",
            "correcta": "Son las mujeres y los hombres que legalmente pertenecen al Ejército y Fuerza Aérea, con un grado de la escala jerárquica.",
            "opciones": [
                "Son las mujeres y los hombres que legalmente pertenecen al Ejército y Fuerza Aérea, con un grado de la escala jerárquica.",
                "Son únicamente los generales en activo.",
                "Son solo quienes reciben una recompensa.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "6. ¿De quién es facultad exclusiva el ascenso de Generales, Jefes y Oficiales? (Art. 3°)",
            "correcta": "Del Presidente de la República.",
            "opciones": [
                "Del Presidente de la República.",
                "De los soldados de mayor antigüedad.",
                "De cualquier comandante de sección.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "7. ¿Quién puede determinar el ascenso de Oficiales previo acuerdo del Presidente? (Art. 3°)",
            "correcta": "El Secretario.",
            "opciones": [
                "El Secretario.",
                "El Cabo de mayor antigüedad.",
                "El Congreso local.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "8. ¿De quién es facultad ascender a los militares de clase de Tropa? (Art. 4°)",
            "correcta": "Del Secretario.",
            "opciones": [
                "Del Secretario.",
                "Del Presidente municipal.",
                "De cualquier civil autorizado.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "9. ¿Qué ascensos pueden conferir los Comandantes de Unidades o Jefes de Dependencias? (Art. 4°)",
            "correcta": "Ascensos de Soldados a Cabos, comunicados hasta que sean aprobados por la Secretaría.",
            "opciones": [
                "Ascensos de Soldados a Cabos, comunicados hasta que sean aprobados por la Secretaría.",
                "Ascensos de Cabos a Generales.",
                "Ascensos de Oficiales a Jefes sin aprobación.",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "10. Selecciona los tipos de ascensos que pueden otorgarse. (Art. 6°)",
            "correctas": [
                "En tiempo de paz",
                "En tiempo de guerra",
            ],
            "opciones": [
                "En tiempo de paz",
                "En tiempo de guerra",
                "En tiempo de vacaciones",
                "En tiempo electoral",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "11. ¿Cuál es la finalidad de los ascensos en tiempo de paz? (Art. 7°)",
            "correcta": "Cubrir las vacantes en los cuadros del Ejército o Fuerza Aérea con militares aptos y preparados para el grado inmediato superior.",
            "opciones": [
                "Cubrir las vacantes en los cuadros del Ejército o Fuerza Aérea con militares aptos y preparados para el grado inmediato superior.",
                "Otorgar descansos prolongados.",
                "Sustituir las recompensas militares.",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "12. Selecciona circunstancias que se consideran para conferir ascensos. (Art. 8°)",
            "correctas": [
                "Tiempo de servicios",
                "Antigüedad en el grado",
                "Buena conducta militar y civil",
                "Buena salud",
                "Aptitud profesional",
                "Capacidad física",
            ],
            "opciones": [
                "Tiempo de servicios",
                "Antigüedad en el grado",
                "Buena conducta militar y civil",
                "Buena salud",
                "Aptitud profesional",
                "Capacidad física",
                "Preferencia personal del evaluador",
                "Popularidad entre compañeros",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "13. ¿Qué curso o preparación se considera para conferir ascensos? (Art. 8°)",
            "correcta": "La aprobación en los cursos de formación, capacitación, perfeccionamiento o superiores y demás que establezca la normativa vigente en educación militar.",
            "opciones": [
                "La aprobación en los cursos de formación, capacitación, perfeccionamiento o superiores y demás que establezca la normativa vigente en educación militar.",
                "Solamente cursos civiles no relacionados.",
                "Únicamente experiencia fuera del servicio.",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "14. Selecciona requisitos para que un Soldado ascienda a Cabo. (Art. 11)",
            "correctas": [
                "Haber servido cuando menos un año en el Ejército o Fuerza Aérea",
                "Satisfacer los requisitos de buena conducta militar y civil",
                "Satisfacer el requisito de buena salud",
                "Satisfacer el requisito de aptitud profesional",
                "Satisfacer el requisito de capacidad física",
            ],
            "opciones": [
                "Haber servido cuando menos un año en el Ejército o Fuerza Aérea",
                "Satisfacer los requisitos de buena conducta militar y civil",
                "Satisfacer el requisito de buena salud",
                "Satisfacer el requisito de aptitud profesional",
                "Satisfacer el requisito de capacidad física",
                "Haber servido diez años obligatoriamente",
                "Contar con recomendación civil obligatoria",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "15. Selecciona requisitos para ascender de Cabo a Sargento Segundo y de Sargento Segundo a Sargento Primero. (Art. 12)",
            "correctas": [
                "Tener antigüedad mínima de un año en el grado",
                "Haber servido durante esa antigüedad encuadrado en unidades de su arma o en funciones militares propias de su especialidad",
                "Aprobar el curso respectivo en la Escuela de Clases que corresponda",
                "Satisfacer los requisitos de buena conducta militar y civil, buena salud, aptitud profesional y capacidad física",
            ],
            "opciones": [
                "Tener antigüedad mínima de un año en el grado",
                "Haber servido durante esa antigüedad encuadrado en unidades de su arma o en funciones militares propias de su especialidad",
                "Aprobar el curso respectivo en la Escuela de Clases que corresponda",
                "Satisfacer los requisitos de buena conducta militar y civil, buena salud, aptitud profesional y capacidad física",
                "Haber sido elegido por votación popular",
                "Recibir una recompensa económica previa",
            ],
        },
    ]

    if "ascensos_respuestas" not in st.session_state:
        st.session_state.ascensos_respuestas = {}

    correctas = 0

    for i, p in enumerate(preguntas):
        key_respuesta = f"{usuario}_{seccion_id}_respuesta_{i}"
        key_confirmada = f"{usuario}_{seccion_id}_confirmada_{i}"

        st.markdown("---")
        st.markdown(f"### {p['pregunta']}")

        ya_confirmada = st.session_state.ascensos_respuestas.get(
            key_confirmada, False
        )

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
                key_check = f"{usuario}_{seccion_id}_pregunta_{i}_opcion_{j}"

                marcado = st.checkbox(
                    opcion,
                    key=key_check,
                    disabled=ya_confirmada,
                )

                if marcado:
                    respuesta.append(opcion)

        if not ya_confirmada:
            if st.button(
                "Confirmar respuesta",
                key=f"btn_{usuario}_{seccion_id}_{i}",
            ):
                if p["tipo"] == "radio" and respuesta is None:
                    st.warning("Selecciona una respuesta primero.")
                elif p["tipo"] == "multiple" and len(respuesta) == 0:
                    st.warning("Selecciona al menos una respuesta.")
                else:
                    st.session_state.ascensos_respuestas[key_respuesta] = respuesta
                    st.session_state.ascensos_respuestas[key_confirmada] = True
                    st.rerun()

        else:
            respuesta_guardada = st.session_state.ascensos_respuestas.get(
                key_respuesta
            )

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
        for i, p in enumerate(preguntas):
            st.session_state.ascensos_respuestas.pop(
                f"{usuario}_{seccion_id}_confirmada_{i}",
                None,
            )
            st.session_state.ascensos_respuestas.pop(
                f"{usuario}_{seccion_id}_respuesta_{i}",
                None,
            )

            if p["tipo"] == "radio":
                st.session_state.pop(
                    f"{usuario}_{seccion_id}_respuesta_{i}",
                    None,
                )

            elif p["tipo"] == "multiple":
                for j in range(len(p["opciones"])):
                    st.session_state.pop(
                        f"{usuario}_{seccion_id}_pregunta_{i}_opcion_{j}",
                        None,
                    )

        st.rerun()
