import math


def perimetroTriangulo(X1, Y1, X2,Y2, X3, Y3):
    p = math.sqrt(((X2-X1)**2)+((Y2-Y1)**2)) + math.sqrt(((X3-X2)**2)+((Y3-Y2)**2)) + math.sqrt(((X3-X1)**2)+((Y3-Y1)**2))    
    return(p)


while True:
    try:
        X1 = float(input("Digite la coordenada en X1: "))
        break
    except Exception as e:
        print("Error, numero no valido", e)

while True:
    try:
        Y1 = float(input("Digite la  coordenada en Y1: "))
        break
    except Exception as e:
        print("Error, numero no valido", e)


while True:
    try:
        X2 = float(input("Digite la coordenada en X2: "))
        break
    except Exception as e:
        print("Error, numero no valido", e)


while True:
    try:
        Y2 = float(input("Digite la coordenada en Y2: "))
        break
    except Exception as e:
        print("Error, numero no valido", e)


while True:
    try:
        X3 = float(input("Digite la coordenada en X3: "))
        break
    except Exception as e:
        print("Error, numero no valido", e)


while True:
    try:
        Y3 = float(input("Digite la coordenada en Y3: "))
        break
    except Exception as e:
        print("Error, numero no valido", e)


p = perimetroTriangulo(X1,Y1, X2,Y2,X3,Y3)


print(f"el perimetro  de un triangulo en coordenadas P({X1,Y1}), Q({X2,Y2}) , Q({X3,Y3}) es : {p:,.1f}")

