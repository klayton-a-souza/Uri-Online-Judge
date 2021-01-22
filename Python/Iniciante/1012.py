a,b,c = input().split(" ")

a = float(a)
b = float(b)
c = float(c)

areaTringulo = (a*c)/2
areaCirculo = (c**2)*(3.14159)
areaTrapezio = ((a+b)/2)*c
areaQuadrado = b**2
areaRetangulo = a*b

print("TRIANGULO: %.3f"%areaTringulo)
print("CIRCULO: %.3f"%areaCirculo)
print("TRAPEZIO: %.3f"%areaTrapezio)
print("QUADRADO: %.3f"%areaQuadrado)
print("RETANGULO: %.3F"%areaRetangulo)