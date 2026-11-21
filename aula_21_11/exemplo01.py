import math
a = b = c = delta = 0

x1 = x2 = raiz = 0.0

a = int(input("Insira o valor para A: "))
b = int(input("Insira o valor para B: "))
c = int(input("Insira o valor para C: "))

delta = b**2 - 4*a*c
if delta < 0:
    print("Delta é negativo, não gera valor real !!")
else:
    raiz = math.sqrt(delta)

    x1 = (-b + raiz)/2*a
    x2 = (-b - raiz)/2*a

    print(f"Delta é: {delta}")
    print(f"X' : {x1}")
    print(f"X'' : {x2}")