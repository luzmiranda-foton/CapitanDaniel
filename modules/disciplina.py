import streamlit as st
import json


def cargar_progreso():
    try:
        with open("data/progreso.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}


def guardar_progreso(data):
    with open("data/progreso.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def show():
    st.title("📘 Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos")
    st.subheader("Cuestionario - Primera parte")

    progreso = cargar_progreso()

    preguntas = [
        {
            "pregunta": "1. ¿Cuál es el objeto de la Ley de Disciplina del Ejército y Fuerza Aérea Mexicanos? (Art. 1°)",
            "correcta": "La presente Ley tiene por objeto preservar la disciplina militar como principio de orden y obediencia que regula la conducta de los individuos que integran el Ejército y Fuerza Aérea Mexicanos. Sus disposiciones son de observancia obligatoria para todos los militares que integran el Ejército y Fuerza Aérea Mexicanos de conformidad con su Ley Orgánica.",
            "opciones": [
                "Regular únicamente los ascensos y recompensas del personal militar.",
                "La presente Ley tiene por objeto preservar la disciplina militar como principio de orden y obediencia que regula la conducta de los individuos que integran el Ejército y Fuerza Aérea Mexicanos. Sus disposiciones son de observancia obligatoria para todos los militares que integran el Ejército y Fuerza Aérea Mexicanos de conformidad con su Ley Orgánica.",
                "Establecer exclusivamente las reglas de retiro y seguridad social militar.",
            ],
        },
        {
            "pregunta": "2. ¿Qué exige el servicio de las armas según el Art. 1° Bis?",
            "correcta": "El servicio de las armas exige que el militar lleve el cumplimiento del deber hasta el sacrificio y que anteponga al interés personal, el respeto a la Constitución Política de los Estados Unidos Mexicanos, la soberanía de la Nación, la lealtad a las instituciones y el honor del Ejército y Fuerza Aérea Mexicanos.",
            "opciones": [
                "El servicio de las armas exige únicamente obedecer órdenes administrativas.",
                "El servicio de las armas exige que el militar lleve el cumplimiento del deber hasta el sacrificio y que anteponga al interés personal, el respeto a la Constitución Política de los Estados Unidos Mexicanos, la soberanía de la Nación, la lealtad a las instituciones y el honor del Ejército y Fuerza Aérea Mexicanos.",
                "El servicio de las armas permite anteponer el interés personal cuando no exista orden directa.",
            ],
        },
        {
            "pregunta": "3. ¿Qué debe observar el militar conforme al Art. 2°?",
            "correcta": "El militar debe observar buen comportamiento, para que el pueblo deposite su confianza en el Ejército y Fuerza Aérea y los considere como la salvaguarda de sus derechos.",
            "opciones": [
                "El militar debe observar buen comportamiento, para que el pueblo deposite su confianza en el Ejército y Fuerza Aérea y los considere como la salvaguarda de sus derechos.",
                "El militar debe actuar solo conforme a sus intereses personales.",
                "El militar debe evitar relacionarse con la sociedad civil en todo momento.",
            ],
        },
        {
            "pregunta": "4. ¿En qué consiste la disciplina en el Ejército y Fuerza Aérea según el Art. 3°?",
            "correcta": "La disciplina en el Ejército y Fuerza Aérea es la norma a que los militares deben ajustar su conducta; tiene como bases la obediencia, y un alto concepto del honor, de la justicia y de la moral, y por objeto, el fiel y exacto cumplimiento de los deberes que prescriben las leyes y reglamentos militares.",
            "opciones": [
                "La disciplina es una recomendación moral sin efectos dentro del servicio.",
                "La disciplina se limita únicamente al saludo militar.",
                "La disciplina en el Ejército y Fuerza Aérea es la norma a que los militares deben ajustar su conducta; tiene como bases la obediencia, y un alto concepto del honor, de la justicia y de la moral, y por objeto, el fiel y exacto cumplimiento de los deberes que prescriben las leyes y reglamentos militares.",
            ],
        },
        {
            "pregunta": "5. ¿Cuál es la base fundamental del Ejército y Fuerza Aérea Mexicanos según el Art. 3° Bis?",
            "correcta": "La disciplina es la base fundamental del Ejército y Fuerza Aérea Mexicanos, los cuales existen primordialmente para defender los intereses de la Patria y preservar su vida institucional.",
            "opciones": [
                "La disciplina es la base fundamental del Ejército y Fuerza Aérea Mexicanos, los cuales existen primordialmente para defender los intereses de la Patria y preservar su vida institucional.",
                "La antigüedad es la base fundamental del Ejército y Fuerza Aérea Mexicanos.",
                "La administración económica es la base fundamental del Ejército y Fuerza Aérea Mexicanos.",
            ],
        },
        {
            "pregunta": "6. ¿Qué exige la disciplina entre el superior y el subalterno? (Art. 4°)",
            "correcta": "La disciplina exige respeto y consideraciones mutuas entre el superior y el subalterno, la infracción de esta norma de conducta se castigará de conformidad con las leyes y reglamentos militares.",
            "opciones": [
                "La disciplina exige respeto y consideraciones mutuas entre el superior y el subalterno, la infracción de esta norma de conducta se castigará de conformidad con las leyes y reglamentos militares.",
                "La disciplina exige solamente obediencia del subalterno, sin obligación del superior.",
                "La disciplina permite faltas de respeto cuando exista urgencia del servicio.",
            ],
        },
        {
            "pregunta": "7. ¿Cómo debe proceder el militar en el cumplimiento de sus obligaciones? (Art. 5°)",
            "correcta": "El militar debe proceder de un modo legal, justo y enérgico en el cumplimiento de sus obligaciones, a fin de obtener la estimación y obediencia de sus subalternos. Es deber del superior educar y dirigir a los individuos que la Nación pone bajo su mando.",
            "opciones": [
                "El militar debe proceder de forma discrecional, aunque no sea legal.",
                "El militar debe proceder de un modo legal, justo y enérgico en el cumplimiento de sus obligaciones, a fin de obtener la estimación y obediencia de sus subalternos. Es deber del superior educar y dirigir a los individuos que la Nación pone bajo su mando.",
                "El militar debe delegar siempre sus obligaciones al subalterno.",
            ],
        },
        {
            "pregunta": "8. ¿Qué facultad tiene el superior en caso de extrema necesidad en actos del servicio? (Art. 6°)",
            "correcta": "En caso de extrema necesidad en actos del servicio, el superior podrá servirse de sus armas o de la fuerza a su mando para obtener obediencia a sus órdenes o mantener la disciplina.",
            "opciones": [
                "En caso de extrema necesidad, el superior debe suspender todas sus órdenes.",
                "En caso de extrema necesidad en actos del servicio, el superior podrá servirse de sus armas o de la fuerza a su mando para obtener obediencia a sus órdenes o mantener la disciplina.",
                "En caso de extrema necesidad, el superior no puede intervenir en la conducta de sus subalternos.",
            ],
        },
        {
            "pregunta": "9. ¿De qué es responsable el superior respecto a las tropas que tiene a su mando? (Art. 7°)",
            "correcta": "El superior será responsable del orden en las tropas que tuviere a su mando, así como del cumplimiento de las obligaciones del servicio, sin que pueda disculparse en ningún caso con la omisión y descuido de sus subalternos.",
            "opciones": [
                "El superior solo es responsable de sus actos personales, no de sus tropas.",
                "El superior será responsable del orden en las tropas que tuviere a su mando, así como del cumplimiento de las obligaciones del servicio, sin que pueda disculparse en ningún caso con la omisión y descuido de sus subalternos.",
                "El superior puede disculparse siempre con la omisión de sus subalternos.",
            ],
        },
        {
            "pregunta": "10. ¿Qué prohíbe el Art. 14 respecto a las órdenes que puede dar el militar?",
            "correcta": "Queda estrictamente prohibido al militar dar órdenes cuya ejecución constituya un delito; el militar que las expida y el subalterno que las cumpla, serán responsables conforme al Código de Justicia Militar.",
            "opciones": [
                "Queda estrictamente prohibido al militar dar órdenes cuya ejecución constituya un delito; el militar que las expida y el subalterno que las cumpla, serán responsables conforme al Código de Justicia Militar.",
                "El militar puede dar cualquier orden si proviene de un superior.",
                "Solo será responsable el subalterno que cumpla la orden.",
            ],
        },
        {
            "pregunta": "11. ¿Qué se entiende por actos del servicio según el Art. 15?",
            "correcta": "Debe entenderse por actos del servicio, los prescritos por las leyes, reglamentos y disposiciones de observancia general que dicte la Superioridad.",
            "opciones": [
                "Debe entenderse por actos del servicio únicamente los realizados en campaña.",
                "Debe entenderse por actos del servicio, los prescritos por las leyes, reglamentos y disposiciones de observancia general que dicte la Superioridad.",
                "Debe entenderse por actos del servicio solo las órdenes verbales informales.",
            ],
        },
        {
            "pregunta": "12. ¿Qué prohíbe el Art. 17 respecto a la política?",
            "correcta": "Queda estrictamente prohibido al militar en servicio activo, inmiscuirse en asuntos políticos, directa o indirectamente, salvo aquel que disfrute de licencia que así se lo permita en términos de lo dispuesto por las leyes; así como pertenecer al estado eclesiástico o desempeñarse como ministro de cualquier culto religioso, sin que por ello pierda los derechos que le otorga la Constitución Política de los Estados Unidos Mexicanos.",
            "opciones": [
                "Queda estrictamente prohibido al militar en servicio activo, inmiscuirse en asuntos políticos, directa o indirectamente, salvo aquel que disfrute de licencia que así se lo permita en términos de lo dispuesto por las leyes; así como pertenecer al estado eclesiástico o desempeñarse como ministro de cualquier culto religioso, sin que por ello pierda los derechos que le otorga la Constitución Política de los Estados Unidos Mexicanos.",
                "El militar en servicio activo puede participar libremente en asuntos políticos sin restricciones.",
                "El militar solo tiene prohibido participar en política durante actos oficiales, pero no fuera de ellos.",
            ],
        },
        {
            "pregunta": "13. ¿Qué obligación tiene el militar respecto al saludo? (Art. 18)",
            "correcta": "El militar está obligado a saludar a sus superiores y a los de su misma jerarquía, conforme se prescriben los reglamentos, así como a corresponder el saludo de sus subalternos.",
            "opciones": [
                "El saludo militar es opcional fuera de instalaciones militares.",
                "El militar está obligado a saludar únicamente a sus superiores directos.",
                "El militar está obligado a saludar a sus superiores y a los de su misma jerarquía, conforme se prescriben los reglamentos, así como a corresponder el saludo de sus subalternos.",
            ],
        },
        {
            "pregunta": "14. ¿Qué debe hacer el militar que tenga alguna queja en relación con las disposiciones superiores? (Art. 42)",
            "correcta": "El militar que tenga alguna queja en relación con las disposiciones superiores o las obligaciones que le impone el servicio, podrá acudir ante el superior inmediato para la solución de sus demandas y, en caso de no ser debidamente atendido, podrá llegar por rigurosa escala, hasta el Presidente de la República, si es necesario.",
            "opciones": [
                "El militar debe presentar su queja directamente ante cualquier autoridad civil.",
                "El militar que tenga alguna queja en relación con las disposiciones superiores o las obligaciones que le impone el servicio, podrá acudir ante el superior inmediato para la solución de sus demandas y, en caso de no ser debidamente atendido, podrá llegar por rigurosa escala, hasta el Presidente de la República, si es necesario.",
                "El militar no puede presentar quejas relacionadas con el servicio.",
            ],
        },
        {
            "pregunta": "15. ¿Qué consecuencias tiene para el militar que infrinja la Ley de Disciplina? (Art. 43)",
            "correcta": "Todo militar que infrinja la presente Ley, así como algún precepto reglamentario, se hará acreedor a un correctivo disciplinario, de acuerdo con su jerarquía en el Ejército y Fuerza Aérea y, si la magnitud de su falta constituye un delito, quedará sujeto a lo dispuesto por el Código de Justicia Militar.",
            "opciones": [
                "Todo militar que infrinja la Ley solo recibirá una advertencia verbal.",
                "Todo militar que infrinja la presente Ley, así como algún precepto reglamentario, se hará acreedor a un correctivo disciplinario, de acuerdo con su jerarquía en el Ejército y Fuerza Aérea y, si la magnitud de su falta constituye un delito, quedará sujeto a lo dispuesto por el Código de Justicia Militar.",
                "Todo militar que infrinja la Ley será sancionado únicamente por autoridades civiles.",
            ],
        },
    ]

    st.info("Selecciona una respuesta en cada pregunta. El sistema te dirá al instante si es correcta o incorrecta.")

    correctas = 0

    for i, p in enumerate(preguntas):
        st.markdown("---")
        st.markdown(f"### {p['pregunta']}")

        respuesta = st.radio(
            "Elige una opción:",
            p["opciones"],
            key=f"disciplina_pregunta_{i}",
            index=None
        )

        if respuesta is not None:
            if respuesta == p["correcta"]:
                st.success("✅ Correcto")
                correctas += 1
            else:
                st.error("❌ Incorrecto")

    st.markdown("---")

    total = len(preguntas)
    porcentaje = correctas / total

    st.write(f"Avance actual del cuestionario: **{correctas}/{total}**")
    st.progress(porcentaje)

    if st.button("📊 Finalizar primera parte"):
        if correctas == total:
            progreso["disciplina_parte1"] = True
            guardar_progreso(progreso)
            st.success("🎉 Primera parte aprobada y progreso guardado.")
        elif porcentaje >= 0.70:
            progreso["disciplina_parte1"] = True
            guardar_progreso(progreso)
            st.success(f"✅ Aprobaste con {correctas}/{total}. Progreso guardado.")
        else:
            progreso["disciplina_parte1"] = False
            guardar_progreso(progreso)
            st.warning(f"Necesitas mínimo 70%. Obtuviste {correctas}/{total}. Intenta de nuevo.")

    if progreso.get("disciplina_parte1", False):
        st.success("✅ Progreso guardado: Primera parte completada.")
