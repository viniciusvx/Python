
def intruções ():
 try:
  while True:
   print("===O QUE É PRECISO PARA DOAR SANGUE===")
   print("POSSUI DOCUMENTO OFICIAL COM FOTO?: ")
   op = int(input(" 1-sim 2-não\n"))
   if op != 1 and op != 2:
     print("Numero inválido")
   if op == 2:
      print("NÃO PODE REALIZAR A DOAÇÃO!")
      exit()
   if op == 1:
     
     print("SEU PESO É ACIMA DE 51 KG?: ")
     op = int(input(" 1-sim 2-não\n"))
   if op != 1 and op != 2:
     print("Numero inválido")
     if op == 2:
      print("NÃO PODE REALIZAR A DOAÇÃO!")
      exit()
   if op == 1:
   
    print("VOCÊ ESTÁ GRIPADO OU COM OUTRAS INFECÇÕES?: ")
    op= int(input(" 1-sim 2-não\n"))
   if op != 1 and op != 2:
     print("Numero inválido")
   elif op == 1:
      print("NÃO PODE REALIZAR A DOAÇÃO")
      exit()
   
   elif op == 2:
    print("VOCÊ ESTÁ DESCANSADO E ALIMENTADO?: ")
   op = int(input(" 1-sim 2-não\n"))
   if op != 1 and op != 2:
     print("Numero inválido")
     if op == 2:
      print("NÃO PODE REALIZAR A DOAÇÃO!")
      exit()
   if op == 1:
    
    idade = int(input("INFORME A SUA IDADE: "))
    if idade >=16 and idade < 18:
        menor_idade=int(input("VOCÊ ESTÁ ACOMPANHADO E COM AUTORIZAÇÃO DO RESPONSÁVEL: 1-sim 2-não"))
        if menor_idade == 1:
           print("PODE REALIZAR A DOAÇÃO")
        elif menor_idade == 2:
         print("VOCÊ NÃO PODE REALIZAR A DOAÇÃO")
    elif idade <16:
       print("VOCÊ NÃO PODE REALIZAR A DOAÇÃO")
    
    elif idade >=18 and idade <=60:
      print("PODE REALIZAR A DOAÇÃO")

    elif idade >=61:
       print("É A SUA PRIMEIRA DOAÇÃO?")
       op = int(input(" 1-sim 2-não\n"))
       if op != 1 and op != 2:
         print("Numero inválido".upper())
       
       if op == 1:
         print("VOCÊ NÃO PODE, O LIMITE PARA A PRIMERIA DOAÇÃO É DE 60 anos, 11 meses e 29 dias")
       else:
           print("PODE REALIZAR A DOAÇÃO")

   elif op == 2:
    print("NÃO PODE REALIZAR A DOAÇÃO!")
    exit()
 except ValueError:
    print("Dados inseridos de forma incorreta")

    
 return intruções




