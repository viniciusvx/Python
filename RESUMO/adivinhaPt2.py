numero_desconhecido = 42
chute = int(input("Digite um numero: "))

if chute == numero_desconhecido:
    print("Parabéns!!Você acertou número")
else:
    if(chute> numero_desconhecido):
       print("Você errou! o seu chute é maior que o número desconhecido")
    else:
       print("Você errou! o seu chute é menor que o número desconhecido")