valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1.0 , 0.50, 0.25, 0.10, 0.05 , 0.01]

print("NOTAS:")
for nota in notas:
    quantNotas = int((valor/nota))
    print("{} nota(s) de R$ {:.2f}".format(quantNotas,nota))
    valor -= quantNotas * nota
print("MOEDAS:")
for moeda in moedas:
    quantMoedas = int(round(valor,2) / moeda)
    print("{} moeda(s) de R$ {:.2f}".format(quantMoedas,moeda))
    valor -= quantMoedas * moeda