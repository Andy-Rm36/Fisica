import streamlit as st

import streamlit.components.v1 as components

components.html(
    """
    <link href="https://fonts.googleapis.com/css2?family=Varela+Round&display=swap" rel="stylesheet"> 
    <h1 style="font-family: 'Varela Round', serif; color: #464646;  font-size: 30px;">
        Bibliografía
    </h1>
    """,
    height=70
)

st.markdown("""- Comunidad de Madrid. Campos electromagnéticos. https://www.comunidad.madrid/servicios/salud/campos-electromagneticos
- TOPREGAL. Carga puntual. https://www.topregal.es/es/glosario/carga-puntual.html

""")
