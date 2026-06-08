notas =    [[5.0, 4.5, 7.0, 5.2, 6.1],
            [2.1, 6.5, 8.0, 7.0, 6.7],
            [8.6, 7.0, 9.1, 8.7, 9.3]]

cont = soma = 0

for linha in range (len(notas)):
    print(f"linhas percorridas: {linha}")
   
    for coluna in range(len(notas[linha])):
        print(f"colunas percorridas: {coluna}")
        print(f"Valores da matriz: {notas[linha][coluna]}")
   
        soma += notas[linha][coluna]
        cont += 1

media = soma/cont
print(media)