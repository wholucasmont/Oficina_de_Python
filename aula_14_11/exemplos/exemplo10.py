#condicional composta
#crie um algoritmo p/ controlar a entrada de pessoas numa festa
#entre com o nome e a idade
#se o cidadão for maior de idade ele pode entrar

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

if idade >= 18:
    print(f"O(A) {nome} está liberado(a)  !! ")
else:
    print(f"O(A) {nome} está proibido(a) !! ")

print("\nFim do algoritmo !")