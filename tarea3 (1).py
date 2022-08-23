#Ejercicios Tarea 3
##Juan Esteban Becerra Gutiérrez ID: 8965694

#Ejercicio 1#########
def imprimiral100():
    for i in range(1, 100):
        if i % 7 == 0 and i % 2 != 0:
            print(i)

    i = 0
    while i < 100:
        if i % 7 == 0 and i % 2 != 0:
            print(i)
        i +=1
imprimiral100()
#Ejercicio 2############

def leerNumeros():
    v = int(input())
    cant = 0
    prod = 1
    sump = 0
    sumimp = 0
    resta = 0
    sumaM17 = 0

    while v != -1:
        cant = cant + 1
        prod = prod * v
        if v % 2 == 0:
            sump = sump + v
        else:
            sumimp = sumimp + v
        if v > 17:
            sumaM17 = sumaM17 + v
        v = int(input())
    
        resta = sump - sumimp 
    ans = (cant,prod,resta,sumaM17)
    print(ans)

leerNumeros()

#Ejercicio 3#####################
def esprimo(n1):
    for i in range(2, n1):
        if n1 % i == 0:
            return False
    return True
def esprimo2(n2):
    i = 1
    while i < n2:
        if n2 % i == 0:
            return False
    return True
def leerImprimir():
    casos = int(input())
    for i in range (casos):
        n1 = int(input())
        n2 = int(input())
        f0 = esprimo(n1)
        f1 = esprimo2(n2)
        print(f0)
        print(f1)
leerImprimir()

##Ejercicio 4#############
def imprimirPrimos(n,m):
  i = n
  for i in range(n,m):
    if esprimo(i) == True:
      print(i)
def leerimprimir():
  casos = int(input())
  for i in range(casos):
    n = int(input())
    m = int(input())
    f = imprimirPrimos(n,m)
    return f
leerimprimir()
##Ejercicio 5####
def potencia(a,b):
  res = a
  i = 1
  while i < b:
    res *=a
    i +=1
  return res
def leerimprimir2():
  casos = int(input())
  for i in range(casos):
    a = int(input())
    b = int(input())
    f = potencia(a,b)
    print(f)
leerimprimir2()

##Ejercicio 6##########

def imprimirsuceción():
    n = int(input())
    i = 1
    cad = ""
    while i <= n:
        an =((-1/i)**i)
        if i < n:
            cad = cad + str(an) + ", "
        elif i == n:
            cad = cad + str(an)
        i +=1
    print(cad)
imprimirsuceción()

##Ejercicio 7######

def imprimirasteriscos(num):
    astact = (2*num-1)
    for i in range(num):
        cad = ""
        for j in range(astact):
            cad = cad + "*"
        print(cad)
        astact = astact - 2

def leerimprimir3():
    casos = int(input())
    for i in range(casos):
        v = int(input())
        f3 = imprimirasteriscos(v)
    return f3
leerimprimir3()

##Ejercicio 8#####
def simpsonrule(a, b, n):
    h = (b-a)/n
    k = 0
    res = 0
    operacion = 0
    while k <= n:
        yk = (a+k*h)**3
        if k == 0:
          operacion += yk
        elif k == n:
          operacion += yk
        elif k % 2 == 0:
          operacion += 2*yk
        elif k % 2 != 0:
          operacion += 4*yk
        k += 1
    res = (h/3)*operacion
    return res
    
def leerimprimir4():
    casos = int(input())
    for i in range(casos):
        a = int(input())
        b = int(input())
        n = int(input())
        funcion = simpsonrule(a,b,n)
        print(funcion)
leerimprimir4()
    
## Ejercicio 9#####
def sumarimparesrango(a,b):
    suma = 0
    i = a
    while i >= a and i <= b:
        if i % 2 != 0:
            suma +=i
        i +=1
    return suma
def leerimprimir5():
  casos = int(input())
  for i in range(casos):
    a = int(input())
    b = int(input())
    f5 = sumarimparesrango(a,b)
    print("Case " + str(i+1) + ": " + str(f5))
leerimprimir5()

## Ejercico 10######### Ejercicio hecho en grupos clase del 22 de Sep/2021
def determinarJugador(n, k, p):
  i = 0
  while i < p:
    i += 1 
    if k < n:
      k += 1
    elif k == n:
      k = 1
  return k
  
def leerimprimir6():
  casos = int(input())
  i = 0
  while i < casos:
    n = int(input())
    k = int(input())
    p = int(input())
    resp = determinarJugador(n, k, p)
    print("Case " + str(i + 1) + ": " + str(resp))
    i += 1
leerImprimir()

##Ejercico 11##############
def imprimirLineasNumeros():
    n = int(input())
    cant = n
    num = n
    for i in range(cant):
      num = (n*(i+1))
      cad = str(num)
      j = n
      for j in range(n-1):
        num2 = num - j
        cad = cad + " " + str(num2-1)
      print(cad)
imprimirLineasNumeros()