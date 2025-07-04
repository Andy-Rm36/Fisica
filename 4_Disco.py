import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

k = 9e9

import streamlit.components.v1 as components

components.html(
    """
    <link href="https://fonts.googleapis.com/css2?family=Varela+Round&display=swap" rel="stylesheet"> 
    <h1 style="font-family: 'Varela Round', serif; color: #464646;  font-size: 40px;">
        🧲 Campo eléctrico de un disco cargado
    </h1>
    """,
    height=150
)

st.markdown(r"""
Este simulador ayuda a mostrar y calcular el campo eléctrico en el eje de un disco 
            cargado uniformemente, para esto estaremos utilizando la fórmula:
""")
st.latex(r"""E(x) = 2\pi k \sigma \left(1 - \frac{x}{\sqrt{R^2 + x^2}}\right)""")

st.markdown(r"""- El disco se encuentra en el plano **YZ**, centrado en el origen.
- La **flecha gris** indica la distancia \( x \) desde el centro al punto \( P \).
- La **flecha roja o azul** indica la dirección y magnitud del campo eléctrico en \( P \).""")

# Datos
sigma = st.slider("Densidad superficial de carga σ (μC/m²)", -50.0, 50.0, 10.0, step=0.5) * 1e-6
R = st.slider("Radio del disco (m)", 0.1, 2.0, 1.0, step=0.1)
x = st.slider("Distancia x a partir del centro al punto P (m)", -2.0, 2.0, 0.5, step=0.01)

# Campo eléctrico
E = 2 * np.pi * k * sigma * (1 - x / np.sqrt(R**2 + x**2))
flecha_campo = np.clip(E * 0.5, -2, 2)  # ajustar para la visualización

# ---------------- GRAFICA ---------------- #
# Disco en el plano
theta = np.linspace(0, 2*np.pi, 100)
radii = np.linspace(0, R, 30)
Theta, Radii = np.meshgrid(theta, radii)
Y = Radii * np.cos(Theta)
Z = Radii * np.sin(Theta)
X = np.zeros_like(Y)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Disco 
ax.plot_surface(X, Y, Z, color='orange', alpha=0.5, linewidth=0)

# Centro 
ax.scatter(0, 0, 0, color='black', s=50, label='Centro del disco (O)')

# Distancia x
ax.quiver(0, 0, 0, x, 0, 0, color='gray', linewidth=2, linestyle='dashed')
ax.text(x/2, 0.05, 0.05, f"Distancia x = {x:.2f} m", color='gray')

# Punto P 
ax.scatter(x, 0, 0, color='black', s=60)
ax.text(x, 0, 0.05, "P", fontsize=13, color='black')

# Direccion campo eléctrico 
color = 'red' if E > 0 else 'blue'
ax.quiver(0, 0, 0, flecha_campo, 0, 0, color=color, linewidth=2, label='Campo eléctrico E')

ax.text(flecha_campo, 0, 0.05, "→ E", fontsize=13, color=color)

# Ejes 
ax.set_xlim(-2, 2)
ax.set_ylim(-R - 0.2, R + 0.2)
ax.set_zlim(-R - 0.2, R + 0.2)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Gráfica del disco en 3D")
ax.legend()

# Resultado del campo
st.write(f"**Campo eléctrico en x = {x:.2f} m:** `{E:.2e} N/C`")

# Vista del disco
st.pyplot(fig, clear_figure=True)
