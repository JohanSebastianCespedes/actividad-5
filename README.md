# actividad-5
import streamlit as st
import math

# Configuración de página de Streamlit
st.set_page_config(
    page_title="Guía 3 - Parte 2: Algoritmia y Lógica",
    page_icon="💻",
    layout="wide"
)

# Título Principal
st.title("💻 Guía 3: Lógica de Programación y Algoritmia - Parte 2")
st.markdown("Desarrollo de las actividades de cálculo geométrico y lógica de números en Python.")

# Navegación en el menú lateral
opcion = st.sidebar.radio(
    "Selecciona un Módulo de la Parte 2:",
    ["1. Geometría (Áreas y Perímetros)", "2. Lógica Numérica (Par/Impar, Primos)", "3. Explicación de YOLO"]
)

# ==============================================================================
# MÓDULO 1: CÁLCULO DE ÁREAS Y PERÍMETROS (PUNTO 1)
# ==============================================================================
if opcion == "1. Geometría (Áreas y Perímetros)":
    st.header("📐 Módulo 1: Cálculo de Áreas y Perímetros")
    st.write("Selecciona una figura geométrica para ingresar sus parámetros, ver la ecuación y calcular los resultados.")

    figura = st.selectbox(
        "Elige una figura geométrica:",
        ["Rectángulo", "Cuadrado", "Triángulo", "Círculo", "Paralelogramo"]
    )

    st.markdown("---")

    if figura == "Rectángulo":
        st.subheader("🔹 Rectángulo")
        st.latex(r"\text{Área} = b \cdot h \quad \Big| \quad \text{Perímetro} = 2 \cdot (b + h)")
        
        col1, col2 = st.columns(2)
        with col1:
            base = st.number_input("Base (b)", min_value=0.1, value=5.0, step=0.5)
            altura = st.number_input("Altura (h)", min_value=0.1, value=3.0, step=0.5)
        
        area = base * altura
        perimetro = 2 * (base + altura)
        
        with col2:
            st.success(f"**Área:** {area:.2f} u²")
            st.info(f"**Perímetro:** {perimetro:.2f} u")

    elif figura == "Cuadrado":
        st.subheader("🔹 Cuadrado")
        st.latex(r"\text{Área} = l^2 \quad \Big| \quad \text{Perímetro} = 4 \cdot l")
        
        col1, col2 = st.columns(2)
        with col1:
            lado = st.number_input("Lado (l)", min_value=0.1, value=4.0, step=0.5)
        
        area = lado ** 2
        perimetro = 4 * lado
        
        with col2:
            st.success(f"**Área:** {area:.2f} u²")
            st.info(f"**Perímetro:** {perimetro:.2f} u")

    elif figura == "Triángulo":
        st.subheader("🔹 Triángulo")
        st.latex(r"\text{Área} = \frac{b \cdot h}{2} \quad \Big| \quad \text{Perímetro} = a + b + c")
        
        col1, col2 = st.columns(2)
        with col1:
            base = st.number_input("Base (b)", min_value=0.1, value=4.0, step=0.5)
            altura = st.number_input("Altura (h)", min_value=0.1, value=3.0, step=0.5)
            lado_a = st.number_input("Lado a", min_value=0.1, value=3.0, step=0.5)
            lado_c = st.number_input("Lado c", min_value=0.1, value=5.0, step=0.5)
        
        area = (base * altura) / 2.0
        perimetro = lado_a + base + lado_c
        
        with col2:
            st.success(f"**Área:** {area:.2f} u²")
            st.info(f"**Perímetro:** {perimetro:.2f} u")

    elif figura == "Círculo":
        st.subheader("🔹 Círculo")
        st.latex(r"\text{Área} = \pi \cdot r^2 \quad \Big| \quad \text{Perímetro} = 2 \cdot \pi \cdot r")
        
        col1, col2 = st.columns(2)
        with col1:
            radio = st.number_input("Radio (r)", min_value=0.1, value=3.0, step=0.5)
        
        area = math.pi * (radio ** 2)
        perimetro = 2 * math.pi * radio
        
        with col2:
            st.success(f"**Área:** {area:.2f} u²")
            st.info(f"**Perímetro:** {perimetro:.2f} u")

    elif figura == "Paralelogramo":
        st.subheader("🔹 Paralelogramo")
        st.latex(r"\text{Área} = b \cdot h \quad \Big| \quad \text{Perímetro} = 2 \cdot (a + b)")
        
        col1, col2 = st.columns(2)
        with col1:
            base = st.number_input("Base (b)", min_value=0.1, value=6.0, step=0.5)
            altura = st.number_input("Altura (h)", min_value=0.1, value=4.0, step=0.5)
            lado_a = st.number_input("Lado inclinado (a)", min_value=0.1, value=5.0, step=0.5)
        
        area = base * altura
        perimetro = 2 * (lado_a + base)
        
        with col2:
            st.success(f"**Área:** {area:.2f} u²")
            st.info(f"**Perímetro:** {perimetro:.2f} u")


