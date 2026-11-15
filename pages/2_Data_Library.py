import os
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="NASA PSI Data Library", page_icon="🚀", layout="wide")

st.title("Explorador de Datos Experimentales: PSI-117")
st.markdown("Visualización de series temporales y parámetros de combustión extraídos de los CSVs de la NASA.")

# 1. Ruta del archivo ReadMe Excel maestro
excel_path = "data/csv_data/PSI-117_Analyzed Data_ReadMe_List_of_Data.xlsx"

@st.cache_data
def cargar_readme(path):
    if os.path.exists(path):
        return pd.read_excel(path)
    return None

df_readme = cargar_readme(excel_path)

if df_readme is None:
    st.error(f"⚠️ No se ha encontrado el archivo ReadMe en la ruta esperada: `{excel_path}`. Comprueba la estructura de tu carpeta `data/`.")
else:
    st.success("¡Índice de datos cargado correctamente!")
    
    # 2. Barra lateral para filtros (por ejemplo, por tipo de experimento / subcarpeta o combustible si existe la columna)
    st.sidebar.header("Filtros de Datos")
    
    # Intentamos detectar columnas clave de forma flexible
    columnas = df_readme.columns.tolist()
    st.sidebar.write(f"Columnas detectadas: {len(columnas)}")
    
    # Selector genérico basado en la primera columna disponible o nombre de archivo
    if len(columnas) > 0:
        selected_row_idx = st.sidebar.selectbox(
            "Selecciona un experimento / registro:",
            options=df_readme.index,
            format_func=lambda x: f"Registro {x} - {str(df_readme.iloc[x].values[:2])}"
        )
        
        # Mostrar los metadatos de ese experimento concreto
        st.subheader("Metadatos del Experimento Seleccionado")
        selected_meta = df_readme.loc[selected_row_idx]
        st.dataframe(selected_meta.to_frame(name="Valor"))
        
        # 3. Buscar y cargar el CSV asociado (asumiendo que hay una columna que indica el nombre del fichero o buscando en MST/PROC1)
        # Buscamos en las celdas de la fila seleccionada si alguna apunta a un archivo .csv
        csv_filename = None
        for val in selected_meta.values:
            if isinstance(val, str) and val.strip().endswith(".csv"):
                csv_filename = val.strip()
                break
        
        # Si no está explícito en una celda, permitimos buscar manualmente o barremos las carpetas MST / PROC1
        st.subheader("Gráfica del Experimento")
        
        # Listar todos los CSVs disponibles en MST y PROC1 para que el usuario pueda seleccionarlos directamente si lo prefiere
        all_csvs = []
        for root, dirs, files in os.walk("data/csv_data"):
            for file in files:
                if file.endswith(".csv"):
                    all_csvs.append(os.path.join(root, file))
        
        if all_csvs:
            chosen_csv = st.selectbox("O selecciona directamente un archivo CSV de la investigación:", all_csvs)
            
            if chosen_csv:
                try:
                    df_csv = pd.read_csv(chosen_csv)
                    st.write(f"Mostrando datos de: `{os.path.basename(chosen_csv)}`")
                    st.dataframe(df_csv.head())
                    
                    # Generar gráfica interactiva con Plotly si el CSV tiene al menos 2 columnas (ej. Tiempo y Variable)
                    if df_csv.shape[1] >= 2:
                        x_col = st.selectbox("Eje X (ej. Tiempo)", df_csv.columns, index=0)
                        y_col = st.selectbox("Eje Y (ej. Temperatura / Diámetro)", df_csv.columns, index=1 if len(df_csv.columns) > 1 else 0)
                        
                        fig = px.line(df_csv, x=x_col, y=y_col, title=f"Evolución de {y_col} frente a {x_col}")
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.warning("El CSV seleccionado no tiene suficientes columnas para una gráfica de líneas.")
                except Exception as e:
                    st.error(f"Error al leer el archivo CSV: {e}")
        else:
            st.warning("No se han encontrado archivos CSV en las subcarpetas de `data/csv_data`.")