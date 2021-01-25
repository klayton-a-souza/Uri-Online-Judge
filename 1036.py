A,B,C = input().split(" ")

A = float(A)
B = float(B)
C = float(C)

raiz = (B**2)-4*A*C
divisao = 2*A

if(raiz < 0):
    print("Impossivel calcular")
elif(divisao == 0):
    print("Impossivel calcular")
else:
    raiz = raiz**0.5
    x1 = (-B + raiz)/divisao
    x2 = (-B - raiz)/divisao
    print("R1 = {:.5f}".format(x1))
    print("R2 = {:.5f}".format(x2))