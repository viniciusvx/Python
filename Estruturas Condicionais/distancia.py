urg = input("A entrega é urgente? (sim/nao)\n").lower()
if urg == "sim":
 print("A entrega será de forma prioritária e urgente")
 exit()
else:
 dist=int(input("digite a sua distancia: \n"))
if dist >=300:
    print("A entrega é longa")
else:
    print("A entrega é padrao")
    
