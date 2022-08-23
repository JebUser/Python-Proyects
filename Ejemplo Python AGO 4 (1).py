#Ejemplo agosto 4
#Ejemplo sobre elementos básicos de python

"""
Ejemplos sobre otra forma sobre comentarios en pyhton
Curso básico de python
"""

"""
Las "variables" en python sirven para representar elementos
del sistema ya sean variables o constantes. Darle identidad
"""
####Variables en python
###Tipos de valores: tipos de datos

##Números: Enteros, decimales, racionales e irracionales

num = 1044783
x = 10.4
y= -20
z = 1e10
n = 1e-5

numeroMesas = 10
numMesasDisp = 5

###Cadena de texto: Strings representados por " " o ' '

S = "Cadena de texto de ejemplo: Hola mundo!"
v = "123"
T = 'Juan Esteban'

### Valores de verdad: Booleanos: True o False

P = True
R = False

###Agrupaciones de valores: tuplas, listas, diccionarios, conjuntos

listaNombre = ["Carlos", "Juan", "Ana", "Maria", "Felipe"] #Lista []
tuplaNombre = ("Carlos", "Juan", "Ana", "Maria", "Felipe") #Tupla ()

###Mostrar en pantalla: Print

print(T)
print(numeroMesas)
print(100)
print("Hola programador!")
print(x, y, z, "Se muestran numeros equisde")


#Ejemplos de pyhton Agosto 9
#Operaciones artimeticas
## +, -, *, /, //, %, **, math.pow(potencias), math.sqrt(raiz cuadrada)

import math

n1 = (2+3)
n2 = n1*6
n3 = n2/3

print(n1, n2, n3)

##Operacions comparativas
## >, <, >=, <=, ==

var1 = n1 == n2
print(var1)

var2= True #True =1 y False =0
var3= var2 + 10

print(var3)
##Operadores lógicos
#AND Operador que da True en caso de que A y B sean verdaderos
#OR Operador que da True en caso de A o B sean verdaderos
#NOT Operador que da True en caso de que A o B sean falsos
##Condicionales 
"""
Operador IF condición:
    aquí van las órdenes que se ejecutan si la condición es cierta
    y que pueden ocupar varias .

    La condición se evalúa siempre.
Si el resultado es True se ejecuta el bloque de sentencias
Si el resultado es False no se ejecuta el bloque de sentencias.

Operador IF Else permite que un programa ejecute unas instrucciones 
cuando se cumple una condición y otras instrucciones cuando no se cumple esa condición.

if condición:
    aquí van las órdenes que se ejecutan si la condición es cierta
    y que pueden ocupar varias líneas
else:
    y aquí van las órdenes que se ejecutan si la condición es
    falsa y que también pueden ocupar varias líneas

Operador IF ELIF ELSE
La construcción if ... else ... se puede extender añadiendo la instrucción elif:

La estructura de control if ... elif ... else ... permite encadenar varias condiciones.
 elif es una contracción de else if.

 if condición
    aqui va las ordenes en caso de que SOLO la primera condición se cumpla
elif condición
    aqui van las ordenes en caso de no se halla cumplido la condición 1
else:
    aqui van las ordenes en caso de no se cumpliera las 2 condiciones anteriores

"""
###Operaciones en cadena
cad= "Hola mundo"
cad2= "super"
print(cad)
print(len(cad))

cad3= cad + "" + cad2 #concatenación
print(cad3)
print(cad3 + str(24)) 
#24---->"24"
#como pos0=cad[9]
#como print(pos0)

###Ejemplo
"""
Un estudiante desea saber si el numero de creditos que tienen
sus materias que piensa matricular supera el maximo permitido (18).
En caso de que si desplegar un mensaje
"""

#Desglose de la info
#   Estudiante, Materias

#Pienzas de info
#   limite max de creditos: limcreditos=18
#   numeros de creditos de cada materia: cred1, cred2, cred3,...
cred1=3
cred2=4
cred3=2
cred4=3
cred5=3
totalcred=cred1 + cred2 + cred3 + cred4 + cred5
limcreditos=18
if totalcred > limcreditos:
    print("El estudiante supera el límite maximo de créditos")
else:
    print("El estudiante no supera el límite maximo de créditos")

print("Este mensaje se encuentra fuera del condicional, despues del if")
