

nome = input("Digite o nome do vendedor: ")
salario_base = 1750.0
comissao = novo_salario = 0.0

total_vendas = float(input("Digite o valor total das vendas: "))
if total_vendas <= 1000.0:
    comissao = total_vendas*1/100
elif total_vendas <= 5000.0:
    comissao = total_vendas*2/100
elif total_vendas <= 10000.0:
    comissao = total_vendas*3/100
else:
    comissao = total_vendas*4/100

print(f"O vendedor: {nome} receberá R${salario_base} + sua comissão: R${comissao}")
print(f"Salário mais comissão: {salario_base + comissao:.2f}")