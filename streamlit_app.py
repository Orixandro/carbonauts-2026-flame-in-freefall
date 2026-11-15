import streamlit as st

# Navegacion

pagina_principal = st.Page("pages/1_AI_Browser.py", title="AI Powered Data Browser", icon="🚀", default=True)
pagina_about = st.Page("pages/2_About_Us.py", title="About Us", icon="👥")
pagina_info = st.Page("pages/3_Scientific_Background.py", title="Scientific Background", icon="📋")

pg = st.navigation([pagina_principal, pagina_about, pagina_info])

pg.run()