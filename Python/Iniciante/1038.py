codigo,quantidade = input().split(" ")

codigo = int(codigo)
quantidade = int(quantidade)

precoProdutos = [4.00, 4.50, 5.00, 2.00, 1.50]
calculoPreco = (quantidade) * (precoProdutos[codigo-1])
print("Total: R$ {:.2f}".format(calculoPreco))