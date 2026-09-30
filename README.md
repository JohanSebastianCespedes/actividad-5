# actividad-5
import streamlit as st
import math

st.set_page_config(page_title="Calculadora Geométrica", page_icon="📐")

st.title("📐 Calculadora de Áreas y Perímetros")
st.write("Selecciona una figura geométrica para ver sus fórmulas y realizar los cálculos.")

figura = st.sidebar.selectbox(
    "Selecciona la figura",
    ["Rectángulo", "Cuadrado", "Triángulo", "Círculo", "Paralelogramo"]
)

if figura == "Rectángulo":
    st.header("Rectángulo")
    st.latex(r"\text{Área} = b \cdot h \quad | \quad \text{Perímetro} = 2 \cdot (b + h)")
    
    col1, col2 = st.columns(2)
    with col1:
        base = st.number_input("Base (b)", min_value=0.0, value=5.0)
        altura = st.number_input("Altura (h)", min_value=0.0, value=3.0)
    
    area = base * altura
    perimetro = 2 * (base + altura)
    
    with col2:
        st.success(f"**Área:** {area:.2f}")
        st.info(f"**Perímetro:** {perimetro:.2f}")

elif figura == "Cuadrado":
    st.header("Cuadrado")
    st.latex(r"\text{Área} = l^2 \quad | \quad \text{Perímetro} = 4 \cdot l")
    
    lado = st.number_input("Lado (l)", min_value=0.0, value=4.0)
    area = lado ** 2
    perimetro = 4 * lado
    
    st.success(f"**Área:** {area:.2f}")
    st.info(f"**Perímetro:** {perimetro:.2f}")

elif figura == "Triángulo":
    st.header("Triángulo")
    st.latex(r"\text{Área} = \frac{b \cdot h}{2} \quad | \quad \text{Perímetro} = a + b + c")
    
    base = st.number_input("Base (b)", min_value=0.0, value=4.0)
    altura = st.number_input("Altura (h)", min_value=0.0, value=3.0)
    lado_a = st.number_input("Lado a", min_value=0.0, value=3.0)
    lado_c = st.number_input("Lado c", min_value=0.0, value=5.0)
    
    area = (base * altura) / 2
    perimetro = lado_a + base + lado_c
    
    st.success(f"**Área:** {area:.2f}")
    st.info(f"**Perímetro:** {perimetro:.2f}")

elif figura == "Círculo":
    st.header("Círculo")
    st.latex(r"\text{Área} = \pi \cdot r^2 \quad | \quad \text{Perímetro} = 2 \cdot \pi \cdot r")
    
    radio = st.number_input("Radio (r)", min_value=0.0, value=3.0)
    
    area = math.pi * (radio ** 2)
    perimetro = 2 * math.pi * radio
    
    st.success(f"**Área:** {area:.2f}")
    st.info(f"**Perímetro:** {perimetro:.2f}")

elif figura == "Paralelogramo":
    st.header("Paralelogramo")
    st.latex(r"\text{Área} = b \cdot h \quad | \quad \text{Perímetro} = 2 \cdot (a + b)")
    
    base = st.number_input("Base (b)", min_value=0.0, value=6.0)
    altura = st.number_input("Altura (h)", min_value=0.0, value=4.0)
    lado_a = st.number_input("Lado inclinado (a)", min_value=0.0, value=5.0)
    
    area = base * altura
    perimetro = 2 * (lado_a + base)
    
    st.success(f"**Área:** {area:.2f}")
    st.info(f"**Perímetro:** {perimetro:.2f}")
