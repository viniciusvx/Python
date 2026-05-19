dados=[]
disciplinas = []
def cadastrar_aluno():
  nome=input("insira o nome do aluno: ")
  idade=int(input("Qual é a idade do aluno: "))
  sexo= input("Informe o sexo: F  / M \n")
  dados.append([nome,idade,sexo]) #NÃO PODE ESQUECER DOS COLCHETES
  print("CADASTRO REALIZADO !!!")




def cadastrar_disciplina():
  disciplina=int("informe a disciplina: ")
  ch = int(input("Informe a carga horária: "))
  disciplinas.append([disciplina,ch])


while True:
    print("----SISTEMA ACADEMICO----")
    print("1- cadastrar aluno")
    print("2- cadastrar disciplinas")
    op=int(input("informe o que deseja: "))

    if op == 1:
       cadastrar_aluno()
    elif op == 2:
       cadastrar_disciplina()
    else:
       print("SAINDO DO SISTEMA....")


 