nenglish  =int(input("Digite el numero de usuarios que se subscribio a el periodico de English: "))

lenglish = []
lfrench = []

while True:
    try:
        for i in range(nenglish):
            ne =int(input("Digite numero en  English: "))
            if(ne<0):
                print("Error valor no puede ser negativo")
                continue
            lenglish.append(ne)
        break
    except Exception as e:
        print("Error",e)

nfrench =int(input("Digite el numero de usuarios que se subscribio a el periodico de french: "))


while True:
    try:
        nf =int(input("Digite numero en french: "))
        if(nf<0):
            print("Error valor no puede ser negativo")
            continue
        lfrench.append(nf)
        o = input("Desea agregar mas datos? si: 0 no; s")

        if(o.lower()== "s"):
            break
        else:
            continue
    except Exception as e:
        print("Error",e)


lenglish = set(lenglish)
lfrench = set(lfrench)

onlyenglish = lenglish - lfrench

print(len(onlyenglish))




