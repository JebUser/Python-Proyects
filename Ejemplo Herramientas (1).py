#Ejemplo herramientas computacionales. Valores matematicos
#operadores
# + - * / **(potencia) //(división entera) math

import math

#print(math.sqrt(4)) modulo matematico
numero1= int(input("Ingrese numero 1: "))
numero2 = int(input("Ingrese numero 2: "))
suma = numero1 + numero2
print("La suma es: ", suma)

#Introducción a los condicionales
#Operadores >, <, >=, <=, ==, !=(diferente de)
#Operador de comparación == A==10(tiene esa variable ese valor?)
#Operador diferente de != 

#Operadores lógicos: and, or, not
#AND ambas condiciones tienen que ser verdad para que sea verdadero
##nota >3 and nota <5
#OR alguna condicion tiene que ser verdad para que sea verdadero
#nota <0 or nota >5

#Condicionaes
#If condicion:
#   instrucción

nota=eval(input("Ingrese la nota: ")
          
    if nota >3:
        print("paso la materia")
    else
    print("fin")

### Ejemplo contadores
print("con while")
contador=1
while contador<=1:
    estudiante=input("ingrese nombre: ")
    nota1=eval(input("nota1: "))
    nota2=eval(input("nota2: "))
    promedio= (nota1+nota2)/2
    print("su promedio es: ", promedio)
    contador= contador + 1
    
print("con for")
for valor in  range(3):
    estudiante=input("ingrese nombre: ")
    nota1=eval(input("nota1: "))
    nota2=eval(input("nota2: "))
    promedio= (nota1+nota2)/2
    print("su promedio es: ", promedio)
#Problema: imprimir los # pares del 1 al 10
while contador<=10:
    if contador%2==0:
        print(contador)
    contador=contador + 1
