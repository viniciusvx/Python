mulheres= 0 
homens_18 = 0

while True:
 for i in range(5):
     idade=int(input("Digite a sua idade: "))
     if idade<0:
        break
     sexo = input("M - MASCULINO || F - FEMININO \n")
     if sexo == "F" or sexo == "f":
        mulheres = mulheres + 1
     elif sexo == "M" or sexo =="m":
        if idade >= 18:
            homens_18 = homens_18 + 1
 print(f" total de mulhres é: {mulheres}")
 print(f" total de homens é: {homens_18}")