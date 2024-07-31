# for i in range(1,11):
#    print(i)
"""
numbers = [0,1,2,3,4]
for num in numbers[::2]: # Recorrido de 2 en dos 
    print(num)

numbers2 = [0,1,2,3,4]
for num in numbers2:  
    print(num)


fruits = {
    #llave : valor
    "Fresa": "roja",
    "Limon": "verde",
    "Papaya": "amarilla",
    "Guayaba": "rosada"
}

for name, color in fruits.items():
    print(f"{name} es {color}")


for item in fruits:
    print(item) #solo dan las llaves

print(fruits["Fresa"]) # solo da el valor de la llave

want_greet = "s"

while want_greet == "s":
    print("Hola que tal! :D")
    want_greet = input("Quieres otro saludo? [s/n]")
print("Que tengas un buen dia pro!")

# Ejemplo con contador
day = 0
week = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado", "Domingo"]
while day < 7:
    print(f"Hoy es {week[day]}")
    day += 1

    
# Ejemplo de break
animals = ["cat", "dog", "rabbit", "horse", "dolphin"]
for animal in animals:
    if "o" in animal:
        break
    print(animal)

# Ejemplo de continue
animals = ["cat", "dog", "rabbit", "horse", "dolphin"]
for animal in animals:
    if "o" in animal:
        continue
    print(animal)
"""
for i in range(1,101):
    
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        