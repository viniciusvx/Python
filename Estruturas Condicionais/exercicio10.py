a = int(input("Digite o valor de: a "))
b = int(input("Digite o valor de: b "))
c = int(input("Digite o valor de: c "))

delta = (b**2) - (4*a*c)

print(f"O valor de delta é: {delta}")

if delta < 0:
    print("Não existem raízes reais")
else:
    x1 = (-b + (delta**0.5)) / (2*a)
    x2 = (-b - (delta**0.5)) / (2*a)

    print("Agora vou te mostrar Bhaskara")
    print(f"Esse é x1 = {x1:.2f}")
    print(f"Esse é x2 = {x2:.2f}")