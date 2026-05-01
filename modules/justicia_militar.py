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
    st.title("Código de Justicia Militar")

    usuario = st.session_state.get("usuario")

    if not usuario:
        st.warning("⚠️ Primero escribe tu nombre en la página principal.")
        st.stop()

    seccion_id = "justicia_militar_parte1"
    dificultad = "🟠 Medio "

    progreso = cargar_progreso()

    st.markdown("## Primera parte")
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
            "pregunta": "1. Lee el siguiente texto:\n\nTodo delito del orden militar produce responsabilidad criminal, esto es, sujeta a una pena al que lo comete aunque sólo haya obrado con imprudencia y no con dañada intención.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 99 del Código de Justicia Militar",
            "opciones": [
                "Artículo 99 del Código de Justicia Militar",
                "Artículo 100 del Código de Justicia Militar",
                "Artículo 105 del Código de Justicia Militar",
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
            "pregunta": "3. Lee el siguiente texto:\n\nLa inocencia de todo imputado se presumirá mientras no se declare su responsabilidad mediante sentencia firme, emitida por el juez de la causa y conforme a las reglas establecidas en este Código.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 102 del Código de Justicia Militar",
            "opciones": [
                "Artículo 101 del Código de Justicia Militar",
                "Artículo 102 del Código de Justicia Militar",
                "Artículo 107 del Código de Justicia Militar",
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
            "pregunta": "5. Lee el siguiente texto:\n\nLos delitos serán punibles en todos sus grados de ejecución. Estos son conato, delito frustrado y delito consumado.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 105 del Código de Justicia Militar",
            "opciones": [
                "Artículo 103 del Código de Justicia Militar",
                "Artículo 105 del Código de Justicia Militar",
                "Artículo 108 del Código de Justicia Militar",
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
            "pregunta": "7. Lee el siguiente texto:\n\nHay reincidencia siempre que el condenado por sentencia ejecutoria cometa un nuevo delito, si no ha transcurrido, desde el cumplimiento de la condena, desde que la quebrantare o desde su indulto, por gracia, un término igual al de la prescripción de la pena.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 107 del Código de Justicia Militar",
            "opciones": [
                "Artículo 107 del Código de Justicia Militar",
                "Artículo 108 del Código de Justicia Militar",
                "Artículo 111 del Código de Justicia Militar",
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
            "pregunta": "10. Lee el siguiente texto:\n\nHay acumulación, siempre que alguno es juzgado a la vez por varios delitos ejecutados en actos distintos, y aunque sean conexos entre sí, cuando no se ha pronunciado antes sentencia irrevocable y la acción para perseguirlos no está prescrita.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 108 del Código de Justicia Militar",
            "opciones": [
                "Artículo 100 del Código de Justicia Militar",
                "Artículo 108 del Código de Justicia Militar",
                "Artículo 116 del Código de Justicia Militar",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "11. Selecciona quiénes pueden ser autores de un delito. (Art. 109)",
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
            "pregunta": "12. Selecciona quiénes son cómplices. (Art. 111)",
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
            "tipo": "radio",
            "pregunta": "13. Lee el siguiente texto:\n\nSon encubridores de primera clase, los que sin previo concierto con los delincuentes, los favorecen auxiliándolos, impidiendo que se averigüe el delito o que se descubra a los responsables, u ocultando a éstos en ciertos casos.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 116 del Código de Justicia Militar",
            "opciones": [
                "Artículo 111 del Código de Justicia Militar",
                "Artículo 116 del Código de Justicia Militar",
                "Artículo 122 del Código de Justicia Militar",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "14. Selecciona las penas establecidas en el Código de Justicia Militar. (Art. 122)",
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
            "pregunta": "15. Selecciona bases del Sistema Penitenciario Militar. (Art. 122 Bis)",
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
            "tipo": "radio",
            "pregunta": "16. Lee el siguiente texto:\n\nToda pena temporal tiene tres términos: mínimo, medio y máximo.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 123 del Código de Justicia Militar",
            "opciones": [
                "Artículo 122 del Código de Justicia Militar",
                "Artículo 123 del Código de Justicia Militar",
                "Artículo 128 del Código de Justicia Militar",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "17. ¿Desde cuándo se cuentan las penas de prisión? (Art. 126)",
            "correcta": "Desde la fecha en que se hubiese restringido la libertad del inculpado.",
            "opciones": [
                "Desde la fecha en que se hubiese restringido la libertad del inculpado.",
                "Desde que se publica una noticia.",
                "Desde que termina el juicio civil.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "18. Lee el siguiente texto:\n\nLa pena de prisión consiste en la privación de la libertad desde dieciséis días a sesenta años, sin que este segundo término pueda ser aumentado ni aún por causa de acumulación o reincidencia.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 128 del Código de Justicia Militar",
            "opciones": [
                "Artículo 125 del Código de Justicia Militar",
                "Artículo 128 del Código de Justicia Militar",
                "Artículo 131 del Código de Justicia Militar",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "19. ¿En qué consiste la pena de suspensión de empleo? (Art. 131)",
            "correcta": "En la privación temporal del empleo, remuneración, honores, consideraciones e insignias correspondientes.",
            "opciones": [
                "En la privación temporal del empleo, remuneración, honores, consideraciones e insignias correspondientes.",
                "En la privación absoluta y definitiva del empleo militar.",
                "En una amonestación verbal.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "20. Lee el siguiente texto:\n\nLa destitución de empleo consiste en la privación absoluta del empleo militar que estuviere desempeñando el inculpado.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 136 del Código de Justicia Militar",
            "opciones": [
                "Artículo 128 del Código de Justicia Militar",
                "Artículo 131 del Código de Justicia Militar",
                "Artículo 136 del Código de Justicia Militar",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "21. ¿Cuál es la pena para traición a la patria? (Art. 203)",
            "correcta": "De treinta a sesenta años de prisión.",
            "opciones": [
                "De treinta a sesenta años de prisión.",
                "De uno a tres días de arresto.",
                "Solo suspensión temporal.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "22. ¿Cuál es la pena para espionaje militar? (Art. 206)",
            "correcta": "De treinta a sesenta años de prisión.",
            "opciones": [
                "De treinta a sesenta años de prisión.",
                "De dieciséis días a un mes.",
                "Únicamente destitución.",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "23. Selecciona fines del delito de rebelión militar. (Art. 218)",
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
            "pregunta": "24. Lee el siguiente texto:\n\nSe impondrá pena de treinta a sesenta años de prisión al que promueva o dirija una rebelión, a quien ejerza mando en una región o plaza que se adhiera a la rebelión, y otros supuestos señalados por la ley.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 219 del Código de Justicia Militar",
            "opciones": [
                "Artículo 203 del Código de Justicia Militar",
                "Artículo 219 del Código de Justicia Militar",
                "Artículo 224 del Código de Justicia Militar",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "25. ¿Cuántas personas deben reunirse tumultuariamente para que exista sedición militar? (Art. 224)",
            "correcta": "Diez o más.",
            "opciones": [
                "Diez o más.",
                "Dos o más.",
                "Cincuenta o más.",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "26. Selecciona objetos de la sedición militar. (Art. 224)",
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
