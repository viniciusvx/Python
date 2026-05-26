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




def espera():
  try:
   while True:
    print("===DEVE AGUARDAR PARA DOAR SANGUE===")
    print("transfusão de sangue\ntatuagem\nmicropigmentação\npiercing\ntomou vacina antirrábica/dT(após exposição/mordedura)")
    print("Piercing(oral e genital) após retirada, amamentação após data de parto")
   
    op = int(input("Você realizou alguma dessas operações? 1-sim 2-não: "))
    if op != 1 and op != 2:
         print("Numero inválido")
         break
   
    if op == 1:
       op = int(input("Você esperou o periodo de 1 ano? 1-sim 2-não: "))
       if op != 1 and op != 2:
          print("Numero inválido")
          continue
       if op == 1:
         print("PODE REALIZAR A DOAÇÃO")
      
       elif op == 2:
         print("Você NÃO pode realizar a doação")
       break
    print("=" * 50)

    print("procedimentos endoscópicos(e parceiro),dengue grave")
    op = int(input("Você passou por alugum desses? 1-sim 2-não: "))
    if op != 1 and op != 2:
         print("Numero inválido")
         break
   
    if op == 1:
      op = int(input("Você esperou o periodo de 6 meses? 1-sim 2-não: "))
      if op != 1 and op != 2:
         print("Numero inválido")
         continue
      if op == 1:
         print("PODE REALIZAR A DOAÇÃO")
      else:
         print("Você NÃO pode realizar a doação")
      break
    print("=" * 50)
    
    print("Uso de Prep/PeP oral(após a última aplicação)")
    op = int(input("Você realizou esse procedimento? 1-sim 2-não: "))
    if op != 1 and op != 2:
       break
    if op == 1:
      op = int(input("Você esperou o periodo de 4 meses? 1-sim 2-não: "))
      if op != 1 and op != 2:
         print("Numero inválido")
         continue
      if op == 1:
         print("PODE REALIZAR A DOAÇÃO")
      else:
         print("Você NÃO pode realizar a doação")
      exit()
    print("=" * 50)
    
    print("Uso de PrEP injetável")
    op = int(input("Você realizou esse procedimento por alugum desses? 1-sim 2-não: "))
    if op != 1 and op != 2:
         print("Numero inválido")
         break
   
    if op == 1:
      op = int(input("Você esperou o periodo de 6 meses? 1-sim 2-não: "))
      if op != 1 and op != 2:
         print("Numero inválido")
         continue
      
      if op == 1:
         print("PODE REALIZAR A DOAÇÃO")
      else:
         print("Você NÃO pode realizar a doação")
      break
    print("=" * 50)     
    
    print("Monkeypox")
    op = int(input("Você se infectou por essa doença? 1-sim 2-não: "))
    if op != 1 and op != 2:
         print("Numero inválido")
         break
   
    if op == 1:
      op = int(input("Você esperou o periodo de 1 meses? 1-sim 2-não: "))
      if op != 1 and op != 2:
         print("Numero inválido")
         continue
      if op == 1:
         print("PODE REALIZAR A DOAÇÃO")
      else:
         print("Você NÃO pode realizar a doação")
      break
    print("=" * 50)

    print("Gripe")
    op = int(input("Você teve sintomas de gripe? 1-sim 2-não: "))
    if op != 1 and op != 2:
         print("Numero inválido")
         break
   
    if op == 1:
      op = int(input("Você esperou o periodo de 14 dias após o término dos sintomas? 1-sim 2-não: "))
      if op != 1 and op != 2:
         print("Numero inválido")
         continue
      if op == 1:
         print("PODE REALIZAR A DOAÇÃO")
      else:
         print("Você NÃO pode realizar a doação")
      break
    print("=" * 50)

    print("Gripe(influenza)/Hepatite A e B/Antitetânica/Antirrábica(preventiva)")
    op = int(input("Você realizou esse procedimento por alugum desses? 1-sim 2-não: "))
    if op != 1 and op != 2:
         print("Numero inválido")
         break
   
    if op == 1:
      op = int(input("Você esperou o periodo de 6 meses? 1-sim 2-não: "))
      if op != 1 and op != 2:
         print("Numero inválido")
         continue
      if op == 1:
         print("PODE REALIZAR A DOAÇÃO")
      else:
         print("Você NÃO pode realizar a doação")
      break
    print("=" * 50)

    print("Canetas emagrecedoras (Revisado pela ANVISA)")
    op = int(input("Você utilizou esse medicamento? 1-sim 2-não: "))
    if op != 1 and op != 2:
         print("Numero inválido")
         break
   
    if op == 1:
      op = int(input("Você esperou o periodo de 14 dias após o inicio do trataento? 1-sim 2-não: "))
      if op != 1 and op != 2:
         print("Numero inválido")
         continue
      if op == 1:
         print("PODE REALIZAR A DOAÇÃO")
      else:
         print("Você NÃO pode realizar a doação")
      break
    print("=" * 50)

    print("Vigem para outro esado e/ou países")
    op = int(input("Você realizou esse procedimento por alugum desses? 1-sim 2-não: "))
    if op != 1 and op != 2:
         print("Numero inválido")
         break
   
    if op == 1:
      op = int(input("Você esperou o periodo de 30 dias? 1-sim 2-não: "))
      if op != 1 and op != 2:
         print("Numero inválido")
         continue
      if op == 1:
         print("Será revisado durante a Triagem Clínica(entrevista)")
      else:
         print("Você NÃO pode realizar a doação")
      break
    print("=" * 50)

    print("Covid - 19")
    op = int(input("Você se infectou? 1-sim 2-não: "))
    if op != 1 and op != 2:
         print("Numero inválido")
         break
   
    if op == 1:
      op = int(input("Você esperou o periodo de 7 dias? 1-sim 2-não: "))
      if op != 1 and op != 2:
         print("Numero inválido")
         continue
      if op == 1:
         print("PODE REALIZAR A DOAÇÃO")
      else:
         print("Você NÃO pode realizar a doação")
      break
    print("=" * 50)

    print("Se submeteu a cirurgias(e parceiro)\ninfecções sexualmente transmissíveis - IST")
    op = int(input("Você realizou esse procedimento por alugum desses? 1-sim 2-não: "))
    if op != 1 and op != 2:
         print("Numero inválido")
         break
   
    if op == 1:
      op = int(input("Será analisado!!"))
    break
  except ValueError:
     print("Dados inseridos de forma incorreta")
  return espera
      
