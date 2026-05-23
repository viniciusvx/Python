import random

print("-" * 10, "ADIVINHAR NUMERO", "-" * 10)

print("1 - Nivel 1")
print("2 - Nivel 2")
print("3 - Nivel 3")

nivel = int(input("Escolha o nivel: "))
if nivel == 1:
    total_tentativa = 10
elif nivel == 2:
    total_tentativa = 5
elif nivel == 3:
    total_tentativa = 3
else:
    print("Nivel inválido!")
    exit()

numero_desconhecido = random.randint(1, 100)
pontuacao = 100

for tentativa in range(1, total_tentativa + 1):
    print(f"Tentativa {tentativa} de {total_tentativa}")
    chute = int(input("Digite um numero: "))
    
    if chute == numero_desconhecido:
        print("Parabéns! Você acertou!")
        print(f"Pontuação: {pontuacao}")
        break
    elif chute > numero_desconhecido:
        print("O número secreto é MENOR.")
    else:
        print("O número secreto é MAIOR.")
    pontuacao -= 10
    print(f"Pontuação: {pontuacao}")
else:
    print(f"Você perdeu! O número era {numero_desconhecido}")
