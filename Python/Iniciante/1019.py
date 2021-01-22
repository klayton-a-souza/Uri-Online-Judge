totalSegundos = int(input())

quantidadeHoras = totalSegundos//60//60
segundosHoras = quantidadeHoras*60*60
restante = totalSegundos - segundosHoras
quantidadeMinutos = restante//60
segundosMinutos = quantidadeMinutos*60
quantidadeSegundos = restante - segundosMinutos

print('{}:{}:{}'.format(quantidadeHoras, quantidadeMinutos, quantidadeSegundos))