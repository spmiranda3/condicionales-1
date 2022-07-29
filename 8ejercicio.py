
cantidad = int(input("Ingresa la cantidad de llantas: "))
if cantidad < 5:
    valor_unitario = 240000
    print("valor a pagar", cantidad*valor_unitario)
elif cantidad >= 6 and cantidad < 7:
    valor_unitario = 221000
    print("Valor a pagar", cantidad*valor_unitario)
elif cantidad >= 7:
    valor_unitario = 180000
    print("Vaor a Pagar", cantidad*valor_unitario)
