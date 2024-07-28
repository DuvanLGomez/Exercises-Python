# Función para realizar una operacion and
def operador_and(a, b):
    return a and b

# Función para realizar una operacion or
def operador_or(a, b):
    return a or b #TODO OPERACION OR ENTRE A Y B

# Función para realizar una operacion not
def operador_not(a):
    return not a

# Función principal del programa
def main():
    while True:
        # Mostrar el menú
        print("Operadores Lógicos")
        print("1. AND")
        print("2. OR")
        print("3. NOT")
        print("4. SALIR")

        # Solicitar al usuario que elija una opción
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            a = input("Ingrese el primer booleano: ")
            b = input("Ingrese el segundo booleano: ")
            resultado = operador_and(a, b)
            print("Resultado: ", resultado)
        elif opcion == '2':
            a = input("Ingrese el primer booleano: ")
            b = input("Ingrese el segundo booleano: ")
            resultado = operador_or(a, b) #TODO RETORNAR OPERACION OR EN LA VARIABLE RESULTADO
            print("Resultado: ", resultado)
        elif opcion == '3':
            a = input("Ingrese el booleano: ")
            resultado = operador_not(a, b)
            print("Resultado: ", resultado)
        elif opcion == '4':
            print("Saliendo ...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
