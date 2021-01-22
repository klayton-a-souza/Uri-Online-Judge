nomeVendedor = input()
salarioFixo = float(input())
totalVendasNoMes = float(input())
comicao = 0.15
salarioFinal = (salarioFixo)+(totalVendasNoMes*comicao)
print("TOTAL = R$ %.2f"%salarioFinal)