n = int(input("Digite la cantidad de docentes: "))
dicCategoria = {1:25000,2:30000,3:40000,4:45000,5:60000}

dictDocentes = {}
datosDocente = {}

totalhonorario = 0

for i in range(1,n+1):
    print("Datos del docente",i)
   
    cc = int(input("Digite su cedula"))
    datosDocente["nombre"] = input("Digite su nombre")
    datosDocente["categoria"] = int(input("Digite su categoria"))
    datosDocente["horas_lab"] = int(input("Digite horas laboradas"))
    datosDocente["honorarios"] = dicCategoria.get(datosDocente["categoria"],0) *  datosDocente["horas_lab"]

    dictDocentes[cc] = datosDocente

    totalhonorario += datosDocente["honorarios"]
    print(dictDocentes)


print("\n\n"+"="*30 )

print("*"*12+"Informe"+"*"*12)
print("="*30)
print("NOMBRE\t\tHonorarios")
print("-"*30)
for k, v in dictDocentes.items():
    print(v["nombre"], "\t\t" ,v["honorarios"])
print("-"*30)
print("total de honorarios")
print("-"*30)
print(f"Honorarios : ${totalhonorario}\n\n")

    