## Diccionarios
"""
Los diccionarios hace una relación lista con una clave de forma explicita
Las claves pueden ser numeros, letras, booleanos, tuplas y cadenas
Los valores pueden ser cualquier valor de python
"""
#Diccionario vacio
nombre = {}
a = dict()

#Diccionario con elementos
""" Forma de hacer un diccionario === M = {1:7, 2:3, 5:1} donde el primer valor
es la clave y el 2 el elemento"""
M = {1:7, 2:3, 5:1}
M[2] ##Hallar el valor de acuerdo a la clave
M[6] = 7 ##Si una clave se invoca con un valor, se agrega al diccionario
M[2] = 12 ## Cambiar el valor de acuerdo a la clave

## Tamaño de la lista
print(len(M))
## Recorrer un diccionario
for e in M:
    print(e) ##Muestra la claves del diccionario
for e in M:
    print(e, M[e]) ## Muestra la clave y su elemento del diccionario

## Imprimir listas con valores o claves de un diccionario
print(list(M.keys()))
print(list(M.values()))
print(list(M.items())) ## Imprimir la clave y valor por separado

##Listas dentro de diccionarios
dic = {"hola": [1,2,3,4,6], "mundo":[10,2,5,6]}
print(dic["hola"][1]) #accede a la lista dada su clave

for e in dic:
    for elem in dic[e]:
        print(elem)

## Eliminar elementos de un diccionario: .pop
dic.pop("hola") #Elimina la clave

## Conjuntos

