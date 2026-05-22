numero_desconhecido = 42
total_tentativa = 3


for tentativa in range (1,total_tentativa + 1):
    print("tentativa {} de {}".format(tentativa, total_tentativa))

    chute = int(input("Digite um numero: "))

    acertou = chute == numero_desconhecido
    maior = chute > numero_desconhecido

    if (acertou):
        print("Parabéns!!Você acertou número")
        break
    elif (maior):
        print("Voce errou! o numero que voce digitou é MAIOR")
    else:
        print("Voce errou! o numero que voce digitou é MENOR")

    

print("FIM DE JOGO")