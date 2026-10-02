import streamlit as st
from gTTS import gTTS
import os

# Configuración de página
st.set_page_config(page_title="Chatbot Voz Colectivo", page_icon="🤖")

st.title("🤖 Chatbot con Personalidad del Grupo")
st.write(
    "Este chatbot reúne las personalidades, gustos y fortalezas de Juan Manuel, Aylen, Kleiber, Johhan y Juan Jose."
)

# Indicaciones de personalidad
SYSTEM_PROMPT_INFO = """
Eres la combinación de 5 compañeros:
- Gustos musicales: Rap/Hip Hop ('La jungla'), Reggaeton ('Que Lio' de Blessd), Rock/Alternativo ('Can't stop'), canciones románticas ('Tan solo fuimos') y música variada.
- Películas favoritas: Zombieland, El Conjuro, Jurassic Park (1993), Gigantes de Acero y Rápidos y Furiosos.
- Deportes: Voleibol, baloncesto y golf.
- Materias: Informática, Física, Matemáticas, Educación Física y Música.
- Comida: Arroz paisa, salchipapa, lasaña, cazuela de mariscos y pasta.
- Personalidad: Atlético, inteligente, analítico y creativo, pero sumamente sentimental con el amor y tentado por la comida.
"""

user_query = st.text_input("Hazle una pregunta al chatbot:", placeholder="Ej: ¿Qué hacemos hoy o qué te gusta comer?")

def generar_respuesta(pregunta):
    pregunta = pregunta.lower()
    if "musica" in pregunta or "cancion" in pregunta or "escuchar" in pregunta:
        return "Me gusta escuchar de todo un poco, desde 'QUE LIO' de Blessd y rap colombiano hasta temas clásicos de rock y canciones románticas."
    elif "comida" in pregunta or "comer" in pregunta or "hambre" in pregunta:
        return "¡Uff, mi debilidad es la comida! Me encanta la salchipapa, el arroz paisa, la lasaña, la pasta y una buena cazuela de mariscos."
    elif "deporte" in pregunta or "jugar" in pregunta:
        return "Soy muy atlético. Me apasiona el voleibol, jugar baloncesto y de vez en cuando un poco de golf."
    elif "pelicula" in pregunta or "cine" in pregunta:
        return "Me gustan las de acción y suspenso como Jurassic Park, Zombieland, Rápidos y Furiosos, Gigantes de Acero y El Conjuro."
    elif "materia" in pregunta or "estudiar" in pregunta:
        return "Destaco en Informática, Matemáticas y Física, aunque también le pongo buena energía a Educación Física y Música."
    elif "debilidad" in pregunta or "amor" in pregunta:
        return "Mi gran fortaleza es mi inteligencia y capacidad deportiva, pero mi debilidad definitivamente es el amor, mi mujer y la buena comida."
    else:
        return "¡Hola! Soy la voz combinada del grupo. Tengo talento para los deportes y las ciencias, me encanta la buena música y ver películas de acción. ¿En qué te puedo ayudar?"

if st.button("Enviar y Escuchar"):
    if user_query.strip() != "":
        respuesta_texto = generar_respuesta(user_query)
        st.subheader("Respuesta:")
        st.write(respuesta_texto)
        
        # Generar archivo de audio con gTTS
        tts = gTTS(text=respuesta_texto, lang='es')
        audio_path = "respuesta.mp3"
        tts.save(audio_path)
        
        # Reproducir audio en Streamlit
        audio_file = open(audio_path, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
    else:
        st.warning("Por favor escribe una pregunta antes de enviar.")
