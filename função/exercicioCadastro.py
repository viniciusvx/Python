def cadastrar_aluno():
    aluno = {}
    
    
    aluno["nome"] = input("Digite o nome do aluno: ")
    aluno["idade"] = int(input("Digite a idade do aluno: "))
    aluno["sexo"] = input("Digite o sexo do aluno: ")
    aluno["serie"] = int(input("Digite a serie do aluno: "))
    aluno["disciplinas"] = []  # CORREÇÃO: padronização do nome da chave

    qtd_disciplina = int(input("Quantas disciplinas deseja cadastrar? "))
    for i in range(qtd_disciplina):
        disciplina = cadastrar_disciplina(i)
        aluno["disciplinas"].append(disciplina)
        
    return aluno# SERVE PARA MOSTRAR O RESULTADO DA FUNÇAO ASSIM NÃO PRECISA DAR O PRINT


def cadastrar_disciplina(i):
    disciplina = {}
    
    disciplina["nome"] = input(f"Digite o nome da disciplina: {i + 1}° disciplina ")
    disciplina["notas"] = []  # CORREÇÃO: antes estava "nota"

    for i in range(4):  # CORREÇÃO: não sobrescrever variável i
        nota = float(input(f"Digite a {i+1}° nota: "))  # CORREÇÃO da f-string
        disciplina["notas"].append(nota)
        
          
    disciplina["media"] = calcular_medida(disciplina["notas"])  # CORREÇÃO: média adicionada
    
    return disciplina # SERVE PARA MOSTRAR O RESULTADO DA FUNÇAO ASSIM NÃO PRECISA DAR O PRINT


def calcular_medida(notas):
    media = sum(notas) / len(notas) #SUM VAI SOMAR O NUMERO DE NOTAS E LEN VAI LER QAUNTAS NOTAS FORAM DIGITADAS
    
    return media # SERVE PARA MOSTRAR O RESULTADO DA FUNÇAO ASSIM NÃO PRECISA DAR O PRINT


def menu():
    alunos = []
    while True:
        print("____MENU____")
        print("1- CADASTRAR ALUNO")
        print("2- MOSTRAR RELATORIO")
        print("3- SAIR")
        op = input("Escolha um opção: ")

        if op == "1":
            aluno = cadastrar_aluno()
            alunos.append(aluno)
        
        elif op == "2":
            mostrar_relatorio(alunos)  # CORREÇÃO: faltava passar parâmetro
            
        
        elif op == "3":
            print("Saindo...")
            break  # CORREÇÃO: sair do loop


def mostrar_relatorio(alunos):
    if len(alunos) == 0:
        print("Nenhuma cadastro!")
    else:
        print("---RELATORIO---")
        
        for aluno in alunos:
            print(f"NOME: {aluno['nome']}")
            print(f"IDADE: {aluno['idade']}")
            print(f"SEXO: {aluno['sexo']}")
            print(f"SERIE: {aluno['serie']}")

            print("\nDISCIPLINAS...")

            for disciplina in aluno["disciplinas"]:
                print(f"{disciplina['nome']} -> MEDIA: {disciplina['media']:.2f}")
    

menu()