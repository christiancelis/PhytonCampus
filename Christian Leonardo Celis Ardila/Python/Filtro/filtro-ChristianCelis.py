import json

#quitar los dos caracteres de \n al final de DatosObservatorio

def menu():
    while True:
        print("*"*4+ "Servicio Meteorologico ACME" + "*"*4)
        print("1. Listar por Codigo")
        print("2. Listar por Nombre")
        print("3. Consultar Obserbatorio Especifico")
        print("4. listado de Cantidad")
        print("5. Listado Observatorio Nacional")
        print("6. Agrupacion por observatorio")
        print()
        try:
            opcion = int(input("Digite opcion: "))
            if(opcion<1 or opcion>6):
                print("opcion no valida, digite nuevamente: ")
                continue
            break
        except Exception as e:
            print("No valido",e)
    return opcion

def leercodigo(msg):
    while True:
        try:
            codigo = str(input(msg))
            codigo = codigo.lower()
            if(codigo == "" or not codigo.isalnum()):
                print("\nValor invalido, no debe ser vacio\n")
                continue
            return codigo
        except Exception as e:
            print("\nError\n",e)

def cargarinfocsv(rutaFile):
    lstObserbatorio = []
    try:
        fd = open(rutaFile,"r")
    except Exception as e:
        try:
            fd = open(rutaFile,"w")
        except Exception as e:
            print("Error al intentar abrir el archivo csv")
            fd.close()
            return lstObserbatorio
    try:
        fd.seek(0)
        for linea in fd:
            linea = linea.strip("\n")
            if linea =="":
                continue
            if not linea.startswith("Codigo") or not linea.startswith("codigo"):
                lstObserbatorio.append(linea.split(";"))
    except Exception as e:
        fd.close()
        print("Error al cargar la informacion del csv")
        return lstObserbatorio
    
    fd.close()
    return lstObserbatorio


def cargarinfojson(rutaFile):
    lstobs = []
    try:
        fd = open(rutaFile,"r")
    except Exception as e:
        try:
            fd = open(rutaFile,"w")
        except Exception as d:
            print("Error al intentar abrir el archivo json",d)
            fd.close()
            return  lstobs
    try:
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            lstobs = json.load(fd)
        else:
            lstobs = []
    except Exception as e:
        print("Error al cargar la informacion del archivo json",e)
        fd.close()
        return lstobs
    
    fd.close()
    return lstobs
    

def existecodigo(codigo,lstobservatorio):
    variable = False
    for datos in range(len(lstobservatorio)):
        if(lstobservatorio[datos][0]) == str(codigo):
            variable = True
            return variable
        else:
            variable = False
    return variable

       
def guardarinfoObserbatorio(lstobserbatorio,rutafile):
    try:
        fd = open(rutafile,"w")
    except Exception as e:
        print("error",e) 
        return False
    
    try:
        json.dump(lstobserbatorio,fd)
    except Exception as e:
        print("Error al guardar la información del obserbatorio",e)
        fd.close()
        return False

    fd.close()
    return True


def Ordenarobservatorio(lstobservatorio,Posicion):
    for i in range(len(lstobservatorio)-1):
        for j in range(i+1,len(lstobservatorio)):
            if(lstobservatorio[i][Posicion]>lstobservatorio[j][Posicion]):
                t= lstobservatorio[i]
                lstobservatorio[i] = lstobservatorio[j]
                lstobservatorio[j] = t
    return  lstobservatorio


def OrdenarobservatorioPorPromedio(lstobservatorio):
    for i in range(len(lstobservatorio)-1):
        for j in range(i+1,len(lstobservatorio)):
            if(((int(lstobservatorio[i][3])+int(lstobservatorio[i][4])/2))>(int(lstobservatorio[j][3])+int(lstobservatorio[j][4])/2)):
                t= lstobservatorio[i]
                lstobservatorio[i] = lstobservatorio[j]
                lstobservatorio[j] = t
    return  lstobservatorio


