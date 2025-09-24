import streamlit as st
import matplotlib.pyplot as plt

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

# Valor representativo por color
valores_representativos = {
    nombre: (min_nm + max_nm) // 2
    for nombre, (min_nm, max_nm, _) in colores.items()
}

# Interfaz
st.title("🔬 Propiedades físicas de la luz visible")
color_seleccionado = st.selectbox("Selecciona un color:", list(valores_representativos.keys()))
long_nm = valores_representativos[color_seleccionado]

# Cálculos físicos
long_m = long_nm * 1e-9
frecuencia = c / long_m
energia = h * frecuencia

# Determinar color percibido
color_nombre = 'Infrarrojo'
color_hex = '#808080'
for nombre, valores in colores.items():
    min_nm, max_nm, hexcode = valores
    if min_nm <= long_nm <= max_nm:
        color_nombre = nombre
        color_hex = hexcode
        break

# Normalización para visualización
freq_norm = frecuencia / 1e14
energia_norm = energia / 1e-19
long_norm = long_nm / 100

st.markdown("""
### 🔵 ¿Qué entendemos por luz azul?

En este ejercicio, **la luz azul** hace referencia a la radiación visible emitida por **pantallas de teléfonos móviles, ordenadores, tabletas y televisores LED**.

Esta luz tiene una **longitud de onda corta (450–495 nm)** y una **energía relativamente alta**, lo que la hace perceptible como azul brillante.  
Aunque es parte del espectro visible, su exposición prolongada puede tener efectos sobre el **sueño, la fatiga visual y el ritmo circadiano**.

""")

# Visualización
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar('Longitud de onda (λ)', long_norm, color='gray')
ax.bar('Frecuencia (f)', freq_norm, color='skyblue')
ax.bar('Energía (E)', energia_norm, color=color_hex)
ax.set_title(f'Propiedades de la luz ({long_nm} nm)', color='black')
ax.set_ylabel('Valor normalizado')
st.pyplot(fig)

# Información textual
st.markdown(f"""
**📏 Longitud de onda:** {long_nm} nm  
**📡 Frecuencia:** {frecuencia:.2e} Hz  
**⚡ Energía:** {energia:.2e} J  
**🎨 Color percibido:** {color_nombre}
""")
