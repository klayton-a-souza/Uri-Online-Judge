dias = int(input())

ano = dias//365
print(ano,"ano(s)")
dias = dias - (ano*365)
mes = dias//30
print(mes,"mes(es)")
dias = dias - (mes*30)
print(dias,"dia(s)")