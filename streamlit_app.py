import os
import streamlit as st
from google import genai
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.llms.gemini import Gemini

import nltk

# 1. Configurar un directorio seguro para NLTK en el usuario para evitar el aviso de permisos
nltk_data_dir = os.path.expanduser('~/nltk_data')
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.data.path.insert(0, nltk_data_dir)

# 2. Descargar automáticamente los recursos necesarios si no están presentes
for resource in ['stopwords', 'punkt']:
    try:
        if resource == 'stopwords':
            nltk.data.find('corpora/stopwords')
        else:
            nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download(resource, download_dir=nltk_data_dir, quiet=True)

# 1. Configurar la página de Streamlit
st.set_page_config(page_title="Flame in Freefall - NASA RAG", page_icon="🚀", layout="wide")

st.title("Flame in Freefall: SI-Powered Fire Safety Insights")
st.markdown("Explora los datos de combustión en microgravedad de la NASA mediante Inteligencia Artificial.")

# 2. Configurar la clave de API desde los secretos de Streamlit
api_key = st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error("Falta configurar la GEMINI_API_KEY en los secretos de Streamlit.")
    st.stop()

# Configurar el entorno para Google GenAI
os.environ["GEMINI_API_KEY"] = api_key

# 3. Inicializar los modelos de LlamaIndex usando exclusivamente la API de Gemini
@st.cache_resource
def inicializar_rag():
    # Modelo generativo de Gemini
    llm = Gemini(model="models/gemini-2.5-flash", api_key=api_key)
    
    # Modelo de embeddings oficial de Google por API (cero espacio local requerido)
    embed_model = GeminiEmbedding(model_name="gemini-embedding-2", api_key=api_key)
    
    Settings.llm = llm
    Settings.embed_model = embed_model
    
    # Cargar documentos desde la carpeta 'data'
    if os.path.exists("data") and os.listdir("data"):
        documents = SimpleDirectoryReader("data").load_data()
        index = VectorStoreIndex.from_documents(documents)
        return index.as_query_engine()
    return None

query_engine = inicializar_rag()

# 4. Interfaz de Chat / Consultas
if query_engine is None:
    st.warning("⚠️ No se encontraron documentos en la carpeta `data/`. Sube algunos PDFs de investigación de la PSI para empezar.")
else:
    st.success("¡Base de conocimiento cargada correctamente desde los documentos de la NASA!")
    
    pregunta = st.text_input("Haz una pregunta sobre seguridad contra incendios en microgravedad:")
    
    if st.button("Consultar RAG"):
        if pregunta:
            with st.spinner("Analizando investigaciones de la NASA con Gemini..."):
                respuesta = query_engine.query(pregunta)
                st.subheader("Respuesta:")
                st.write(str(respuesta))
        else:
            st.warning("Por favor, escribe una pregunta.")