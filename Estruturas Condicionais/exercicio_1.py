'''Construa um programa que receba um número inteiro positivo
informado pelo usuário. Caso ele seja par, o programa deve calcular o 
seu quadrado. Mas, se ele for ímpar, deve ser calculado o seu
cubo. Ao fim, o programa deve imprimir o valor calculado.'''

x = int(input("Informe um numero: "))
if x % 2 == 0:
    quadrado = x ** 2
    print(f"{x} é par e o seu quadrado é {quadrado}.")
else:
    cubo = x ** 3
    print(f"{x} é impar e o seu cubo é {cubo}")