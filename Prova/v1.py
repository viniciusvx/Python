pacientes = []

tipos_atendimento = ("consulta", "exame", "retorno")

contadores = {
    "consulta": 0,
    "exame": 0,
    "retorno": 0
}


def salvar_dados():

    arquivo = open(
        'C:/Users/Public/Documents/pacientes.txt',
        'w',
        encoding='utf-8'
    )

    for paciente in pacientes:

        arquivo.write(
            f"{paciente['nome']};"
            f"{paciente['idade']};"
            f"{paciente['tipo_atendimento']};"
            f"{paciente['pagamento']};"
            f"{paciente['valor']}\n"
        )

    arquivo.close()


def carregar_dados():

    try:

        arquivo = open(
            'C:/Users/Public/Documents/pacientes.txt',
            'r',
            encoding='utf-8'
        )

        for linha in arquivo:

            if linha.strip() == "":
                continue

            dados = linha.strip().split(';')

            paciente = {}

            paciente['nome'] = dados[0]
            paciente['idade'] = int(dados[1])
            paciente['tipo_atendimento'] = dados[2]
            paciente['pagamento'] = dados[3]
            paciente['valor'] = float(dados[4])

            pacientes.append(paciente)

            contadores[paciente['tipo_atendimento']] += 1

        arquivo.close()

    except FileNotFoundError:
        print("Nenhum arquivo foi encontrado")


def cadastrar():

    paciente = {}

    paciente['nome'] = input("Informe o nome do paciente: ")

    paciente['idade'] = int(input("Informe a idade do paciente: "))

    if paciente['idade'] < 0:
        print("Idade inválida")
        return

    print("\nTipos de atendimento:")

    contador = 1

    for tipo in tipos_atendimento:
        print(f"{contador} - {tipo}")
        contador += 1

    op = int(input("Informe o tipo de atendimento: "))

    if op not in (1, 2, 3):
        print("Dados inválidos")
        return

    paciente['tipo_atendimento'] = tipos_atendimento[op - 1]

    if op == 1:
        paciente['valor'] = 500
        contadores["consulta"] += 1

    elif op == 2:
        paciente['valor'] = 200
        contadores["exame"] += 1

    elif op == 3:
        paciente['valor'] = 100
        contadores["retorno"] += 1

    paciente['pagamento'] = input(
        "Forma de pagamento (dinheiro/pix/cartao): "
    ).lower()

    if paciente['pagamento'] not in ("dinheiro", "pix", "cartao"):
        print("Forma de pagamento inválida")
        return

    pacientes.append(paciente)

    salvar_dados()

    print("Paciente cadastrado com sucesso!")


def relatorio_pacientes():

    print("\n=== RELATÓRIO DOS PACIENTES ===")

    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
        return

    for paciente in pacientes:

        print(f"\nNome: {paciente['nome']}")
        print(f"Idade: {paciente['idade']}")
        print(f"Tipo de atendimento: {paciente['tipo_atendimento']}")
        print(f"Forma de pagamento: {paciente['pagamento']}")
        print(f"Valor cobrado: R$ {paciente['valor']}")


def adm():

    total = 0
    maior_valor = 0
    paciente_maior = ""

    for paciente in pacientes:

        total += paciente['valor']

        if paciente['valor'] > maior_valor:
            maior_valor = paciente['valor']
            paciente_maior = paciente['nome']

    print("\n=== RELATÓRIO ADM ===")

    print(f"Total de atendimentos: {len(pacientes)}")
    print(f"Valor total arrecadado: R$ {total}")

    print(f"Consultas: {contadores['consulta']}")
    print(f"Exames: {contadores['exame']}")
    print(f"Retornos: {contadores['retorno']}")

    print(f"Maior valor cobrado: R$ {maior_valor}")

    if paciente_maior != "":
        print(f"Paciente que pagou mais: {paciente_maior}")

    if total >= 1000:
        print("Movimento alto")

    elif total >= 500:
        print("Movimento médio")

    else:
        print("Movimento baixo")


carregar_dados()
def menu():

    while True:

        print("\n=== MENU ===")
        print("1 - Cadastrar atendimento")
        print("2 - Relatório dos pacientes")
        print("3 - ADM")
        print("4 - Sair")

        op = input("Escolha uma opção: ")

        if op == "1":
            cadastrar()

        elif op == "2":
            relatorio_pacientes()

        elif op == "3":
            adm()

        elif op == "4":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")

carregar_dados()
menu()