def espera():
  try:
   while True:
    print("===DEVE AGUARDAR PARA DOAR SANGUE===")
    print("TRANSFUSÃO DE\nTATUAGEM\nMICROPIGMENTAÇÃO\nPIERCING\nTOMOU VACINA ANTIRRÁBICA/dT(após exposição/mordedura)")
    print("PIERCING(oral e genital) após retirada, AMAMENTAÇÃO após data de parto")
   
    op = int(input("VOCÊ REALIZOU ALGUMA DESSAS OPERAÇÕES? 1-sim 2-não: "))
    if op != 1 and op != 2:
         print("Numero inválido".upper())
         break
   
    if op == 1:
       op = int(input("Você esperou o periodo de 1 ano? 1-sim 2-não: "))
       if op != 1 and op != 2:
          print("Numero inválido".upper())
          continue
       if op == 1:
         print("PODE REALIZAR A DOAÇÃO")
      
       elif op == 2:
         print("VOCE NÃO PODE REALIZAR A DOAÇÃO")
       exit()
    print("=" * 50)

    print("procedimentos endoscópicos(e parceiro),dengue grave".upper())
    op = int(input("Você passou por alugum desses? 1-sim 2-não: "))
    if op != 1 and op != 2:
         print("Numero inválido")
         continue
   
    if op == 1:
      op = int(input("Você esperou o periodo de 6 meses? 1-sim 2-não: ".upper()))
      if op != 1 and op != 2:
         print("Numero inválido")
         continue
      if op == 1:
         print("PODE REALIZAR A DOAÇÃO")
      else:
         print("Você NÃO pode realizar a doação".upper())
      exit()
    print("=" * 50)
    
    print("Uso de Prep/PeP oral(após a última aplicação)".upper())
    op = int(input("Você realizou esse procedimento? 1-sim 2-não: "))
    if op != 1 and op != 2:
       break
    if op == 1:
      op = int(input("Você esperou o periodo de 4 meses? 1-sim 2-não: ".upper()))
      if op != 1 and op != 2:
         print("Numero inválido")
         continue
      if op == 1:
         print("PODE REALIZAR A DOAÇÃO")
      else:
         print("Você NÃO pode realizar a doação".upper())
      exit()
    print("=" * 50)
    
    print("Uso de PrEP injetável")
    op = int(input("Você realizou esse procedimento? 1-sim 2-não: ".upper()))
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
         print("Você NÃO pode realizar a doação".upper())
      exit()
    print("=" * 50)     
    
    print("Monkeypox")
    op = int(input("Você se infectou por essa doença? 1-sim 2-não: ".upper()))
    if op != 1 and op != 2:
         print("Numero inválido")
         break
   
    if op == 1:
      op = int(input("Você esperou o periodo de 1 meses? 1-sim 2-não: ".upper()))
      if op != 1 and op != 2:
         print("Numero inválido")
         continue
      if op == 1:
         print("PODE REALIZAR A DOAÇÃO")
      else:
         print("Você NÃO pode realizar a doação".upper())
      exit()
    print("=" * 50)

    print("Gripe")
    op = int(input("Você teve sintomas de gripe? 1-sim 2-não: ".upper()))
    if op != 1 and op != 2:
         print("Numero inválido")
         break
   
    if op == 1:
      op = int(input("Você esperou o periodo de 14 dias após o término dos sintomas? 1-sim 2-não: ".upper()))
      if op != 1 and op != 2:
         print("Numero inválido")
         continue
      if op == 1:
         print("PODE REALIZAR A DOAÇÃO")
      else:
         print("Você NÃO pode realizar a doação".upper())
      exit()
    print("=" * 50)

    print("Gripe(influenza)/Hepatite A e B/Antitetânica/Antirrábica(preventiva)".upper())
    op = int(input("Você realizou esse procedimento por alugum desses? 1-sim 2-não: ".upper()))
    if op != 1 and op != 2:
         print("Numero inválido")
         break
   
    if op == 1:
      op = int(input("Você esperou o periodo de 6 meses? 1-sim 2-não: ".upper()))
      if op != 1 and op != 2:
         print("Numero inválido")
         continue
      if op == 1:
         print("PODE REALIZAR A DOAÇÃO")
      else:
         print("Você NÃO pode realizar a doação".upper())
      exit()
    print("=" * 50)

    print("Canetas emagrecedoras (Revisado pela ANVISA)".upper())
    op = int(input("Você utilizou esse medicamento? 1-sim 2-não: "))
    if op != 1 and op != 2:
         print("Numero inválido")
         break
   
    if op == 1:
      op = int(input("Você esperou o periodo de 14 dias após o inicio do trataento? 1-sim 2-não: ".upper()))
      if op != 1 and op != 2:
         print("Numero inválido")
         continue
      if op == 1:
         print("PODE REALIZAR A DOAÇÃO")
      else:
         print("Você NÃO pode realizar a doação".upper())
      exit()
    print("=" * 50)

    print("Vigem para outro estado e/ou países".upper())
    op = int(input("Você realizou? 1-sim 2-não: ".upper()))
    if op != 1 and op != 2:
         print("Numero inválido")
         break
   
    if op == 1:
      op = int(input("Você esperou o periodo de 30 dias? 1-sim 2-não: ".upper()))
      if op != 1 and op != 2:
         print("Numero inválido")
         continue
      if op == 1:
         print("Será revisado durante a Triagem Clínica(entrevista)".upper())
      else:
         print("Você NÃO pode realizar a doação".upper())
      exit()
    print("=" * 50)

    print("Covid - 19")
    op = int(input("Você se infectou? 1-sim 2-não: ".upper()))
    if op != 1 and op != 2:
         print("Numero inválido")
         break
   
    if op == 1:
      op = int(input("Você esperou o periodo de 7 dias? 1-sim 2-não: ".upper()))
      if op != 1 and op != 2:
         print("Numero inválido")
         continue
      if op == 1:
         print("PODE REALIZAR A DOAÇÃO")
      else:
         print("Você NÃO pode realizar a doação".upper())
      exit()
    print("=" * 50)

    print("Se submeteu a cirurgias(e parceiro)\ninfecções sexualmente transmissíveis - IST".upper())
    op = int(input("Você realizou esse procedimento por alugum desses? 1-sim 2-não: "))
    if op != 1 and op != 2:
         print("Numero inválido")
         break
   
    if op == 1:
      op = int(input("Será analisado!!".upper()))
    exit()
  except ValueError:
     print("Dados inseridos de forma incorreta".upper())
  return espera
      

