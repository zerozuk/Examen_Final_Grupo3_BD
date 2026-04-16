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


option = ""
print("===Calculadora Científica Básica===")
while option != "5":
    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    option = input("Ingrese el número de la operación: ")
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
        print("Saliendo de la calculadora...")
