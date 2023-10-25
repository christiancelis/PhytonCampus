dictEst = {}
datosEst = {}

op = 0


def leernota(msg):
    while True:
        try:
            n = int(input(msg))
            if(n<0 or n>5):
                print("Nota fuera de Rango")
                continue
            return n
        except Exception as e:
            print("Error ",e )

while op!=999:

    cc = int(input("Digite codigo: "))
    datosEst["nombre"] = input("Nombre: ")
    datosEst["nota1"] = leernota("nota1: ")
    datosEst["nota2"] = leernota("nota2: ")
    datosEst["nota3"] = leernota("nota3: ")
    datosEst["definitiva"] = (datosEst["nota1"]*0.3 + datosEst["nota2"]*0.3 + datosEst["nota3"]*0.4)

    dictEst[cc] = datosEst

    op = int(input("Continuar: cualquier caracter / Salir: 999: "))


for k, v in dictEst.items():
    print("nombre: ",v["nombre"])
    print("Nota1: ",v["nota1"])
    print("Nota2: ",v["nota2"])
    print("Nota3: ",v["nota3"])
    defi = v["definitiva"]

    print(f"Definitiva: {defi:,.0f}")

    if(v["definitiva"]<3):
        print("Reprobo")
    else:
        print("Aprobo")


