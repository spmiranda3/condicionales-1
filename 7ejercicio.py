
monto = int(input("Ingresa el valor para metodo de pagoun número: "))
if monto < 150000:
    print("pago en efectivo valor", monto)
elif monto >= 150000 and monto < 300000:
    print("pago con celular valor", monto)
elif monto >= 300000 and monto < 600000:
    print("pago con tarjeta debito valor", monto)
else:
    print('pago tarjeta credito')
    monto = int(input('gracias'))
