###Tarea 2: Ejercicios en python.
#Juan Esteban Becerra Gutiérrez

##Soluciones Tarea 2
##Libreria
import math
##Ejercicio 1

def funcion(x, y, z, w):
    ans = None
    ans = (x**(y+2))*(z+8)*(x**2)-(math.sqrt(y)/2)-(x**2)*(y**3)*(w**5)-(8*y)
    return ans

resultado = funcion(3, 4, 5, 7)
##Ejercicio 2

def imprirareas(L, l, l2, b, h, r):
    #Calcular el perimetro de un cuadrado (L lado cuadrado)
    perimetroc= 4*L
    

    #Calcular el perimetro de un rectangul (l es un lado de un rectangulo y l2 es el otro lado)
    perimetror= 2*l + 2*l2
   

    #Calcular el perimetro de un triangulo (b es ka base del triangulo y h es la altura)
    perimetrot= (b*h)/2
    

    #Calcular el perimetro de un circulo (r es el radio del circulo)
    perimetrocirc=2*math.pi*r
    

    return perimetroc, perimetror, perimetrot, perimetrocirc
print(imprirareas(4, 3, 2, 5, 7, 8))
#Ejercicio 3
#Variables a, b, c, d y la operación de n1 + n2

def sumarMayores(a, b, c, d):

    n1 = 0
    n2 = 0
    resultado = 0

    if a >= b and a >= c and a >= d:
        n1 = a
    elif b >= a and b >= c and b >= d:
        n1 = b
    elif c >= a and c >= b and c >= d:
        n1 = c
    else:
        n1 = d
    if n1 == a:
      if b >= c and b >= d:
        n2 = b
      elif c >= b and c >= d:
        n2 = c
      elif d >= b and d >= c:
        n2 = d
    elif n1 == b:
      if a >= c and a >= d:
        n2 = a
      elif c >= a and c >= d:
        n2 = c
      elif d >= a and d >= c:
        n2 = d
    elif n1 == c:
      if a >= b and a >= d:
        n2 = a
      elif b >= a and b >= d:
        n2 = b
      elif d >= a and d >= b:
        n2 = d 
    elif n1 == d:
      if a >= b and a >= c:
        n2 = a
      elif b >= a and b >= c:
        n2 = b
      elif c >= a and c >= b:
        n2 = c

    resultado = n1+n2
    return resultado , n1, n2

#Ejercicio 4

def cuantosEnCuadrante(x1, y1, x2, y2, x3, y3, x4, y4, c):

    result = 0
    
    if c == 1: #Cuadrante 1 x+ y Y+
        if x1>0 and y1>0:
            result= result+1          
        if x2>0 and y2>0:
            result= result+1           
        if x3>0 and y3>0:
            result= result+1         
        if x4>0 and y4>0:
            result= result+1
            
    elif c==2: #Cuadrante 2 x- y Y+
        if x1<0 and y1>0:
            result=result+1 
        if x2<0 and y2>0:
            result=result+1 
        if x3<0 and y3>0:
            result=result+1 
        if x4<0 and y4>0:
            result=result+1 
            
    elif c==3: #Cuadrante 3 x- y Y-
        if x1<0 and y1<0:
            result=result+1 
        if x2<0 and y2<0:
            result=result+1 
        if x3<0 and y3<0:
            result=result+1 
        if x4<0 and y4<0:
            result=result+1 
            
    elif c==4: # Cuadrante 4 x+ y Y-
        if x1>0 and y1>0:
            result=result+1 
        if x2>0 and y2>0:
            result=result+1 
        if x3>0 and y3>0:
            result=result+1 
        if x4>0 and y4>0:
            result=result+1 

    return result

#Ejercicio 5

def Areat(a, b, c):
    proceso = 0
    s = (a+b+c)/2
    proceso= math.sqrt((s*(s-a)*(s-b)*(s-c)))
    return proceso

#Ejercicio 6

def valprestamo(val,tasa,n):
    valorp=0

    valorp=(tasa*val)/(1-(1+tasa)**(-n))

    return valorp

#Ejercicio 7
def ubicacionSector(coordx, coordy):
    sector = None
    if coordx==0 or coordy==0:
        sector = "ESP"
    elif coordx and coordy > 0:
        sector  = "NOr"
    elif coordx < 0 and coordy > 0:
        sector = "NOc"
    elif coordx > 0 and coordy < 0:
        sector = "SOr"
    else:
        sector = "SOc"
    return sector

