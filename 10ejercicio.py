articulos = int(input("Ingresa el numero de articulos: "))
if articulos <= 5:
    valor_unitario = int(input('Dime el numero valor unitario '))
    subtotal = valor_unitario*articulos
    print("valor a pagar", subtotal)
elif articulos > 5 and articulos < 10:
    valor_unitario = int(input('Dime el numero valor unitario '))
    subtotal = valor_unitario*articulos
    descuento = (subtotal*5)/100
    print("valor a pagar", subtotal-descuento)
elif articulos >= 10:
    valor_unitario = int(input('Dime el numero valor unitario '))
    subtotal = valor_unitario*articulos
    descuento = (subtotal*8)/100
    print("valor a pagar", subtotal-descuento)
