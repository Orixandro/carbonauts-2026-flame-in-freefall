import streamlit as st

def show_about_page():
    # Configuración de la página
    st.set_page_config(
        page_title="About us - Carbonauts",
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
            "title": "About Us: Carbonauts",
            "who_we_are_header": "Who We Are",
            "who_we_are_p1": "We are **Carbonauts**, a multidisciplinary team born in Bilbao with a clear goal: "
                             "to use engineering, artificial intelligence, and design to make future space exploration safer.",
            "who_we_are_p2": "We are participating in the **2026 NASA Space Apps Challenge (Bilbao location)** tackling the **Flame in Freefall** challenge. "
                             "Our mission is to transform decades of complex NASA microgravity combustion scientific experiments into an interactive dashboard powered by Superintelligence (SI). "
                             "By doing so, we facilitate access to critical information to prevent and manage fires both in future crewed missions to the Moon and Mars "
                             "and in safety applications right here on Earth.",
            "team_header": "The Team Behind Carbonauts",
            "team_intro": "We combine technical industrial engineering profiles with the creativity of graphic and audiovisual design "
                          "to build a powerful, rigorous, and intuitive tool:",
            "irune_role": "**Project Leader & Aerospace Safety Specialist**",
            "irune_form": "- **Background:** Industrial Technology Engineering student.",
            "irune_desc": "- **Role:** Directs general team coordination, schedule planning, and the final pitch presentation. "
                          "Additionally, she leads the technical validation of experimental data on microgravity combustion and flammability.",
            "haritz_role": "**Team Management, Art Direction & Quality Control**",
            "haritz_form": "- **Background:** Industrial Technology Engineering (Master's student).",
            "haritz_desc": "- **Role:** Supervises project cohesion and internal organization, provides criteria in art direction, "
                          "and conducts comprehensive product reviews to ensure every technical and visual detail meets the highest standards.",
            "alejandro_role": "**Data Engineer, AI & UX/UI Designer**",
            "alejandro_form": "- **Background:** Industrial Technology Engineering (Master's student).",
            "alejandro_desc": "- **Role:** Responsible for processing dataset files from NASA's PSI repository and developing the Superintelligence (SI) model. "
                              "He also designs the visual and interactive architecture of the web platform to translate complex metrics into clear, actionable visualizations.",
            "ugaitz_role": "**Art Director, Graphic Design & Audiovisual Production**",
            "ugaitz_form": "- **Background:** Graphic Design student.",
            "ugaitz_desc": "- **Role:** Gives visual identity to the project. In charge of global graphic design, brand aesthetics, "
                          "and the editing and assembly of the official video used to present our solution to the jury.",
            "vision_header": "Our Vision",
            "vision_text": "We believe scientific data only reaches its true potential when it is understandable and accessible. "
                           "From Bilbao to space, at Carbonauts we work to bridge the gap between NASA's combustion science and the digital tools of tomorrow."
        },
        "Español": {
            "title": "Sobre Nosotros: Carbonauts",
            "who_we_are_header": "Quiénes somos",
            "who_we_are_p1": "Somos **Carbonauts**, un equipo multidisciplinar nacido en Bilbao con un objetivo claro: "
                             "utilizar la ingeniería, la inteligencia artificial y el diseño para hacer que la exploración espacial "
                             "del futuro sea más segura.",
            "who_we_are_p2": "Participamos en el **2026 NASA Space Apps Challenge (sede Bilbao)** afrontando el reto **Flame in Freefall**. "
                             "Nuestra misión es transformar décadas de complejos experimentos científicos de la NASA sobre combustión en microgravedad "
                             "en un panel interactivo impulsado por Superinteligencia (SI). De este modo, facilitamos el acceso a información crítica "
                             "para prevenir y gestionar incendios tanto en futuras misiones tripuladas a la Luna y Marte como en aplicaciones de seguridad "
                             "aquí en la Tierra.",
            "team_header": "El Equipo detrás de Carbonauts",
            "team_intro": "Combinamos perfiles técnicos de ingeniería industrial con la creatividad del diseño gráfico y audiovisual "
                          "para construir una herramienta potente, rigurosa e intuitiva:",
            "irune_role": "**Líder de Proyecto y Especialista en Seguridad Aeroespacial**",
            "irune_form": "- **Formación:** Estudiante de Ingeniería en Tecnología Industrial.",
            "irune_desc": "- **Rol:** Dirige la coordinación general del equipo, la planificación del cronograma "
                          "y la presentación del pitch final. Además, lidera la validación técnica de los datos "
                          "experimentales sobre combustión en microgravedad e inflamabilidad.",
            "haritz_role": "**Gestión de Equipo, Dirección de Arte y Control de Calidad**",
            "haritz_form": "- **Formación:** Ingeniero en Tecnología Industrial (estudiante de Máster).",
            "haritz_desc": "- **Rol:** Supervisa la cohesión y organización interna del proyecto, aporta criterio "
                          "en la dirección artística y se encarga de la revisión integral del producto para garantizar "
                          "que cada detalle técnico y visual cumpla con los más altos estándares.",
            "alejandro_role": "**Ingeniero de Datos, IA y Diseñador UX/UI**",
            "alejandro_form": "- **Formación:** Ingeniero en Tecnología Industrial (estudiante de Máster).",
            "alejandro_desc": "- **Rol:** Responsable de procesar los conjuntos de datos del repositorio PSI de la NASA "
                              "y desarrollar el modelo de Superinteligencia (SI). También diseña la arquitectura visual e "
                              "interactiva de la plataforma web para traducir métricas complejas en visualizaciones claras y accionables.",
            "ugaitz_role": "**Director de Arte, Diseño Gráfico y Producción Audiovisual**",
            "ugaitz_form": "- **Formación:** Estudiante de Diseño Gráfico.",
            "ugaitz_desc": "- **Rol:** Da identidad visual al proyecto. Se encarga del diseño gráfico global, "
                          "la estética de la marca y la edición y montaje del vídeo oficial con el que presentamos "
                          "nuestra solución ante el jurado.",
            "vision_header": "Nuestra Visión",
            "vision_text": "Creemos que los datos científicos sólo alcanzan su verdadero potencial cuando son comprensibles y accesibles. "
                           "Desde Bilbao hacia el espacio, en Carbonauts trabajamos para tender un puente entre la ciencia de la combustión "
                           "de la NASA y las herramientas digitales del mañana."
        }
    }

    lang_dict = t[st.session_state.lang]

    # Contenido de la página
    st.title(lang_dict["title"])
    st.markdown("---")

    # Sección: Quiénes somos
    st.header(lang_dict["who_we_are_header"])
    st.write(lang_dict["who_we_are_p1"])
    st.write(lang_dict["who_we_are_p2"])

    st.markdown("---")

    # Sección: El Equipo detrás de Carbonauts
    st.header(lang_dict["team_header"])
    st.write(lang_dict["team_intro"])

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("Irune")
            st.markdown(lang_dict["irune_role"])
            st.markdown(lang_dict["irune_form"])
            st.markdown(lang_dict["irune_desc"])

        with st.container(border=True):
            st.subheader("Haritz")
            st.markdown(lang_dict["haritz_role"])
            st.markdown(lang_dict["haritz_form"])
            st.markdown(lang_dict["haritz_desc"])

    with col2:
        with st.container(border=True):
            st.subheader("Alejandro")
            st.markdown(lang_dict["alejandro_role"])
            st.markdown(lang_dict["alejandro_form"])
            st.markdown(lang_dict["alejandro_desc"])

        with st.container(border=True):
            st.subheader("Ugaitz")
            st.markdown(lang_dict["ugaitz_role"])
            st.markdown(lang_dict["ugaitz_form"])
            st.markdown(lang_dict["ugaitz_desc"])

    st.markdown("---")

    # Sección: Nuestra Visión
    st.header(lang_dict["vision_header"])
    st.write(lang_dict["vision_text"])

if __name__ == "__main__":
    show_about_page()