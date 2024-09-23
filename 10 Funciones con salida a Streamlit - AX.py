# Ejercicio 10: Configuración de la aplicación
import streamlit as st

# Funciones

def saludar(nombre):
    return f"Hola, {nombre}!"

def sumar(a, b):
    return a + b

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def calcular_precio_final(precio_original, descuento=10, impuesto=16):
    precio_con_descuento = precio_original * (1 - descuento / 100)
    return precio_con_descuento * (1 + impuesto / 100)

def sumar_lista(numeros):
    return sum(numeros)

def producto(nombre_producto, cantidad=1, precio_unitario=10):
    return cantidad * precio_unitario

def numeros_pares_e_impares(numeros):
    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]
    return pares, impares

def multiplicar_todos(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

def informacion_personal(**kwargs):
    return kwargs

def calculadora_flexible(num1, num2, operacion='suma'):
    operaciones = {
        'suma': num1 + num2,
        'resta': num1 - num2,
        'multiplicacion': num1 * num2,
        'division': num1 / num2 if num2 != 0 else 'Error: División por cero'
    }
    return operaciones.get(operacion, 'Operación no válida')

# Configuración de la interfaz en Streamlit

st.title("10 Funciones con salida a Streamlit - AX")

# Sidebar para seleccionar el ejercicio
ejercicio = st.sidebar.selectbox("Selecciona un ejercicio:", [
    "Saludo", "Suma de dos números", "Área de un triángulo", "Calculadora de descuento",
    "Suma de una lista", "Funciones con valores predeterminados", "Números pares e impares",
    "Multiplicación con *args", "Información personal con **kwargs", "Calculadora flexible"
])

# Ejecución de cada ejercicio según la selección

if ejercicio == "Saludo":
    nombre = st.text_input("Ingresa tu nombre:")
    if st.button("Saludar"):
        st.write(saludar(nombre))

elif ejercicio == "Suma de dos números":
    a = st.number_input("Número 1:", 0)
    b = st.number_input("Número 2:", 0)
    if st.button("Sumar"):
        st.write(f"La suma es: {sumar(a, b)}")

elif ejercicio == "Área de un triángulo":
    base = st.number_input("Base del triángulo:", 0.0)
    altura = st.number_input("Altura del triángulo:", 0.0)
    if st.button("Calcular área"):
        st.write(f"El área del triángulo es: {calcular_area_triangulo(base, altura)}")

elif ejercicio == "Calculadora de descuento":
    precio_original = st.number_input("Precio original:", 0.0)
    descuento = st.number_input("Descuento (%) (por defecto 10):", 10)
    impuesto = st.number_input("Impuesto (%) (por defecto 16):", 16)
    if st.button("Calcular precio final"):
        st.write(f"El precio final es: {calcular_precio_final(precio_original, descuento, impuesto)}")

elif ejercicio == "Suma de una lista":
    numeros = st.text_input("Ingresa los números separados por comas:")
    if st.button("Sumar lista"):
        lista_numeros = list(map(int, numeros.split(',')))
        st.write(f"La suma de la lista es: {sumar_lista(lista_numeros)}")

elif ejercicio == "Funciones con valores predeterminados":
    nombre_producto = st.text_input("Nombre del producto:")
    cantidad = st.number_input("Cantidad (por defecto 1):", 1)
    precio_unitario = st.number_input("Precio unitario (por defecto 10):", 10)
    if st.button("Calcular total"):
        st.write(f"El precio total a pagar es: {producto(nombre_producto, cantidad, precio_unitario)}")

elif ejercicio == "Números pares e impares":
    numeros = st.text_input("Ingresa los números separados por comas:")
    if st.button("Clasificar números"):
        lista_numeros = list(map(int, numeros.split(',')))
        pares, impares = numeros_pares_e_impares(lista_numeros)
        st.write(f"Números pares: {pares}")
        st.write(f"Números impares: {impares}")

elif ejercicio == "Multiplicación con *args":
    numeros = st.text_input("Ingresa los números separados por comas:")
    if st.button("Multiplicar"):
        lista_numeros = list(map(int, numeros.split(',')))
        st.write(f"El resultado de la multiplicación es: {multiplicar_todos(*lista_numeros)}")

elif ejercicio == "Información personal con **kwargs":
    nombre = st.text_input("Nombre:")
    edad = st.number_input("Edad:", 0)
    direccion = st.text_input("Dirección:")
    if st.button("Mostrar información"):
        info = informacion_personal(nombre=nombre, edad=edad, direccion=direccion)
        st.write("Información personal:")
        for k, v in info.items():
            st.write(f"{k}: {v}")

elif ejercicio == "Calculadora flexible":
    num1 = st.number_input("Número 1:", 0.0)
    num2 = st.number_input("Número 2:", 0.0)
    operacion = st.selectbox("Selecciona una operación:", ["suma", "resta", "multiplicacion", "division"])
    if st.button("Calcular"):
        resultado = calculadora_flexible(num1, num2, operacion)
        st.write(f"El resultado es: {resultado}")
