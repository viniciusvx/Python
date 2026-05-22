# =========================================
# OPERADORES ARITMÉTICOS
# =========================================

# +  Adição
# -  Subtração
# *  Multiplicação
# /  Divisão
# // Divisão inteira
# %  Resto da divisão
# ** Potenciação

print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 // 3)
print(10 % 3)
print(2 ** 3)


# =========================================
# STRINGS
# =========================================

texto1 = "Revisão"
texto2 = "De novo"

# Concatenar strings

print(texto1 + texto2)

# Repetir texto

print(texto1 * 3)

# Métodos de string

print(texto2.upper())
print(texto2.capitalize())
print(texto2.lower())


# =========================================
# ENTRADA DE DADOS
# =========================================

frase = input("Digite algo:\n")
print(frase)

numero = input("Digite um número:\n")
print("O número digitado foi " + numero)

nome = input("Digite seu nome:\n")
idade = input("Digite sua idade:\n")

# Método format

print("Seu nome é {} e sua idade é {}".format(nome, idade))

# f-string

print(f"Seu nome é {nome} e sua idade é {idade}")