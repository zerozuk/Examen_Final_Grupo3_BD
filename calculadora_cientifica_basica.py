import math


# operaciones básicas
def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b


# potenciación y raíz
def math_pow(a, b):
    return math.pow(a, b)


def math_sqrt(a):
    if a < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo"
    return math.sqrt(a)


option = ""

print("===Calculadora Científica Básica===")
while option != "7":
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potenciación")
    print("6. Raíz Cuadrada")
    print("7. Salir")
    option = input("Ingrese el número de la operación que desea realizar: ")

    if option == "1":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("===Resultado:", suma(num1, num2))
    elif option == "2":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("===Resultado:", resta(num1, num2))
    elif option == "3":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("===Resultado:", multiplicacion(num1, num2))
    elif option == "4":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("===Resultado:", division(num1, num2))
    elif option == "5":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("===Resultado:", math_pow(num1, num2))
    elif option == "6":
        num = float(input("Ingrese el número: "))
        print("===Resultado:", math_sqrt(num))
    elif option == "7":
        print("Saliendo de la calculadora...")

    else:
        print("Opción no válida. Ingrese un número del 1 al 7.")
