def area_circulo():  # funcion del area del circulo
    radio = int(input('Dime cuantos cm mide el radio: '))
    solucion = 3, 1416*radio**2
    print('El Área del circulo = {} cm2'.format(solucion))


def area_cuadrado():  # funcion del area del perimetro
    lado = int(input('Dime el valor del lado en cm: '))
    solucion = lado*4
    print('El perimetro = {} cm'.format(solucion))


def area_Rectangulo():  # funcion del area del perimetro
    base = int(input('Dime el valor de la base en cm: '))
    altura = int(input('Dime el valor de la altura en cm: '))
    solucion = base*altura
    print('El area = {} cm'.format(solucion))


def area_Triangulo():  # funcion del area del perimetro
    base = int(input('Dime el valor de la base en cm: '))
    altura = int(input('Dime el valor de la altura en cm: '))
    solucion = (base*altura)/2

    print('El area = {} cm'.format(solucion))


def area_Rombo():  # funcion del area del perimetro
    dmayor = int(input('Dime el valor de la diagonal mayor en cm: '))
    dmenor = int(input('Dime el valor de la diagonal menor en cm: '))
    solucion = (dmenor*dmayor)/2

    print('El area = {} cm'.format(solucion))


def area_Trapecio():  # funcion del area del perimetro
    baseMenor = int(input('Dime el valor de la Base menor en cm: '))
    baseMayor = int(input('Dime el valor de la Base Mayor en cm: '))
    Altura = int(input('Dime el valor de la altura en cm: '))

    solucion = ((baseMenor*baseMayor)*Altura)/2

    print('El area = {} cm'.format(solucion))


def menu():  # solo muestra el menú para elegir
    print('''
1_ Area de un circulo
2_ Area de un cuadrado
3_ Area de un Rectangulo
4_ Area de un Triangulo
5_ Area de un Rombo
6_ Area trapecio
'''
          )


menu()
# pregunta almacenada en la variable que te lleva a las funciones
elegir = int(input('Elige 1,2,3,4,5,6: '))
if elegir == 1:
    area_circulo()
elif elegir == 2:
    area_cuadrado()
elif elegir == 3:
    area_Rectangulo()
elif elegir == 4:
    area_Triangulo()
elif elegir == 5:
    area_Rombo()
elif elegir == 6:
    area_Trapecio()
else:
    print('Sólo puedes elegir 1 al  6')
    elegir = int(input('Elige 1 al 6: '))
