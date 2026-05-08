# palavra="paralelepipedo"

#frutas = ["laranja","maça","goiaba","pera"]
#frutas = frutas + ["uva","abacaxi","morango","banana","kiwi"]
#print(frutas)

#frutas[7] ="banana da terra"
#frutas.remove("uva")


#print(frutas)

#print(frutas[3:6])

#numeros=[1,2,3,4,5]
#print(numeros)
#numeros[1]=numeros[3] + numeros[2]
#print(numeros)

numeros = [1,2,3,4,5]
print(numeros)
numeros.append(6) #adicioan 1 item
print(numeros)
numeros.extend(["laranja","maça","uva"]) #adiciona 1 ou +
print(numeros)
numeros.insert(2,"casa") #adicionar o item e dar a posiçao especifica
print(numeros)
numeros.remove("laranja")#remove pela palavra        
print(numeros)
numeros.pop(5)#remove pelo indice
print(numeros)