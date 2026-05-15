'''SISTEMA ESCOLAR
CADASTRAR O ALUNO
CADASTRAR DISCIPLINA
IDADE
SEXO
TURMA
O PROFESSOR LANÇA 2 NOTAS E NO FINAL IMPRIME O BOLETIM,LANÇOU 4 NOTAS IMPRIME'''

alunos={}
print("-"* 20)
print("===MENU===")
print("-"* 20)
while True:
    alu=input("Informe o nome do aluno:\n ")
    disciplina=input("informe a disciplina:\n ")
    turma=int(input("Qual é a turma?:\n "))
    alunos[alu]= {
        "disciplina": disciplina,
        "turma": turma          
        }
    print(alunos)

