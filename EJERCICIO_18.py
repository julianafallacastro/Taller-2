#ENTRADAS
prestamos=int(input("ingrese la cantidad de préstamo en bolívares: "))
tiempo=float(input("Ingrese la cantidad  de tiempo: "))
intereses=float(input("Ingrese la cantidad de intereses pagos: "))
#Caja Negra
razon=round((intereses*100)/(prestamos*tiempo),2)
#SALIDA
print("El porcentaje anual cobrado en el préstamo es de:", razon)