#Ejercicio 8
def tieneanemia(nivelhemo, edadmeses):

    resultado = None

    if edadmeses > 0 and edadmeses <1:
        if nivelhemo >= 13 and nivelhemo <= 26:
            resultado = False
        else:
            resultado = True
    if edadmeses > 1 and edadmeses <6:
        if nivelhemo >= 10 and nivelhemo <= 18:
            resultado = False
        else:
            resultado = True
    if edadmeses > 6 and edadmeses <12:
        if nivelhemo >= 11 and nivelhemo <= 15:
            resultado = False
        else:
            resultado = True
    if edadmeses > 12 and edadmeses <60:
        if nivelhemo >= 11.5 and nivelhemo <= 15:
            resultado = False
        else:
            resultado = True
    if edadmeses > 60 and edadmeses <120:
        if nivelhemo >= 12.6 and nivelhemo <= 15.5:
            resultado = False
        else:
            resultado = True
    if edadmeses > 120 and edadmeses <180:
        if nivelhemo >= 13 and nivelhemo <= 15.5:
            resultado = False
        else:
            resultado = True
    if edadmeses > 180:
        if nivelhemo >= 12 and nivelhemo <= 19:
            resultado = False
        else:
            resultado = True

    return resultado
#Ejercicio 9

def determinarTriangulo(x1, y1, x2, y2, x3, y3):

    lado1 = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    lado2 = math.sqrt((x3-x2)**2 + (y3-y2)**2)
    lado3 = math.sqrt((x3-x1)**2 + (y3-y1)**2)
    figura = None
    if lado1 == lado2 and lado1 == lado3:
        figura = "Equilatero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        figura = "Isosceles"
    elif lado1 != lado2 and lado1 != lado3:
        figura = "Escaleno"
    return figura, lado1, lado2, lado3

###Ejercicio 10
###Ejercicio hecho en grupo clase 30/08/2021
def beca(parcial1ip, parcial2ip, parcial3ip, tareasip, proyectoip, parcial1im, parcial2im, proyectoim, tareasim, parcial1mf, parcial2mf, notafinalt):
  
  aplicabeca = None
  materiasganadas = 0
  
  ####Introducción a la programación####
  parcial1ip = parcial1ip * 0.2
  parcial2ip = parcial2ip * 0.2
  parcial3ip = parcial3ip * 0.2
  tareasip = tareasip * 0.2  
  proyectoip = proyectoip * 0.2
  notafinalip = parcial1ip + parcial2ip + parcial3ip + tareasip + proyectoip
  
  if notafinalip >= 3.0:
    materiasganadas = materiasganadas + 1
  ##########Introducción al Modelado########
  parcial1im = parcial1im * 0.3
  parcial2im = parcial2im * 0.3
  proyectoim = proyectoim * 0.2
  tareasim = tareasim * 0.2
  
  notafinalim = parcial1im + parcial2im + proyectoim + tareasim

  if notafinalim >= 3.0:
    materiasganadas = materiasganadas + 1
  
  ########## Matematicas Fundamentales#############
  parcial1mf = parcial1mf * 0.5
  parcial2mf = parcial1im * 0.5
  
  notafinalmf = parcial1mf + parcial2mf

  if notafinalmf >= 3.0:
    materiasganadas = materiasganadas + 1
  ######Teologia####
  if notafinalt >= 3.0:
    materiasganadas = materiasganadas + 1
  ####APLICACIÓN BECA#####
  if materiasganadas >= 3:
    aplicabeca = True
  else:
    aplicabeca = False

  return aplicabeca

###Ejercicio 11
def cuantoscanales(act, obj):
    numerocanales = 0
    op1 = math.fabs(obj-act)
    op2 =(100-obj)+act
    op3 =(100-act)+obj
    if op1 < op2 and op1 < op3:
        numerocanales = op1
    elif op2 < op1 and op2 < op3:
        numerocanales = op2
    else:
        numerocanales = op3

    return numerocanales
###Ejercicio12

def quienGanador(pr1j1, pr1j2, pr2j1, pr2j2, pr3j1, pr3j2, pr4j1, pr4j2, pr5j1, pr5j2):### pr(numero) es puntos de la ronda y j(numero) es jugador
    ganador = None
    rganadasj1 = 0
    rganadasj2 = 0
###Ronda1
    if pr1j1 > pr1j2:
        rganadasj1 = rganadasj1 + 1
    else:
        rganadasj2 = rganadasj2 + 1
    if pr2j1 > pr2j2:
        rganadasj1 = rganadasj1 + 1
    else:
        rganadasj2 = rganadasj2 + 1
    if pr3j1 > pr3j2:
        rganadasj1 = rganadasj1 + 1
    else:
        rganadasj2 = rganadasj2 + 1
    if pr4j1 > pr4j2:
        rganadasj1 = rganadasj1 + 1
    else:
        rganadasj2 = rganadasj2 + 1
    if pr5j1 > pr5j2:
        rganadasj1 = rganadasj1 + 1
    else:
        rganadasj2 = rganadasj2 + 1

    if rganadasj1 > rganadasj2:
        ganador = "Jugador 1"
    else:
        ganador = "Jugador 2"

    return ganador
