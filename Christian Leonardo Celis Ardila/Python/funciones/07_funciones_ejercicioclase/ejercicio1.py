import math


def distancia(Xt, Yt, Xs,Ys):
    d = math.sqrt(((Xt-Xs)**2)-((Yt-Ys)**2))    
    return(d)


while True:
    try:
        Xt = float(input("Digite la coordenada en X1: "))
        break
    except Exception as e:
        print("Error, numero no valido", e)

while True:
    try:
        Yt = float(input("Digite la  coordenada en Y1: "))
        break
    except Exception as e:
        print("Error, numero no valido", e)


while True:
    try:
        Xs = float(input("Digite la coordenada en X2: "))
        break
    except Exception as e:
        print("Error, numero no valido", e)


while True:
    try:
        Ys = float(input("Digite la coordenada en Y2: "))
        break
    except Exception as e:
        print("Error, numero no valido", e)


d = distancia(Xt,Yt, Xs,Ys)

print(f"La distancia de dos puntos en coordenadas T({Xt,Yt}), T({Xs,Ys}) es : {d:,.1f}")






