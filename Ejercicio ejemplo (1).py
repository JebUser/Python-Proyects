def personarestante(s1, s2, s3):
    Persona= None
    if s1 > s2 and s1 < s3:
        Persona= s1
    elif s1 < s2 and s1 > s3:
        Persona = s1
    elif s2 > s1 and s2 < s3:
        Persona= s2
    elif s2 < s1 and s2 > s3:
        Persona= s2
    elif s3 > s1 and s3 < s1:
        Persona= s3
    elif s3 < s1 and s3 > s1:
        Persona= s3



def leerImprimir():
    casos = int(input())
    for i in range(casos):

       s1 = int(input())
       s2 = int(input())
       s3 = int(input())

       v=personarestante(s1,s2,s3)
       print("Case" + str(i+1) + "+ " + str(v))
