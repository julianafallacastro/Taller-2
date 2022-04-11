#ENTRADAS
ph=int(input("Ingrese el pago por hora: "))
ht=int(input("Ingrese el número denhoras trabajadas: "))
#Caja Negra
s=(ph*ht)
d=(s*0.20)
sn=(s-d)
#SALIDA
print("Su sueldo neto con el descuento es de: ", sn)