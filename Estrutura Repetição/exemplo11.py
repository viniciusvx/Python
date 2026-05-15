import random
n = [2,4,7,1,3,5,6]
random.shuffle(n)
n.sort()#ORDENAÇÃO CRESCENTE
print(n)
n.sort(reverse=True)#DECRESCENTE
print(n)

copia = list(n)
print(n)
print(copia)

n.clear()#limpa os dados da lista
print(n)