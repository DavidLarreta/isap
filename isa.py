import streamlit as st

# Inicializar el puntaje de estrés
stress_sum = 0

# Título y bienvenida
st.title("Encuesta: Midiendo tu Estrés")
nombre = st.text_input("Por favor, ingresa tu nombre:")
st.write(f"Bienvenido, {nombre}, a la encuesta 'Midiendo tu Estrés'. Esta encuesta te ayudará a conocer tu nivel de estrés.")

# Pregunta 1
st.write("1. ¿Con qué frecuencia sientes tensión muscular o dolor de cabeza?")
res = st.selectbox("Selecciona una opción:", ["A) Casi nunca", "B) A veces", "C) Frecuentemente", "D) Todo el tiempo"])
if res == "A) Casi nunca":
    stress_sum += 1
elif res == "B) A veces":
    stress_sum += 2
elif res == "C) Frecuentemente":
    stress_sum += 3
elif res == "D) Todo el tiempo":
    stress_sum += 4

# Pregunta 2
st.write("2. ¿Cuánto te cuesta concentrarte en tareas diarias o laborales?")
res2 = st.selectbox("Selecciona una opción:", ["A) Ningún problema", "B) Un poco difícil a veces", "C) Bastante difícil", "D) Muy difícil siempre"])
if res2 == "A) Ningún problema":
    stress_sum += 1
elif res2 == "B) Un poco difícil a veces":
    stress_sum += 2
elif res2 == "C) Bastante difícil":
    stress_sum += 3
elif res2 == "D) Muy difícil siempre":
    stress_sum += 4

# Pregunta 3
st.write("3. ¿Te encuentras reaccionando de forma irritable o impaciente a situaciones cotidianas?")
res3 = st.selectbox("Selecciona una opción:", ["A) Rara vez o nunca", "B) Ocasionalmente", "C) Frecuentemente", "D) Todo el tiempo"])
if res3 == "A) Rara vez o nunca":
    stress_sum += 1
elif res3 == "B) Ocasionalmente":
    stress_sum += 2
elif res3 == "C) Frecuentemente":
    stress_sum += 3
elif res3 == "D) Todo el tiempo":
    stress_sum += 4

# Pregunta 4
st.write("4. ¿Cuánto duermes normalmente en una noche?")
res4 = st.selectbox("Selecciona una opción:", ["A) Más de 7 horas", "B) Entre 5 y 7 horas", "C) Entre 3 y 5 horas", "D) Menos de 3 horas"])
if res4 == "A) Más de 7 horas":
    stress_sum += 1
elif res4 == "B) Entre 5 y 7 horas":
    stress_sum += 2
elif res4 == "C) Entre 3 y 5 horas":
    stress_sum += 3
elif res4 == "D) Menos de 3 horas":
    stress_sum += 4

# Pregunta 5
st.write("5. ¿Qué tan seguido sientes que tienes demasiadas cosas que hacer y no tiempo suficiente?")
res5 = st.selectbox("Selecciona una opción:", ["A) Casi nunca", "B) Algunas veces", "C) La mayoría del tiempo", "D) Todo el tiempo"])
if res5 == "A) Casi nunca":
    stress_sum += 1
elif res5 == "B) Algunas veces":
    stress_sum += 2
elif res5 == "C) La mayoría del tiempo":
    stress_sum += 3
elif res5 == "D) Todo el tiempo":
    stress_sum += 4

# Mostrar el resultado final
if st.button("Calcular nivel de estrés"):
    st.write(f"Tu puntaje total de estrés es: {stress_sum}")
    
    # Interpretación del puntaje
    if stress_sum <= 5:
        st.write("Nivel de estrés bajo.")
    elif 6 <= stress_sum <= 10:
        st.write("Nivel de estrés moderado.")
    elif 11 <= stress_sum <= 15:
        st.write("Nivel de estrés alto.")
    else:
        st.write("Nivel de estrés muy alto. Considera buscar formas de reducir tu estrés.")
