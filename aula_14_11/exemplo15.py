
op = 0
pag = troco =  x = soma = 0.0

for i in range(3):
    print("\n### SISTEMA DE VENDAS ###")
    print("1 - XSALADA + SUCO = R$ 12.0")
    print("2 - XTUDO + SUCO = R$ 14.0")
    print("3 - PASTEL + SUCO = R$ 8.0")
    print("4 - SOPA + SUCO = R$ 18.0")

    op = int(input("Digite o número do combo: "))

match op:
    case 1:
        print("1 - XSALADA + SUCO = R$ 12.0")
        x = 12.00
    case 2:
        print("1 - XTUDO + SUCO = R$ 14.0")
        x = 14.00
    case 3:
        print("1 - PASTEL + SUCO = R$ 8.0")
        x = 8.0
    case 4:
        print("1 - SOPA + SUCO = R$ 18.0")
        x = 18.0
    case _:
        print(" Opção invalida !")

soma += x
print(f"\nO total: R$ {soma} ")

pag = float(input("\nDigiteo pagamento: "))

print(f"\nO troco: R$ {pag - soma}")






