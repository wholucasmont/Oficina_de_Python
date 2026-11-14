#condicional composta
#crie um algoritmo p/ controlar a media e o status de um aluno, 3 notas.
#se a media for maior ou igual a 6 o status é aprovado, senão é reprovado
from sympy.strategies.core import switch

nome = input("Digite o nome: ")
n1 = float(input("Digite a N1: "))
n2 = float(input("Digite a N2: "))
n3 = float(input("Digite a N3: "))
media = (n1 + n2 + n3) / 3

if media >= 6.0:
    print(f"O(A) {nome} está aprovado(a)  !! ")
else:
    print(f"O(A) {nome} está reprovado(a) !! ")

print("\nFim do algoritmo !")
