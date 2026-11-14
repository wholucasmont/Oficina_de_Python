#crie um algoritmo para entrar com o nome, a nota 1, 2 e 3 de um aluno
#e calcular a média
nome = input("Digite seu nome: ")
n1 = float(input("Digite a N1: "))
n2 = float(input("Digite a N2: "))
n3 = float(input("Digite a N3: "))
media = (n1 + n2 + n3) / 3

print(f"O aluno {nome}, a média das suas notas {n1}, {n2}, {n3} é : {media}")