codigo = input("Digite el codigo del estudiante: ")
Nombre = input("Digite el nombre del estudiante: ")
programa = ""
bandera = 1
cont = 0

ValorNeto = 0
ValorMatricula = 0

while(bandera != 0):

    print("*"* 30)
    print("1. Tecnico de sistemas\n")
    print("2. Tecnico en desarrollo de videojuegos")     
    print("3. Tecnico en animacion digital")
    print("*"* 30)
    n = int(input("Digite numero de programa ACADEMICO"))
    print("*"* 30)
    print("TIPO 1: rendimiento academico: 50% Matricula")
    print("TIPO 2. deporte: 40% Matricula")
    print("Tipo 3: No aplica")
    print("*"* 30)
    

    n2 = int(input("Digite el numero correspondiente al tipo de beca: "))

    if(n2==1):
        Beca = 0.5
    elif(n2==2):
        Beca = 0.4
    else: Beca = 0

    if(n ==1):
        ValorMatricula = 800_000
        programa = "Tecnico de sistemas"
    elif(n ==2):
        ValorMatricula = 1_000_000
        programa = "Tecnico en desarrollo de videojuegos"

    elif(n ==2):
        ValorMatricula = 1_200_000
        programa = "Tecnico en Animacion digital" 

    ValorNeto = ValorMatricula - (ValorMatricula * Beca)
    
    print("*" * 30)    
    print(Nombre)
    print(codigo)
    print(programa)
    print(ValorNeto)
    print("*" * 30)

    cont +=1

    bandera = int(input("si desea continuar escriba 1 de lo contrario 0: "))

    if(bandera != 0):
        codigo = input("Digite el codigo del estudiante: ")
        Nombre = input("Digite el nombre del estudiante: ")

print("Numero de veces", cont)