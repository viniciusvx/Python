'''Uma empresa concederá um aumento de salário aos seus
funcionários, variável de acordo com o cargo, conforme a tabela
abaixo:

Cargo Aumento               (%)
Programador de Sistemas     30
Analista de Sistemas        20
Analista de Banco de Dados  15
Crie um programa que solicite ao usuário o salário e o cargo de
um determinado funcionário. Na sequência, o programa deve calcular e 
imprimir o seu novo salário. 
Caso o cargo informado não
esteja na tabela, o programa deve imprimir “Cargo inválido”.'''

print("-*" * 20)
print("1 - Programador de Sistemas")
print("2 - Analista de Sistemas")
print("3 - Analista de Banco de Dados")
print("-*" * 20)

salario = float(input("Digite seu salario R$: "))
cargo = int(input("Digite o cargo:"))
if cargo < 1 or cargo > 3:
    print("Cargo Inválido")
    exit()
elif cargo == 1:
    #salario = salario * 1.3
    salario *= 1.3
    #salario = salario * 0.30 + salario
    print(f"Novo Salário é de R$ {salario:.2f}")
elif cargo == 1:
    #salario = salario * 1.3
    salario *= 1.2
    #salario = salario * 0.30 + salario
    print(f"Novo Salário é de R$ {salario:.2f}")
else:
    #salario = salario * 1.3
    salario *= 1.15
    #salario = salario * 0.30 + salario
    print(f"Novo Salário é de R$ {salario:.2f}")