#Hacer un programa que lea N estudiantes (Nombre y NOta)
#NOs muestre el promedio de una clase, el estudiante con mayor nota , el estudiante con menor nota, 

def leerint(msg):
    while True:
        try:
            n = int(input(msg))
            if(n<1):
                print("Valor invalido, debe ser mayor a cero")
            return n
        except Exception as e:
            print("Error",e)


def leernombre(msg):
    while True:
        try:
            n = input(msg)
            n.strip()

            if(n==0 or not n.isalnum()):
                print("Nombre no valido")
            return n
        except Exception as e:
            print("Error al ingresar el nombre", e)

def leernota(msg):
    while True:
        try:
            nota = float(input(msg))
            if(nota<0 and nota>5):
                print("nota invalida, debe ser mayor que 0 y menor o igual a 5")
            return nota
        except Exception as e:
            print("Error al ingresar la nota", e)


n = leerint("Digite numero de estudiantes: ")

lstNombres = []
lstNotas = []

for i in range(1, n+1):
    print(f"Datos del estudiante numero : {i} ")
    lstNombres.append(leernombre("Nombre: ?"))
    lstNotas.append(leernota("NOta: ?"))


prom = sum(lstNotas)/ n

print(lstNombres)
print(lstNotas)



#encontrar y buscar el estudiante con mayor nota

mayor =  max(lstNotas)
indicemax = lstNotas.index(mayor)
nombreMayor =  lstNombres[indicemax]

print("*"*30)
print(nombreMayor)
print(mayor)
print("*"*30)




menor =  min(lstNotas)
indicemenor = lstNotas.index(menor)
nombremenor =  lstNombres[indicemenor]


print("*"*30)
print(nombremenor)
print(menor)
print("*"*30)

