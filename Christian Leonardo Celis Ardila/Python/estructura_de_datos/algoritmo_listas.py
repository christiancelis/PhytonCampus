#funcion que busca un elemento en la lista
#si lo encuentra devuelve una funcion
#si no lo encuentra devuelve -1

def indice_elemento(lst,element):
    for i in range(len(lst)):
        if(element == lst[i]):
            return i
    return -1

def Existenlist(lst, element):
    for i in lst:
        if(i == element):
            return True
    return False


