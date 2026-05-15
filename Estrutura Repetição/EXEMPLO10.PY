import random
nomes =[]
print("-"* 20)
print("BEM VINDO AO SORTEADOR")
print("-"* 20)

while True:
    
    nome= input ("Digite um nome: ")
    nomes.append(nome)
    op= input("Deseja continuar [S][N]?")
    if op.upper() == "N":
        break
    
print(nomes)

random.shuffle(nomes)
print(F"lista embaralhada: {nomes}")
sorteio = random.choice(nomes)
print(f" O nome do cara de sorte é: {sorteio}")

while True:
    op= input("Deseja continuar [S][N]?")
    if op.upper() == "N":
        break
    nomes.remove(sorteio)
    print(sorteio)
    sorteio = random.choice(nomes)
    print(f" O nome do cara de sorte é: {sorteio}") 
else:
    print("fim do sorteio...")
    exit()

     
    
    
    