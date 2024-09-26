import streamlit as st

st.title("10 Funciones Simplificadas - AX")

# Sidebar para seleccionar el ejercicio
ejercicio = st.sidebar.selectbox("Selecciona un ejercicio:", [
    "Saludo", "Suma de dos números", "Área de un triángulo", "Calculadora de descuento",
    "Suma de una lista", "Valores predeterminados", "Números pares e impares",
    "Multiplicación", "Información personal", "Calculadora flexible"
])

if ejercicio == "Saludo":
    nombre = st.text_input("Ingresa tu nombre:")
    if st.button("Saludar"):
        st.write(f"Hola, {nombre}!")

elif ejercicio == "Suma de dos números":
    a = st.number_input("Número 1:", 0)
    b = st.number_input("Número 2:", 0)
    if st.button("Sumar"):
        st.write(f"La suma es: {a + b}")

elif ejercicio == "Área de un triángulo":
    base = st.number_input("Base del triángulo:", 0.0)
    altura = st.number_input("Altura del triángulo:", 0.0)
    if st.button("Calcular área"):
        st.write(f"El área del triángulo es: {0.5 * base * altura}")

elif ejercicio == "Calculadora de descuento":
    precio = st.number_input("Precio original:", 0.0)
    descuento = st.number_input("Descuento (%) (por defecto 10):", 10)
    impuesto = st.number_input("Impuesto (%) (por defecto 16):", 16)
    if st.button("Calcular precio final"):
        precio_descuento = precio * (1 - descuento / 100)
        st.write(f"El precio final es: {precio_descuento * (1 + impuesto / 100)}")

elif ejercicio == "Suma de una lista":
    numeros = st.text_input("Ingresa los números separados por comas:")
    if st.button("Sumar lista"):
        lista_numeros = list(map(int, numeros.split(',')))
        st.write(f"La suma de la lista es: {sum(lista_numeros)}")

elif ejercicio == "Valores predeterminados":
    producto = st.text_input("Nombre del producto:")
    cantidad = st.number_input("Cantidad (por defecto 1):", 1)
    precio = st.number_input("Precio unitario (por defecto 10):", 10)
    if st.button("Calcular total"):
        st.write(f"Total a pagar: {cantidad * precio}")

elif ejercicio == "Números pares e impares":
    numeros = st.text_input("Ingresa los números separados por comas:")
    if st.button("Clasificar números"):
        lista_numeros = list(map(int, numeros.split(',')))
        pares = [n for n in lista_numeros if n % 2 == 0]
        impares = [n for n in lista_numeros if n % 2 != 0]
        st.write(f"Pares: {pares}")
        st.write(f"Impares: {impares}")

elif ejercicio == "Multiplicación":
    numeros = st.text_input("Ingresa los números separados por comas:")
    if st.button("Multiplicar"):
        lista_numeros = list(map(int, numeros.split(',')))
        resultado = 1
        for num in lista_numeros:
            resultado *= num
        st.write(f"El resultado es: {resultado}")

elif ejercicio == "Información personal":
    nombre = st.text_input("Nombre:")
    edad = st.number_input("Edad:", 0)
    direccion = st.text_input("Dirección:")
    if st.button("Mostrar información"):
        st.write(f"Nombre: {nombre}")
        st.write(f"Edad: {edad}")
        st.write(f"Dirección: {direccion}")

elif ejercicio == "Calculadora flexible":
    num1 = st.number_input("Número 1:", 0.0)
    num2 = st.number_input("Número 2:", 0.0)
    operacion = st.selectbox("Selecciona una operación:", ["suma", "resta", "multiplicacion", "division"])
    if st.button("Calcular"):
        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "multiplicacion":
            resultado = num1 * num2
        elif operacion == "division":
            resultado = num1 / num2 if num2 != 0 else "Error: División por cero"
        st.write(f"El resultado es: {resultado}")
