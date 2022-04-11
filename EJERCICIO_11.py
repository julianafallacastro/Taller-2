#ENTRADAS
nombre=str(input("Ingrese el nombre del empleado:"))
ht=int(input("Ingrese el número de horas que se trabajaron: "))
ph=float(input("Ingrese el valor de pago de hora: "))
he=int(input("Ingrese el número de horas extras que se trabajaron: "))
th=int(input("Ingrese el total de hijos: "))
#Caja Negra
sb=(ht*ph)
d=(sb*0.05)+(sb*0.02)+(sb*0.07)
a=sb+250000+(173000*th)+100000+((ph*0.25))
sn=a-d
#SALIDAS
print("Las asignaciones que se le dieron al empleado son: ", a)
print("Las deducciones que se le dieron al empleado son: ", d)
print("El sueldo base del trabajador es: ", sb)
print("El sueldo neto a pagar al empleado es: ", sn)

