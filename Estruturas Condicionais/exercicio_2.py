'''Construa um programa que solicite ao usuário dois números
positivos. Em seguida, o programa deve apresentar o seguinte
menu:
1. Média ponderada, com pesos 2 e 3, respectivamente
2. Quadrado da soma dos 2 números
3. Cubo do menor número
Escolha uma opção:
De acordo com a opção informada, o programa deve calcular a
operação apresentada no menu. Se a opção escolhida for inválida, 
o programa deve mostrar a mensagem “Opção inválida” e ser
encerrado. '''

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))
print("MENU")
print("1. Média ponderada, com pesos 2 e 3, respectivamente")
print("2. Quadrado da soma dos 2 números")
print("3. Cubo do menor número")
op = int(input("Escolha uma opção: "))

if op < 1 or op > 3:
    print("Opção INVALIDA!!!")
    exit()
elif op == 1:
    media = (num1 * 2) + (num2 * 3) / 5
    print(f"\n Média ponderada calculada: {media:.2f}")
elif op == 2:
    quadrado = (num1 + num2) ** 2
    print(f"\nO quadrado  da soma dos numeros: {quadrado:.2f}")
else:
    if num1 < num2:
        cubo = num1 ** 3
        print(f"\n {num1:.2f} é o menor numero e o seu cubo é {cubo:.2f}")
    else:
        cubo = num2 ** 3
        print(f"\n {num2:.2f} é o menor numero e o seu cubo é {cubo:.2f}")