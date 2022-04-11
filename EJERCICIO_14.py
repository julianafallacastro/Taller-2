#ENTRADAS
kv=float(input("Ingrese el costo por kilovatio: "))
lan=int(input("Ingrese el valor de la lectura anterior: "))
lac=int(input("Ingrese el  valor de la lectura actual: "))
#Caja Negra
costo=(lac-lan)*kv
#SALIDA
print("El monto a pagar por energía es de:", costo)
