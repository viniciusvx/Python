abrir_arquivo = open('C:/Users/vboxuser/Documents/primeiro_arquivo.txt','w') #VAI ABRIR UM ARQUIVO E APGAR TUDO O QUE TEM NELE


abrir_arquivo.write("numeros pares de 1 a 100 " )
for i in range(1,101):
    if i % 2 == 0:
        abrir_arquivo.write (f"{i}\n")
print("Gravação realizada com sucesso")

abrir_arquivo.close()

abertura = open ('C:/Users/vboxuser/Documents/primeiro_arquivo.txt','r')
print(abertura.readlines())
abertura.close()
    