def listarObservatorio(lstTemp):

    print("+--------------+--------------+--------------+---------------+---------------+")
    print("!              !              !              !               !               !")
    print(f"!   Codigo     !    Nombre    !     Fecha    !  Temp Maxima  !   Tem Minima  !") 
    print("!              !              !              !               !               !")                                     
    print("+--------------+--------------+--------------+---------------+---------------+")
  
    for i in range(len(lstTemp)):
        Concat1 = "!"+" "*(int((14-len(lstTemp[i][0]))/2))+ str(lstTemp[i][0]) +" "*(int((14-len(lstTemp[i][0]))/2)-3)
        Concat2 = "!"+" "*(int((14-len(lstTemp[i][0]))/2))+ str(lstTemp[i][1]) +" "*(int((14-len(lstTemp[i][0]))/2)-1)
        Concat3 = "!"+" "*(int((14-len(lstTemp[i][0]))/2))+ str(lstTemp[i][2]) +" "*(int((14-len(lstTemp[i][0]))/2)-1)
        Concat4 = "!"+" "*(int((14-len(lstTemp[i][0]))/2))+ str(lstTemp[i][3]) +" "*(int((14-len(lstTemp[i][0]))/2)-1)
        Concat5 = "!"+" "*(int((14-len(lstTemp[i][0]))/2))+ str(lstTemp[i][4]) +" "*(int((14-len(lstTemp[i][0]))/2)-1) + "!"

        print("!              !              !              !               !             !")
        print(Concat1+Concat2+Concat3+Concat4+Concat5)
        print("!              !              !              !               !              !")
        print("+--------------+--------------+--------------+---------------+--------------+")



def listarObservatorioCodigo(lstTemp,codigo):

    print("+--------------+--------------+--------------+---------------+---------------+")
    print("!              !              !              !               !               !")
    print(f"!   Codigo     !    Nombre    !     Fecha    !  Temp Maxima  !   Tem Minima  !") 
    print("!              !              !              !               !               !")                                     
    print("+--------------+--------------+--------------+---------------+---------------+")
  
    for i in range(len(lstTemp)):
        if(lstTemp[i][0] == codigo):
            Concat1 = "!"+" "*(int((14-len(lstTemp[i][0]))/2))+ str(lstTemp[i][0]) +" "*(int((14-len(lstTemp[i][0]))/2)-3)
            Concat2 = "!"+" "*(int((14-len(lstTemp[i][0]))/2))+ str(lstTemp[i][1]) +" "*(int((14-len(lstTemp[i][0]))/2)-1)
            Concat3 = "!"+" "*(int((14-len(lstTemp[i][0]))/2))+ str(lstTemp[i][2]) +" "*(int((14-len(lstTemp[i][0]))/2)-1)
            Concat4 = "!"+" "*(int((14-len(lstTemp[i][0]))/2))+ str(lstTemp[i][3]) +" "*(int((14-len(lstTemp[i][0]))/2)-1)
            Concat5 = "!"+" "*(int((14-len(lstTemp[i][0]))/2))+ str(lstTemp[i][4]) +" "*(int((14-len(lstTemp[i][0]))/2)-1) + "!"

            print("!              !              !              !               !             !")
            print(Concat1+Concat2+Concat3+Concat4+Concat5)
            print("!              !              !              !               !              !")
            print("+--------------+--------------+--------------+---------------+--------------+")

