
def NotaDef(n1,n2,n3,n4,n5):
    defi = (n1+n2+n3+n4+n5)/5    
    return defi


while True:
    try:
        n1 = float(input("Digite valor trabajo 1: "))
        if(n1<0 or n1>5):
            print("ERROR NUmero fuera de rango")
            continue
        break
    except Exception as e:
        print("Error ", e)


while True:
    try:
        n2 = float(input("Digite valor trabajo 2: "))
        if(n2<0 or n2>5):
            print("ERROR NUmero fuera de rango")
            continue
        break
    except Exception as e:
        print("Error ", e)


while True:
    try:
        n3 = float(input("Digite valor trabajo 3: "))
        if(n3<0 or n3>5):
            print("ERROR NUmero fuera de rango")
            continue
        break
    except Exception as e:
        print("Error ", e)

while True:
    try:
        n4 = float(input("Digite valor trabajo 4: "))
        if(n4<0 or n4>5):
            print("ERROR NUmero fuera de rango")
            continue
        break
    except Exception as e:
        print("Error ", e)


while True:
    try:
        n5 = float(input("Digite valor trabajo 5: "))
        if(n5<0 or n5>5):
            print("ERROR NUmero fuera de rango")
            continue
        break
    except Exception as e:
        print("Error ", e)

def reporte(defi):
    val = False
    if(defi>3):
        val = True
        
    return val

defi = NotaDef(n1,n2,n3,n4,n5)
rep = reporte(defi)

if(rep == True):
    print("Paso el año")
else:
    print("Perdio el año")



print(f"El valor de la definitiva es : {defi:,.1f}")
