#ENTRADAS
compra=int(input("ingrese el valor total de su compra:"))
#Caja Negra
descuento=compra*0.15
valorapagar=compra-descuento
#SALIDA
print("el cliente obtiene un descuento de:", descuento, "Y ahora por su compra debe pagar:", valorapagar)