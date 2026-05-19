#def primo (x):
    #for i in range (2,x):
     
     #if x%i == 0:
      #return "não é primo"
     
   # return "é primo"
    
   
#print(primo(10))

def testar_primo(n):
    teste = 1
    for i in range (2,n):
        if n % i == 0:
            teste =+1
    if teste != 1:
        print("NÃO é primo")
    else:
        print("é primo")
testar_primo(11)