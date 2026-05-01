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
    st.title("⚖️ Código de Justicia Militar")

    usuario = st.session_state.get("usuario")

    if not usuario:
        st.warning("⚠️ Primero escribe tu nombre en la página principal.")
        st.stop()

    seccion_id = "justicia_militar_parte1"
    dificultad = "🟠 Medio "

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
            "pregunta": "1. ¿Qué responsabilidad produce todo delito del orden militar? (Art. 99)",
            "correcta": "Produce responsabilidad criminal y sujeta a una pena al que lo comete.",
            "opciones": [
                "Produce responsabilidad criminal y sujeta a una pena al que lo comete.",
                "Produce únicamente una llamada de atención.",
                "No produce responsabilidad si fue por imprudencia.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "2. ¿Qué debe hacer el militar que tenga noticia de un delito de competencia de tribunales militares? (Art. 100)",
            "correcta": "Ponerlo inmediatamente en conocimiento del Ministerio Público por los conductos debidos.",
            "opciones": [
                "Ponerlo inmediatamente en conocimiento del Ministerio Público por los conductos debidos.",
                "Esperar a que otro militar lo denuncie.",
                "Resolverlo personalmente sin avisar.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "3. ¿Cuándo no es punible la infracción del Art. 100?",
            "correcta": "Cuando el delincuente esté ligado con el militar por ciertos vínculos de parentesco.",
            "opciones": [
                "Cuando el delincuente esté ligado con el militar por ciertos vínculos de parentesco.",
                "Cuando el delito sea grave.",
                "Cuando el militar esté de descanso.",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "4. Selecciona cómo pueden ser los delitos del orden militar. (Art. 101)",
            "correctas": [
                "Intencionales",
                "No intencionales o de imprudencia",
            ],
            "opciones": [
                "Intencionales",
                "No intencionales o de imprudencia",
                "Administrativos únicamente",
                "Civiles electorales",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "5. ¿Cómo se presume la inocencia de todo imputado? (Art. 102)",
            "correcta": "Mientras no se declare su responsabilidad mediante sentencia firme.",
            "opciones": [
                "Mientras no se declare su responsabilidad mediante sentencia firme.",
                "Solo hasta que sea detenido.",
                "Solo durante las primeras 24 horas.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "6. ¿Cuándo es punible la imprudencia? (Art. 103)",
            "correcta": "Cuando se consume y no sea tan leve que solo se castigaría con prisión de un mes si fuera delito intencional.",
            "opciones": [
                "Cuando se consume y no sea tan leve que solo se castigaría con prisión de un mes si fuera delito intencional.",
                "Siempre, aunque no se consume.",
                "Nunca es punible.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "7. ¿Cómo se castigan las infracciones que solamente constituyen faltas? (Art. 104)",
            "correcta": "De acuerdo con lo que prevenga la Ordenanza o leyes que la substituyan.",
            "opciones": [
                "De acuerdo con lo que prevenga la Ordenanza o leyes que la substituyan.",
                "Con pena de treinta a sesenta años.",
                "Con destitución automática.",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "8. Selecciona los grados de ejecución punibles de los delitos. (Art. 105)",
            "correctas": [
                "Conato",
                "Delito frustrado",
                "Delito consumado",
            ],
            "opciones": [
                "Conato",
                "Delito frustrado",
                "Delito consumado",
                "Delito imaginario",
                "Falta administrativa simple",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "9. ¿En qué consiste el conato? (Art. 106)",
            "correcta": "En ejecutar hechos encaminados directa e inmediatamente a la consumación, sin llegar al acto que la constituye.",
            "opciones": [
                "En ejecutar hechos encaminados directa e inmediatamente a la consumación, sin llegar al acto que la constituye.",
                "En consumar totalmente el delito.",
                "En recibir una condena firme.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "10. ¿Cuándo hay reincidencia? (Art. 107)",
            "correcta": "Cuando el condenado por sentencia ejecutoria comete un nuevo delito dentro del término correspondiente.",
            "opciones": [
                "Cuando el condenado por sentencia ejecutoria comete un nuevo delito dentro del término correspondiente.",
                "Cuando alguien comete una falta por primera vez.",
                "Cuando se dicta absolución.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "11. ¿Cuándo hay acumulación? (Art. 108)",
            "correcta": "Cuando alguien es juzgado a la vez por varios delitos ejecutados en actos distintos.",
            "opciones": [
                "Cuando alguien es juzgado a la vez por varios delitos ejecutados en actos distintos.",
                "Cuando solo existe un delito.",
                "Cuando ya existe sentencia irrevocable previa.",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "12. Selecciona quiénes pueden ser autores de un delito. (Art. 109)",
            "correctas": [
                "Los que conciben, resuelven cometer, preparan y ejecutan el delito",
                "Los que son la causa determinante del delito",
                "Los que ejecutan materialmente el acto en que el delito queda consumado",
                "Los que teniendo el deber de impedir o castigar un delito se obligan a no estorbarlo",
            ],
            "opciones": [
                "Los que conciben, resuelven cometer, preparan y ejecutan el delito",
                "Los que son la causa determinante del delito",
                "Los que ejecutan materialmente el acto en que el delito queda consumado",
                "Los que teniendo el deber de impedir o castigar un delito se obligan a no estorbarlo",
                "Los que no tuvieron conocimiento alguno del delito",
                "Los que denunciaron inmediatamente el hecho",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "13. Selecciona quiénes son cómplices. (Art. 111)",
            "correctas": [
                "Los que ayudan a los autores en los preparativos del delito",
                "Los que proporcionan instrumentos, armas u otros medios adecuados",
                "Los que dan instrucciones para cometerlo",
                "Los que toman parte indirecta o accesoria en la ejecución",
                "Los que ocultan cosas robadas o dan asilo a delincuentes por pacto anterior",
            ],
            "opciones": [
                "Los que ayudan a los autores en los preparativos del delito",
                "Los que proporcionan instrumentos, armas u otros medios adecuados",
                "Los que dan instrucciones para cometerlo",
                "Los que toman parte indirecta o accesoria en la ejecución",
                "Los que ocultan cosas robadas o dan asilo a delincuentes por pacto anterior",
                "Los que denuncian el delito por conductos debidos",
                "Los que impiden la comisión del delito",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "14. Selecciona formas de encubrimiento de primera clase. (Art. 116)",
            "correctas": [
                "Auxiliar a los delincuentes para que se aprovechen de los instrumentos o cosas del delito",
                "Impedir que se averigüe el delito",
                "Impedir que se descubra a los responsables",
                "Ocultar a los responsables si tienen costumbre de hacerlo u obran por retribución",
            ],
            "opciones": [
                "Auxiliar a los delincuentes para que se aprovechen de los instrumentos o cosas del delito",
                "Impedir que se averigüe el delito",
                "Impedir que se descubra a los responsables",
                "Ocultar a los responsables si tienen costumbre de hacerlo u obran por retribución",
                "Poner el delito en conocimiento del Ministerio Público",
                "Cumplir una sentencia firme",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "15. Selecciona las penas establecidas en el Código de Justicia Militar. (Art. 122)",
            "correctas": [
                "Prisión",
                "Suspensión de empleo o comisión militar",
                "Destitución de empleo",
            ],
            "opciones": [
                "Prisión",
                "Suspensión de empleo o comisión militar",
                "Destitución de empleo",
                "Multa escolar",
                "Arresto civil voluntario",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "16. Selecciona bases del Sistema Penitenciario Militar. (Art. 122 Bis)",
            "correctas": [
                "Trabajo",
                "Capacitación para el trabajo",
                "Educación",
                "Salud",
                "Deporte",
                "Adiestramiento",
                "Instrucción militar",
                "Respeto a los derechos humanos",
            ],
            "opciones": [
                "Trabajo",
                "Capacitación para el trabajo",
                "Educación",
                "Salud",
                "Deporte",
                "Adiestramiento",
                "Instrucción militar",
                "Respeto a los derechos humanos",
                "Castigo sin proceso",
                "Aislamiento permanente obligatorio",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "17. ¿Cuáles son los tres términos de toda pena temporal? (Art. 123)",
            "correctas": [
                "Mínimo",
                "Medio",
                "Máximo",
            ],
            "opciones": [
                "Mínimo",
                "Medio",
                "Máximo",
                "Inicial",
                "Final",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "18. ¿Desde cuándo se cuentan las penas de prisión? (Art. 126)",
            "correcta": "Desde la fecha en que se hubiese restringido la libertad del inculpado.",
            "opciones": [
                "Desde la fecha en que se hubiese restringido la libertad del inculpado.",
                "Desde que se publica una noticia.",
                "Desde que termina el juicio civil.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "19. ¿En qué consiste la pena de prisión militar? (Art. 128)",
            "correcta": "En la privación de la libertad desde dieciséis días a sesenta años.",
            "opciones": [
                "En la privación de la libertad desde dieciséis días a sesenta años.",
                "En una multa económica únicamente.",
                "En suspensión de clases militares.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "20. ¿En qué consiste la pena de suspensión de empleo? (Art. 131)",
            "correcta": "En la privación temporal del empleo, remuneración, honores, consideraciones e insignias correspondientes.",
            "opciones": [
                "En la privación temporal del empleo, remuneración, honores, consideraciones e insignias correspondientes.",
                "En la privación absoluta y definitiva del empleo militar.",
                "En una amonestación verbal.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "21. ¿En qué consiste la destitución de empleo? (Art. 136)",
            "correcta": "En la privación absoluta del empleo militar que estuviere desempeñando el inculpado.",
            "opciones": [
                "En la privación absoluta del empleo militar que estuviere desempeñando el inculpado.",
                "En una suspensión de tres días.",
                "En una recompensa por servicios.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "22. ¿Cuál es la pena para traición a la patria? (Art. 203)",
            "correcta": "De treinta a sesenta años de prisión.",
            "opciones": [
                "De treinta a sesenta años de prisión.",
                "De uno a tres días de arresto.",
                "Solo suspensión temporal.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "23. ¿Cuál es la pena para espionaje militar? (Art. 206)",
            "correcta": "De treinta a sesenta años de prisión.",
            "opciones": [
                "De treinta a sesenta años de prisión.",
                "De dieciséis días a un mes.",
                "Únicamente destitución.",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "24. Selecciona fines del delito de rebelión militar. (Art. 218)",
            "correctas": [
                "Abolir o reformar la Constitución Federal",
                "Impedir la elección de los Supremos Poderes de la Federación",
                "Usurpar funciones de los Supremos Poderes",
                "Separar de su cargo al Presidente de la República",
                "Abolir o reformar la Constitución Política de alguno de los Estados",
            ],
            "opciones": [
                "Abolir o reformar la Constitución Federal",
                "Impedir la elección de los Supremos Poderes de la Federación",
                "Usurpar funciones de los Supremos Poderes",
                "Separar de su cargo al Presidente de la República",
                "Abolir o reformar la Constitución Política de alguno de los Estados",
                "Solicitar vacaciones",
                "Pedir cambio de unidad",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "25. ¿Cuál es la pena para quien promueva o dirija una rebelión militar? (Art. 219)",
            "correcta": "De treinta a sesenta años de prisión.",
            "opciones": [
                "De treinta a sesenta años de prisión.",
                "De dos a cinco días de arresto.",
                "Solo una amonestación.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "26. ¿Cuántas personas deben reunirse tumultuariamente para que exista sedición militar? (Art. 224)",
            "correcta": "Diez o más.",
            "opciones": [
                "Diez o más.",
                "Dos o más.",
                "Cincuenta o más.",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "27. Selecciona objetos de la sedición militar. (Art. 224)",
            "correctas": [
                "Impedir la promulgación de una ley",
                "Impedir la ejecución de una ley",
                "Impedir la celebración de una elección popular",
                "Impedir el libre ejercicio de funciones de una autoridad",
                "Impedir el cumplimiento de una providencia judicial o administrativa",
            ],
            "opciones": [
                "Impedir la promulgación de una ley",
                "Impedir la ejecución de una ley",
                "Impedir la celebración de una elección popular",
                "Impedir el libre ejercicio de funciones de una autoridad",
                "Impedir el cumplimiento de una providencia judicial o administrativa",
                "Solicitar permiso ordinario",
                "Presentar una queja por conducto regular",
            ],
        },
    ]

    if "justicia_militar_respuestas" not in st.session_state:
        st.session_state.justicia_militar_respuestas = {}

    correctas = 0

    for i, p in enumerate(preguntas):
        key_respuesta = f"{usuario}_{seccion_id}_respuesta_{i}"
        key_confirmada = f"{usuario}_{seccion_id}_confirmada_{i}"

        st.markdown("---")
        st.markdown(f"### {p['pregunta']}")

        ya_confirmada = st.session_state.justicia_militar_respuestas.get(
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
                    st.session_state.justicia_militar_respuestas[key_respuesta] = respuesta
                    st.session_state.justicia_militar_respuestas[key_confirmada] = True
                    st.rerun()

        else:
            respuesta_guardada = st.session_state.justicia_militar_respuestas.get(
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
            st.session_state.justicia_militar_respuestas.pop(
                f"{usuario}_{seccion_id}_confirmada_{i}",
                None,
            )
            st.session_state.justicia_militar_respuestas.pop(
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
