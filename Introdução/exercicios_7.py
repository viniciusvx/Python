'''Uma imobiliária paga aos seus corretores um salário base
de R$ 1.500,00. Além disso, uma comissão de R$ 200,00 por
cada imóvel vendido e 5% do valor de cada venda. Construa
um programa que solicite o nome do corretor, a quantidade
de imóveis vendidos e o valor total de suas vendas. Ao fim, o
programa deve calcular e escrever o salário final do corretor de
imóveis.'''

sal_base = 1500
comissao = 200
porce = 0.05
corretor = input("Digite o nome do corretor: ")
qtd_vendas = int(input("Informe a quantidade de imóveis vendidos: "))
tot_vendas = float(input("Informe o valor total de vendas R$: "))

sal_final = sal_base + (comissao * qtd_vendas) + (tot_vendas * porce)

print(f"Salário final do corretor {corretor} é de R$: {sal_final:.2f}")