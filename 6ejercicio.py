numeros = []
contador = 1

while len(numeros) < 3:

    numero_como_cadena = input("Ingrese el número " + str(contador) + ": ")

    try:
        numero = float(numero_como_cadena)

        if numero in numeros:
            print("El número ya existe")
        else:

            numeros.append(numero)

            contador = contador + 1
    except:
        print("Número no válido")


for i in numeros:
    for j in range(len(numeros) - 1):
        if numeros[j] > numeros[j+1]:
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]

for numero in numeros:
    print(numero)
