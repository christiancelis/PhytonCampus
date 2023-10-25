
bandera = True

def ValidacionFecha(fecha):
    fecha = fecha.strip()
    fecha = fecha.split("/")
    año = fecha[0]
    mes = fecha[1]
    dia = fecha[2]

    if(len(dia)==2 and len(mes)==2 and len(año)==4):
        bandera = True
    else:
        bandera = False
    
    return bandera


while True:
    try:
        Fecha = input("Digite fecha en formato yyyy/mm/dd: ")
        if(not Fecha.isdigit):
            print("ERROR fecha no puede contener letras ")
            continue

        val = ValidacionFecha(Fecha)

        if(val==False):
            print("Formato incorrecto")
            continue 
        break
    except Exception as e:
        print("Error ", e)


print(f" la fecha:  {Fecha} tiene formato correcto")

