def longString(str):
    try:
        long = 0 
        while str[long] != None:
            long += 1
    except:
        pass #no haga nada
    
    return long

def PrepararCafe(insumo1, insumo2):
    salida=""

    if(insumo1.lower()=="cafe" and insumo2.lower()=="agua"):
        salida = "tinto"
    else:
        salida = "Daño la cafetera" 
    
    return(salida)

print("*" * 20)
taza = (PrepararCafe("cafe","agua"))
print(taza)
print(longString(taza))
print("*" * 20)

