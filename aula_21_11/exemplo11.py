
qtddias = 0
op = 0
pagamento = troco = vlr = 0.0
status = "Disponivel"

while op != 7:
    print("\n --- ALUGUEL FAMETRO ---")
    print("\n 1 - GOL - R$ 90,00 A DIARIA ")
    print("\n 2 - Polo - R$ 110,00 A DIARIA ")
    print("\n 3 - Dolphin - R$ 220,00 A DIARIA ")

    op = int(input("\nDigite o código do carro para o aluguel ou 7 para sair: "))

    match(op):
        case 1:
            print("\n 1 - GOL - R$ 90,00 A DIARIA ")
            vlr = 90.00
        case 2:
            print("\n 2 - Polo - R$ 110,00 A DIARIA ")
            vlr = 110.0
        case 3:
            print("\n 3 - Dolphin - R$ 220,00 A DIARIA ")
            vlr = 220.0
        case _:
            print("Opção invalida")

    qtddias = float(input("\nDigite a quantidade de Dias:"))
    vlraluguel = qtddias * vlr
    print(f"O valor do aluguel é: {vlraluguel}")


    pagamento = float(input("\nDigite o valor a pagar: "))
    troco = pagamento - vlraluguel
    print(f"\nO valor do troco é: {troco}")
    print("-"*30)

