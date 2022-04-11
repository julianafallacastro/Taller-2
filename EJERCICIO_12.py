#ENTRADAS
from ast import Eq


em=float(input("Ingrese la nota del exámen de matemáticas: "))
tm1=float(input("Ingrese la nota de la tarea 1 de matemáticas: "))
tm2=float(input("Ingrese la nota de la tarea 2 de matemáticas: "))
tm3=float(input("Ingrese la nota de la tarea 3 de matemáticas: "))
ef=float(input("Ingrese la nota del exámen de Física: "))
tf1=float(input("Ingrese la nota de la tarea 1 de Física : "))
tf2=float(input("Ingrese la nota  la tarea 2 de Física: "))
eq=float(input("Ingrese la nota del exámen de Química: "))
tq1=float(input("Ingrese la nota de la tarea 1 de Química: "))
tq2=float(input("Ingrese la nota de la tarea 2 de Química: "))
tq3=float(input("Ingrese la nota de la tarea 3 de Química: "))
#Caja Negra
cfm=round((em*0.90)+(((tm1+tm2+tm3)/3)*0.10),2)
cff=round((ef*0.80)+(((tf1+tf2)/2)*0.20),2)
cfq=round((eq*0.85)+(((tq1+tq2+tq3)/3)*0.15),2)
pg=(cfm+cff+cfq)/3
#SALIDA
print("El promedio general del estudiante es de: ", pg)
