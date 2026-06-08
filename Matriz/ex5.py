matriz = []
for l in range(3):
    linha = []
    for c in range(3):
        msg=f'Numero da celula [{l}][{c}?:'
        linha.append(int(input(msg))) #CRIOU UMA VARIVEL DIRETO E JÁ ADICIONOU ELA NA LINHA QUANDO O USUARIO DIGITA 
    
    matriz.append(linha)

pares = 0
impares =0

for linha in matriz: #TODAS AS LINHAS DA MATRIZ
    for e in linha: #CADA ELMTENTO DA LINHA
        if e % 2 == 0:
            pares += 1
        else:
            impares +=1

for linha in matriz:
    print(linha)

print(f"A matriz contem {pares} numeros pares")
print(f"A matriz contem {impares} numeros impares")