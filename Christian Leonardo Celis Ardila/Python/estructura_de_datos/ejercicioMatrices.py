
#llenar matrices
def CalcProducMAx(matrizVenta, lstProducto):

    filas = len(matrizVenta)
    lstTotalVentas = [0] * filas
    for f in range(filas):
        lstTotalVentas[f] = sum(matrizVenta[f])* lstProducto[f]
    print(lstTotalVentas)
    return lstTotalVentas.index(max(lstTotalVentas))+1

def CalcularDiasemanamaxingreso(matrizVenta, lstProducto):

    lstVentas = [0] * 7
    cont = 0
    sum = 0 
    for f in range(len(matrizVenta)):
        for c in range(len(matrizVenta[f])):
            lstVentas[c] =   lstVentas[c]+ (matrizVenta[f][c] * lstProducto[f])
        
    print(lstVentas)
    return lstVentas.index(max(lstVentas))+1

matrizVenta = [[100,88,92,94,85,110,118],
                [30,42,31,32,38,40,37],
                [23,35,39,45,55,60,61],
                [45,50,56,65,47,57,68],
                [18,25,33,21,22,28,32]]
lstProducto = [1500,5000,6500,2500,22500]

#productMasINgresosSem = CalcProducMAx(matrizVenta, lstProducto)
diasemana = CalcularDiasemanamaxingreso(matrizVenta, lstProducto)
print("EL dia de la semana con mayor ingreso es: ")
if(diasemana==1):
    print("lunes")
elif(diasemana==2):
    print("martes")
elif(diasemana==3):
    print("miercoles")
elif(diasemana==4):
    print("jueves")
elif(diasemana==5):
    print("viernes")
elif(diasemana==6):
    print("sabado")
elif(diasemana==7):
    print("domingo")





    



