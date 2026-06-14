from calculadora import sum, sub, mul, div, pow, sqrt, root, fact
import os

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("======= CALCULADORA =======")

    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Raíz n-ésima")
    print("8. Factorial")

    opcion = input("Seleccione una operación (1-8): ")

    match opcion:
        case '1':
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", sum(a, b))

        case '2':
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", sub(a, b))

        case '3':
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", mul(a, b))

        case '4':
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            try:
                print("Resultado:", div(a, b))
            except ValueError as e:
                print(f"Error: {e}")

        case '5':
            base = float(input("Base: "))
            exponente = float(input("Exponente: "))
            print("Resultado:", pow(base, exponente))

        case '6':
            numero = float(input("Número: "))
            try:
                print("Resultado:", sqrt(numero))
            except ValueError as e:
                print(f"Error: {e}")
        
        case '7':
            numero = float(input("Número: "))
            indice = float(input("Índice: "))
            try:
                print("Resultado:", root(numero, indice))
            except ValueError as e:
                print(f"Error: {e}")

        case '8':
            n = float(input("Número: "))
            try:
                print("Resultado:", fact(n))
            except ValueError as e:
                print(f"Error: {e}")

        case _:
            print("Opción no válida")
    input("Presione Enter para continuar...")
