
peso = int(input('Ingrese el peso: '))
talla = int(input('Ingrese la talla: '))
masa_corporal = (peso/talla**2)*10000
if masa_corporal < 20:
    print("Desnutrido", masa_corporal)
elif masa_corporal >= 20 and masa_corporal < 25:
    print("Normal", masa_corporal)
elif masa_corporal >= 25 and masa_corporal < 30:
    print("Sobre peso", masa_corporal)
elif masa_corporal >= 30 and masa_corporal < 35:
    print("Obesidad grado 1", masa_corporal)
elif masa_corporal >= 35 and masa_corporal < 40:
    print("Obesidad grado 2", masa_corporal)
elif masa_corporal > 40:
    print("Obesidad grado 3", masa_corporal)
