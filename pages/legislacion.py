import streamlit as st

st.set_page_config(page_title="Legislación - Quiz")

st.title("🛡️ Compendio de Legislación Militar")
st.subheader("Ley Federal de Armas de Fuego y Explosivos")
st.caption("Última reforma: 07 de junio de 2024")

# --- FORMULARIO COMPLETO ---
with st.form("quiz_legislacion"):
    st.write("### Responde con cuidado:")

    # NIVEL 1
    q1 = st.radio("1. ¿Qué carácter tienen las disposiciones de la Ley Federal de Armas de Fuego y Explosivos? (Art. 1°)",
        ["Interés Privado", "Interés Público", "Interés Militar", "Interés Político"])

    q2 = st.multiselect("2. ¿A quiénes corresponde la aplicación de esta Ley? (Art. 2°)",
        ["Presidente de la República", "Secretaría de Gobernación", "SEDENA", "Autoridades Federales competentes", "Cualquier ciudadano"])

    q3 = st.radio("3. ¿A quién corresponde el control de todas las armas en el país? (Art. 4°)",
        ["Solo a la SEDENA", "A los Gobiernos Estatales", "Al Ejecutivo de la Unión por conducto de SEGOB y SEDENA", "A la Guardia Nacional"])

    q4 = st.radio("4. ¿Qué tipo de publicidad de armas se autoriza por interés público? (Art. 5°)",
        ["Cualquier arma de fuego", "Armas exclusivas del Ejército", "Armas deportivas para fines cinegéticos y de tiro", "Ninguna publicidad está permitida"])

    q5 = st.radio("5. ¿Qué debe hacerse con la posesión de toda arma de fuego según el Art. 7?",
        ["Guardarla en secreto", "Manifestarla a la SEDENA para inscripción en el Registro Federal", "Solo registrarla si es de alto calibre", "No es necesario registrarla si es para defensa"])

    q6 = st.radio("6. ¿Qué armas pueden portar los ejidatarios y comuneros fuera de zonas urbanas? (Art. 9°)",
        ["Cualquier pistola 9mm", "Rifle .22 o escopeta (excepto cañón corto o calibre superior al 12)", "Solo machetes y herramientas", "Fusiles de asalto"])

    q7 = st.radio("7. ¿Cuál es el calibre máximo permitido para pistolas semi-automáticas de ciudadanos? (Art. 9°)",
        [".45 ACP", ".380 (9mm.)", ".357 Magnum", "9mm Parabellum"])

    q8 = st.radio("8. ¿Qué se requiere para portar armas legalmente? (Art. 24°)",
        ["Tener el arma registrada", "Ser mayor de edad solamente", "La licencia respectiva", "Pertenecer a un club de tiro solamente"])

    q9 = st.radio("9. ¿Cuál es la vigencia de las licencias PARTICULARES de portación? (Art. 25°)",
        ["De por vida", "Cada año", "Cada dos años", "Cada seis meses"])

    q10 = st.radio("10. ¿A quién corresponde la facultad exclusiva de autorizar fábricas y comercios de armas? (Art. 37°)",
        ["Al Secretario de la Defensa", "Al Congreso de la Unión", "Al Presidente de la República", "A los Gobernadores"])

    # NIVEL 2
    q11 = st.radio("11. ¿Qué revólveres pueden poseerse o portarse según el Art. 9°?",
        ["Cualquier calibre mientras no sea automático", "Calibres no superiores al .38 Especial (excepto .357 Magnum)", "Solo calibre .22", "Calibres superiores al .380"])

    st.write("**12. Selecciona las armas que un deportista de tiro o cacería SÍ puede autorizar (Art. 10):**")
    q12_1 = st.checkbox("Pistolas calibre .38 con fines de tiro olímpico")
    q12_2 = st.checkbox("Escopetas con cañón inferior a 635 mm (25 pulgadas)")
    q12_3 = st.checkbox("Rifles de alto poder de repetición no convertibles en automáticos")
    q12_4 = st.checkbox("Carabinas calibre .30")

    q14 = st.radio("14. Sobre la Charrería, ¿cuál es la condición para portar revólveres de mayor calibre? (Art. 10)",
        ["Pueden ir cargados si es zona rural", "Deben llevarlos descargados y como complemento del atuendo", "Solo pueden usarlos en el lienzo charro", "No tienen permitido calibres mayores"])

    st.write("**16. De la siguiente lista, selecciona las que SÍ son para USO EXCLUSIVO del Ejército (Art. 11):**")
    ex_1 = st.checkbox("Pistolas calibre 9 mm Parabellum y Luger")
    ex_2 = st.checkbox("Revólveres calibre .38 Especial")
    ex_3 = st.checkbox("Fusiles y carabinas calibre .223 y 7.62 mm")
    ex_4 = st.checkbox("Bayonetas, sables y lanzas")
    ex_5 = st.checkbox("Pistolas calibre .380")

    q18 = st.radio("18. ¿Se consideran armas prohibidas los utensilios o herramientas de trabajo? (Art. 13)",
        ["Sí, siempre que sean punzocortantes", "No, pero su uso se limita al local o sitio de trabajo/deporte", "Solo si se portan en la ciudad", "Sí, según el Código Penal"])

    q20 = st.radio("20. ¿Qué obligación impone poseer armas en el domicilio para seguridad? (Art. 15)",
        ["Ninguna, es un derecho privado", "Informar a la policía municipal", "Manifestarlas a la SEDENA para su registro", "Pedir permiso a los vecinos"])

    # NIVEL 3
    q22 = st.radio("22. ¿En qué plazo debe manifestarse la ADQUISICIÓN de un arma a la SEDENA? (Art. 17)",
        ["15 días naturales", "30 días naturales", "30 días hábiles", "60 días"])

    q24 = st.radio("24. ¿Quién tiene la facultad de determinar cuántas municiones puedes poseer por cada arma? (Art. 19)",
        ["El Gobierno del Estado", "La Secretaría de Gobernación", "La Secretaría de la Defensa Nacional", "El club de tiro"])

    q26 = st.radio("26. ¿Se pueden poseer armas PROHIBIDAS en colecciones o museos? (Art. 21)",
        ["No, bajo ninguna circunstancia", "Sí, siempre que tengan valor cultural o histórico y con permiso de SEDENA", "Sí, si son antiguas únicamente", "Solo si pertenecen al Gobierno"])

    q30 = st.selectbox("30. Sobre las clases de licencias y su vigencia (Art. 25), elige la opción CORRECTA:",
        ["Las particulares duran 5 años","Las particulares se revalidan cada 2 años; las oficiales mientras dure el cargo","Todas las licencias duran 1 año","Las oficiales se revalidan cada 2 años"])

    req_1 = st.checkbox("Tener un modo honesto de vivir")
    req_2 = st.checkbox("Haber cumplido con el Servicio Militar Nacional (si aplica)")
    req_3 = st.checkbox("No consumir drogas o psicotrópicos")
    req_4 = st.checkbox("Ser dueño de un negocio propio")
    req_5 = st.checkbox("No tener impedimento físico o mental para el manejo de armas")

    q32 = st.radio("32. ¿Cuál es el término para que la autoridad expida una licencia tras la solicitud? (Art. 26)",
        ["15 días hábiles", "30 días naturales", "50 días hábiles", "90 días"])

    q33 = st.radio("33. ¿Bajo qué condición migratoria puede un extranjero obtener licencia de portación? (Art. 27)",
        ["Visitante temporal", "Residente permanente", "Cualquier extranjero con pasaporte", "Solo diplomáticos"])

    # NIVEL 4
    c_1 = st.checkbox("Cuando se use el arma fuera de los lugares autorizados")
    c_2 = st.checkbox("Cuando el arma se modifique en sus características originales")
    c_3 = st.checkbox("Cuando los poseedores cambien de domicilio sin avisar")
    c_4 = st.checkbox("Por prestar el arma a un familiar")

    q40 = st.radio("40. ¿Las credenciales de agentes honorarios facultan para portar armas? (Art. 33)",
        ["Sí, por ser autoridad", "No, requieren licencia correspondiente", "Solo en su jurisdicción"])

    q43 = st.radio("43. ¿En qué lugares está prohibido a los particulares asistir armados? (Art. 36)",
        ["Solo en bancos", "En manifestaciones, asambleas y celebraciones públicas", "En cualquier lugar fuera de su casa"])

    enviar = st.form_submit_button("🚀 TERMINAR EXAMEN")

