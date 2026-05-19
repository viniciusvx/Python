def soma (a,b):
    soma = a + b
    return soma

def subtracao (a,b):
    soma = a - b
    return subtracao

def multiplicaçao (a,b):
    return multiplicaçao

def divisao (a,b):
    divisao= a / b
    return divisao

def menu ():
    print("CALCULADORA")
    print("1- SOMA")
    print("2- SUBTRAÇÃO")
    print("3- MULTIPLICAÇÃO")
    print("4- DIVISÃO")
    op = int(input("Informe a opção que deseja: "))
    a = float(input("Informe o 1° numero: "))
    b = float(input("Informe o 2° numero: "))

    if op == 1:
     print(soma(a,b))

    elif op == 2:
     print(subtracao(a,b))

    elif op == 3:
     print(multiplicaçao(a,b))

    elif op == 4:
     print(divisao(a,b))
    
    else:
       print("Opcão incorreta")
menu()