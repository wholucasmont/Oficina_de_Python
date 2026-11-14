#crie um algoritmo que o nome do aluno
#as 2 notas, calcule a media e adicione o status
#aprovado, emxame e reprovado

nome = input("Digite o nome do aluno: ")
n1 = float(input("Digite a Nota 1 do aluno: "))
n2 = float(input("Digite a Nota 2 do aluno: "))

media = (n1 + n2) / 2

if media >= 6:
    print(f"O aluno: {nome} está aprovado com média {media}")
elif media >= 4 and media < 6:
    print(f"O aluno: {nome} está em exame de recuperação com média {media}")
else:
    print(f"O aluno: {nome} está reprovado com média {media}")
