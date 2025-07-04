import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

k = 9e9

import streamlit.components.v1 as components

components.html(
    """
    <link href="https://fonts.googleapis.com/css2?family=Varela+Round&display=swap" rel="stylesheet"> 
    <h1 style="font-family: 'Varela Round', serif; color: #464646;  font-size: 40px;">
        🧲 Campo Eléctrico de una barra 
    </h1>
    """,
    height=100
)

st.markdown("""
En el esquema encontramos que:
- EL punto **P** se encuentra a una distancia `d` a la izquierda del extremo de la barra.
- La barra tiene carga uniforme y longitud `ℓ`.
- El campo eléctrico se calcula en el punto `P` con la fórmula:
""")
st.latex(r"E = \frac{kQ}{d(d + ℓ)}")

# Datos
Q_uC = st.slider("Carga total Q (μC)", -10.0, 10.0, 5.0, step=0.1)
l = st.slider("Longitud de la barra ℓ (m)", 0.1, 2.0, 1.0, step=0.1)
d = st.slider("Distancia d del punto P a la barra (m)", 0.01, 3.0, 1.0, step=0.01)

Q = Q_uC * 1e-6  # μC → C

E = k * Q / (d * (d + l))

# Resultado
st.write(f"**Campo eléctrico en P (x = 0):** {E:.2e} N/C")

# ---------- GRAFICA ----------
fig, ax = plt.subplots(figsize=(9, 2))

# Barra
x_ini = d
x_fin = d + l
ax.plot([x_ini, x_fin], [0, 0], color='orange', linewidth=10, label='Barra cargada')

# Punto P 
ax.plot(0, 0, 'ko', label='Punto P')

# Campo eléctrico 
flecha_color = 'red' if Q > 0 else 'blue'
sentido = -1 if Q > 0 else 1
ax.arrow(0, 0, sentido * 0.5, 0, head_width=0.05, head_length=0.1,
         fc=flecha_color, ec=flecha_color, label='Campo eléctrico')


ax.text((x_ini + x_fin)/2, 0.1, 'Barra cargada (ℓ)', ha='center', color='orange')
ax.text(0, 0.1, 'P', ha='center', color='black')
ax.text(d/2, -0.1, 'd', ha='center', fontsize=10)
ax.annotate('', xy=(0, -0.05), xytext=(d, -0.05),
            arrowprops=dict(arrowstyle='<->', color='gray'))


# Ejes
ax.set_xlim(-1, x_fin + 1)
ax.set_ylim(-0.3, 0.3)
ax.set_yticks([])
ax.set_xlabel("Eje X (m)")
ax.legend()
ax.set_title("Configuración: punto antes de una barra cargada uniformemente")

st.pyplot(fig, clear_figure=True)
