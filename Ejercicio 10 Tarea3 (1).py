## Ejercicio 10
## Grupo: Juan Becerra Gutierrez, Samuel Solarte, Andres Diaz, Laura Lozano, Juan David Troncoso
    # 5 jugadores
    # 2 jugador incial
    # 5 pases

def determinarJugador(n, k, p):
  i = 0
  while i < p:
    i += 1 
    if k < n:
      k += 1
    elif k == n:
      k = 1
  return k
  
def leerImprimir():
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