import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Constantes físicas
h = 6.626e-34  # J·s
c = 3e8        # m/s

# Diccionario de colores aproximados por longitud de onda
colores = {
    'Violeta': (380, 450, '#8B00FF'),
    'Azul': (450, 495, '#0000FF'),
    'Verde': (495, 570, '#00FF00'),
    'Amarillo': (570, 590, '#FFFF00'),
    'Naranja': (590, 620, '#FFA500'),
    'Rojo': (620, 750, '#FF0000')
}

valores_representativos = {
    nombre: (min_nm + max_nm) // 2
    for nombre, (min_nm, max_nm, _) in colores.items()
}

# Menú lateral
seccion = st.sidebar.selectbox("📂 Navegación", [
    "Propiedades físicas de la luz azul",
    "Comparación: luz azul natural vs pantallas",
    "Visualización comparativa por color",
    "Analogía: luz azul vs ola del mar",
    "Comparación de ondas de luz por color"
])

# Sección 1
if seccion == "Propiedades físicas de la luz azul":
    st.title("🔵 Luz azul: propiedades físicas")
    st.markdown("""
    En este ejercicio, **la luz azul** se refiere a la radiación visible emitida por **pantallas de teléfonos móviles, ordenadores, tabletas y televisores LED**.

    Esta luz tiene una **longitud de onda corta (450–495 nm)** y una **energía relativamente alta**, lo que la hace perceptible como azul brillante.  
    Aunque es parte del espectro visible, su exposición prolongada puede tener efectos sobre el **sueño, la fatiga visual y el ritmo circadiano**.
    """)

    modo_log = st.radio("Modo de visualización:", ["Escala visual (normalizada)", "Escala real (logarítmica)"])

    if modo_log == "Escala visual (normalizada)":
        # Datos normalizados
        longitud_onda_nm = [450, 495]
        frecuencia_THz = [606, 668]
        energia_J = [h * c / (l * 1e-9) for l in longitud_onda_nm]
        energia_norm = sum(energia_J) / 2 / 1e-19

        fig, ax = plt.subplots()
        ax.bar(['Longitud de onda (nm)', 'Frecuencia (THz)', 'Energía (J)'],
               [sum(longitud_onda_nm) / 2,
                sum(frecuencia_THz) / 2,
                energia_norm],
               color='blue')
        ax.set_title('Propiedades físicas de la luz azul (escaladas)')
        st.pyplot(fig)

    else:
        # Datos reales con escala logarítmica
        longitudes_nm = [450, 495]
        frecuencias_Hz = [c / (l * 1e-9) for l in longitudes_nm]
        energias_J = [h * f for f in frecuencias_Hz]

        valores = [
            sum(longitudes_nm) / 2,
            sum(frecuencias_Hz) / 2,
            sum(energias_J) / 2
        ]

        labels = ['Longitud de onda (nm)', 'Frecuencia (Hz)', 'Energía (J)']

        fig, ax = plt.subplots()
        ax.bar(labels, valores, color='blue')
        ax.set_yscale('log')
        ax.set_title('Propiedades físicas de la luz azul (escala logarítmica)')
        st.pyplot(fig)

    st.markdown("""
    🔍 **¿Por qué la energía en julios parece tan pequeña?**

    La energía de un fotón azul es del orden de \(10^{-19}\) julios, lo que la hace casi invisible en una escala lineal.  
    Por eso usamos escalas logarítmicas o normalizaciones para visualizarla junto a otras propiedades como la frecuencia o la longitud de onda.
    """)

# Sección 2
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
            energia_norm *= 0.4

        ax.bar(fuente, energia_norm, color='blue' if "natural" in fuente else 'deepskyblue')

    ax.set_ylabel("Energía normalizada (simulada)")
    ax.set_title("Comparación de energía entre fuentes de luz azul")
    st.pyplot(fig)

    st.markdown(f"""
    **🌤 Luz azul natural (cielo):** ~470 nm  
    **📱 Luz azul artificial (pantallas):** ~455 nm  
    **🕶️ Filtro activado:** {"Sí" if filtro_activo else "No"}  
    """)

# Sección 3
elif seccion == "Visualización comparativa por color":
    st.title("🎨 Comparación física por color de luz")
    color_seleccionado = st.selectbox("Selecciona un color:", list(valores_representativos.keys()))
    long_nm = valores_representativos[color_seleccionado]

    long_m = long_nm * 1e-9
    frecuencia = c / long_m
    energia = h * frecuencia

    freq_norm = frecuencia / 1e14
    energia_norm = energia / 1e-19
    long_norm = long_nm / 100

    color_hex = colores[color_seleccionado][2]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar('Longitud de onda (λ)', long_norm, color='gray')
    ax.bar('Frecuencia (f)', freq_norm, color='skyblue')
    ax.bar('Energía (E)', energia_norm, color=color_hex)
    ax.set_title(f'Propiedades de la luz ({long_nm} nm)', color='black')
    ax.set_ylabel('Valor normalizado')
    st.pyplot(fig)

    st.markdown(f"""
    **📏 Longitud de onda:** {long_nm} nm  
    **📡 Frecuencia:** {frecuencia:.2e} Hz  
    **⚡ Energía:** {energia:.2e} J  
    **🎨 Color percibido:** {color_seleccionado}
    """)
    
 # Sección 4

elif seccion == "Analogía: luz azul vs ola del mar":
    st.title("🌊🔵 Analogía: onda de luz vs ola del mar")

    st.markdown("""
    Esta visualización compara una **onda de luz** con una **ola del mar** para entender tres conceptos clave:

    - 📏 **Longitud de onda**: distancia entre crestas.
    - 🔁 **Frecuencia**: número de ciclos por segundo.
    - ⚡ **Energía**: proporcional a la frecuencia.

    Puedes modificar la longitud de onda de la luz para ver cómo cambia su frecuencia.
    """)

    # Slider para longitud de onda de la luz (en nm)
    long_nm = st.slider("Longitud de onda de la luz (nm)", min_value=380, max_value=750, value=470, step=10)
    long_m = long_nm * 1e-9
    frecuencia_luz = c / long_m

    # Parámetros simulados
    x = np.linspace(0, 4 * np.pi, 500)
    freq_mar = 1.0
    mar = np.sin(freq_mar * x)
    luz = 0.3 * np.sin(frecuencia_luz / 1e15 * x)  # escala visual

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(x, mar, label='🌊 Ola del mar (frecuencia baja)', color='deepskyblue', linewidth=2)
    ax.plot(x, luz, label=f'🔆 Onda de luz ({long_nm} nm)', color='orange', linewidth=1.5)
    ax.set_title("Comparación de ondas: mar vs luz")
    ax.set_xlabel("Espacio (simulado)")
    ax.set_ylabel("Amplitud")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    st.markdown(f"""
    ### 🔍 Observaciones

    - Longitud de onda seleccionada: **{long_nm} nm**
    - Frecuencia calculada: **{frecuencia_luz:.2e} Hz**
    - A mayor longitud de onda, menor frecuencia.
    - La energía de la luz es proporcional a su frecuencia: **más frecuencia → más energía**.

    Esta analogía ayuda a visualizar cómo las ondas pueden compartir propiedades pero comportarse de forma muy distinta según el medio y la escala.
    """)





