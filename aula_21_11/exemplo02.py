import math


def resolver_equacao_segundo_grau():
    a = float(input("Insira o valor para A: "))
    b = float(input("Insira o valor para B: "))
    c = float(input("Insira o valor para C: "))

    if a == 0:
        print("O valor de A deve ser diferente de zero para ser uma equação do 2º grau.")
        return

    delta = b**2 - 4 * a * c
    print(f"Delta é: {delta}")

    if delta < 0:
        print("Delta é negativo: não existem raízes reais.")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Delta é zero: há apenas uma raiz real -> x = {x}")
    else:
        raiz = math.sqrt(delta)
        x1 = (-b + raiz) / (2 * a)
        x2 = (-b - raiz) / (2 * a)
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")


if __name__ == "__main__":
    resolver_equacao_segundo_grau()
