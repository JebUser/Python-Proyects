#Ejercicio 9

def determinarTriangulo(x1, y1, x2, y2, x3, y3):

    lado1 = math.sqrt((abs(x1-x2))**2 + (abs(y1-y2))**2) ## Tenía que dar la funcion "round" para que diera el resultado de abajo.
    lado2 = math.sqrt((abs(x2-x3))**2 + (abs(y2-y3))**2) ## como "round(math.sqrt((abs(x2-x3))**2 + (abs(y2-y3))**2))"
    lado3 = math.sqrt((abs(x1-x3))**2 + (abs(y1-y3))**2)
    figura = None
    if lado1 == lado2 and lado1 == lado3:
        figura = "Equilatero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        figura = "Isoceles"
    elif lado1 != lado2 and lado1 != lado3:
        figura = "Escaleno"
    print(lado1, lado2, lado3)
    return figura
##Prints solo para verificar datos
ejemplo4 = determinarTriangulo(0, 0, 4, 0, 2, 3)
print(ejemplo4)

