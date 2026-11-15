import streamlit as st

def show_about_page():
    # Configuración de la página (opcional si ya se define en el archivo principal)
    st.set_page_config(
        page_title="About us - Carbonauts",
        page_icon="🚀",
        layout="wide"
    )

    st.title("Sobre Nosotros: Carbonauts")
    st.markdown("---")

    # Sección: Quiénes somos
    st.header("Quiénes somos")
    st.write(
        "Somos **Carbonauts**, un equipo multidisciplinar nacido en Bilbao con un objetivo claro: "
        "utilizar la ingeniería, la inteligencia artificial y el diseño para hacer que la exploración espacial "
        "del futuro sea más segura."
    )
    st.write(
        "Participamos en el **2026 NASA Space Apps Challenge (sede Bilbao)** afrontando el reto **Flame in Freefall**. "
        "Nuestra misión es transformar décadas de complejos experimentos científicos de la NASA sobre combustión en microgravedad "
        "en un panel interactivo impulsado por Superinteligencia (SI). De este modo, facilitamos el acceso a información crítica "
        "para prevenir y gestionar incendios tanto en futuras misiones tripuladas a la Luna y Marte como en aplicaciones de seguridad "
        "aquí en la Tierra."
    )

    st.markdown("---")

    # Sección: El Equipo detrás de Carbonauts
    st.header("El Equipo detrás de Carbonauts")
    st.write(
        "Combinamos perfiles técnicos de ingeniería industrial con la creatividad del diseño gráfico y audiovisual "
        "para construir una herramienta potente, rigurosa e intuitiva:"
    )

    # Distribución en columnas para mostrar los perfiles de forma visual y ordenada
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("Irune")
            st.markdown("**Líder de Proyecto y Especialista en Seguridad Aeroespacial**")
            st.markdown("- **Formación:** Estudiante de Ingeniería en Tecnología Industrial.")
            st.markdown(
                "- **Rol:** Dirige la coordinación general del equipo, la planificación del cronograma "
                "y la presentación del pitch final. Además, lidera la validación técnica de los datos "
                "experimentales sobre combustión en microgravedad e inflamabilidad."
            )

        with st.container(border=True):
            st.subheader("Haritz")
            st.markdown("**Gestión de Equipo, Dirección de Arte y Control de Calidad**")
            st.markdown("- **Formación:** Ingeniero en Tecnología Industrial (estudiante de Máster).")
            st.markdown(
                "- **Rol:** Supervisa la cohesión y organización interna del proyecto, aporta criterio "
                "en la dirección artística y se encarga de la revisión integral del producto para garantizar "
                "que cada detalle técnico y visual cumpla con los más altos estándares."
            )

    with col2:
        with st.container(border=True):
            st.subheader("Alejandro")
            st.markdown("**Ingeniero de Datos, IA y Diseñador UX/UI**")
            st.markdown("- **Formación:** Ingeniero en Tecnología Industrial (estudiante de Máster).")
            st.markdown(
                "- **Rol:** Responsable de procesar los conjuntos de datos del repositorio PSI de la NASA "
                "y desarrollar el modelo de Superinteligencia (SI). También diseña la arquitectura visual e "
                "interactiva de la plataforma web para traducir métricas complejas en visualizaciones claras y accionables."
            )

        with st.container(border=True):
            st.subheader("Ugaitz")
            st.markdown("**Director de Arte, Diseño Gráfico y Producción Audiovisual**")
            st.markdown("- **Formación:** Estudiante de Diseño Gráfico.")
            st.markdown(
                "- **Rol:** Da identidad visual al proyecto. Se encarga del diseño gráfico global, "
                "la estética de la marca y la edición y montaje del vídeo oficial con el que presentamos "
                "nuestra solución ante el jurado."
            )

    st.markdown("---")

    # Sección: Nuestra Visión
    st.header("Nuestra Visión")
    st.write(
        "Creemos que los datos científicos sólo alcanzan su verdadero potencial cuando son comprensibles y accesibles. "
        "Desde Bilbao hacia el espacio, en Carbonauts trabajamos para tender un puente entre la ciencia de la combustión "
        "de la NASA y las herramientas digitales del mañana."
    )

if __name__ == "__main__":
    show_about_page()