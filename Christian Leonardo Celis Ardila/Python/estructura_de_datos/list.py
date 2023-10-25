milista = ["Juan","Yulieth","Lorenzo","Manuel","David"]

print(milista)
print(milista[1])


milista[1] = "Julieth"
print(milista)


#slices

print(milista[2:4])
print(milista[::-1])


nomCampers_juan = ["Daniela","Maria","Juliana","Sandra","Carolina"]

print(nomCampers_juan)


#nomCampers_juan += nomCampers_juan

#
# print(nomCampers_juan)

milista.append("Kevin")
print(milista)


milista.extend(nomCampers_juan)
print(milista[-1])


milista.insert(1,"carlos")
print(milista)

#si no se le da indice se elimina el ultimo elemento de la lista
milista.pop()
print(milista)


milista.pop(-3)
print(milista)

#elimina el valor dado sino lo encuentra manda una excepcion, hay que usar try:
milista.remove("Sandra")
print(milista)


milista.sort()
print(milista)

milista.sort(reverse=True)
print(milista)