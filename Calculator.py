def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Por favor, introduzca un número válido.")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    while b == 0:
        print("El divisor no puede ser cero. Por favor, introduzca un nuevo número.")
        b = get_number("Introduzca el segundo número: ")
    return a / b

def mostrar_menu():
    print("Seleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Introduzca el número de la operación que desea realizar: ")

        if opcion == '5':
            print("Gracias por usar la calculadora. ¡Adiós!")
            break

        if opcion not in {'1', '2', '3', '4'}:
            print("Opción no válida. Por favor, intente de nuevo.")
            continue

        a = get_number("Introduzca el primer número: ")
        b = get_number("Introduzca el segundo número: ")

        if opcion == '1':
            resultado = sumar(a, b)
            operacion = "suma"
        elif opcion == '2':
            resultado = restar(a, b)
            operacion = "resta"
        elif opcion == '3':
            resultado = multiplicar(a, b)
            operacion = "multiplicación"
        elif opcion == '4':
            resultado = dividir(a, a)
            operacion = "división"

        print(f"El resultado de la {operacion} de {a} y {b} es {resultado}")

if __name__ == "__main__":
    main()