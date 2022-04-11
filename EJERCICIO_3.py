#ENTRADAS
v1=int(input("Ingresa el número de venta 1: "))
v2=int(input("Ingresa el número de venta 2: "))
v3=int(input("Ingresa el número de venta 3: "))
sueldo=int(input("Ingresa el sueldo base: "))
#Caja Negra
sb=v1+v2+v3
comision=sb*0.10
tp=comision+sb
#SALIDAS
print("El sueldo base es de: ", sb)
print("La comisión es de: ", comision)
print("El total a pagar es de: ", tp)