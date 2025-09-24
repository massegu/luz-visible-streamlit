import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Constantes físicas
h = 6.626e-34  # J·s
c = 3e8        # m/s

# Menú lateral
seccion = st.sidebar.selectbox("📂 Navegación", [
    "Propiedades físicas de la luz azul",
    "Comparación: luz azul natural vs pantallas"
])

# Sección 1: Propiedades físicas
if seccion == "Propiedades físicas de la luz azul":
    st.title("🔵 Luz azul: propiedades físicas")
    st.markdown("""
    En este ejercicio, **la luz azul** se refiere a la radiación visible emitida por **pantallas de teléfonos móviles, ordenadores, tabletas y televisores LED**.

    Esta luz tiene una **longitud de onda corta (450–495 nm)** y una **energía relativamente alta**, lo que la hace perceptible como azul brillante.  
    Aunque es parte del espectro visible, su exposición prolongada puede tener efectos sobre el **sueño, la fatiga visual y el ritmo circadiano**.
    """)

    # Datos
    longitud_onda_nm = [450, 495]
    frecuencia_THz = [606, 668]
    energia_eV = [2.5, 2.75]

    # Visualización
    fig, ax = plt.subplots()
    ax.bar(['Longitud de onda (nm)', 'Frecuencia (THz)', 'Energía (eV)'],
           [sum(longitud_onda_nm)/2, sum(frecuencia_THz)/2, sum(energia_eV)/2],
           color='blue')
    ax.set_title('Propiedades físicas de la luz azul')
    st.pyplot(fig)

# Sección 2: Comparación espectral
elif seccion == "Comparación: luz azul natural vs pantallas":
    st.title("🌤📱 Comparación de luz azul: natural vs pantallas")

    fuentes = {
        "Luz azul natural (cielo)": 470,
        "Luz azul artificial (pantallas)": 455
    }

    filtro_activo = st.checkbox("🕶️ Activar filtro de luz azul")

    fig, ax = plt.subplots(figsize=(8, 5))
    for fuente, long_nm in fuentes.items():
        long_m = long_nm * 1e-9
        frecuencia = c / long_m
        energia = h * frecuencia
        energia_norm = energia / 1e-19

        if filtro_activo and fuente == "Luz azul artificial (pantallas)":
            energia_norm *= 0.4  # simula atenuación

        ax.bar(fuente, energia_norm, color='blue' if "natural" in fuente else 'deepskyblue')

    ax.set_ylabel("Energía normalizada (simulada)")
    ax.set_title("Comparación de energía entre fuentes de luz azul")
    st.pyplot(fig)

    st.markdown(f"""
    **🌤 Luz azul natural (cielo):** ~470 nm  
    **📱 Luz azul artificial (pantallas):** ~455 nm  
    **🕶️ Filtro activado:** {"Sí" if filtro_activo else "No"}  
    """)

