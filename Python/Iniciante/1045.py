A,B,C = input().split(" ")

A = float(A)
B = float(B)
C = float(C)

lista = sorted([A,B,C],reverse = True)

if((lista[0]) >= (lista[1]+lista[2])):
    print("NAO FORMA TRIANGULO")
else:
    if((lista[0]**2) == ((lista[1]**2)+(lista[2]**2))):
        print("TRIANGULO RETANGULO")

    if((lista[0]**2)>((lista[1]**2)+(lista[2]**2))):
        print("TRIANGULO OBTUSANGULO")

    if((lista[0]**2)<((lista[1]**2) + (lista[2]**2))):
        print("TRIANGULO ACUTANGULO")

    if(A == B == C):
        print("TRIANGULO EQUILATERO")

    if(((A==B)and (A != C)))or((A==C)and(A!=B))or(((C == B) and (A != C))):
        print("TRIANGULO ISOSCELES")