def listarObservatorioCantidad(lstTemp,codigo):
    print(lstTemp)
    cantidad = 0
    sumapromedio = 0
    tempmax = 0
    max = [""]
    min = [lstTemp[0]]
    tempmin = int(lstTemp[0][4])
    for i in range(len(lstTemp)):
        if(lstTemp[i][0] == codigo):
            cantidad +=1
            sumapromedio += (int(lstTemp[i][3])+int(lstTemp[i][4])/2)
            if (int(lstTemp[i][3]))>tempmax:
                max.clear()
                max.append(lstTemp[i])
                tempmax = int(lstTemp[i][3])
            else:
                if(int(lstTemp[i][3]))==tempmax:
                    max.append(lstTemp[i])
            if (int(lstTemp[i][4]))<tempmin:
                min.clear()
                min.append(lstTemp[i])
                tempmin = int(lstTemp[i][4])
            else:
                if(min[0][2] == lstTemp[i][2]):
                    continue

                if(int(lstTemp[i][4]))==tempmin:
                    min.append(lstTemp[i])

    print("Listado de observaciones")
    print(f"La cantidad de Observaciones con codigo {codigo}fueron: {cantidad}")
   # print(f"La observacion con la temperatura maxima fue: Nombre: {templist[0][1]}, Fecha: {templist[0][2]}, Temperatura Maxima: {templist[0][3]}")
    #print(f"La observacion con la temperatura minima  fue: Nombre: {templist[1][1]}, Fecha: {templist[1][2]}, Temperatura Maxima: {templist[1][3]}")
    print(f"EL Promedio de temperatura de todos los valores por el codigo {codigo} fue {sumapromedio/cantidad}")
    print(max)
    print(min)
    print("\n")


def listarObservatorioCodigoyPromedio(lstTemp,codigo):

    print("+--------------+--------------+--------------+")
    print("!              !              !              !")
    print(f"!   Codigo     !    Nombre    !    Promedio Temp   !") 
    print("!              !              !              !")                                     
    print("+--------------+--------------+--------------+")
  
    for i in range(len(lstTemp)):
        if(lstTemp[i][0] == codigo):
            Concat1 = "!"+" "*(int((14-len(lstTemp[i][0]))/2))+ str(lstTemp[i][0]) +" "*(int((14-len(lstTemp[i][0]))/2)-3)
            Concat2 = "!"+" "*(int((14-len(lstTemp[i][0]))/2))+ str(lstTemp[i][1]) +" "*(int((14-len(lstTemp[i][0]))/2)-1)
            Concat5 = "!"+" "*(int((14-len(lstTemp[i][4]))/2))+ (str(int(lstTemp[i][3])+int(lstTemp[i][4])/2)) +" "*+ (int((14-len(lstTemp[i][4]))/2)-1) + "!"

            print("!              !              !")
            print(Concat1+Concat2+Concat5)
            print("!              !              !")
            print("+--------------+--------------+")






def listarObservatorioNacional(lstTemp):

    print("+--------------+--------------+--------------+---------------+---------------+")
    print("!              !              !              !               !               !")
    print(f"!   Codigo     !    Nombre    !     Temp Maxima    !  Tem Minima  !  Promedio    !") 
    print("!              !              !              !               !               !")                                     
    print("+--------------+--------------+--------------+---------------+---------------+")
  
    cont = 1
    for i in range(len(lstTemp)):
            if(cont==10):
                cont=1
                opcion = input("Desea Continuar? si: cualquier caracter  no: n" )
                if opcion.lower()== "n":
                    return        
            Concat1 = "!"+" "*(int((14-len(lstTemp[i][0]))/2))+ str(lstTemp[i][0]) +" "*(int((14-len(lstTemp[i][0]))/2)-3)
            Concat2 = "!"+" "*(int((14-len(lstTemp[i][1]))/2))+ str(lstTemp[i][1]) +" "*(int((14-len(lstTemp[i][1]))/2)-1)
            Concat3 = "!"+" "*(float((14-len(lstTemp[i][2]))/2))+ str(lstTemp[i][3]) +" "*(int((14-len(lstTemp[i][2]))/2)-1)
            Concat4 = "!"+" "*(float((14-len(lstTemp[i][3]))/2))+ str(lstTemp[i][4]) +" "*(float((14-len(lstTemp[i][3]))/2)-1) + "!"
            Concat5 = "!"+" "*(float((14-len(lstTemp[i][4]))/2))+ (str(float(lstTemp[i][3])+float(lstTemp[i][4])/2)) +" "*+ (int((14-len(lstTemp[i][4]))/2)-1) + "!"
            
            print("!              !              !              !               !             !")
            print(Concat1+Concat2+Concat3+Concat4+Concat5)
            print("!              !              !              !               !              !")
            print("+--------------+--------------+--------------+---------------+--------------+")
            cont+=1
    return


