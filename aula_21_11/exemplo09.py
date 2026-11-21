# crie um algoritmo para contar quantos produtos foram informados
# guardar o mais caro e o mais barato
# mostrar o preco de todo o estoque e a media de preco
# ate o usuario digitar sair


x = "sair"
produto = nomemaior = nomemenor = ""
preco = soma = maiorv = 0.0
menorv = 10000

cont = 0
while produto != x:
    produto = input("Digite um produto ou sair para fechar o programa: ")
    if produto == x:
        break
    else:
        preco = float(input("Digite o preço do produto:  : "))

     #maior preço dentre os produtos cadastrados
    if(preco > maiorv):
        maiorv = preco
        nomemaior = produto

     #menor preço dentre os produtos cadastrados
    if(preco < menorv):
        menorv = preco
        nomemenor = produto

    print(f"{produto} cadastrado com sucesso !")
    print("-"*20)
    cont = cont + 1
    soma+=preco

print(f"\n\nA quantidade de produtos informados é: {cont}")
print(f"\nO produto com maior preço é: {nomemaior} R$ {maiorv}")
print(f"\nO produto com o menor preço é: {nomemenor} R$ {menorv}")
print(f"\nA soma de todos os preços: R$ {soma}")
print(f"\nA media de preços dos produtos: R$ {soma/cont}")