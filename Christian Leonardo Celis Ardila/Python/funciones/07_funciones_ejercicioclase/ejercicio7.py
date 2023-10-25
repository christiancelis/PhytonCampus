bandera = False


def primo(num):
    bandera = False
    cont = 0
    divisor = ""
    sum = 0
    for i in range(1,num +1):
        if(num%i==0):
            print(i)
            cont +=1
            sum = sum + i

        if(cont==2 and sum == (num+1)):
            bandera = True
        
        if(cont>3):
            bandera = False
            break


    return bandera



while True:
    try:
        num = int(input("Digite un numero entero: "))
        if(num<0):
            print("ERROR NUmero no puede ser negativo")
            continue
        break
    except Exception as e:
        print("Error ", e)

bandera = primo(num)

if(bandera == True):
    print(f"El numero {num} es un numero primo")
else:
    print(f"El numero {num} NO es un numero primo")




            