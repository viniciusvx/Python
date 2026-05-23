'''SOLICITAR AO USUARIO DIGITAR UM NUMERO E MOSTRAR O MES
COLOCAR EM LOOP
MOSTRAR DE TRÁS PARA FRENTE NO FINAL'''

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
print(meses)


while True: 
    mes = int(input("Infome o numero do mês que desja: "))
    mes = mes - 1
    print(meses[mes])
    break
print("--MESES INVERTIDO--")

for meses in range (12,1):
    print(meses)




    





