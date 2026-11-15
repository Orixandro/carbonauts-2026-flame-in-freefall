import streamlit as st

def show_scientific_background_page():
    # Configuración de la página (opcional si ya se define en el archivo principal)
    st.set_page_config(
        page_title="Scientific Background - Carbonauts",
        page_icon="🚀",
        layout="wide"
    )

    st.title("Marco Teórico: Seguridad contra Incendios en Entornos Espaciales")
    st.markdown("---")

    # Sección 1: Introducción y Justificación del Problema
    st.header("1. Introducción y Justificación del Problema")
    st.write(
        "Los procesos de combustión se encuentran entre los fenómenos más complejos y críticos para la seguridad en la "
        "exploración espacial tripulada. A diferencia de los entornos terrestres, el control del fuego en hábitats confinados "
        "fuera de la Tierra representa una de las mayores amenazas operacionales. La gestión inadecuada de los riesgos de ignición "
        "pone en peligro directo la vida de la tripulación y la viabilidad de misiones de larga duración hacia la Luna, Marte y más allá."
    )

    st.markdown("---")

    # Sección 2: Comportamiento del Fuego en Microgravedad
    st.header("2. Comportamiento del Fuego en Microgravedad")
    st.write(
        "En la Tierra, la combustión está fuertemente condicionada por la gravedad debido a los gradientes de densidad (flotabilidad), "
        "donde los gases calientes ascienden y generan corrientes convectivas que dan a la llama su característica forma y alimentan el flujo de oxígeno."
    )
    st.write(
        "En condiciones de microgravedad (caída libre), la ausencia de flotabilidad altera radicalmente la física del fuego:"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.subheader("🌀 Sin Convección Natural")
            st.markdown(
                "Los gases calientes no se desplazan verticalmente, eliminando el parpadeo de las llamas "
                "y simplificando el sistema hacia dinámicas de difusión molecular unidimensionales."
            )

    with col2:
        with st.container(border=True):
            st.subheader("🔵 Morfología Esférica")
            st.markdown(
                "Las llamas adoptan una estructura esférica y difusa (frecuentemente de tonalidad azulada) "
                "que depende exclusivamente de la lenta difusión molecular del oxígeno para mantenerse."
            )

    with col3:
        with st.container(border=True):
            st.subheader("⚠️ Límites de Propagación")
            st.markdown(
                "Materiales sólidos y líquidos presentan umbrales de inflamabilidad diferentes a la gravedad terrestre (1g), "
                "demostrando que los estándares tradicionales no siempre son conservativos."
            )

    st.markdown("---")

    # Sección 3: Antecedentes Históricos y Accidentes Críticos
    st.header("3. Antecedentes Históricos y Accidentes Críticos")
    st.write(
        "La historia aeroespacial ha estado marcada por incidentes graves que han impulsado la evolución normativa "
        "(como los estándares de la serie NASA-STD-6001):"
    )

    col_h1, col_h2 = st.columns(2)

    with col_h1:
        with st.container(border=True):
            st.subheader("🚀 Apolo 1 (1967)")
            st.markdown(
                "Un arco eléctrico en una atmósfera de oxígeno puro a presión provocó un incendio letal en la fase de pruebas, "
                "exigiendo un rediseño absoluto de los materiales y composiciones atmosféricas a bordo."
            )

        with st.container(border=True):
            st.subheader("🛰️ Estación Espacial Mir (1997)")
            st.markdown(
                "El fallo de un generador de oxígeno de combustible sólido (SFOG) desató un incendio intenso y denso humo "
                "que comprometió temporalmente el acceso a una cápsula de escape."
            )

    with col_h2:
        with st.container(border=True):
            st.subheader("💥 Apolo 13 (1970)")
            st.markdown(
                "La explosión de un tanque de oxígeno demostró la vulnerabilidad crítica de los sistemas de soporte vital "
                "presurizados en ruta hacia la Luna."
            )

        with st.container(border=True):
            st.subheader("⚠️ Misiones Recientes (Artemis II)")
            st.markdown(
                "Alertamientos tempranos por presencia de humo recuerdan que el riesgo de incendios sigue latente "
                "a grandes distancias de la Tierra."
            )

    st.markdown("---")

    # Sección 4: Factores de Riesgo en Hábitats Espaciales y Rovers
    st.header("4. Factores de Riesgo en Hábitats Espaciales y Rovers")
    st.write(
        "Las condiciones operativas de las estaciones orbitales, bases lunares, marcianas y rovers presurizados "
        "incrementan la probabilidad de ignición y propagación rápida:"
    )

    risk_col1, risk_col2 = st.columns(2)

    with risk_col1:
        with st.container(border=True):
            st.subheader("🧪 Atmósferas Enriquecidas")
            st.markdown(
                "Para compatibilizar trajes y mitigar descompresión, los hábitats operan con concentraciones de oxígeno "
                "superiores al 30% (frente al 21% terrestre), elevando exponencialmente la inflamabilidad."
            )

        with st.container(border=True):
            st.subheader("⚡ Fuentes de Ignición Eléctrica")
            st.markdown(
                "Fallos en el cableado, cortocircuitos o arcos eléctricos cerca de paneles de control activos."
            )

    with risk_col2:
        with st.container(border=True):
            st.subheader("🛠️ Sistemas de Soporte Vital")
            st.markdown(
                "Los botes de oxígeno (SFOG) representan puntos críticos de fallo si se contaminan con hidrocarburos, "
                "sustancias orgánicas o residuos de manipulación."
            )

        with st.container(border=True):
            st.subheader("💨 Dinámica de Ventilación Forzada")
            st.markdown(
                "A diferencia de la Tierra, los sistemas de aire acondicionado transportan y suministran oxígeno de manera "
                "constante al frente de fuego, facilitando una propagación rápida y silenciosa."
            )

    st.markdown("---")

    # Sección 5: Aplicación Práctica: Del Dato Científico a la Ingeniería de Seguridad
    st.header("5. Aplicación Práctica: Del Dato Científico a la Ingeniería de Seguridad")
    st.write(
        "Para mitigar estos riesgos, el aprovechamiento de bases de datos experimentales (como la base Physical Science Informatics - PSI de la NASA) "
        "resulta fundamental. Mediante el uso de herramientas inteligentes de síntesis, clasificación e interpretación de datos, "
        "los ingenieros pueden estructurar de manera óptima las tres fases defensivas del ciclo de vida del fuego:"
    )

    f1, f2, f3 = st.columns(3)

    with f1:
        with st.container(border=True):
            st.subheader("1️⃣ Prevención")
            st.markdown(
                "Selección estricta de materiales y modelado predictivo de inflamabilidad bajo condiciones de gravedad reducida."
            )

    with f2:
        with st.container(border=True):
            st.subheader("2️⃣ Detección")
            st.markdown(
                "Calibración avanzada de sensores y umbrales de riesgo capaces de discriminar partículas de combustión frente a polvo o interferencias."
            )

    with f3:
        with st.container(border=True):
            st.subheader("3️⃣ Extinción")
            st.markdown(
                "Desarrollo e implementación de agentes supresores y procedimientos operativos eficaces en entornos confinados de microgravedad."
            )

if __name__ == "__main__":
    show_scientific_background_page()