## Ejercicios tarea 5
## Juan Esteban Becerra Gutiérrez
## ID: 8965694


##Ejercicio 1
def sinonimos():
    d = {}
    num = int(input())
    palabras = input()
    l = palabras.split()
    for i in range(num):
        d[l[i]] = []
    
    operaciones = int(input())
    for i in range(operaciones):
        operacion = input()
        op = operacion.split()
############################################
#Este apartado añade a las claves los sinonimos o crea nuevas claves
        if op[0] == "A":
            if op[1] in d:
                d[op[1]].append(op[2])
            else:
                d[op[1]] = [op[2]]
############################################
#Este apartado quita de la lista de la clave el sinonimo seleccionado
        elif op[0] == "D":
            if op[1] in d:
                if op[2] in d[op[1]]:
                    d[op[1]].pop(op[2])
                else:
                    print("invalid word")
            else:
                print("invalid word")
############################################
##Este apartado verifica si s1 es sinomino de s2 y viceversa
        elif op[0] == "R":
            if op[1] in d:
                if op[2] in d[op[1]]:
                    print (op[1], "is synonym of", op[2])
                elif op[1] in d[op[2]]:
                    print (op[2], "is synonym of", op[1])
                else:
                    print("not found")

sinonimos()

##Ejercicio 2
def obtenerInversa(d):
    dic = {}
####Este apartado agrega las claves del diccionario
    for e in d:
        for i in range(len(d[e])):
            dic[d[e][i]] = []
####Este apartado agrega a las listas de las claves en que diccionario esta cada clave
    for e in dic:
        for h in d:
            for i in range(len(d[h])):
                if d[h][i] == e:
                    dic[e].append(h)

    return dic

##Ejercicio 3
def obtenerElementos(l):
    repetidos = []
    for h in range(len(l)):
        ref = set(l[h])
        for i in range(len(l)):
            if l[h] != l[i]:
                c = set(l[i])
                v = ref.intersection(c)
                for e in v: #### Este ciclo para quitar los corchetes de los conjuntos
                    repetidos.append(e)
    c1 = set(repetidos)
    c1 = list(c1)
    return c1

##Ejercicio 4
def organizarPalabras(p):
    dic = {}
    frase = p.split()
    for i in frase:
        dic[i[0]] = [] ##crea el diccionario con las palabras
    for j in dic:
        for e in frase: ##mira la inicial de cada palabra para agregarla al diccionario
            if e[0] == j:
                dic[j].append(e)
    return dic

##Ejercicio 5
## a)
def obtenerEstudiantes(c):
    estudiantes = set()
    for i in c:
        for e in c[i]:
            estudiantes.add(e[0]) ## agrega los estudiantes a un conjunto "estudiantes"
    lista = []
    for e in estudiantes: ##Pasa los elementos del conjunto "estudiantes" a una lista
        lista.append(e)
    return lista

## b)
def estudiantesEnComun(c, m1, m2):
    l = []
    l1 = [] ## l1 y l2 son listas de las materias
    l2 = []
    for j in c:
        if j == m1:
            for e in c[j]: ##agrega cada estudiante y su código de la materia "m1" como tupla
                l1.append((e[0],e[1]))
        if j == m2:
            for e in c[j]: ##agrega cada estudiante y su código de la materia "m2" como tupla
                l2.append((e[0],e[1]))
    c1 = set(l1) ## Convierte a conjutno "l1" y "l2"
    c2 = set(l2)
    v = c1.intersection(c2) ##Busca los estudiantes que ven ambos cursos
    for b in v:
            l.append(b)
    return l

##Ejercicio 6
def concatenar(l1,l2):
    conc = 0
    lis = []
    for i in l1:
        for j in l2:
            c = i+j  ##recorre ambos conjuntos y combina las palabras de cada posicion del conjunto
            lis.append(c)
    conc = len(lis)
    print(lis)
    return conc

def leerimprimir():
    casos = int(input())
    for i in range(casos):
        l1 = set()
        l2 = set()
        nums = input()
        v = nums.split()
        n1 = int(v[0])
        n2 = int(v[1])
        for e in range(n1):
            p1 = input()
            l1.add(p1)

        for j in range(n2):
            p2 = input()
            l2.add(p2)
        print("Case", i+1,":" ,concatenar(l1,l2))
leerimprimir()