def intruções ():
 try:
  print("===O QUE É PRECISO PARA DOAR SANGUE===")
  print("possui documento oficial com foto? 1-sim 2-não?: ")
  op = int(input(" 1-sim 2-não\n"))
  if op != 1 and op != 2:
     print("Numero inválido")
  if op == 1:
     print("Seu peso é acima de 51 kg 1-sim 2-não: ")
     op = int(input(" 1-sim 2-não\n"))
  if op != 1 and op != 2:
     print("Numero inválido")
  if op == 1:
   print("Você está gripado ou com outras infecções?: ")
   op = int(input(" 1-sim 2-não\n"))
  if op != 1 and op != 2:
     print("Numero inválido")
  if op == 1:
   print("Você está descansado e alimentado?: ")
   op = int(input(" 1-sim 2-não\n"))
  if op != 1 and op != 2:
     print("Numero inválido")
  if op == 1:
     print("Você PODE realizar a doação de sangue!")
  
  if op == 1:
    idade = int(input("Informe a sua idade: "))
    if idade >=16 and idade < 18:
        print("Você pode doar, mas apenas acompanhado de seus responsáveis e com a autorização")
    elif idade <16:
       print("Você não pode realizar a doação")
    
    elif idade >=18 and idade <=60:
      print("Você pode realizar a doação de sangue")

    elif idade >=61:
       print("É a sua primeira doação?")
       op = int(input(" 1-sim 2-não\n"))
       if op != 1 and op != 2:
         print("Numero inválido")
       if op == 1:
         print("Você não pode doar, o limite para a primeria doação é de 60 anos, 11 meses e 29 dias")
       else:
           print("Você pode realizar a doação")

  elif op == 2:
    print("Você não pode realizar a doação de sangue!!")
 except ValueError:
    print("Dados inseridos de forma incorreta")
    
 return intruções
