vocales = ["a","e","i","o","u"]
letras = []
cvocales = [0] * 5

while True:
    try:
        letra = input("Ingrese una letra del abecedario: ")
        if(not letra.isalpha()):
            print("Solo se admiten letras")
            continue
        letras.append(letra)
        op = input("Desea Continuar? [S/N]")
        if(op.lower() != "s" ):
            break
    except Exception as e:
        print("Error")



print("*"*30)

for i in letras:
    if i.lower() in vocales:
        p = vocales.index(i.lower())
        cvocales[p] += 1


for p in range(len(vocales)):
    print(vocales[p], " = ", cvocales[p])



        