#crie um algoritmo que receba um produto e o valor do produto
#se o pagamento for avista a compra tem um desconto de 10%
#se não, é o valor normal e deve mostrar a quantidade de parcelas e o valor
#de cada parcela

nome_produto = input("Digite o nome do produto: ")
valor_produto = float(input("Digite o valor do produto: "))
op = int(input("Digite 1 para pagamento a vista ou 2 para pagar no prazo: "))

if op == 1:
    print(f"O produto: {nome_produto} o valor original: R$ {valor_produto}")
    print(f"O valor do desconto: R$ {valor_produto * 0.1}")
    print(f"O valor com desconto: R$ {valor_produto - valor_produto * 0.1}")
else:
    qtd = int(input("Digite a quantidade de parcelas: "))
    print(f"O produto: {nome_produto} o valor original: R$ {valor_produto}")
    print(f"A quantidade de parcelas: {qtd}")
    print(f"O valor de cada parcela: R$ {valor_produto / qtd}")
    
