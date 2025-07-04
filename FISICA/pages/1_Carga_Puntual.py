import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

import streamlit.components.v1 as components

components.html(
    """
    <link href="https://fonts.googleapis.com/css2?family=Varela+Round&display=swap" rel="stylesheet"> 
    <h1 style="font-family: 'Varela Round', serif; color: #464646;  font-size: 40px;">
        🧲 Simulador de Campo Eléctrico de una Carga Puntual
    </h1>
    """,
    height=150
)

components.html(
    """
    <link href="https://fonts.googleapis.com/css2?family=Varela+Round&display=swap" rel="stylesheet"> 
    <h1 style="font-family: 'Varela Round', serif; color: #464646;  font-size: 20px;">
        ¿Qué es una carga puntual?
    </h1>
    """,
    height=40
)
st.markdown("""Es una idealización de la física clásica según la cual el tamaño, 
forma y estructura de un objeto son irrelevantes siempre y cuando su contexto así lo permita. 
En términos de masa, esto implica que el objeto en cuestión se piensa o se modela como un elemento 
infinitamente pequeño en su volumen. """)


components.html(
    """
    <link href="https://fonts.googleapis.com/css2?family=Varela+Round&display=swap" rel="stylesheet"> 
    <h1 style="font-family: 'Varela Round', serif; color: #464646;  font-size: 20px;">
        Lineas de campo
    </h1>
    """,
    height=40
)
st.markdown("""Debido a su polaridad las lineas de campo que genera son de formas diferente, mientras que una carga puntual 
positiva genera un campo eléctrico que sale radialmente hacia afuera desde la carga, una carga puntual negativa 
genera un campo eléctrico que entra radialmente hacia adentro de la carga""")

# Selec tipo de carga
carga = st.radio("Tipo de carga:", ["Positiva", "Negativa"])
q = 1 if carga == "Positiva" else -1

x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)

# Campo eléctrico 
k = 9e9
den = (X**2 + Y**2)**1.5 + 1e-9 
Ex = k * q * X / den
Ey = k * q * Y / den

# Graficas
fig, ax = plt.subplots()
ax.quiver(X, Y, Ex, Ey, color='red')
ax.plot(0, 0, 'bo' if q > 0 else 'ko', markersize=10) 
ax.set_title("Gráfico de la carga puntual")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')

# Mostrar graficas
st.pyplot(fig, clear_figure=True)
