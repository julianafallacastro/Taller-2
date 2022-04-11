#entradas
mujeres=int(input("Ingrese cantidad de mujeres: "))
hombres=int(input("Ingrese cantidad de hombres: "))
#Caja Negra
Estudiantes=mujeres+hombres
PH=(mujeres/Estudiantes)*100
PH=(hombres/Estudiantes)*100
#salida
print("el porcentaje de estudiantes mujeres es:", round(PH,2))
print("el porcentaje de estudiantes hombres es:", round(PH,2))
