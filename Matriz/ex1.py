def acessando_elementos():
    matriz=[[1,2,3], #linha 0
            [4,5,6], #linha 1
            [7,8,9]  #linha 2
            ]


    print(matriz[0][0]) #linha, coluna

def colunas_e_linhas():
    matriz=[[10,20,30],
           [40,50,60]]
    linhas=len(matriz) #le todos os valores
    colunas=len(matriz[0]) #le a primeira coluna começando por 0
    print("linhas:", linhas)
    print("colunas:", colunas)

def percorrer_matriz():
     matriz=[[1,2,3], #linha 0
            [4,5,6], #linha 1
            [7,8,9]  #linha 2
            ]
     for linha in range(len(matriz)):
         for coluna in range(len(matriz[linha])):
             print(matriz[linha][coluna],
                   end="")
         print()
def calcular_media():#decobre quantas colunas e linhas
    notas = [[5.0, 4.5, 7.0, 5.2, 6.1],
            [2.1, 6.5, 8.0, 7.0, 6.7],
            [8.6, 7.0, 9.1, 8.7, 9.3]]

    cont = soma = 0

    for linha in range(len(notas)): #percorre cada linha
        for coluna in range(len(notas[linha])): #percorre cada coluna
            soma = soma + notas[linha][coluna]
            cont = cont + 1

    media = soma / cont
    print(media)
    print(soma)
    print(cont)
def preencher_matriz_com_input(): #cria uma matriz 
    matriz=[]

    for linha in range(3):
        nova=[]
        for coluna in range(3):
            valor=float(input("Digite a nota: "))
            nova.append(valor)


        matriz.append(nova)
    print(matriz)