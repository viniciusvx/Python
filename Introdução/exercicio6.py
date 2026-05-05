'''IMPLEMENTE UM PROGRAMA QUE CONVERTA O VALOR DE UMA VELOCIDADE MEDIA EM KM/H PARA M/S
PARA ISSO, O USUARIO DEVE INFORMAR O VALOR DA VELOCIDADE MEDIA.SABE QUE O DAOR UTILIZADO PARA CONVERSAO É 3,6'''
a=3.6
n1=float(input("Digite a velocidade media em (km/h)\n"))
conversao =n1/a

print(f"a velocidade media é {n1:.2f}km/h,equivale a {a:.2f} m/s")
