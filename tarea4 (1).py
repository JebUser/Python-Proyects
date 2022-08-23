## Ejercicios tarea 4
## Juan Esteban Becerra Gutiérrez

## Librerias
import math
## Ejercicio 1
def guardarNumeros(l,r):
    lista = []
    for i in range(l,r+1):
        n = False
        for j in range(2, i):
            if i % j == 0:
                n = True
        if n == True:
            lista.append(i)
    return lista

def leerimprimir():
    casos = int(input())
    for i in range(casos):
        l = int(input())
        r = int(input())
        f0 = guardarNumeros(l,r)
        print(f0)
leerimprimir()
## Ejercicio 2
def convertiraDolar(l, t):
    cambio = []
    for i in range(len(l)):
        total = l[i]/t
        cambio.append(total)
    return cambio
def leerimprimir1():
    casos = int(input())
    for i in range(casos):
        linea = input()
        l = linea.split()

    for i in range(len(l)):
        l[i] = int(l[i])
    t = float(input())
    f1 = convertiraDolar(l,t)
    print(f1)
leerimprimir1()

## Ejercicio 3
def masCercaOrigen(x, y):
    distancia = []
    for i in range(len(y)):
        res = math.sqrt((y[i]**2)+(x[i]**2))
        distancia.append(res)       
    distmin = distancia[0]
    for j in range(len(distancia)):
        if distancia[j] < distmin:
            distmin = distancia[j]
    return distmin
## Punto 4
def crearListaDeConteo(l):
    iaparece = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(l)):
        for j in range(len(iaparece)):
            if j == l[i]:
                iaparece[j] +=1
    return iaparece
def leerimprimir2():
    casos = int(input())
    for i in range(casos):
        linea = input()
        l = linea.split()

    for i in range(len(l)):
        l[i] = int(l[i])
    f2 = crearListaDeConteo(l)
    print(f2)
leerimprimir2()

## Ejercicio 5
def cuantosenCuadrante(coords):
    cuadrante = [0,0,0,0]
    for i in range(len(coords)):
        for j in range(len(coords[i])):
            if coords[i][0] > 0 and coords[i][1] > 0:
                cuadrante[0] += 1
            elif coords[i][0] < 0 and coords[i][1] > 0:
                cuadrante[1] += 1
            elif coords[i][0] < 0 and coords[i][1] < 0:
                cuadrante[2] += 1
            elif coords[i][0] > 0 and coords[i][1] > 0:
                cuadrante[3] += 1
    return cuadrante

def leerimprimir3():
    casos = int(input())
    l=[]
    for i in range(casos):
        n = int(input()) # número de puntos que tendra la lista
        for i in range(n): # en este ciclo se leen n líneas cada una con dos valores separados por espacio
            lis = input().split() 
            x = int(lis[0])
            y = int(lis[1])
            l.append([x, y])

    f3 = cuantosenCuadrante(l)
    print(f3)
leerimprimir3()

## Ejercicio 6
l = [["flores", 100000], ["chocolates", 40000], 
    ["chocolatina Jet", 1000], ["concierto", 200000], 
    ["viaje", 2000000], ["empanadas", 2000],
    ["pony malta con pandebono", 3000]]

def determinarRegalos(l, d):
    productos = []
    for i in range(len(l)):
        if l[i][1] <= d:
            productos.append(l[i][0])
    return productos

## Ejercicio 7
def numerosRepetidos(l):
    repetido = False
    contador = 0
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] == l[j]:
                contador += 1
    if contador > len(l):
        repetido = True
    return repetido

def leerimprimir4():
    casos = int(input())
    for i in range(casos):
        linea = input()
        l = linea.split()

    for i in range(len(l)):
        l[i] = int(l[i])
    f4 = numerosRepetidos(l)
    print(f4)
leerimprimir4()

## Ejercicio 8
p = [3, 5, 7, 5, 4, 6, 7, 5, 3, 4, 3, 5, 4]
def contarpicos(p):
    picostotales = 0
    for i in range(len(p)-1):
        if p[i] > p[i+1] and p[i] > p[i-1]:
                picostotales += 1
    return picostotales

## Ejercicio 9
rpartido = [["America", 3, "Cali", 0],
            ["Junior", 2, "America", 3],
            ["Santafe", 2, "Junior", 1],
            ["Cali", 2, "Junior", 2],
            ["America", 1, "Santafe", 1]]
def obtenerPuntos(l,equipo):
    puntosganados = 0
    equipo = str(equipo)
    for i in range(len(l)):
        if l[i][0] == equipo:
            if l[i][1] > l[i][3]:
                puntosganados += 3
            elif l[i][1] == l[i][3]:
                puntosganados += 1
        elif l[i][2] == equipo:
            if l[i][3] > l[i][1]:
                puntosganados += 3
            elif l[i][3] == l[i][1]:
                puntosganados += 1
    return puntosganados
print(obtenerPuntos(rpartido,"America"))

## Ejercicio 10
def completarcarrera(estaciones, gasolinadis, gasrequerida):
    distmenor = []
    i = 0
    while i < estaciones:
        tanque = 0
        j = i
        estacionesdisp = []
        while j < estaciones:
            tanque -= gasrequerida[j]
            if (tanque + gasolinadis[j]) > 0:
                estacionesdisp.append(int(j+1))
            else:
                tanque = 0
            j +=1
        if estacionesdisp != []:
            distmenor.append(estacionesdisp[0])
        i +=1
    if distmenor == []:
        return "Not possible"
    else:
        return "Possible from station " + str(distmenor[0])


def leerimprimir5():
    casos = int(input())
    for j in range(casos):
        estaciones = int(input())
        linea = input()
        l = linea.split()
        linea2 = input()
        l2 = linea2.split()

        for i in range(len(l)):
            l[i] = int(l[i])
            l2[i] = int(l2[i])

        f5 = completarcarrera(estaciones, l, l2)
        print("Case " +str(j+1) + ": " + str(f5))
leerimprimir5()

## Ejercicio 11
def cerosyunosrango(numero, rango):
    ceros = 0
    unos = 0
    i = 0
    for i in range(rango[0], rango[1]+1):
        if numero[i] == '1':
            unos += 1
        elif numero[i] == '0':
            ceros += 1
    if ceros == ((rango[1]+1) - (rango[0])) or unos == ((rango[1]+1) - (rango[0])):
        V = "Yes" 
    else:
        V = "No"
    return V


def leerimprimir6():
    numero = input()
    n = 0
    while numero != "":
        n = n+1
        listnumero = list (numero)
        casosdelnum = int(input())
        listarangos = []
        for h in range(casosdelnum):
            rango = input()
            l = rango.split()
            for j in range(len(l)):
                l[j] = int(l[j])
            if l[0] > l[1]:
                n1 = l[0] 
                n2 = l[1]
                l[0] = n2
                l[1] = n1
            listarangos.append(l)
        print("Case " + str(n) + ": ")
        for i in range(casosdelnum):
            f6 = cerosyunosrango(listnumero, listarangos[i])
            print(f6)
        numero = input()
        
leerimprimir6()