""" sum = 0
a, b = 2, 3

sum = a + b 

sum = sum +1 
print(sum)

sum += 1 # Esta operación hace lo mismo que la linea 6
print(sum)
 """

# Algoritmo de ordenamiento Bubble Sort
arr = [27, 20, 49, 46, 45, 40, 27, 40, 17, 5]

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

print(arr)

# Algoritmo mejorado
arr = [27, 20, 49, 46, 45, 40, 27, 40, 17, 5]

n = len(arr)  # Guardar longitud del arreglo
for i in range(n):
    swapped = False  # Bandera para verificar si hubo intercambios
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            # Intercambio
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
    if not swapped:  # Si no hubo intercambios, el arreglo ya está ordenado
        break

print(arr)