pessoas = []

for i in range(5):
    nome = input(f'Informe o nome da {i + 1}ª pessoa: ')
    idade = int(input(f'Informe a idade de {nome}: '))
    
    pessoas.append([nome, idade])

menor = 0

for i in range(len(pessoas)):
    if pessoas[i][1] < pessoas[menor][1]:
        menor = i

for pessoa in pessoas:
    print(pessoa)

print(f"A pessoa mais nova é {pessoas[menor][0]}")