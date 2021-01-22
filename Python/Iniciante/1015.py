x1,y1 = input().split(" ")
x2,y2 = input().split(" ")

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

calculoX = (x2-x1)**2
calculoY = (y2-y1)**2
distancia = (calculoX+calculoY)**0.5

print("%.4f"%distancia)