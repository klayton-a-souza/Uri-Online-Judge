a,b,c = input().split(" ")

a = int(a)
b = int(b)
c = int(c)

MaiorAB = (a+b+abs(a-b))/2
MaiorABC = (MaiorAB+c+abs(MaiorAB-c))/2

convercao = int(MaiorABC)

print(convercao," eh o maior")