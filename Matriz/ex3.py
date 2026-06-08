notas = []

for i in range(3): #VAI PERCORRER 3 LINHAS
    linha = []
    for j in range(3): #VAI PERCORRER 3 COLUNAS
        msg = f'Nota {j+1} do aluno {i+1}: '
        linha.append(float(input(msg)))
    
    notas.append(linha)
    print(notas)