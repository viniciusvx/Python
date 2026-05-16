alunos = []
disciplinas = []

while True:

    print("-" * 30)
    print("=== MENU ESCOLAR ===")

    opcao_menu = int(input(
        "1 - CADASTRAR ALUNO\n"
        "2 - CADASTRAR DISCIPLINA\n"
        "3 - VER RELATÓRIO\n"
        "4 - SAIR\n"
    ))

    print("-" * 30)

    if opcao_menu == 1:

        while True:

            nome_aluno = input("Nome do aluno: ")

            turmas_validas = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "1°", "2°", "3°"]

            turma_aluno = input("Turma do aluno (1 a 9 ou 1°, 2°, 3°): ")

            if turma_aluno not in turmas_validas: # verifica se a turma digitada pelo aluno está na lista de turmas válidas; se não estiver, considera inválida
             print("Turma inválida!")
              # interrompe a iteração atual do loop e volta para o início, pedindo novamente os dados ao usuário

            idade_aluno = int(input("Idade do aluno: "))

            if idade_aluno < 0:
                print("Idade inválida!")
                continue

            sexo_aluno = input("Sexo [F/M]: ").upper()

            if sexo_aluno != "F" and sexo_aluno != "M":
                print("Sexo inválido!")
                continue

            aluno = {
                "nome": nome_aluno,
                "idade": idade_aluno,
                "sexo": sexo_aluno,
                "turma": turma_aluno,
                "disciplinas": disciplinas.copy() # cria uma cópia da lista de disciplinas para este aluno, evitando que futuras alterações afetem alunos já cadastrados
            }

            alunos.append(aluno)

            continuar = input("Cadastrar outro aluno? [S/N]: ").upper()

            if continuar == "N":
                break

    elif opcao_menu == 2:

        while True:

            nome_disciplina = input("Nome da disciplina: ")

            lista_notas_disciplina = []

            for x in range(4):

                while True:

                    valor_nota = float(input(f"Nota {x + 1} de {nome_disciplina}: "))

                    if valor_nota < 0 or valor_nota > 10:
                        print("Nota inválida!")
                    else:
                        lista_notas_disciplina.append(valor_nota)
                        break

            disciplinas.append({
                "nome_disciplina": nome_disciplina,# armazena o nome da disciplina
                  "notas_disciplina": lista_notas_disciplina  # armazena a lista de 4 notas dessa disciplina
                  })  # adiciona essa disciplina (nome + notas) à lista de disciplinas do aluno
    
            

            continuar = input("Cadastrar outra disciplina? [S/N]: ").upper()

            if continuar == "N":
                break

    elif opcao_menu == 3:

        print("\n===== RELATÓRIO DOS ALUNOS =====")

        for aluno in alunos:

            print("=" * 30)
            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}anos")
            print(f"Sexo: {aluno['sexo']}")
            print(f"Turma: {aluno['turma']}")

            print("Disciplinas cadastradas:")
            
            for disciplina in disciplinas:  # percorre cada disciplina cadastrada na lista de disciplinas
                print(f"- {disciplina['nome_disciplina']}: {disciplina['notas_disciplina']}")  # imprime o nome da disciplina e a lista de notas correspondentes


    elif opcao_menu == 4:
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!") 