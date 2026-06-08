n = int(input("Digite a dimensão N da matriz: "))
m = int(input("Digite a dimensão M da matriz"))

matriz = []

for i in range(n):
    linha = []
    for j in range(m):
        linha.append(0)

    matriz.append(linha)

print(matriz)