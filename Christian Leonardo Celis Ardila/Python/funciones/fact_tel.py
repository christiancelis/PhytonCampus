def leerint(msg):
    while True:
        try:
            n = int(input(msg))
            if(n<1):
                print("Valor invalido, debe ser mayor a cero")
            return n
        except Exception as e:
            print("Error al ingresar el numero", e)


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

def leerEstrato(msg):
    while True:
        try:
            n = int(input(msg))
            if(n<1 or n>5):
                print("estrato invalido , debe ser mayor a cero y menor a 5 (1:5)")
            return n
        except Exception as e:
            print("Error al ingresar el numero", e)

def CalcularTarifa():
    if(estrato == 1):
        return 10_000
    elif(estrato == 2):
        return 15_000
    elif(estrato == 3):
        return 20_000
    elif(estrato == 4):
        return 25_000
    else:
        return 30_000
    
def CalcularImpulso(impulso):
    return 100* impulso

n = int(input("Cantidad de usuarios: "))
valtot = 0

for i in range(1, n+1):
    print("Datos usuario")
    nombre = leernombre("Digite nombre")
    estrato = leerEstrato("Digite el estrato")
    impulso = leerint("Impulso?")
    valtaf = CalcularTarifa()
    Valinp = CalcularImpulso(impulso)

    print("*" * 30)
    print(f"Nombre: {nombre}")
    print(f"Valor a pagar: {valtaf + Valinp}")
    print(f"Tarifa basica: {valtaf}")
    print(f"Valor de impulsos: {Valinp}")

    valtot += Valinp + valtaf


print(f"Valor total de inpulsos: {valtot}")



