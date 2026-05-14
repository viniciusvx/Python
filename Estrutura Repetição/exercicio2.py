''' O PROGRAMA DEVE INFORMAR O NOME DO PREÇO DO MEDICAMENTO E O NOME,O NOME E O VALOR DO MENOR ENTRE ELES E A MEDIA ARITIMETICA 
DOS PREÇOS INFORMADOS, TEM QUE SER 5 MEDICAMENTOS'''

media_preco= 0

medicamento= input("Digite o nome do medicamento:\n ")
preco=float(input("Informe o preço do produto:\n "))
nome_mediacamento = medicamento
menor_preco = preco
media_preco = media_preco + preco

for x in range (4):
    medicamento = input("Digite o nome do medicamento:\n ")
    preco=float(input("Informe o preço:\n "))
    
    if preco < menor_preco:
        menor_preco = preco
        nome_medicamento = medicamento 
        media_preco = media_preco + preco
        
media= media_preco / 5

print(f" O {nome_medicamento} é o mediacamento mais barato, custa R${menor_preco}")
print(f"A media é: {media}")