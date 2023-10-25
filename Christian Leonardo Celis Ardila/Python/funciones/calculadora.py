
def suma(num1,num2):
     return num1 + num2

def resta(num1,num2):
     return num1 - num2

def multiplicacion(num1,num2):
     return num1 * num2

def division(num1,num2):
    try:
        res =  num1 / num2
    except  ZeroDivisionError:
        print("error de division por cero")
    except Exception as e:
        print("Error--",e)
    return res

def menu():
    print("*"*4+ "Menu" + "*"*4)
    print("1. suma")
    print("2. resta")
    print("3. multiplica ")
    print("4. divide")
    print("5.salir")

    while True:
        try:
            opcion = int(input("Digite opcion: "))
            if(opcion<1 or opcion>5):
                print("opcion no valida, digite nuevamente: ")
                continue
            break
        except Exception as e:
            print("No valido",e)
    return opcion


def leernum(Mensaje):
    while True:
        try:
            n = float(input(Mensaje))
            break
        except Exception as e:
            print("Error numero no valido")
    return n

opcion = menu()

while opcion!=5:

    n1 = leernum("Ingrese primer numero: ")
    n2 = leernum("Ingrese segundo numero: ")

    res = 0
    
    if(opcion==1):
        res = suma(n1, n2)
        print((f"La suma de {n1} + {n2} es : {res}"))
    elif(opcion==2):
        res = resta(n1, n2)
        print((f"La resta de {n1} - {n2} es : {res}"))
    elif(opcion==3):
        res = multiplicacion(n1, n2)
        print((f"La multiplicacion de {n1} * {n2} es : {res}"))
    elif(opcion==4):
        res = division(n1, n2)
        print((f"La division de {n1} / {n2} es : {res}"))
 
    while True:
        try:
            opcion = int(input("Desea realizar otra operacion? si: 0 no: 5: "))
            if((opcion<0 or opcion > 5) or ( opcion>0 and opcion<5)):
                print("Rango no valido")
                continue
            break
        except Exception as e:
            print("Error numero no valido")
    
    if(opcion==0):
        opcion = menu()

    
    
        



    
