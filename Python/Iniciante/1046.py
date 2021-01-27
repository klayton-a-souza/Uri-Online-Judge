a,b = input().split(" ")

a = int(a)
b = int(b)

if (a > b):
    duracao = ((23 - a)+(b+1))
    print("O JOGO DUROU",duracao, "HORA(S)")
elif(a == b):
    duracao = 24 
    print("O JOGO DUROU", duracao,"HORA(S)")
else:
    duracao = b - a
    print("O JOGO DUROU", duracao,"HORA(S)")