import streamlit as st

import streamlit.components.v1 as components

components.html(
    """
    <link href="https://fonts.googleapis.com/css2?family=Varela+Round&display=swap" rel="stylesheet"> 
    <h1 style="font-family: 'Varela Round', serif; color: #464646;  font-size: 40px;">
        ⚡ Simuladores de Campos Eléctricos y Magnéticos
    </h1>
    """,
    height=150
)
st.markdown("""Equipo:
- Andrea Romero García.
- Jose de Jesus Cabrera Joaquin.
- Hector Hugo Bautista Martínez""" )

st.markdown("""En esta página se encuentran 4 simuladores, los cuales calcularan 
el campo magnetico de cada elemento dependiendo de los valores que se le ajusten en las barras, mostrando el
            cambio que tienen en las gráficas.""")
st.markdown("Selecciona una simulación en el menú de la izquierda para probarlos.")

st.markdown(
    """
    <div style='text-align: center; margin-top: 50px;'>
        <img src='https://www.atleuropa.es/wp-content/uploads/2018/04/2000px-VFPt_charges_plus_minus_thumb.svg_-1024x768.png' width='300'>
    </div>
    """,
    unsafe_allow_html=True
)

components.html(
    """
    <link href="https://fonts.googleapis.com/css2?family=Varela+Round&display=swap" rel="stylesheet"> 
    <h1 style="font-family: 'Varela Round', serif; color: #464646;  font-size: 20px;">
        ¿Qué es el campo magnetico?
    </h1>
    """,
    height=50
)

st.markdown("""Para entender los simuladores primero necesitamos saber que un campo electromagnético 
es la combinación de campos eléctricos y magnéticos que se producen por la oscilación o aceleración de 
cargas eléctricas. Estas ondas pueden viajar a través del vacío y son responsables de diversas interacciones 
en el universo, como la electricidad en nuestros hogares. """)
