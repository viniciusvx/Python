import random
notas=[]
media=0

nota=int(input("Informe a sua nota:\n "))
notas.append(nota)
media = media + nota
if nota<0 or nota>10:
    print("ERRO.")
    exit()


for x in range (3):
 nota=int(input("Informe a sua nota:\n "))
 notas.append(nota)
 media = media + nota
 if nota<0 or nota>10:
     print("ERRO.")
     exit()
 
 
print(notas)


#MENOR = MIN(NOTAS)
#MAIOR = MAX(NOTAS)
#MEDIA = SUM(NOTAS) / LEN(NOTAS)
print(f"A maior nota é {max(notas)}")


print(f"A menor nota é {min(notas)}")


media1 = media/4
print(f"A media das notas é: {media1}")