def restricoes():
  try:
    print("-"*10,"QUEM NÃO PODE DOAR SANGUE","-"*10)
    print("- Você teve Hepatite após 11 anos de idade? 1-sim 2-não")
    op = int(input(" 1-sim 2-não\n"))
  if op != 1 and op != 2:
     print("Numero inválido")
  if op == 2:
     print("-Você teve Doença de Chagas, Câncer, Sífilis? 1-sim 2-não")
     op = int(input(" 1-sim 2-não\n"))
  if op != 1 and op != 2:
     print("Numero inválido")
  if op == 2:
    print("- Você se relacionou com pessoas infectadas pelo HIV e seus parceiros? 1-sim 2-não")
    op = int(input(" 1-sim 2-não\n"))
  if op != 1 and op != 2:
     print("Numero inválido")
  if op == 2:
    print("- Você se relacionou com homens e mulheres com parceiro (a) eventual ou múltiplos parceiros sexuais, que mantêm relações com ou sem uso de preservativo? 1-sim 2-não")
    op = int(input(" 1-sim 2-não\n"))
  if op != 1 and op != 2:
     print("Numero inválido")
  if op == 2:
    print("- Você convive compartilha seringas 1-sim 2-não.")
    op = int(input(" 1-sim 2-não\n"))
  if op != 1 and op != 2:
     print("Numero inválido")
  if op == 2:
    print("- Você faz uso de drogas injetáveis ilícitas? 1-sim 2-não")
    op = int(input(" 1-sim 2-não\n"))
  if op != 1 and op != 2:
     print("Numero inválido")
  if op == 1:
    print("Voce não pode realizar a adoção")
  
    pergunta = int(input("Você possui algo no qual foi descrito acima?\nDigite 1 - SIM ou 2 - NÃO:\n"))
    if pergunta == 1:
            print("Você NÃO pode doar sangue!!!")
            print("Saindo do Sistema...")
    elif pergunta == 2:
            print("Você está apto para realizar a doação")
    else:
       print("Numero Invalido") 
  except ValueError:
    print("Numero Invalido")
    
    return restricoes
    

def recomendações():
   print("-"*10,"INTERVALO ENTRE AS DOAÇÕES","-"*10)
   print("Gênero Biológico Masculino......60 dias - Máximo 4 vezes no período de 12 meses")
   print("Gênero Biológico Feminino......90 dias - Máximo 3 vezes no período de 12 meses")
   print(" "*5,"(O sistema poderá exigir mais 2 dias para o intervalo de doações)"," "*5)
   print("=" * 80)
   return recomendações

def menu():
  try:
   while True:
    print("==========MENU==========")
    print("1 - RECOMENDAÇÕES")
    print("2 - INSTRUÇÕES")
    print("3 - RESTRIÇÕES")
    print("4 - TEMPO DE ESPERA")
    print("5 - Sair")
    op = int(input("Infome a sua opção: "))
    if op < 1 or op >5:
         print("Numero inválido")
         break

    if op == 1:
      recomendações()
    elif op == 2:
      intruções()
    elif op == 3:
      restricoes()
    elif op == 4:
      espera()
    elif op == 5:
       print("SAINDO...")
       exit()
  except ValueError:
     print("Dados inseridos incorretamente")

menu()

