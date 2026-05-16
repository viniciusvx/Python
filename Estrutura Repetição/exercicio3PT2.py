dic_alunos = {}
media = 0

while True:

    print("=" * 30)
    print("-----MENU ESCOLAR-----")
    print("=" * 30)

    op = int(input(
        "1-CADASTRAR ALUNO\n"
        "2-NOTAS E DISCIPLINAS\n"
        "3-BOLETIM\n"
        "4-SAIR\n"
    ))

    while True:

        if op == 1:

            print("===CADASTRO===")

            nome = input("Informe o nome do aluno: ")
            idade = int(input("Qual é a idade do aluno?: "))

            if idade < 0:
                print("Idade inválida!")
                continue

            turma_validas = ["1","2","3","4","5","6","7","8","9","1°","2°","3°"]

            turma = input("1 a 9 (FUNDAMENTAL) - 1° a 3° (MÉDIO): ")

            if turma not in turma_validas:
                print("Turma inválida!")
                continue

            genero = input("Qual é o genero do aluno:[F][M] ").upper()

            if genero != "F" and genero != "M":
                print("Gênero inválido!")
                continue

            dic_alunos[nome] = {
                "idade": idade,
                "turma": turma,
                "genero": genero,
                "disciplinas": {}
            }

            print("Aluno cadastrado!")
            break

        if op == 2:

            print("===NOTAS & DISCIPLINAS===")

            aluno_cadastrado = input("Qual aluno deseja cadastrar notas?: ")

            if aluno_cadastrado not in dic_alunos:
                print("Aluno não encontrado!")
                break

            while True:

                dis = input("Qual é a disciplina?: ")
                notas = []

                for x in range(4):

                    nota = float(input(f"Digite a {x+1} nota de {dis}: "))
                    notas.append(nota)

                dic_alunos[aluno_cadastrado]["disciplinas"][dis] = notas

                op2 = input("Nova disciplina? [S][N] ").upper()

                if op2 == "N":
                    break

            break

        if op == 3:

            aluno = input("Qual aluno deseja ver?: ")

            if aluno not in dic_alunos:
                print("Aluno não encontrado!")
                break

            print("=" * 30)
            print(f"Aluno: {aluno}")

            for disciplina, notas in dic_alunos[aluno]["disciplinas"].items(): # percorre cada disciplina e as notas do aluno

                media = sum(notas) / 4

                print("-" * 30)
                print(f"Disciplina: {disciplina}")
                print(f"Notas: {notas}")
                print(f"Média: {media}")

                if media >= 7:
                    print("APROVADO")
                else:
                    print("REPROVADO")

            break

        if op == 4:

            print("Saindo...")
            exit()