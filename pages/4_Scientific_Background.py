import streamlit as st

def show_scientific_background_page():
    # Configuración de la página
    st.set_page_config(
        page_title="Scientific Background - Carbonauts",
        page_icon="🚀",
        layout="wide"
    )

    # Selector de idioma en la barra lateral superior
    if 'lang' not in st.session_state:
        st.session_state.lang = "English"

    selected_lang = st.sidebar.radio("🌐 Language / Idioma", ["English", "Español"], horizontal=True)
    st.session_state.lang = selected_lang

    # Diccionario de traducciones
    t = {
        "English": {
            "title": "Theoretical Framework: Fire Safety in Space Environments",
            "sec1_header": "1. Introduction and Problem Justification",
            "sec1_text": "Combustion processes are among the most complex and critical phenomena for safety in crewed space exploration. "
                         "Unlike terrestrial environments, fire control in confined habitats outside Earth represents one of the greatest operational threats. "
                         "Inadequate management of ignition risks directly endangers crew lives and the viability of long-duration missions to the Moon, Mars, and beyond.",
            
            "sec2_header": "2. Fire Behavior in Microgravity",
            "sec2_p1": "On Earth, combustion is heavily conditioned by gravity due to density gradients (buoyancy), "
                       "where hot gases rise and generate convective currents that give the flame its characteristic shape and feed the oxygen flow.",
            "sec2_p2": "In microgravity conditions (free fall), the absence of buoyancy radically alters the physics of fire:",
            "c1_title": "🌀 No Natural Convection",
            "c1_text": "Hot gases do not move vertically, eliminating flame flickering and simplifying the system toward one-dimensional molecular diffusion dynamics.",
            "c2_title": "🔵 Spherical Morphology",
            "c2_text": "Flames adopt a spherical and diffuse structure (frequently bluish in hue) that depends exclusively on the slow molecular diffusion of oxygen to sustain itself.",
            "c3_title": "⚠️ Propagation Limits",
            "c3_text": "Solid and liquid materials exhibit flammability thresholds different from Earth gravity (1g), demonstrating that traditional standards are not always conservative.",
            
            "sec3_header": "3. Historical Background and Critical Accidents",
            "sec3_intro": "Aerospace history has been marked by severe incidents that have driven regulatory evolution (such as NASA-STD-6001 standards):",
            "apolo1_title": "🚀 Apollo 1 (1967)",
            "apolo1_text": "An electrical arc in a pressurized pure oxygen atmosphere caused a lethal fire during the test phase, demanding an absolute redesign of materials and onboard atmospheric compositions.",
            "mir_title": "🛰️ Mir Space Station (1997)",
            "mir_text": "The failure of a solid fuel oxygen generator (SFOG) triggered an intense fire and dense smoke that temporarily compromised access to an escape capsule.",
            "apolo13_title": "💥 Apollo 13 (1970)",
            "apolo13_text": "The explosion of an oxygen tank demonstrated the critical vulnerability of pressurized life support systems en route to the Moon.",
            "artemis_title": "⚠️ Recent Missions (Artemis II)",
            "artemis_text": "Early smoke alerts remind us that the risk of fires remains latent at great distances from Earth.",
            
            "sec4_header": "4. Risk Factors in Space Habitats and Rovers",
            "sec4_intro": "The operational conditions of orbital stations, lunar bases, Martian bases, and pressurized rovers increase the probability of ignition and rapid propagation:",
            "risk1_title": "🧪 Enriched Atmospheres",
            "risk1_text": "To accommodate spacesuits and mitigate decompression sickness, habitats operate with oxygen concentrations exceeding 30% (compared to 21% on Earth), exponentially increasing flammability.",
            "risk2_title": "⚡ Electrical Ignition Sources",
            "risk2_text": "Wiring failures, short circuits, or electrical arcs near active control panels.",
            "risk3_title": "🛠️ Life Support Systems",
            "risk3_text": "Oxygen canisters (SFOG) represent critical failure points if contaminated with hydrocarbons, organic substances, or handling residues.",
            "risk4_title": "💨 Forced Ventilation Dynamics",
            "risk4_text": "Unlike Earth, air conditioning systems continuously transport and supply oxygen to the fire front, facilitating rapid and silent propagation.",
            
            "sec5_header": "5. Practical Application: From Scientific Data to Safety Engineering",
            "sec5_text": "To mitigate these risks, leveraging experimental databases (such as NASA's Physical Science Informatics - PSI database) is essential. "
                         "Through intelligent data synthesis, classification, and interpretation tools, engineers can optimally structure the three defensive phases of the fire lifecycle:",
            "f1_title": "1️⃣ Prevention",
            "f1_text": "Strict material selection and predictive modeling of flammability under reduced gravity conditions.",
            "f2_title": "2️⃣ Detection",
            "f2_text": "Advanced calibration of sensors and risk thresholds capable of discriminating combustion particles from dust or environmental interference.",
            "f3_title": "3️⃣ Extinction",
            "f3_text": "Development and implementation of effective suppression agents and operational procedures in confined microgravity environments."
        },
        "Español": {
            "title": "Marco Teórico: Seguridad contra Incendios en Entornos Espaciales",
            "sec1_header": "1. Introducción y Justificación del Problema",
            "sec1_text": "Los procesos de combustión se encuentran entre los fenómenos más complejos y críticos para la seguridad en la "
                         "exploración espacial tripulada. A diferencia de los entornos terrestres, el control del fuego en hábitats confinados "
                         "fuera de la Tierra representa una de las mayores amenazas operacionales. La gestión inadecuada de los riesgos de ignición "
                         "pone en peligro directo la vida de la tripulación y la viabilidad de misiones de larga duración hacia la Luna, Marte y más allá.",
            
            "sec2_header": "2. Comportamiento del Fuego en Microgravedad",
            "sec2_p1": "En la Tierra, la combustión está fuertemente condicionada por la gravedad debido a los gradientes de densidad (flotabilidad), "
                       "donde los gases calientes ascienden y generan corrientes convectivas que dan a la llama su característica forma y alimentan el flujo de oxígeno.",
            "sec2_p2": "En condiciones de microgravedad (caída libre), la ausencia de flotabilidad altera radicalmente la física del fuego:",
            "c1_title": "🌀 Sin Convección Natural",
            "c1_text": "Los gases calientes no se desplazan verticalmente, eliminando el parpadeo de las llamas y simplificando el sistema hacia dinámicas de difusión molecular unidimensionales.",
            "c2_title": "🔵 Morfología Esférica",
            "c2_text": "Las llamas adoptan una estructura esférica y difusa (frecuentemente de tonalidad azulada) que depende exclusivamente de la lenta difusión molecular del oxígeno para mantenerse.",
            "c3_title": "⚠️ Límites de Propagación",
            "c3_text": "Materiales sólidos y líquidos presentan umbrales de inflamabilidad diferentes a la gravedad terrestre (1g), demostrando que los estándares tradicionales no siempre son conservativos.",
            
            "sec3_header": "3. Antecedentes Históricos y Accidentes Críticos",
            "sec3_intro": "La historia aeroespacial ha estado marcada por incidentes graves que han impulsado la evolución normativa (como los estándares de la serie NASA-STD-6001):",
            "apolo1_title": "🚀 Apolo 1 (1967)",
            "apolo1_text": "Un arco eléctrico en una atmósfera de oxígeno puro a presión provocó un incendio letal en la fase de pruebas, exigiendo un rediseño absoluto de los materiales y composiciones atmosféricas a bordo.",
            "mir_title": "🛰️ Estación Espacial Mir (1997)",
            "mir_text": "El fallo de un generador de oxígeno de combustible sólido (SFOG) desató un incendio intenso y denso humo que comprometió temporalmente el acceso a una cápsula de escape.",
            "apolo13_title": "💥 Apolo 13 (1970)",
            "apolo13_text": "La explosión de un tanque de oxígeno demostró la vulnerabilidad crítica de los sistemas de soporte vital presurizados en ruta hacia la Luna.",
            "artemis_title": "⚠️ Misiones Recientes (Artemis II)",
            "artemis_text": "Alertamientos tempranos por presencia de humo recuerdan que el riesgo de incendios sigue latente a grandes distancias de la Tierra.",
            
            "sec4_header": "4. Factores de Riesgo en Hábitats Espaciales y Rovers",
            "sec4_intro": "Las condiciones operativas de las estaciones orbitales, bases lunares, marcianas y rovers presurizados incrementan la probabilidad de ignición y propagación rápida:",
            "risk1_title": "🧪 Atmósferas Enriquecidas",
            "risk1_text": "Para compatibilizar trajes y mitigar descompresión, los hábitats operan con concentraciones de oxígeno superiores al 30% (frente al 21% terrestre), elevando exponencialmente la inflamabilidad.",
            "risk2_title": "⚡ Fuentes de Ignición Eléctrica",
            "risk2_text": "Fallos en el cableado, cortocircuitos o arcos eléctricos cerca de paneles de control activos.",
            "risk3_title": "🛠️ Sistemas de Soporte Vital",
            "risk3_text": "Los botes de oxígeno (SFOG) representan puntos críticos de fallo si se contaminan con hidrocarburos, sustancias orgánicas o residuos de manipulación.",
            "risk4_title": "💨 Dinámica de Ventilación Forzada",
            "risk4_text": "A diferencia de la Tierra, los sistemas de aire acondicionado transportan y suministran oxígeno de manera constante al frente de fuego, facilitando una propagación rápida y silenciosa.",
            
            "sec5_header": "5. Aplicación Práctica: Del Dato Científico a la Ingeniería de Seguridad",
            "sec5_text": "Para mitigar estos riesgos, el aprovechamiento de bases de datos experimentales (como la base Physical Science Informatics - PSI de la NASA) resulta fundamental. "
                         "Mediante el uso de herramientas inteligentes de síntesis, clasificación e interpretación de datos, los ingenieros pueden estructurar de manera óptima las tres fases defensivas del ciclo de vida del fuego:",
            "f1_title": "1️⃣ Prevención",
            "f1_text": "Selección estricta de materiales y modelado predictivo de inflamabilidad bajo condiciones de gravedad reducida.",
            "f2_title": "2️⃣ Detección",
            "f2_text": "Calibración avanzada de sensores y umbrales de riesgo capaces de discriminar partículas de combustión frente a polvo o interferencias.",
            "f3_title": "3️⃣ Extinción",
            "f3_text": "Desarrollo e implementación de agentes supresores y procedimientos operativos eficaces en entornos confinados de microgravedad."
        }
    }

    lang_dict = t[st.session_state.lang]

    # Contenido de la página
    st.title(lang_dict["title"])
    st.markdown("---")

    # Sección 1
    st.header(lang_dict["sec1_header"])
    st.write(lang_dict["sec1_text"])

    st.markdown("---")

    # Sección 2
    st.header(lang_dict["sec2_header"])
    st.write(lang_dict["sec2_p1"])
    st.write(lang_dict["sec2_p2"])

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.subheader(lang_dict["c1_title"])
            st.markdown(lang_dict["c1_text"])

    with col2:
        with st.container(border=True):
            st.subheader(lang_dict["c2_title"])
            st.markdown(lang_dict["c2_text"])

    with col3:
        with st.container(border=True):
            st.subheader(lang_dict["c3_title"])
            st.markdown(lang_dict["c3_text"])

    st.markdown("---")

    # Sección 3
    st.header(lang_dict["sec3_header"])
    st.write(lang_dict["sec3_intro"])

    col_h1, col_h2 = st.columns(2)

    with col_h1:
        with st.container(border=True):
            st.subheader(lang_dict["apolo1_title"])
            st.markdown(lang_dict["apolo1_text"])

        with st.container(border=True):
            st.subheader(lang_dict["mir_title"])
            st.markdown(lang_dict["mir_text"])

    with col_h2:
        with st.container(border=True):
            st.subheader(lang_dict["apolo13_title"])
            st.markdown(lang_dict["apolo13_text"])

        with st.container(border=True):
            st.subheader(lang_dict["artemis_title"])
            st.markdown(lang_dict["artemis_text"])

    st.markdown("---")

    # Sección 4
    st.header(lang_dict["sec4_header"])
    st.write(lang_dict["sec4_intro"])

    risk_col1, risk_col2 = st.columns(2)

    with risk_col1:
        with st.container(border=True):
            st.subheader(lang_dict["risk1_title"])
            st.markdown(lang_dict["risk1_text"])

        with st.container(border=True):
            st.subheader(lang_dict["risk2_title"])
            st.markdown(lang_dict["risk2_text"])

    with risk_col2:
        with st.container(border=True):
            st.subheader(lang_dict["risk3_title"])
            st.markdown(lang_dict["risk3_text"])

        with st.container(border=True):
            st.subheader(lang_dict["risk4_title"])
            st.markdown(lang_dict["risk4_text"])

    st.markdown("---")

    # Sección 5
    st.header(lang_dict["sec5_header"])
    st.write(lang_dict["sec5_text"])

    f1, f2, f3 = st.columns(3)

    with f1:
        with st.container(border=True):
            st.subheader(lang_dict["f1_title"])
            st.markdown(lang_dict["f1_text"])

    with f2:
        with st.container(border=True):
            st.subheader(lang_dict["f2_title"])
            st.markdown(lang_dict["f2_text"])

    with f3:
        with st.container(border=True):
            st.subheader(lang_dict["f3_title"])
            st.markdown(lang_dict["f3_text"])

if __name__ == "__main__":
    show_scientific_background_page()