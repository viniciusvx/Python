salario_base=1500
comissao=200

nome=input("Digite o nome do corretor que te atendeu:\n ")
qntd=int(input("Digite a quantidade de imoveis vendidos:\n "))
total_vendas=float(input("Digite o valor total da vendas em R$:\n "))



salario_final= salario_base + (comissao*qntd) + (total_vendas *0.05)
print(f"o seu salario era de {salario_base:.2f} R$")
print(f"após as vendas seu salario deste mes é {salario_final:.2f}R$")