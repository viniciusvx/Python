dic_alunos = {}

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

    # ================= CADASTRO =================
    if op == 1:

        print("===CADASTRO===")

        nome = input("Informe o nome do aluno: ")
        idade = int(input("Qual é a idade do aluno?: "))

        if idade < 0:
            print("Idade inválida!")
            continue

        turma_validas = ["1","2","3","4","5","6","7","8","9","1°","2°","3°"]

        turma = input("1 a 9 (FUNDAMENTAL) - 1° a 3° (MÉDIO): ")

        if turma not in turma_validas:# SE A TURMA QUE O USUARIO DIGITAR NÃO ESTIVER DENTRO DE TURMAS VALIDAS
            print("Turma inválida!")
            continue

        genero = input("Qual é o genero do aluno:[F][M] ").upper()

        if genero != "F" and genero != "M":# SE O GENERO DIGITADO FOR DIFERENTE DE(!=) F OU M
            print("Gênero inválido!")
            continue

        dic_alunos[nome] = {   # AQUI ESTÁ SALVANDO AS INFORMAÇÕES [NOME DO ALUNO]
            "idade": idade,    # IDADE : IDADE QUE O USUARIO DIGITOU
            "turma": turma,    # TURMA: TURMA QUE O USUARIO DIGITOU
            "genero": genero,  # GENERO: GENERO QUE O USUARIO DIGITOU
            "disciplinas": {}  # DISCIPLINAS : ESTÁ VAZIA POIS QUANDO O USUARIO CADASTRAR VAI VIR PRA CÁ
        }

        print("Aluno cadastrado!!!")

    # ================= NOTAS =================
    elif op == 2:

        print("===NOTAS & DISCIPLINAS===")

        aluno_cadastrado = input("Qual aluno deseja cadastrar notas?: ")

        if aluno_cadastrado not in dic_alunos: # SE O NOME DO ALUNO QUE ELE DIGITAR NÃO ESTIVER NO DICIONÁRIO
            print("Aluno não encontrado!")
            continue

        while True:

            dis = input("Qual é a disciplina?: ")
            notas = []

            for x in range(4): # SE EU COLOCASSE O WHILE EM CIMA, ELE NÃO IRIA PARAR O CODIGO QUANDO ESTIVESSE ERRADO
                while True:
                 nota = float(input(f"Digite a {x+1}° nota de {dis}: "))
                 if nota<0 or nota >10:
                    print("Nota inválida, digite novamente: ")
                    continue
                 else:
                    notas.append(nota)

            dic_alunos[aluno_cadastrado]["disciplinas"][dis] = notas
            #DIC_ALUNOS[VINI][DISCIPLINA][MATEMATICA] = 10,9,8,7

            op2 = input("Nova disciplina? [S][N] ").upper()

            if op2 == "N":
                break

    # ================= BOLETIM =================
    elif op == 3:

        aluno = input("Qual aluno deseja ver?: ")

        if aluno not in dic_alunos: # SE O ALUNO NÃO ESTIVER CADASTRADO NO DICIONÁRIO
            print("Aluno não encontrado!")
            continue

        print("=" * 30)
        print(f"Aluno: {aluno}")

        disciplinas = dic_alunos[aluno]["disciplinas"]
        #Guarda as disciplinas do aluno numa variável chamada disciplinas

        if not disciplinas:#SE NÃO TIVER NENHUMA DISCIPLINA CADASTRADA
            print("Nenhuma disciplina cadastrada!")
            continue

        for disciplina, notas in disciplinas.items():
            #para cada matéria e suas notas, repita o código abaixo
            media = sum(notas) / len(notas)

            print("-" * 30)
            print(f"Disciplina: {disciplina}")
            print(f"Notas: {notas}")
            print(f"Média: {media:.1f}")

            if media >= 7:
                print("APROVADO")
            else:
                print("REPROVADO")

    # ================= SAIR =================
    elif op == 4:

        print("Saindo...")
        break

    # ================= OPÇÃO INVÁLIDA =================
    else:
        print("Opção inválida!")