def restricoes():
  try:
    while True:
      print("-"*10,"QUEM NÃO PODE DOAR SANGUE","-"*10)
      print("- Você teve Hepatite após 11 anos de idade? ".upper())
      op = int(input(" 1-sim 2-não\n"))
      if op == 1:
       print("NÃO PODE REALIZAR A DOAÇÃO!")
       exit()
      if op != 1 and op != 2:
       print("opção inválida".upper())
       break
      if op == 2:
     
       print("-Você teve Doença de Chagas, Câncer, Sífilis? ".upper())
       op = int(input(" 1-sim 2-não\n"))
      if op != 1 and op != 2:
       print("opção inválida".upper())
       break
      if op == 1:
       print("NÃO PODE REALIZAR A DOAÇÃO!")
       exit()
      if op == 2:
      
       print("- Você se relacionou com pessoas infectadas pelo HIV e seus parceiros? ".upper())
       op = int(input(" 1-sim 2-não\n"))
      if op != 1 and op != 2:
        print("opção inválida".upper())
        break
      if op == 1:
        print("NÃO PODE REALIZAR A DOAÇÃO!")
        exit()
      
      if op == 2:
        print("- Você se relacionou com homens e mulheres com parceiro (a) eventual ou múltiplos parceiros sexuais, que mantêm relações com ou sem uso de preservativo?".upper())
        op = int(input(" 1-sim 2-não\n"))
        if op != 1 and op != 2:
         print("opção inválida".upper())
        if op == 1:
         print("NÃO PODE REALIZAR A DOAÇÃO!")
         exit()
      if op == 2:
     
       print("- Você compartilha seringas ".upper())
       op = int(input(" 1-sim 2-não\n"))
       if op != 1 and op != 2:
        print("opção inválida".upper())
        break
      if op == 1:
       print("NÃO PODE REALIZAR A DOAÇÃO!")
       exit()
      if op == 2:
     
       print("- Você faz uso de drogas injetáveis ilícitas? ".upper())
       op = int(input(" 1-sim 2-não\n"))
      if op != 1 and op != 2:
       print("opção inválida".upper())
       break
      if op == 1:
       print("NÃO PODE REALIZAR A DOAÇÃO!")
       exit()
  
      elif op == 2:
            print("Você está apto para realizar a doação")
            exit()
    
  except ValueError:
    print("Numero Invalido")
    
    return restricoes
    

def recomendações():
  try:
   while True:
    genero = input("Digite o seu genero [F][M]: ").upper()
    if genero != "F" and genero != "M":
      print("Dados inválidos")
      continue
    if genero == "F":
     dias=int(input("Escreva há quantos dias você fez sua última doação: "))
     if dias <0:
       print("Dados incorretos!")
       break
     if dias <=90:
       print("Você deve aguardar até 90 dias para doar novamente")
       exit()
     elif dias > 90:
       print("PODE REALIZAR A DOAÇÃO")
       exit()

       
   
    elif genero == "M":
     dias=int(input("Escreva há quantos dias você fez sua última doação: "))
     if dias <0:
       print("Dados incorretos!")
       break
     if dias <=60:
       print("Você deve aguardar até 60 dias para doar novamente")
       exit()
     elif dias > 60:
       print("PODE REALIZAR A DOAÇÃO")
       exit()

   print("=" * 80)
  except ValueError:
    print("DADOS INVÁliDOS")
    exit()
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
         print("OPÇÃO INVÁLIDA")
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

