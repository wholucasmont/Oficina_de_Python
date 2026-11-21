# crie um algoritmo para entrar com um modelo de um carro e o valor dele
# ao final deve mostrar o total de preço de todos os carros somados
# cadastre 4 carros

modelo = nome = ""
preco = soma = vlr = 0.0

for i in range(1, 6):
    modelo = input("Digite modelo do carro: ")
    preco = float(input("Digite o preco do carro: "))

    soma+=preco

    if preco > vlr:
        nome = modelo
        vlr = preco

print(f"Todos os preços dos carros somados: {soma}")

print(f"O carro mais carro: {nome} R$: {vlr}")