# --- CALIFICACIÓN ---
if enviar:
    puntos = 0

    # Nivel 1
    if q1 == "Interés Público": puntos += 1
    if set(q2) == {"Presidente de la República","Secretaría de Gobernación","SEDENA","Autoridades Federales competentes"}: puntos += 1
    if q3 == "Al Ejecutivo de la Unión por conducto de SEGOB y SEDENA": puntos += 1
    if q4 == "Armas deportivas para fines cinegéticos y de tiro": puntos += 1
    if q5 == "Manifestarla a la SEDENA para inscripción en el Registro Federal": puntos += 1
    if q6 == "Rifle .22 o escopeta (excepto cañón corto o calibre superior al 12)": puntos += 1
    if q7 == ".380 (9mm.)": puntos += 1
    if q8 == "La licencia respectiva": puntos += 1
    if q9 == "Cada dos años": puntos += 1
    if q10 == "Al Presidente de la República": puntos += 1

    # Nivel 2
    if q11 == "Calibres no superiores al .38 Especial (excepto .357 Magnum)": puntos += 1
    if q12_1 and not q12_2 and q12_3 and not q12_4: puntos += 1
    if q14 == "Deben llevarlos descargados y como complemento del atuendo": puntos += 1
    if ex_1 and not ex_2 and ex_3 and ex_4 and not ex_5: puntos += 1
    if q18 == "No, pero su uso se limita al local o sitio de trabajo/deporte": puntos += 1
    if q20 == "Manifestarlas a la SEDENA para su registro": puntos += 1

    # Nivel 3
    if q22 == "30 días naturales": puntos += 1
    if q24 == "La Secretaría de la Defensa Nacional": puntos += 1
    if q26 == "Sí, siempre que tengan valor cultural o histórico y con permiso de SEDENA": puntos += 1
    if q30 == "Las particulares se revalidan cada 2 años; las oficiales mientras dure el cargo": puntos += 1
    if req_1 and req_2 and req_3 and not req_4 and req_5: puntos += 1
    if q32 == "50 días hábiles": puntos += 1
    if q33 == "Residente permanente": puntos += 1

    # Nivel 4
    if c_1 and c_2 and c_3 and not c_4: puntos += 1
    if q40 == "No, requieren licencia correspondiente": puntos += 1
    if q43 == "En manifestaciones, asambleas y celebraciones públicas": puntos += 1

    st.divider()
    st.balloons()
    st.header(f"🎯 Resultado Final: {puntos} aciertos")

    if puntos >= 20:
        st.success("🔥 Nivel pro, listo para el examen")
    elif puntos >= 12:
        st.warning("⚠️ Vas bien, pero repasa algunos artículos")
    else:
        st.error("❌ Hay que estudiar más")
