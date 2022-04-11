import math
#ENTRADAS
a=float(input("Ingrese el lado a: "))
b=float(input("Ingrese el lado b: "))
c=float(input("Ingrese el lado c: "))
#Caja Negra
s=(a+b+c)/2
Área=math.sqrt(s*(s-a)*(s-b)*(s-c))
#SALIDA
print("el Área es: ", round(Área, 2))