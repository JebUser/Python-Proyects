## Examen 5
## Juan Esteban Becerra Gutiérrez
## ID: 8965694

#Ejercicio 1
def obtenerRango(d):
    c1 = set()
    for e in d:
        for i in d[e]:
            c1.add(i)

    c1 = list(c1)
    return c1
#Ejercicio 2
def bombearCadena(cad, dic):
    res = ""
    for i in cad:
        if i in dic:
            for j in range(dic[i]):
                res += i

    return res
#Ejercicio 3

def acumularGoles(l1, l2):
    dic = {}
    for i in l1:
        dic[i[1]] = 0
    dic2= {}
    for i in l2:
        dic2[i[0]] = 0
    
    for e in dic2:
        puntos = 0
        for i in l2:
            if e == i[0]:
                puntos += i[2]
        for j in l2:
            dic2[e] = puntos
    
    for a in dic:
        for i in dic2:
            puntostotales = 0
            for e in l1:
                if i == e[0]:
                    puntostotales += dic2[i]
                dic[a] = puntostotales
                
    return dic
#Ejercicio 4
def obtenerEstudiantes(c):
    estudiantes = set()
    for i in c:
        for e in c[i]:
            estudiantes.add(e[0])
    lista = []
    for e in estudiantes:
        lista.append(e)
    return lista
