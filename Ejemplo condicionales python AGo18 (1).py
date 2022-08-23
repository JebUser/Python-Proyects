##Ejemplo condicionales y funciones python
###Juan quiere enumerar los días de la semana del 1 a 7 y quisiera saber el nombre de cada día
### a partir del numero correspondiente

#Datos: Los numeros del 1 al 7, el nombre de los días de la semana , el numero de día que se quiere
####### averiguar el nombre.

#nombre
#día

dia=6

if dia==1:
    nombre="Lunes"
elif dia==2:
    nombre="Martes"
elif dia==3:
    nombre="Miercoles"
elif dia==4:
    nombre="Jueves"
elif dia==5:
    nombre="Viernes"
elif dia==6:
    nombre="Sabado"
elif dia==7:
    nombre="Domingo"
else :
    nombre="Error"

print("El nombre del día es: ", nombre)

#######################

##Funciones

##f(x)= x**2 + 2x
##f(2) Se remplaza x por 2
##f(x, y, z)= x*y + x/z - z
##f(2, 3, 5)

###Funcion def: Definir operaciones
## Si tiene la instrucción "Return" es una función, sino, un procedimiento
def funcion(x):
    ans = None
    ans = (x**2) + (2+x)
    return ans
var = funcion(2)
print(var)
