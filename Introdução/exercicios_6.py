'''Implemente um programa que converta o valor de uma 
velocidade média em km/h para m/s. 
Para isso, o usuário deve informar o valor da 
velocidade média. Sabe-se que o fator utilizado para 
essa conversão é 3,6.'''

vel_km = float(input("Informe a Vm (km/h): "))
vel_m = vel_km / 3.6
print(f"{vel_km:.2f} Km/h equivale a {vel_m:.2f}")