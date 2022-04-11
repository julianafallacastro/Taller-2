#ENTRADAS
ch=float(input("Ingrese la cantidad de chelines austriacos: "))
drc=float(input("Ingrese la canridad de dracmas griegos: "))
pst=float(input("Ingrese la cantidad de pesetas: "))
#Caja Negra
cp=ch*(956.871/100)
dff=drc*(88.607/100)*(1/20.110)
pd=pst*(1/122.499)
pli=pst*(100/9.289)
#SALIDAS
print(ch, "Chelines austriacos equivalen a: ", round(cp,2),"pesetas")
print(drc, "Dracmas griegos equivalen a: ", round(dff,2), "Francos franceses")
print(pst, "Pesetas equivalen a: ", round(pd,2),"Dólares")
print(ch, "Pesetas equivalen a: ", round(pli,2), "Liras italianas")