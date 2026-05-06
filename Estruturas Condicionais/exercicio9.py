programador= 0.3
analista_sistema=0.2
analista_banco=0.15

while True:
    salario=float(input("Digite o seu salario: "))
    cargo=int(input("1-programador\n 2- analista de sistemas\n 3-analista de banco de dados\n"))
    
    if cargo<1 or cargo>3:
        print("CARGO INVÁLIDO!!")
        exit()

    if cargo ==1:
        print("Voce é um programador e receberá um aumento de 30%")
        aumento= (salario * programador) + salario
        print(f"O seu salario era de: {salario}$")
        print(F"Após o aumento ficou: {aumento}$")
        break
    
    elif cargo ==2:
        print("Voce é um analista de sistemas e receberá um aumento de 20%")
        aumento= (salario * analista_sistema) + salario
        print(f"O seu salario era de: {salario}$")
        print(F"Após o aumento ficou: {aumento}$")
        break
    
    elif cargo ==3:
        print("Voce é um analista de banco de dados e receberá um aumento de 15%")
        aumento= (salario * analista_banco) + salario
        print(f"O seu salario era de: {salario}$")
        print(F"Após o aumento ficou: {aumento}$")
        break
    
        
    

