import streamlit as st

st.title("10 Funciones Simplificadas - AX")

# Sidebar para seleccionar el ejercicio
e = st.sidebar.selectbox("Selecciona un ejercicio:", ["Saludo", "Suma de dos números", "Área de un triángulo", "Calculadora de descuento", "Suma de una lista", "Valores predeterminados", "Números pares e impares", "Multiplicación", "Información personal", "Calculadora flexible"
])

if e == "Saludo":
    a = st.text_input("Ingresa tu nombre:")
    if st.button("Saludar"):
        st.write(f"Hola, {a}!")

elif e == "Suma de dos números":
    a = st.number_input("Número 1:", 0)
    b = st.number_input("Número 2:", 0)
    if st.button("Sumar"):
        st.write(f"La suma es: {a + b}")

elif e == "Área de un triángulo":
    a = st.number_input("Base del triángulo:", 0.0)
    b = st.number_input("Altura del triángulo:", 0.0)
    if st.button("Calcular área"):
        st.write(f"El área del triángulo es: {0.5 * a * b}")

elif e == "Calculadora de descuento":
    a = st.number_input("Precio original:", 0.0)
    b = st.number_input("Descuento (%) (por defecto 10):", 10)
    c = st.number_input("Impuesto (%) (por defecto 16):", 16)
    if st.button("Calcular precio final"):
        d = a * (1 - b / 100)
        st.write(f"El precio final es: {d * (1 + c / 100)}")

elif e == "Suma de una lista":
    a = st.text_input("Ingresa los números separados por comas:")
    if st.button("Sumar lista"):
        b = list(map(int, a.split(',')))
        st.write(f"La suma de la lista es: {sum(b)}")

elif e == "Valores predeterminados":
    a = st.text_input("Nombre del producto:")
    b = st.number_input("Cantidad (por defecto 1):", 1)
    c = st.number_input("Precio unitario (por defecto 10):", 10)
    if st.button("Calcular total"):
        st.write(f"Total a pagar: {b * c}")

elif e == "Números pares e impares":
    a = st.text_input("Ingresa los números separados por comas:")
    if st.button("Clasificar números"):
        b = list(map(int, a.split(',')))
        pares = [n for n in b if n % 2 == 0]
        impares = [n for n in b if n % 2 != 0]
        st.write(f"Pares: {pares}")
        st.write(f"Impares: {impares}")

elif e == "Multiplicación":
    a = st.text_input("Ingresa los números separados por comas:")
    if st.button("Multiplicar"):
        b = list(map(int, a.split(',')))
        c = 1
        for n in b:
            c *= n
        st.write(f"El resultado es: {c}")

elif e == "Información personal":
    a = st.text_input("Nombre:")
    b = st.number_input("Edad:", 0)
    c = st.text_input("Dirección:")
    if st.button("Mostrar información"):
        st.write(f"Nombre: {a}")
        st.write(f"Edad: {b}")
        st.write(f"Dirección: {c}")

elif e == "Calculadora flexible":
    a = st.number_input("Número 1:", 0.0)
    b = st.number_input("Número 2:", 0.0)
    c = st.selectbox("Selecciona una operación:", ["suma", "resta", "multiplicacion", "division"])
    if st.button("Calcular"):
        if c == "suma":
            resultado = a + b
        elif c == "resta":
            resultado = a - b
        elif c == "multiplicacion":
            resultado = a * b
        elif c == "division":
            resultado = a / b if b != 0 else "Error: División por cero"
        st.write(f"El resultado es: {resultado}")
