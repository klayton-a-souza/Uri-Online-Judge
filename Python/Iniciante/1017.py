tempoGasto = int(input())
velocidadeMedia = int(input())

consumoMedio = 12
calculoDistancia = velocidadeMedia*tempoGasto
consumoTotal = calculoDistancia/consumoMedio

print("%.3f"%consumoTotal)