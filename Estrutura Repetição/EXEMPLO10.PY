import random

nomes = [
    "pedro", "Camily", "carlos", "maria",
    "karol", "enrique", "Ana", "fred",
    "leonardo", "julia", "felipeMarinha",
    "felipeNormal","Fabio"
]

print("-" * 20)
print("BEM VINDO AO SORTEADOR")
print("-" * 20)

# Embaralha os nomes
random.shuffle(nomes)

print("\nORDEM SORTEADA:\n")

# Mostra os nomes um por um
for nome in nomes:
    print(nome)

print("\nFim do sorteio...")
    