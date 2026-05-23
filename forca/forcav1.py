print("*" * 50)
print("-" * 5, 'Bem vindo ao jogo da forca',"-" * 5)
print("*" * 50)
palavra_secreta = "algoritmo"
letras_encontrada = ["_","_","_","_","_","_","_","_","_"]
acertou = False
enforcou = False
erros = 0

while(not acertou and not enforcou):
    palpite=input("Qual a letra?\n")
    if (palpite in palavra_secreta):
     posicao=0
     for letra in palavra_secreta:
        if (palpite.upper() == letra.upper()):
            letras_encontrada[posicao] = letra
        
        posicao = posicao+1
    else:
       erros += 1

    enforcou = erros ==5
    acertou = "_" not in letras_encontrada
    print(letras_encontrada)

if (acertou):
   print("Voce ganhou")
else:
   print("Voce perdeu")

print("fim de jogo")    