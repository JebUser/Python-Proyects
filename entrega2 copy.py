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

"""
##Entrada
"""
"""
##Salida
"""
"""

###############
def codeGeneration(cad):
    ops = []
    n = 0
    i = 0
    
    while i < (len(cad)):
        if i != len(cad)-1:

            if i == 0: ###### Inicio de la cadena
                ops.append("L " +str(cad[i]))
                if cad[i+2] != "+":
                    if cad[i+2] != "-":
                        if cad[i+2] != "*":
                            if cad[i+2] != "/":
                                ops.append("ST $"+ str(n))
                                n +=1
            ######### Intermedio de la cadena
            elif cad[i] != "+":
                if cad[i] != "-":
                    if cad[i] != "*":
                        if cad[i] != "/":
                ##### Mira las operaciones
                            if cad[i+1] == "+":
                                ops.append("A " + str(cad[i]))
                                ops.append("ST $"+ str(n))
                                n +=1
                            if cad[i+1] == "-":
                                ops.append("S " + str(cad[i]))
                                ops.append("ST $"+ str(n))
                                n +=1
                            if cad[i+1] == "*":
                                ops.append("M " + str(cad[i]))
                                ops.append("ST $"+ str(n))
                                n +=1
                            if cad[i+1] == "/":
                                ops.append("D " + str(cad[i]))
                                ops.append("ST $"+ str(n))
                                n +=1
                            elif cad[i+1] != "+":
                                if cad[i+1] != "-":
                                    if cad[i+1] != "*":
                                        if cad[i+1] != "/":
                                            ops.append("L "+ str(cad[i]))
                                            if cad[i+2] != "+":
                                                if cad[i+2] != "-":
                                                    if cad[i+2] != "*":
                                                        if cad[i+2] != "/":
                                                            ops.append("ST $"+ str(n))
                                                            n +=1

        i +=1
    for i in ops:
        print(i)

codeGeneration("AB+CCD-EF*GH/")
"""
def leerimprimir():
    expresion = input()
    while expresion != "":
        print("Datos leídos = ", expresion)
        expresion = input()
       
leerimprimir()
"""