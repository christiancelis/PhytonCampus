
def sumadivisores(num1, num2):
    val = True
    sum1 = 0
    sum2 = 0

    for i in range(1,num1):
        if(num1%i==0):
            sum1 += i

    for j in range(1, num2):
        if(num2%j==0):
            sum2 += j

    if(num1==sum2 and num2==sum1):
      val = True
    else:
        val = False  
    
    return val


while True:
    try:
        n1 = int(input("Digite un numero entero: "))
        if(n1<0):
            print("No se admiten numero negativos: ")
            continue
        break
    except Exception as e:
        print("Error ", e)


while True:
    try:
        n2 = int(input("Digite un numero entero: "))
        if(n2<0):
            print("No se admiten numero negativos: ")
            continue
        break
    except Exception as e:
        print("Error ", e)

val = sumadivisores(n1, n2)

if(val == True):
    print(f"Los numeros {n1} y {n2} son amigos")
else:
    print(f"Los numeros {n1} y {n2} NO son amigos")
