def restricoes():
  try:
    print("-"*10,"QUEM NÃO PODE DOAR SANGUE","-"*10)
    print("- Você teve Hepatite após 11 anos de idade? 1-sim 2-não")
    pergunta_restrições
     
    print("-Você teve Doença de Chagas, Câncer, Sífilis? 1-sim 2-não")
    pergunta_restrições
       
    print("- Você se relacionou com pessoas infectadas pelo HIV e seus parceiros? 1-sim 2-não")
    pergunta_restrições
    
    print("- Você se relacionou com homens e mulheres com parceiro (a) eventual ou múltiplos parceiros sexuais, que mantêm relações com ou sem uso de preservativo? 1-sim 2-não")
    pergunta_restrições

    print("- Você convive compartilha seringas 1-sim 2-não.")
    pergunta_restrições
     
    print("- Você faz uso de drogas injetáveis ilícitas? 1-sim 2-não")
    op = int(input(" 1-sim 2-não\n"))
    if op != 1 and op != 2:
     print("Numero inválido")
    if op == 1:
     print("Voce não pode realizar a adoção")
 
    elif op == 2:
            print("Você está apto para realizar a doação")
    else:
       print("Numero Invalido") 
  except ValueError:
    print("Numero Invalido")
    
    return restricoes
    
def pergunta_restrições():
  op = int(input(" 1-sim 2-não\n"))
  if op != 1 and op != 2:
     print("Numero inválido")
  if op == 2:
   return pergunta_restrições
  
restricoes()