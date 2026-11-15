import streamlit as st

# Navegacion

pagina_principal = st.Page("pages/1_AI_Browser.py", title="AI Powered Data Browser", icon="🚀", default=True)
pagina_datos = st.Page("pages/2_Data_Library.py", title="Data Library", icon="💾")
pagina_about = st.Page("pages/3_About_Us.py", title="About Us", icon="👥")
pagina_info = st.Page("pages/4_Scientific_Background.py", title="Scientific Background", icon="🔬")

pg = st.navigation([pagina_principal, pagina_datos, pagina_about, pagina_info])

pg.run()