import math

print("Calculadora de Bhaskara")

a = float(input("Informe o coeficient a: "))
b = float(input("Informe o coeficient b: "))
c = float(input("Informe o coeficient c: "))

print(f"{a}x²+{b}x+{c}")

delta = b**2 - 4*a*c

if delta < 0:
    print("Não existem raizes reais")
elif delta == 0:
    raiz = -b / (2*a)
    print(f"Existe apenas uma raiz real: {raiz}")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Existem duas raizes reias: {raiz1} e {raiz2}")