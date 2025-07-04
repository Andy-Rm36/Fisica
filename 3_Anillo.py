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
        🧲 Campo Eléctrico de un Anillo Cargado 
    </h1>
    """,
    height=150
)

st.markdown(r"""
El anillo cargado se encuentra en el plano YZ, con centro en el origen.  
La flecha parte del centro del anillo y muestra el campo eléctrico en el eje X:
""")
st.latex(r"""E = \frac{k Q x}{(a^2 + x^2)^{3/2}}""")

st.markdown("""- La longitud de la flecha depende de la distancia \( x \).
- La letra **P** aparece en la punta de la flecha, que representa el punto donde se mide el campo.""")

# Datos
Q_uC = st.slider("Carga total Q (μC)", -10.0, 10.0, 5.0, step=0.1)
a = st.slider("Radio del anillo (m)", 0.01, 1.0, 0.5, step=0.01)
x = st.slider("Distancia x sobre el eje X (m)", -2.0, 2.0, 0.5, step=0.01)

Q = Q_uC * 1e-6

E = k * Q * x / ((a**2 + x**2)**1.5)

flecha_longitud = np.clip(E * 0.5, -1.5, 1.5)

# --------------- GRAFICA ----------------
theta = np.linspace(0, 2 * np.pi, 100)
x_ring = np.zeros_like(theta)
y_ring = a * np.cos(theta)
z_ring = a * np.sin(theta)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plano YZ
ax.plot(x_ring, y_ring, z_ring, color='orange', linewidth=2, label='Anillo cargado')

# Centro 
ax.scatter(0, 0, 0, color='black', s=50, label='Centro del anillo (O)')

# Flecha desde el origen 
color = 'red' if E > 0 else 'blue'
ax.quiver(0, 0, 0, flecha_longitud, 0, 0,
          color=color, linewidth=2, label='Campo eléctrico E')

# Punto P 
ax.text(flecha_longitud, 0, 0.05, "P", fontsize=14, color='black')

# Ejes 
ax.set_xlim(-2, 2)
ax.set_ylim(-1.2, 1.2)
ax.set_zlim(-1.2, 1.2)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Campo eléctrico en eje X desde un anillo cargado")
ax.legend()

# Resultado
st.write(f"**Campo eléctrico en x = {x:.2f} m:** `{E:.2e} N/C`")

st.pyplot(fig, clear_figure=True)
