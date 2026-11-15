import os
import streamlit as st
import pymupdf  # PyMuPDF para lectura robusta de PDFs de la NASA
from llama_index.core import (
    Settings, 
    VectorStoreIndex, 
    StorageContext, 
    load_index_from_storage, 
    Document
)
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
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

case_loaded = False
case_created = False

# 3. Configurar la página de Streamlit
st.set_page_config(page_title="Flame in Freefall - Carbonauts", page_icon="🚀", layout="wide")

st.title("Flame in Freefall: SI-Powered Fire Safety Insights")
st.markdown("Explore NASA's microgravity combustion data using Artificial Intelligence.")

# 4. Configurar la clave de API desde los secretos de Streamlit
api_key = st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error("GEMINI_API_KEY not configured.")
    st.stop()

hf_token = st.secrets.get("HF_TOKEN")

# Configurar el entorno para Google GenAI
os.environ["GEMINI_API_KEY"] = api_key

if hf_token:
    os.environ["HF_TOKEN"] = hf_token

# 5. Inicializar el RAG: HuggingFace local para embeddings + Gemini Cloud para respuestas
@st.cache_resource
def inicializar_rag():
    global case_loaded
    global case_created
    # Modelo generativo de Gemini en la nube para redactar respuestas
    llm = Gemini(model="models/gemini-3.5-flash-lite", api_key=api_key)
    
    # Modelo de embeddings ejecutándose localmente (evita límites de cuota en la API)
    embed_model = HuggingFaceEmbedding(model_name="all-MiniLM-L6-v2")
    
    Settings.llm = llm
    Settings.embed_model = embed_model

    persist_dir = "./vector_store"
    
    if os.path.exists(persist_dir) and os.listdir(persist_dir):
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        index = load_index_from_storage(storage_context)
        case_loaded = True
    else:
        if os.path.exists("data") and os.listdir("data"):
            cleaned_documents = []
            
            # Recorremos los PDFs de la carpeta data usando PyMuPDF (pymupdf)
            for file_name in os.listdir("data"):
                if file_name.lower().endswith(".pdf"):
                    file_path = os.path.join("data", file_name)
                    doc_pymupdf = pymupdf.open(file_path)
                    
                    for page_num in range(len(doc_pymupdf)):
                        page = doc_pymupdf[page_num]
                        text = page.get_text()
                        
                        # Limpiamos caracteres extraños y nos aseguramos de que no esté vacía
                        if text and len(text.strip()) > 20:
                            safe_text = text.encode("utf-8", "ignore").decode("utf-8")
                            cleaned_documents.append(
                                Document(
                                    text=safe_text, 
                                    metadata={"file_name": file_name, "page": page_num + 1}
                                )
                            )
            
            if not cleaned_documents:
                return None
                
            index = VectorStoreIndex.from_documents(cleaned_documents)
            index.storage_context.persist(persist_dir=persist_dir)
            case_created = True
        else:
            return None
            
    return index.as_query_engine(similarity_top_k=5)

query_engine = inicializar_rag()

# 6. Interfaz de Chat / Consultas
if query_engine is None:
    st.warning("No valid documents found in `data/`. Scientific PDFs missing.")
else:
    if case_loaded:
        st.success("Existing model found and loaded successfully!")
    if case_created:
        st.success("Knowledge base successfully loaded and vectorized locally!")
    
    pregunta = st.text_input("Ask a question about fire safety in microgravity:")
    
    if st.button("Query RAG 🔎"):
        if pregunta:
            with st.spinner("Analyzing NASA research with Gemini..."):
                respuesta = query_engine.query(pregunta)
                st.subheader("Answer:")
                st.write(str(respuesta))
        else:
            st.warning("Please write a question.")