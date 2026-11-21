#crie um algoritmo para contar quantos produtos foram informados
#até o usuario digitar sair

x = "sair"
produto = ""
cont = 0
while produto != x:
    produto = input("Digite um produto ou sair para fechar o programa: ")
    if produto.lower() == "sair":
        break
    else:
        print(f"{produto} cadastrado com sucesso !")
        cont = cont + 1

print(f"\n\nA quantidade de produtos informados é: {cont}")



