"""
    name = input("Bienvedido, cuál es tu nombre? ")
print(f"¡Hola {name}!")

num_1 = int(input("Ingresa el primer numero a sumar: "))
num_2 = int(input("Ingresa el segundo numero a sumar: "))
sum = num_1 + num_2
print(f"El resultado de la suma es: {sum}")

"""
# print("\n" + "Programa para calcular el area de un triángulo" + "\n")
# base = int(input("Ingresa la base del triángulo: "))
# height = int(input("Ingresa la altura del triángulo: "))

# area = (base * height) / 2
# print("\n" + f"El area del triangulo es: {area}" + "\n")

# print("\n" + "Programa para perificar edades iguales " + "\n")
# age_1 = int(input("Introdusca la edad numero 1: "))
# age_2 = int(input("Introdusca la edad numero 2: "))

# def verify ():
#     if(age_1 == age_2):
#         return True
#     else:
#         return False
    
# print(verify())

# print("\n" + "Programa para convertir dolares a pesos colombianos" + "\n")

# dolares = int(input("Ingresa los dolares a convertir: "))

# pesos = dolares * 4000
# print("\n" + f"Los {dolares} dolares convertidos a pesos son: {pesos} pesos colombianos" + "\n")



print("\n" + "Programa para convertir grados centigrados a grados Fahrenheit" + "\n")

centigrados = int(input("Ingresa los grados centigrados a convertir: "))

fahrenheit = (centigrados * (9/5)) + 32

print("\n" + f"Los {centigrados} grados centigrados convertidos a grados fahrenheit son:{fahrenheit: .1f} grados" + "\n")

