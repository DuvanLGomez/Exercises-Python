print("Buen dia, ¿Cual es tu nombre?")
name = input()
print("¡Bienvenido " + name + ", al restaurante buen gusto!")
menu = {1: "Pizza napolitana", 2: "Osobuco", 3: "Pasta a la carbonara"}
menu_str = "\n".join([f"{key}: {value}" for key, value in menu.items()])
print("Para el dia de hoy tenemos el siguiente menu: " + "\n" + menu_str)
print("¿Qué desea comer hoy? eliga una opción.")
pedido = input()
orden = menu[int(pedido)]
TIEMPO_ENTREGA = 30 
print("¿A que dirección quiere que lo llevemos?")
adress = input()
print("Perfecto "+ name + " su pedido de " + orden + " será entregado en " + str(TIEMPO_ENTREGA) + " minutos " + "en la dirección " + adress )
