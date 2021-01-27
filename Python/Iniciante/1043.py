A,B,C = input().split(" ")

A = float(A)
B = float(B)
C = float(C)

lista = [A,B,C]
listaOrdenada = sorted(lista)

soma = listaOrdenada[0]+listaOrdenada[1]
perimetro = A+B+C
area = ((A+B)/2)*C

if(soma > listaOrdenada[2]):
    print("Perimetro = {:.1f}".format(perimetro))
else:
    print("Area = {:.1f}".format(area))