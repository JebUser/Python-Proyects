# Examen 2
# Juan Esteban Becerra Gutiérrez
# ID: 8965694

# Punto 1
def leerNumeros():
    n = int(input())
    num = 0
    prod = 1
    sump = 0
    sumimp = 0
    resta = 0
    sumaM17 = 0
    while n != -1:
        num += 1
        prod *=n
        if n % 2 == 0:
            sump += n
        else:
            sumimp += n
        if n > 17:
            sumaM17 += n
        n = int(input())
        resta = sump - sumimp 
    t = (num, prod, resta, sumaM17)
    print(t)
leerNumeros()

# Punto 2
def obtenerOcurrencias(l, e):
    naparece = []
    for i in range(len(l)):
        if e == l[i]:
            naparece.append(i)
    return naparece

# Punto 3
def determinarParejaSuma(l,v):
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] != l[j]:
                if (l[i] + l[j]) == v:
                    return True
    return False

# Punto 4
def crearDeListaDeConteo(l):
    naparecen = []
    for i in range(len(l)):
        for j in range(l[i]):
            naparecen.append(i)

    return naparecen

# Punto 5
def contarInversiones(l):
    inversiones = 0
    for i in range(len(l)):
        for j in range(i, len(l)):
                if l[i] != l[j]:
                    if l[i] > l[j]:
                        inversiones += 1
    return inversiones
