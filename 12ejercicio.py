def menu():  # solo muestra el menú para elegir
    print('''
1_ Femenino
2_ Masculino
'''
          )


menu()
# pregunta almacenada en la variable que te lleva a las funciones
elegir = int(input('Elige 1,2,'))
if elegir == 1:
    edad = int(input('Ingrese el edad: '))
    numero_pulsaciones = (220-edad)/10
    print("numero de pulsaciones", numero_pulsaciones)
elif elegir == 2:
    edad = int(input('Ingrese el edad: '))
    numero_pulsaciones = (210-edad)/10
    print("numero de pulsaciones", numero_pulsaciones)
