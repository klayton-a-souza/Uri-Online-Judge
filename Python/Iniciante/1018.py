valor = int(input())
notas = [100,50,20,10,5,2,1]

for nota in notas:
    quantNotas = int(valor/nota)
    print("{} nota(s) de R$ {:.2f}".format(quantNotas,nota))
    valor -= quantNotas * nota