## Entrega 2 del proyecto
## Este código es de autoría unica hecha por el estudiante:
## Juan Esteban Becerra Gutiérrez
## ID: 8965694

##Código de honor.

"""
Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali, los valores éticos y la integri-
dad son tan importantes como la excelencia académica. En este curso se espera que los estudiantes se comporten ética
y honestamente, con los más altos niveles de integridad escolar. En particular, se asume que cada estudiante adopta el
siguiente código de honor:

Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
a seguir los más altos estándares de integridad académica.

Integridad académica se refiere a ser honesto, dar crédito a quien lo merece y respetar el trabajo de los demás. Por eso
es importante evitar plagiar, engañar, ‘hacer trampa’, etc. En particular, el acto de entregar un programa de computador
ajeno como propio constituye un acto de plagio; cambiar el nombre de las variables, agregar o eliminar comentarios
y reorganizar comandos no cambia el hecho de que se está copiando el programa de alguien más. Para más detalles
consultar el Reglamento de Estudiantes, Sección VI.
"""

##Propósito del programa
"""
El propósito del programa es traducir cadenas de texto ingresadas por el usuario a código de lenguaje
ensamblador.
"""
##Entrada
"""
La entrada consiste cadenas de texto que contienen expresiones formadas por letras de 'A' a 'Z', y por
operandos(+,-,*,/,@(negación)). Las entradas pueden ser infinitas pero cada una debe estar separada en
linea diferente.
"""
##Salida
"""
Con cada entrada se debe imprimir las instrucciones en orden y de acuerdo a las expresiones que se dieron
en la entrada, cada una en una linea diferente. Por cada entrada se debe imprimir su conjunto de
instrucciones separadas de un espcacio en blanco.
"""

###############
def codeGeneration(cad):
    ops = []
    symb = ["+","-","*","/","@"]
    n = 1
    for i in range(len(cad)-1):
        if cad[i] not in symb:
            if cad[i+1] == "@":
                ops.append("L " + str(cad[i]))
                ops.append("N")
                ops.append("ST $" + str(n-1))
                n+=1
            elif cad[i+1] in symb:
                if cad[i+1] == "+":
                    ops.append("A " + str(cad[i]))
                elif cad[i+1] == "-":
                    ops.append("S " + str(cad[i]))
                elif cad[i+1] == "*":
                    ops.append("M " + str(cad[i]))
                elif cad[i+1] == "/":
                    ops.append("D " + str(cad[i]))

                if n > 1:
                    if i+1 != len(cad)-1:
                        m = 2
                        for e in range(n-1):
                            if i+m < len(cad):
                                if cad[i+m] == "+":
                                    ops.append("A " + "$"+ str(n-m))
                                    m +=1
                                elif cad[i+m] == "-":
                                    ops.append("N")                               
                                    ops.append("A " + "$"+ str(n-m))
                                    m +=1
                                elif cad[i+m] == "*":
                                    ops.append("M " + "$"+ str(n-m))
                                    m+=1
                                elif cad[i+m] == "/":
                                    ops.append("ST $" + str(n-1))
                                    ops.append("L " + "$" + str(n-2))
                                    ops.append("D " + "$"+ str(n-1))
                                    m+=1
                                    n -=1
                                elif cad[i+m] == "@":
                                    ops.append("N")
                                    m+1
                ops.append("ST $" + str(n-1))
                n+=1
            elif cad[i] not in symb:
                ops.append("L " + str(cad[i]))
                if cad[i+2] == "@" or cad[i+2] not in symb:
                    ops.append("ST $" + str(n-1))
                    n+=1

    return ops
    

def leerimprimir():
    expresion = input()
    operaciones = []
    while expresion != "":
        operaciones.append(expresion)
        expresion = input()
    for e in operaciones:
        v = codeGeneration(e)
        for i in range(len(v)-1):
            print(v[i])
        print("")
leerimprimir()
