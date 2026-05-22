

def nivel_facil():
  numero_desconhecido = 42
  total_tentativa = 10
  pontuacao = 100
  for tentativa in range (1,total_tentativa + 1):
    print(f"tentativa {tentativa} de {total_tentativa}")

    chute = int(input("Digite um numero: "))

    acertou = chute == numero_desconhecido
    maior = chute > numero_desconhecido
    pontuacao = pontuacao - 10

    if (acertou):
        print("Parabéns!!Você acertou número")
        break

    elif (maior):
        print("Voce errou! o numero que voce digitou é MAIOR")
        print(f"sua pontuação é de: {pontuacao}")
    else:
        print("Voce errou! o numero que voce digitou é MENOR")
        print(f"sua pontuação é de: {pontuacao}")
    return nivel_facil

def nivel_medio():
   numero_desconhecido = 42
   total_tentativa = 5
   pontuacao = 100
   for tentativa in range (1,total_tentativa + 1):
    print(f"tentativa {tentativa} de {total_tentativa}")

    chute = int(input("Digite um numero: "))

    acertou = chute == numero_desconhecido
    maior = chute > numero_desconhecido
    pontuacao = pontuacao - 20

    if (acertou):
        print("Parabéns!!Você acertou número")
        break

    elif (maior):
        print("Voce errou! o numero que voce digitou é MAIOR")
        print(f"sua pontuação é de: {pontuacao}")
    else:
        print("Voce errou! o numero que voce digitou é MENOR")
        print(f"sua pontuação é de: {pontuacao}")
    return nivel_medio

def nive_dificil():
   numero_desconhecido = 42
   total_tentativa = 3
   pontuacao = 100
   for tentativa in range (1,total_tentativa + 1):
    print(f"tentativa {tentativa} de {total_tentativa}")

    chute = int(input("Digite um numero: "))

    acertou = chute == numero_desconhecido
    maior = chute > numero_desconhecido
    pontuacao = pontuacao - 30

    if (acertou):
        print("Parabéns!!Você acertou número")
        break

    elif (maior):
        print("Voce errou! o numero que voce digitou é MAIOR")
        print(f"sua pontuação é de: {pontuacao}")
    else:
        print("Voce errou! o numero que voce digitou é MENOR")
        print(f"sua pontuação é de: {pontuacao}")
    
   



   

    