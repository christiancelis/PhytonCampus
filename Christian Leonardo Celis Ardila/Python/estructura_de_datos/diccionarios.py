# dic = {}
#empleado = dict()
empleado = {"Nombre":["Christian","Celis"], "Cargo":"Programador","Salario":4000000}


print(empleado["Cargo"])

print(empleado["Nombre"][0])
print(empleado["Salario"])


empleado["Nombre"].append("Leonardo")

print(empleado["Nombre"][2])

print(empleado)


#Internamente funciona bajo una funcion hash

##Agregar llave a un diccionario.
empleado[1] = "Programador Senior"
print(empleado)

print(empleado.keys())

print(empleado.values())


#Modificar un valor de una llave existente
empleado["Salario"] = 4000000
print(empleado)

# #Borrar una llave y valor de diccionario
# del empleado["Salario"]
# print(empleado)


# #Borrar todo el diccionario

# empleado = {}
# print(empleado)

#Copiar diccionario de otro diccionario
oficina = empleado.copy()
oficina["Salario"] = 5000000

print(oficina)
print(empleado)


#items

print(empleado.items())


for i in empleado.keys():
    print(i)

for i in empleado.values():
    print(i)

#borrar llave y  valor en diccionario
empleado.pop("Salario")
print(empleado)


#elimina la ultima llave valor en ser insertada

empleado.popitem()
print(empleado)


empleado.setdefault("Salario","1200")
print(empleado)

