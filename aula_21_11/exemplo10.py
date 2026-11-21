aluno = ""
x = "sair"
status = ""
n1 = n2 = media = mediageral = 0.0
cont = 0

while aluno != x:
    aluno = input("Digite o nome do aluno ou sair para fechar o programa: ")
    if aluno == x:
        break
    else:
        n1 = float(input("Digite a nota 1: "))
        n2 = float(input("Digite a nota 2: "))
        media = (n1 + n2) / 2
        if media >= 5:
            status = "Aprovado"
            print(f"O aluno {aluno}  a media: {media} e o status: {status}")
        else:
            status = "Reprovado"
            print(f"O aluno {aluno}  a media: {media} e o status: {status}")

        cont=cont+1
        mediageral += media

print(f"A quantidade de alunos: {cont}")
print(f"A media geral da turma: {mediageral/cont}")

