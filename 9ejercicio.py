

tamaño = int(input("Ingresa el tamaño de la pizza: "))
if tamaño == 1:
    ingredientes = int(input('Dime el numero de ingredientes '))
    valoringredientes = ingredientes*4000
    valor_unitario = 15000
    print("valor a pagar", valor_unitario+valoringredientes,)
elif tamaño == 2:
    ingredientes = int(input('Dime el numero de ingredientes '))
    valoringredientes = ingredientes*4000
    valor_unitario = 24000
    print("valor a pagar", valor_unitario+valoringredientes,)
elif tamaño == 3:
    ingredientes = int(input('Dime el numero de ingredientes '))
    valoringredientes = ingredientes*4000
    valor_unitario = 36000
    print("valor a pagar", valor_unitario+valoringredientes,)
