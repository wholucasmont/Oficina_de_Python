#crie um programa que calcule a media ponderada de duas notas,
#onde a primeira nota tem peso 2 e a segunda nota tem peso 3.
nome = input("Digite seu nome: ")
n1 = float(input("Digite a N1: "))
n2 = float(input("Digite a N2: "))
media = (n1*2 + n2*3) /5

print(f"O aluno {nome}, a média das suas notas {n1}, {n2} é : {media}")