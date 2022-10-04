caminoA = 0
caminoB = 0 

caminoA=(int)(input("¿En qué punto es la primera misión(punto más cercano a 0)?"))
caminoB=(int)(input("¿En qué punto es la segunda misión(punto más lejano a 0?"))

if(caminoA<0 and caminoB<0):
    print("La distancia recorrida es: ",abs(caminoB),)
if(caminoA>0 and caminoB>0):
    print("La distancia recorrida es: ",caminoB,)
if(caminoA<0 and caminoB>0):
    print("La distancia recorrida es: ",abs(caminoA)*2+caminoB,)
if(caminoA>0 and caminoB<0):
    print("La distancia recorrida es: ",abs(caminoB)*2+caminoA,)