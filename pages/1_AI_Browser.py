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

# Configuración básica de NLTK
nltk_data_dir = os.path.expanduser('~/nltk_data')
os.makedirs(nltk_data_dir, exist_ok=True)
if nltk_data_dir not in nltk.data.path:
    nltk.data.path.append(nltk_data_dir)

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

st.set_page_config(page_title="Flame in Freefall - Carbonauts", page_icon="🚀", layout="wide")

st.title("Flame in Freefall: SI-Powered Fire Safety Insights")
st.markdown("Explore NASA's microgravity combustion data using Artificial Intelligence.")
st.markdown(
    '<p style="color: #808080; font-size: 0.85em; font-style: italic;">'
    '<strong>Disclaimer:</strong> This model has been trained exclusively using files from research studies 117, 159, and 10. '
    'The AI model is not exhaustive and may omit certain information in some cases.'
    '</p>',
    unsafe_allow_html=True
)

api_key = st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error("GEMINI_API_KEY not configured.")
    st.stop()

hf_token = st.secrets.get("HF_TOKEN")
os.environ["GEMINI_API_KEY"] = api_key
if hf_token:
    os.environ["HF_TOKEN"] = hf_token

@st.cache_resource
def inicializar_rag():
    global case_loaded
    global case_created
    
    # LLM en la nube
    llm = Gemini(model="models/gemini-3.5-flash-lite", api_key=api_key)
    
    # --- CAMBIO CLAVE: Modelo de Embeddings de Alta Gama ---
    # Usamos BAAI/bge-large-en-v1.5 para una comprensión semántica y científica superior
    # embed_model = HuggingFaceEmbedding(model_name="all-mpnet-base-v2")
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-large-en-v1.5")
    
    Settings.llm = llm
    Settings.embed_model = embed_model
    
    # Parámetros de fragmentación de alta precisión
    Settings.chunk_size = 512
    Settings.chunk_overlap = 64

    persist_dir = "./vector_store"
    
    if os.path.exists(persist_dir) and os.listdir(persist_dir):
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        index = load_index_from_storage(storage_context)
        case_loaded = True
    else:
        if os.path.exists("data") and os.listdir("data"):
            cleaned_documents = []
            
            for file_name in os.listdir("data"):
                if file_name.lower().endswith(".pdf"):
                    file_path = os.path.join("data", file_name)
                    doc_pymupdf = pymupdf.open(file_path)
                    
                    # --- FILTRO ANTI-DEDICATORIAS ---
                    # Nos saltamos las primeras páginas (portada, índice, dedicatorias suelen estar entre la 1 y la 4 o 5)
                    # Ajusta este rango si tu paper empieza antes o después.
                    # pagina_inicio = min(4, len(doc_pymupdf) - 1)
                    
                    for page_num in range(0, len(doc_pymupdf)):
                        page = doc_pymupdf[page_num]
                        text = page.get_text()
                        
                        if text and len(text.strip()) > 30:
                            # Evitar indexar páginas que traten exclusivamente de agradecimientos o dedicatorias
                            lower_text = text.lower()
                            if "dedication" in lower_text or "acknowledgments" in lower_text and len(text.strip()) < 500:
                                continue
                                
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
            
    return index.as_query_engine(similarity_top_k=6)

query_engine = inicializar_rag()

if query_engine is None:
    st.warning("No valid documents found in `data/`. Scientific PDFs missing.")
else:
    if case_loaded:
        st.success("Existing model found and loaded successfully!")
    if case_created:
        st.success("Knowledge base successfully loaded and vectorized locally with BGE-Large!")
    
    pregunta = st.text_input("Ask a question about fire safety in microgravity:")
    
    if st.button("Query RAG 🔎"):
        if pregunta:
            with st.spinner("Analyzing NASA research with BGE-Large & Gemini..."):
                respuesta = query_engine.query(pregunta)
                st.subheader("Answer:")
                st.write(str(respuesta))
        else:
            st.warning("Please write a question.")