def listarObservatorioAgrupadoOB(lstTemp):
    codigos = []
    for i in range(len(lstTemp)):
        if not lstTemp[i][0] in codigos:
            codigos.append(lstTemp[i][0])
            listarObservatorioCodigoyPromedio(lstTemp,lstTemp[i][0])
    return

def AgregarLista(lstobserbatoriocsv,lstobserbatoriojson):
    bandera = True
    if lstobserbatoriojson == []: 
        for datos in range(len(lstobserbatoriocsv)):
            if(lstobserbatoriocsv[datos][0] != "Codigo"):
                lstobserbatoriojson.append(lstobserbatoriocsv[datos])
    else:
        for datos in range(len(lstobserbatoriocsv)):
            if(lstobserbatoriocsv[datos][0] != "Codigo"):
                for j in range(len(lstobserbatoriojson)):
                    if(lstobserbatoriocsv[datos][0]!=lstobserbatoriojson[j][0] and lstobserbatoriocsv[datos][2]!= lstobserbatoriojson[j][2] ):
                        bandera = True
                    else:
                        bandera = False
                        break

                if bandera == True: 
                    print(lstobserbatoriocsv[datos])

    print(lstobserbatoriojson)      
    print()       
    return lstobserbatoriojson

def main():   

    rutafilecsv = "Christian Leonardo Celis Ardila/Python/Filtro/Datos.csv"
    rutafilejson = "Christian Leonardo Celis Ardila/Python/Filtro/DatosObservatorio.json"

    lstobserbatoriocsv = cargarinfocsv(rutafilecsv)
    lstobserbatoriojson = cargarinfojson(rutafilejson)

    lstobserbatoriojson = AgregarLista(lstobserbatoriocsv,lstobserbatoriojson)
    
    if guardarinfoObserbatorio(lstobserbatoriojson,rutafilejson) == True:
        print("informacion guardada con exito")
    else:
        print("Ocurrio un error al guardar la informacion")


    while True:
        opcion = menu()
        if(opcion==1):
            Posicion = 0
            lstTemp = Ordenarobservatorio(lstobserbatoriojson,Posicion)
            listarObservatorio(lstTemp)
        elif(opcion==2):
            Posicion = 1
            lstTemp = Ordenarobservatorio(lstobserbatoriojson,Posicion)
            listarObservatorio(lstTemp)
        elif(opcion == 3):
            Posicion =2
            lstTemp = Ordenarobservatorio(lstobserbatoriojson,Posicion)
            while True:
                codigo = leercodigo("Ingrese codigo observatorio: ")
                if(existecodigo(codigo,lstobserbatoriojson)):
                    listarObservatorioCodigo(lstTemp,codigo)
                    break
                else:
                    print("Codigo no existe")
                    continue
        elif(opcion==4):
             while True:
                codigo = leercodigo("Ingrese codigo observatorio: ")
                if(existecodigo(codigo,lstobserbatoriojson)):
                    listarObservatorioCantidad(lstobserbatoriojson,codigo)
                    break
                else:
                    print("Codigo no existe")
                    continue
        elif(opcion==5):
            Posicion = 0
            lstTemp = Ordenarobservatorio(lstobserbatoriojson,Posicion)
            listarObservatorioNacional(lstTemp)
        elif(opcion==6):
            lstTemp = OrdenarobservatorioPorPromedio(lstobserbatoriojson)
            listarObservatorioAgrupadoOB(lstTemp)

main()
