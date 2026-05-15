'''SISTEMA ESCOLAR
CADASTRAR O ALUNO
CADASTRAR DISCIPLINA
IDADE
SEXO
TURMA
O PROFESSOR LANÇA 4 NOTAS E NO FINAL IMPRIME O BOLETIM,LANÇOU 4 NOTAS IMPRIME'''

alunos={}
disciplinas=[]
print("-"* 20)
print("===MENU===")
menu=int(input("1- CADASTRAR ALUNO/2-CADASTRAR DISCIPLINA/3-TURMAS\n"))
print("-"* 20)

while True:
    while True:
     if menu == 1:
        alunos1=input("Informe o nome do aluno:\n ")
        idade=int(input("Digite a idade do aluno:\n "))
        sexo=input("Qual é o sexo:[F][M]")
        if sexo.upper() == "F":
            print("Sexo feminino")

        elif sexo.upper() == "M":
            print("Sexo masculino")

        else:
            print("Sexo inválido")
        alunos[alunos1] = { "IDADE": idade,
        "SEXO": sexo 
            
        }
     if menu == 2:
        dis=input("informe a materia que deseja cadastrar: ")
        disciplinas.append(dis)
        op=input("Deseja cadastrar nova materia? [S][N]")
        if op.upper() == "N":
            break
            
        
        
        
        
    
        