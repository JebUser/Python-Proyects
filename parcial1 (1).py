##Parcial 1
##Juan Esteban Becerra Gutiérrez ID: 8965694

##Ejercicio1

"""
Componentes del Usuario de Facebook
Información personal
    Nombre C
    Apellidos C
    Fecha de Nacimiento C
    Lugar de residencia V
    Foto personal V
    Número de teléfono V
Información general
    Estado sentimental V
    Posición politica V
    Ocupación actual V
    Ubicación actual
Lista de amigos
    Mejores amigos V
    Amigos Normales C
Cuentas asociadas
    Cuenta de Instragram C
    Cuenta de Messenger C
    Cuenta de Whatsapp C
Actividad en la red
    Fotos subidas C
    Videos subidos C
    Mensajes subidos C
    Publicaciones gustadas V
    Grupos a los que pertence V
"""

## Ejercicio 2
def g(a, b, c, d):
    resultado = 0

    if c < 0:
        resultado =((a+b)**(3-c))*(c+d)
    elif c == 0:
        if 3-d > 0:
            resultado = (a**(b+2))*(c**3-d)      
    elif c > 0:
        resultado = 3**(a+b) + ((4-a-c)/d) + a**2

    return resultado

##Ejercicio 3
def ubicacion(centrox, centroy, coordx, coordy):
    sector = None
    if coordx==centrox or coordy==centroy:
        sector = "Esp"
    elif coordx > centrox and coordy > centroy:
        sector  = "NOr"
    elif coordx < centrox and coordy > centroy:
        sector = "NOc"
    elif coordx > centrox and coordy < centroy:
        sector = "SOr"
    else:
        sector = "SOc"
    return sector

## Ejercicio 4
def cuantospuntos(gap1, gbp1, gap2, gbp2, gap3, gbp3, gap4, gbp4): ##gNpX es goles del equipo N en el partido x
    puntosobtenidos = 0

    if gap1 > gbp1:
        puntosobtenidos = puntosobtenidos + 3
    elif gap1 == gbp1:
        puntosobtenidos = puntosobtenidos + 1

    if gap2 > gbp2:
        puntosobtenidos = puntosobtenidos + 3
    elif gap2 == gbp2:
        puntosobtenidos = puntosobtenidos + 1

    if gap3 > gbp3:
        puntosobtenidos = puntosobtenidos + 3
    elif gap3 == gbp3:
        puntosobtenidos = puntosobtenidos + 1

    if gap4 > gbp4:
        puntosobtenidos = puntosobtenidos + 3
    elif gap4 == gbp4:
        puntosobtenidos = puntosobtenidos + 1

    return puntosobtenidos

##Ejercicio 5
def verificarMayor(diaZ, mesZ, añoZ, diaD, mesD, añoD, diaT, mesT, añoT):
    Zatlanesmayor = None
    if añoZ <= añoD and añoZ <= añoT:
        if mesZ <= mesD and mesZ <= mesT:
            if diaZ <= diaD and diaZ <= diaT:
                Zatlanesmayor = True
            else:
                Zatlanesmayor = False
        else:
            Zatlanesmayor = False
    else:
        Zatlanesmayor = False

    return Zatlanesmayor
