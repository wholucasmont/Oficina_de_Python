#digite o nome a idade e o salário de uma pessoa e calcule o INSS
#que é de 11% e mostre o desconto e o novo salário

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salario: "))
inss = salario*0.11
novosal = salario - inss

print(f"O seu nome é {nome}, sua idade é {idade} e seu salario é R${salario}")
print(f"O desconto do INSS: R$ {inss}, o novo salário: R${novosal}")