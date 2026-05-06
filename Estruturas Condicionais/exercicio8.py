n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

while True:
    print("MENU")
    res=int(input("1-media ponderada com peso 2 e 3\n 2-quadrado da soma dos 2 numeros\n 3-cubo do menor numero\n"))
    
    if res<1 or res>3:
        print("OPÇÃO INVÁLIDA!")
        break
    
    
    if res == 1:
        media_ponderada=(((n1*2) + (n2*3))/ (2+3))
        print(f"A media ponderada com peso 2 e 3 é: {media_ponderada}")
        break
    
    if res == 2:
        soma= n1+n2
        quadrado_soma= soma **2
        print(f"O quadrado da soma dos dois numero é: {quadrado_soma}")
        break
    if res == 3:
        if n1 < n2:
            menor = n1
        else:
            menor = n2

        cubo = menor ** 3
        print(f"O menor numero é {menor}, e o cubo é: {cubo}")
        break
    
       

    
