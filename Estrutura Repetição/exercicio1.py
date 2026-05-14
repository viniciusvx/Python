a = int(input("informe um numero: \n"))
b = int(input("informe um numero:  \n "))

if a<b:
 soma = 0
 for x in range (a,b +1):
     soma = soma + x
     print (f"Soma dos intervalos no intervalo de {a} e {b} é: {soma}")
else:
    print("ERRO. A deve ser menor que B")