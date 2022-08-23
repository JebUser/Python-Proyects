##Ejercicios Tipo Tarea 3
##Ejercicio 1
def imprimirnumeros(n, m):
    for i in range(n, m + 1):
        if i % 3 != 0 and i % 4 !=0:
            print(i)
        i += 1
imprimirnumeros(2,20)
##Ejercicio 2
def leernumeros():
    cant=0
    suma=0
    v=int(input())
    while v >= 0:
        cant += 1
        suma += v
        v= int(input())
    ans=(cant, suma)
    print(ans)
#Ejercicio 3
def leernotas(n1):
    for i in range(n1):
        nota=float(input())
        suma += nota
    ans = suma / n
    print(ans)
##Ejercicio 4
def espotencia(v,n2):
    pot = 1
    while pot < v:
        pot *= n2
    if pot == v:
        ans = True
    else:
        ans = False
def leerimprimir():
    casos=int(input())
    for i in range(casos):
        p = int(input())
        t = int(input())
        r = espotencia(p,t)
        print(r
leerimprimir()
