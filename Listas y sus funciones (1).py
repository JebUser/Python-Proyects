## Estructuras de datos.
Lista = [1,3,4,5]
"""
Facilita para no crear variables.
a = 1
b = 3
c = 4
d = 5
"""
#Función Len.
## La función len imprime el tamaño de la lista
print(len(Lista))
##Función append
##Esta función permiten agregar valor a la lista
Lista.append(6)
##Manera para rescatar un valor de la lista
## "Lista"[N] ---> Lista[3]
print(Lista[3])

##Tuplas
##La tuplas no se pueden cambiar.
t = (4,5)
## Las tuplas no se pueden colocar ciertas listas (objetos) pero si tuplas dentro de otra
t2 = (4,5(1,2))
t3 = (4,5[2,6])
#Se pueden agregar datos
t2.append(7)
#Se puede mirar el tamaño y el elemento de especifico de las tuplas
print(len(t2))
print(t2[2])
