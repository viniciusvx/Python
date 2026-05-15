'''SISTEMA ESCOLAR
CADASTRAR O ALUNO
CADASTRAR DISCIPLINA
IDADE
SEXO
TURMA
O PROFESSOR LANÇA 4 NOTAS E NO FINAL IMPRIME O BOLETIM,LANÇOU 4 NOTAS IMPRIME'''
 

alunos = {}
disciplinas = []
notas = []
while True:

    print("-" * 20)
    print("=== MENU ===")

    menu = int(input(
        "1- CADASTRAR ALUNO\n"
        "2- CADASTRAR DISCIPLINA\n"
        "3- Ver relatorio\n"
        "4- sair\n"
    ))

    print("-" * 20)

    if menu == 1:

        while True:

            alunos1 = input("Informe o nome do aluno:\n ")
            idade = int(input("Digite a idade do aluno:\n "))

            if idade < 0:
                print("ERRO: idade inválida")
                continue

            sexo = input("Qual é o sexo:[F][M]\n")

            if sexo.upper() == "F":
                print("Sexo feminino")

            elif sexo.upper() == "M":
                print("Sexo masculino")

            else:
                print("Sexo inválido")
                continue

            

            for x in range(4):

                while True:
                    nota = float(input("Digite a nota do aluno:\n "))

                    if nota < 0 or nota > 10:
                        print("ERRO: nota inválida")
                        continue
                    else:
                        notas.append(nota)
                        break

            alunos[alunos1] = {
                "IDADE": idade,
                "SEXO": sexo,
                "NOTAS": notas
            }

            op = input("Deseja cadastrar novo aluno? [S][N]\n")

            if op.upper() == "N":
                break

    elif menu == 2:

        while True:

            dis = input("Informe a matéria que deseja cadastrar:\n ")
            disciplinas.append(dis)

            op = input("Deseja cadastrar nova matéria? [S][N]\n")

            if op.upper() == "N":
                break

    elif menu == 3:
        print("-" * 20)
        print(alunos)
        print(notas)
        print(disciplinas)
        print("-" * 20)

    elif menu == 4:
        break