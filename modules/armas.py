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


def mostrar_cuestionario(preguntas, seccion_id, dificultad, titulo):
    usuario = st.session_state.get("usuario")

    if not usuario:
        st.warning("⚠️ Primero escribe tu nombre en la página principal.")
        st.stop()

    progreso = cargar_progreso()

    st.markdown(f"## {titulo}")
    st.info(f"👤 Usuario: **{usuario}**")
    st.info(f"🔥 Dificultad del tema: **{dificultad}**")

    if usuario in progreso and seccion_id in progreso[usuario]:
        datos = progreso[usuario][seccion_id]
        st.success(
            f"Progreso guardado: {datos['color']} — "
            f"{datos['porcentaje']}% — {datos['mensaje']}"
        )

    key_estado = f"{seccion_id}_respuestas"

    if key_estado not in st.session_state:
        st.session_state[key_estado] = {}

    correctas = 0

    for i, p in enumerate(preguntas):
        key_respuesta = f"{usuario}_{seccion_id}_respuesta_{i}"
        key_confirmada = f"{usuario}_{seccion_id}_confirmada_{i}"

        st.markdown("---")
        st.markdown(f"### {p['pregunta']}")

        ya_confirmada = st.session_state[key_estado].get(key_confirmada, False)

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
                    st.session_state[key_estado][key_respuesta] = respuesta
                    st.session_state[key_estado][key_confirmada] = True
                    st.rerun()

        else:
            respuesta_guardada = st.session_state[key_estado].get(key_respuesta)

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

    if st.button("📊 Finalizar sección", key=f"finalizar_{seccion_id}"):
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

    if st.button("🔄 Reiniciar intento", key=f"reiniciar_{seccion_id}"):
        for i, p in enumerate(preguntas):
            st.session_state[key_estado].pop(
                f"{usuario}_{seccion_id}_confirmada_{i}",
                None,
            )
            st.session_state[key_estado].pop(
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


def show():
    st.title("🔫 Ley Federal de Armas de Fuego y Explosivos")

    dificultad = "🔴 Difícil"

    preguntas_parte1 = [
        {
            "tipo": "radio",
            "pregunta": "1. Lee el siguiente texto:\n\nLas disposiciones de esta Ley son de interés público.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 1° de la Ley Federal de Armas de Fuego y Explosivos",
            "opciones": [
                "Artículo 1° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 4° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 7° de la Ley Federal de Armas de Fuego y Explosivos",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "2. Selecciona a quiénes corresponde la aplicación de esta Ley. (Art. 2°)",
            "correctas": [
                "El Presidente de la República",
                "La Secretaría de Gobernación",
                "La Secretaría de la Defensa Nacional",
                "Las demás autoridades federales en los casos de su competencia",
            ],
            "opciones": [
                "El Presidente de la República",
                "La Secretaría de Gobernación",
                "La Secretaría de la Defensa Nacional",
                "Las demás autoridades federales en los casos de su competencia",
                "Únicamente los municipios",
                "Exclusivamente los particulares",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "3. ¿Qué intervención tienen las autoridades de las entidades federativas, municipios y demarcaciones territoriales? (Art. 3°)",
            "correcta": "Tendrán la intervención que esta Ley y su Reglamento señalan, en sus correspondientes ámbitos de competencia.",
            "opciones": [
                "Tendrán la intervención que esta Ley y su Reglamento señalan, en sus correspondientes ámbitos de competencia.",
                "No tienen ninguna intervención.",
                "Pueden modificar libremente la Ley.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "4. Lee el siguiente texto:\n\nCorresponde al Ejecutivo de la Unión por conducto de las Secretarías de Gobernación y de la Defensa Nacional, dentro de sus respectivas atribuciones, el control de todas las armas en el país, para cuyo efecto se llevará un Registro Federal de Armas.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 4° de la Ley Federal de Armas de Fuego y Explosivos",
            "opciones": [
                "Artículo 2° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 4° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 10° de la Ley Federal de Armas de Fuego y Explosivos",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "5. ¿Qué obligación tienen el Ejecutivo Federal y los gobiernos locales en materia de armas? (Art. 5°)",
            "correcta": "Realizar campañas educativas permanentes que induzcan a reducir la posesión, portación y uso de armas de cualquier tipo.",
            "opciones": [
                "Realizar campañas educativas permanentes que induzcan a reducir la posesión, portación y uso de armas de cualquier tipo.",
                "Promover la portación libre de armas.",
                "Eliminar todo registro de armas.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "6. ¿Qué tipo de publicidad se autoriza respecto a las armas por razones de interés público? (Art. 5°)",
            "correcta": "Solo la publicidad de armas deportivas para fines cinegéticos y de tiro, en los términos del Reglamento.",
            "opciones": [
                "Solo la publicidad de armas deportivas para fines cinegéticos y de tiro, en los términos del Reglamento.",
                "Toda publicidad sin restricción.",
                "Publicidad de cualquier arma en redes sociales.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "7. Lee el siguiente texto:\n\nSon supletorias de esta Ley las leyes o reglamentos federales que traten materias conexas.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 6° de la Ley Federal de Armas de Fuego y Explosivos",
            "opciones": [
                "Artículo 6° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 8° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 12° de la Ley Federal de Armas de Fuego y Explosivos",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "8. ¿Qué obligación existe respecto a la posesión de toda arma de fuego? (Art. 7°)",
            "correcta": "Debe manifestarse a la Secretaría de la Defensa Nacional para su inscripción en el Registro Federal de Armas.",
            "opciones": [
                "Debe manifestarse a la Secretaría de la Defensa Nacional para su inscripción en el Registro Federal de Armas.",
                "Debe ocultarse en el domicilio.",
                "Debe registrarse únicamente ante una autoridad municipal.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "9. Lee el siguiente texto:\n\nNo se permitirá la posesión ni portación de las armas prohibidas por la Ley ni de las reservadas para el uso exclusivo del Ejército, Armada y Fuerza Aérea, salvo los casos de excepción señalados en esta Ley.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 8° de la Ley Federal de Armas de Fuego y Explosivos",
            "opciones": [
                "Artículo 8° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 14° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 24° de la Ley Federal de Armas de Fuego y Explosivos",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "10. ¿Qué pistolas pueden poseerse o portarse en términos del Art. 9°, fracción I?",
            "correcta": "Pistolas de funcionamiento semi-automático de calibre no superior al .380, con las excepciones señaladas en la Ley.",
            "opciones": [
                "Pistolas de funcionamiento semi-automático de calibre no superior al .380, con las excepciones señaladas en la Ley.",
                "Cualquier pistola sin límite de calibre.",
                "Pistolas automáticas de ráfaga.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "11. ¿Qué revólveres pueden poseerse o portarse conforme al Art. 9°, fracción II?",
            "correcta": "Revólveres en calibres no superiores al .38 Especial, excepto el calibre .357 Magnum.",
            "opciones": [
                "Revólveres en calibres no superiores al .38 Especial, excepto el calibre .357 Magnum.",
                "Revólveres de cualquier calibre.",
                "Solo revólveres calibre .357 Magnum.",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "12. Selecciona armas que pueden poseer y portar ejidatarios, comuneros y jornaleros del campo fuera de zonas urbanas, conforme al Art. 9°.",
            "correctas": [
                "Un arma de las mencionadas en el artículo",
                "Un rifle de calibre .22",
                "Una escopeta de cualquier calibre permitida por la Ley",
            ],
            "opciones": [
                "Un arma de las mencionadas en el artículo",
                "Un rifle de calibre .22",
                "Una escopeta de cualquier calibre permitida por la Ley",
                "Armas de uso exclusivo sin excepción",
                "Explosivos industriales sin permiso",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "13. Selecciona armas que podrán autorizarse a deportistas de tiro o cacería conforme al Art. 10°.",
            "correctas": [
                "Pistolas, revólveres y rifles calibre .22 de fuego circular",
                "Pistolas de calibre .38 con fines de tiro olímpico o de competencia",
                "Escopetas en calibres y modelos permitidos",
                "Rifles de alto poder de repetición o semiautomáticos no convertibles en automáticos",
                "Las demás armas de características deportivas conforme a normas legales aplicables",
            ],
            "opciones": [
                "Pistolas, revólveres y rifles calibre .22 de fuego circular",
                "Pistolas de calibre .38 con fines de tiro olímpico o de competencia",
                "Escopetas en calibres y modelos permitidos",
                "Rifles de alto poder de repetición o semiautomáticos no convertibles en automáticos",
                "Las demás armas de características deportivas conforme a normas legales aplicables",
                "Armas automáticas de ráfaga",
                "Artefactos explosivos improvisados",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "14. ¿Qué autorización especial tienen quienes practican charrería respecto a revólveres? (Art. 10°)",
            "correcta": "Podrá autorizárseles revólveres de mayor calibre como complemento del atuendo charro, debiendo llevarlos descargados.",
            "opciones": [
                "Podrá autorizárseles revólveres de mayor calibre como complemento del atuendo charro, debiendo llevarlos descargados.",
                "Podrán llevar cualquier arma cargada en todo momento.",
                "No podrán tener ninguna autorización especial.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "15. Lee el siguiente texto:\n\nLa posesión de cartuchos correspondientes a las armas que pueden poseerse o portarse se limitará a las cantidades que se establecen en el artículo 50 de esta Ley, por cada arma manifestada en el Registro Federal de Armas.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 10 Bis de la Ley Federal de Armas de Fuego y Explosivos",
            "opciones": [
                "Artículo 10 Bis de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 14° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 25° de la Ley Federal de Armas de Fuego y Explosivos",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "16. Selecciona armas, municiones o materias de uso exclusivo del Ejército, Armada y Fuerza Aérea conforme al Art. 11°.",
            "correctas": [
                "Revólveres calibre .357 Magnum y superiores a .38 Especial",
                "Pistolas calibre 9 mm. Parabellum, Luger y similares",
                "Fusiles, mosquetones, carabinas y tercerolas en calibres señalados por la Ley",
                "Armas con sistema de ráfaga, sub-ametralladoras, metralletas y ametralladoras",
                "Cañones, piezas de artillería, morteros y carros de combate",
                "Aeronaves de guerra y su armamento",
            ],
            "opciones": [
                "Revólveres calibre .357 Magnum y superiores a .38 Especial",
                "Pistolas calibre 9 mm. Parabellum, Luger y similares",
                "Fusiles, mosquetones, carabinas y tercerolas en calibres señalados por la Ley",
                "Armas con sistema de ráfaga, sub-ametralladoras, metralletas y ametralladoras",
                "Cañones, piezas de artillería, morteros y carros de combate",
                "Aeronaves de guerra y su armamento",
                "Utensilios de cocina",
                "Herramientas de jardinería comunes",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "17. ¿Cuáles son armas prohibidas para efectos de esta Ley? (Art. 12°)",
            "correcta": "Las señaladas en el Código Penal correspondiente en materia común y federal.",
            "opciones": [
                "Las señaladas en el Código Penal correspondiente en materia común y federal.",
                "Todas las herramientas de trabajo.",
                "Todos los instrumentos deportivos.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "18. Lee el siguiente texto:\n\nNo se considerarán como armas prohibidas los utensilios, herramientas o instrumentos para labores de campo o de cualquier oficio, arte, profesión o deporte que tengan aplicación conocida como tales.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 13° de la Ley Federal de Armas de Fuego y Explosivos",
            "opciones": [
                "Artículo 9° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 13° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 31° de la Ley Federal de Armas de Fuego y Explosivos",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "19. ¿Qué debe hacerse en caso de extravío, robo, destrucción, aseguramiento o decomiso de un arma? (Art. 14°)",
            "correcta": "Debe hacerse del conocimiento de la Secretaría de la Defensa Nacional en los términos y conductos establecidos.",
            "opciones": [
                "Debe hacerse del conocimiento de la Secretaría de la Defensa Nacional en los términos y conductos establecidos.",
                "No debe reportarse.",
                "Debe publicarse únicamente en redes sociales.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "20. ¿Qué obligación impone la posesión de armas en el domicilio? (Art. 15°)",
            "correcta": "Manifestarlas a la Secretaría de la Defensa Nacional para su registro.",
            "opciones": [
                "Manifestarlas a la Secretaría de la Defensa Nacional para su registro.",
                "Prestarlas libremente a cualquier persona.",
                "Modificarlas sin autorización.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "21. ¿Qué debe manifestar la persona física para el control de la posesión de armas? (Art. 16°)",
            "correcta": "Un único domicilio de residencia permanente para sí y sus familiares.",
            "opciones": [
                "Un único domicilio de residencia permanente para sí y sus familiares.",
                "Todos sus domicilios temporales sin excepción.",
                "Solo su domicilio laboral.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "22. Lee el siguiente texto:\n\nToda persona que adquiera una o más armas está obligada a manifestarlo a la Secretaría de la Defensa Nacional en un plazo de treinta días. La manifestación se hará por escrito, indicando marca, calibre, modelo y matrícula si la tuviera.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 17° de la Ley Federal de Armas de Fuego y Explosivos",
            "opciones": [
                "Artículo 15° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 17° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 24° de la Ley Federal de Armas de Fuego y Explosivos",
            ],
        },
    ]

    preguntas_parte2 = [
        {
            "tipo": "radio",
            "pregunta": "1. ¿Están obligados los servidores públicos y jefes de cuerpos de policía a hacer la manifestación de armas? (Art. 18°)",
            "correcta": "Sí, están obligados a hacer la manifestación correspondiente.",
            "opciones": [
                "Sí, están obligados a hacer la manifestación correspondiente.",
                "No, están totalmente exceptuados.",
                "Solo si pertenecen a municipios.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "2. ¿Qué facultad tiene la Secretaría de la Defensa Nacional respecto a armas de tiro o cacería? (Art. 19°)",
            "correcta": "Determinar en cada caso qué armas de tiro o cacería pueden poseerse y sus dotaciones de municiones.",
            "opciones": [
                "Determinar en cada caso qué armas de tiro o cacería pueden poseerse y sus dotaciones de municiones.",
                "Autorizar cualquier arma sin límite.",
                "Eliminar todos los registros.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "3. Lee el siguiente texto:\n\nLos Clubes o Asociaciones de deportistas de tiro y cacería deberán estar registrados en las Secretarías de Gobernación y de la Defensa Nacional, cumpliendo los requisitos del Reglamento.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 20° de la Ley Federal de Armas de Fuego y Explosivos",
            "opciones": [
                "Artículo 18° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 20° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 30° de la Ley Federal de Armas de Fuego y Explosivos",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "4. ¿Quiénes pueden poseer colecciones o museos de armas y qué se requiere? (Art. 21°)",
            "correcta": "Personas físicas o morales, públicas o privadas, previo permiso correspondiente de la Secretaría de la Defensa Nacional.",
            "opciones": [
                "Personas físicas o morales, públicas o privadas, previo permiso correspondiente de la Secretaría de la Defensa Nacional.",
                "Solo militares en activo sin permiso.",
                "Únicamente extranjeros turistas.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "5. ¿Qué deben solicitar los particulares que tengan colecciones de armas para adquirir nuevas piezas? (Art. 22°)",
            "correcta": "Autorización para la adquisición y posesión de nuevas armas destinadas a enriquecer la colección o museo, e inscribirlas.",
            "opciones": [
                "Autorización para la adquisición y posesión de nuevas armas destinadas a enriquecer la colección o museo, e inscribirlas.",
                "Solo avisar verbalmente.",
                "No deben solicitar nada.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "6. Lee el siguiente texto:\n\nLas armas que formen parte de una colección podrán enajenarse como tal, o por unidades, en los términos de esta Ley y previo permiso escrito de la Secretaría de la Defensa Nacional y demás autoridades competentes.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 23° de la Ley Federal de Armas de Fuego y Explosivos",
            "opciones": [
                "Artículo 21° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 23° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 35° de la Ley Federal de Armas de Fuego y Explosivos",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "7. ¿Qué se requiere para portar armas y quiénes quedan exceptuados? (Art. 24°)",
            "correcta": "Se requiere la licencia respectiva; los miembros del Ejército, Armada y Fuerza Aérea quedan exceptuados en los casos y condiciones aplicables.",
            "opciones": [
                "Se requiere la licencia respectiva; los miembros del Ejército, Armada y Fuerza Aérea quedan exceptuados en los casos y condiciones aplicables.",
                "No se requiere licencia para particulares.",
                "Solo se requiere credencial escolar.",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "8. Selecciona las clases de licencias para portación de armas. (Art. 25°)",
            "correctas": [
                "Particulares",
                "Oficiales",
            ],
            "opciones": [
                "Particulares",
                "Oficiales",
                "Escolares",
                "De cortesía",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "9. ¿Cada cuánto deberán revalidarse las licencias particulares? (Art. 25°)",
            "correcta": "Cada dos años.",
            "opciones": [
                "Cada dos años.",
                "Cada seis meses.",
                "Nunca se revalidan.",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "10. Selecciona requisitos para que una persona física obtenga licencia particular de portación de armas. (Art. 26°)",
            "correctas": [
                "Tener un modo honesto de vivir",
                "Haber cumplido el Servicio Militar Nacional, en caso de estar obligado",
                "No tener impedimento físico o mental para el manejo de armas",
                "No haber sido condenado por delito cometido con empleo de armas",
                "No consumir drogas, enervantes o psicotrópicos",
                "Acreditar la necesidad de portar armas",
            ],
            "opciones": [
                "Tener un modo honesto de vivir",
                "Haber cumplido el Servicio Militar Nacional, en caso de estar obligado",
                "No tener impedimento físico o mental para el manejo de armas",
                "No haber sido condenado por delito cometido con empleo de armas",
                "No consumir drogas, enervantes o psicotrópicos",
                "Acreditar la necesidad de portar armas",
                "No tener estudios básicos",
                "Ser menor de edad",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "11. Lee el siguiente texto:\n\nEl término para expedir las licencias particulares y colectivas será de cincuenta días hábiles, contados a partir de que se presenta la solicitud correspondiente.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 26° de la Ley Federal de Armas de Fuego y Explosivos",
            "opciones": [
                "Artículo 24° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 26° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 31° de la Ley Federal de Armas de Fuego y Explosivos",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "12. ¿Bajo qué condición pueden los extranjeros obtener autorización para portar armas? (Art. 27°)",
            "correcta": "Cuando satisfagan los requisitos correspondientes y acrediten su calidad de residentes permanentes, salvo permisos temporales deportivos.",
            "opciones": [
                "Cuando satisfagan los requisitos correspondientes y acrediten su calidad de residentes permanentes, salvo permisos temporales deportivos.",
                "Cuando sean turistas sin ningún requisito.",
                "Cuando presenten solo identificación extranjera.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "13. ¿Cuál es la vigencia de los permisos extraordinarios de portación temporal de armas? (Art. 28°)",
            "correcta": "Seis meses, con posibilidad de renovación semestral si la comisión es mayor.",
            "opciones": [
                "Seis meses, con posibilidad de renovación semestral si la comisión es mayor.",
                "Un día únicamente.",
                "Cinco años sin renovación.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "14. ¿Qué armas pueden portar los servidores públicos extranjeros con permiso del Art. 28°?",
            "correcta": "Las que utilizan en su país de origen como equipamiento institucional, si son revólveres o pistolas semiautomáticas de calibre no superior a .40 o equivalente.",
            "opciones": [
                "Las que utilizan en su país de origen como equipamiento institucional, si son revólveres o pistolas semiautomáticas de calibre no superior a .40 o equivalente.",
                "Cualquier arma automática.",
                "Armas sin registrar ni identificar.",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "15. Selecciona las dos clases de licencias oficiales para portación de armas. (Art. 29°)",
            "correctas": [
                "Colectivas",
                "Individuales",
            ],
            "opciones": [
                "Colectivas",
                "Individuales",
                "Temporales escolares",
                "Anónimas",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "16. Lee el siguiente texto:\n\nCorresponde a la Secretaría de la Defensa Nacional, con la salvedad señalada en el artículo 32, la expedición, suspensión y cancelación de las licencias de portación de armas, así como su registro, control y vigilancia.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 30° de la Ley Federal de Armas de Fuego y Explosivos",
            "opciones": [
                "Artículo 30° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 32° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 36° de la Ley Federal de Armas de Fuego y Explosivos",
            ],
        },
        {
            "tipo": "multiple",
            "pregunta": "17. Selecciona casos en que podrán cancelarse las licencias de portación de armas. (Art. 31°)",
            "correctas": [
                "Cuando sus poseedores hagan mal uso de las armas o licencias",
                "Cuando sus poseedores alteren las licencias",
                "Cuando se usen las armas fuera de los lugares autorizados",
                "Cuando se porte un arma distinta a la que ampara la licencia",
                "Cuando el arma amparada por la licencia se modifique en sus características originales",
                "Cuando cambien de domicilio sin manifestarlo a la Secretaría de la Defensa Nacional",
                "Por no cumplir las disposiciones de esta Ley o sus Reglamentos",
            ],
            "opciones": [
                "Cuando sus poseedores hagan mal uso de las armas o licencias",
                "Cuando sus poseedores alteren las licencias",
                "Cuando se usen las armas fuera de los lugares autorizados",
                "Cuando se porte un arma distinta a la que ampara la licencia",
                "Cuando el arma amparada por la licencia se modifique en sus características originales",
                "Cuando cambien de domicilio sin manifestarlo a la Secretaría de la Defensa Nacional",
                "Por no cumplir las disposiciones de esta Ley o sus Reglamentos",
                "Por estudiar el contenido de la Ley",
                "Por renovar la licencia en tiempo",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "18. ¿Qué corresponde a la Secretaría de Gobernación respecto a licencias de portación de armas? (Art. 32°)",
            "correcta": "La expedición, suspensión y cancelación de licencias oficiales individuales a empleados federales, dando aviso a SEDENA.",
            "opciones": [
                "La expedición, suspensión y cancelación de licencias oficiales individuales a empleados federales, dando aviso a SEDENA.",
                "La autorización de todas las armas sin registro.",
                "La cancelación de la Ley.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "19. Lee el siguiente texto:\n\nLas credenciales de agentes o policías honorarios y confidenciales u otras similares no facultan a los interesados para portar armas sin la licencia correspondiente.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 33° de la Ley Federal de Armas de Fuego y Explosivos",
            "opciones": [
                "Artículo 31° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 33° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 37° de la Ley Federal de Armas de Fuego y Explosivos",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "20. ¿Qué información debe constar en las licencias de portación de armas? (Art. 34°)",
            "correcta": "Los límites territoriales en que tengan validez y, en su caso, las áreas específicas autorizadas.",
            "opciones": [
                "Los límites territoriales en que tengan validez y, en su caso, las áreas específicas autorizadas.",
                "Solo el color del arma.",
                "Únicamente la estatura del portador.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "21. ¿Qué autorizan exclusivamente las licencias de portación de armas? (Art. 35°)",
            "correcta": "La portación del arma señalada por la persona a cuyo nombre sea expedida.",
            "opciones": [
                "La portación del arma señalada por la persona a cuyo nombre sea expedida.",
                "La portación de cualquier arma.",
                "La venta libre de armas.",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "22. Lee el siguiente texto:\n\nQueda prohibido a los particulares asistir armados a manifestaciones y celebraciones públicas, asambleas deliberativas, juntas en que se controviertan intereses y actos donde pueda preverse la aparición de tendencias opuestas; se exceptúan desfiles y reuniones con fines deportivos de charrería, tiro o cacería.\n\n¿A qué artículo pertenece?",
            "correcta": "Artículo 36° de la Ley Federal de Armas de Fuego y Explosivos",
            "opciones": [
                "Artículo 24° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 31° de la Ley Federal de Armas de Fuego y Explosivos",
                "Artículo 36° de la Ley Federal de Armas de Fuego y Explosivos",
            ],
        },
        {
            "tipo": "radio",
            "pregunta": "23. ¿A quién corresponde autorizar el establecimiento de fábricas y comercios de armas? (Art. 37°)",
            "correcta": "Al Presidente de la República.",
            "opciones": [
                "Al Presidente de la República.",
                "A cualquier municipio.",
                "A particulares sin permiso.",
            ],
        },
    ]

    tab1, tab2 = st.tabs(["Parte 1: Arts. 1° al 17°", "Parte 2: Arts. 18° al 37°"])

    with tab1:
        mostrar_cuestionario(
            preguntas_parte1,
            "armas_parte1",
            dificultad,
            "Parte 1: Disposiciones generales, posesión y armas permitidas/prohibidas",
        )

    with tab2:
        mostrar_cuestionario(
            preguntas_parte2,
            "armas_parte2",
            dificultad,
            "Parte 2: Registro, portación, licencias y cancelación",
        )