# ==============================================================================
# MÓDULO 2: LÓGICA DE NÚMEROS (PUNTO 2)
# ==============================================================================
elif opcion == "2. Lógica Numérica (Par/Impar, Primos)":
    st.header("🔢 Módulo 2: Evaluación Lógica de Números")

    # Funciones de apoyo
    def es_par(n):
        return n % 2 == 0

    def es_primo(n):
        if n <= 1:
            return False
        for i in range(2, int(math.isqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def es_divisible(a, b):
        if b == 0:
            return "No se puede dividir por cero"
        return a % b == 0

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Ingreso de Datos")
        numero = st.number_input("Ingresa un número entero para evaluar:", value=7, step=1)
        divisor = st.number_input("Ingresa otro número para evaluar divisibilidad:", value=3, step=1)

    with col2:
        st.subheader("Resultados del Análisis")
        
        # Par o impar
        if es_par(numero):
            st.success(f"• **{numero}** es un número **PAR** (residuo `% 2 == 0`).")
        else:
            st.warning(f"• **{numero}** es un número **IMPAR** (residuo `% 2 != 0`).")

        # Es primo
        if es_primo(numero):
            st.success(f"• **{numero}** **SÍ ES PRIMO** (solo divisible por 1 y por él mismo).")
        else:
            st.error(f"• **{numero}** **NO ES PRIMO**.")

        # Divisibilidad
        res_div = es_divisible(numero, divisor)
        if isinstance(res_div, bool):
            if res_div:
                st.info(f"• **{numero}** **SÍ es divisible** exactamente por **{divisor}**.")
            else:
                st.info(f"• **{numero}** **NO es divisible** exactamente por **{divisor}**.")
        else:
            st.error(f"• {res_div}")


# ==============================================================================
# MÓDULO 3: EXPLICACIÓN Y SOLUCIÓN CON YOLO (PUNTO 3)
# ==============================================================================
elif opcion == "3. Explicación de YOLO":
    st.header("👁️ Módulo 3: Arquitectura YOLO y Aplicación Práctica")

    st.subheader("1. ¿Qué es la Arquitectura YOLO en palabras sencillas?")
    st.write("""
    **YOLO** (*You Only Look Once* - Solo miras una vez) es un algoritmo de visión por computadora diseñado para 
    detectar objetos dentro de imágenes o videos en tiempo real.
    
    A diferencia de otros métodos que escanean la imagen repetidamente por secciones, YOLO analiza la imagen completa 
    en un solo paso: divide la imagen en una cuadrícula (grid) y predice simultáneamente qué objetos hay, 
    dónde se encuentran (*bounding boxes*) y el porcentaje de precisión de la detección.
    """)

    st.subheader("2. Propuesta de Aplicación Práctica")
    st.info("""
    **Proyecto:** *Sistema de Seguridad y Verificación de Equipo de Protección Personal (EPP) en Talleres.*
    
    * **Objetivo:** Controlar el acceso seguro a zonas de trabajo y uso de maquinaria.
    * **Funcionamiento:** Una cámara conectada con el modelo YOLO analiza al usuario al ingresar al taller. 
      Si detecta que la persona lleva casco, gafas de seguridad y botas, envía un pulso lógico para abrir la puerta 
      o habilitar la energía de las máquinas. Si falta algún elemento, el sistema activa una alerta visual/sonora.
    """)
