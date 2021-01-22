codigoPeca01 = int(input()) 
numeroPeca01 = int(input())
valorUnitario01 = float(input())

codigoPeca02 = int(input())
numeroPeca02 = int(input())
valorUnitario02 = float(input())

valorPagar01 = numeroPeca01*valorUnitario01 
valorPagar02 = numeroPeca02*valorUnitario02
valorPagar = valorPagar01 + valorPagar02

print("VALOR A PAGAR: R$ %.2f"%valorPagar)