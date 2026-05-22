'''cadastro de hóspede = nome,idade,cpf,tipo de quarto, quantidade de diária
quarto/valor:
standard = 120R$
luxo = 250R$
premium = 400R$
Situação:
Até R$ 500 - econômico
501 até 1500 - Intermediária
acima 1500 - Premium'''

standard = 1
luxo = 1
premium = 1

def cadastrar_hospede():
    try:
        hospede = {}
        hospede["nome"] = input("Informe o nome do hóspede: ")
        hospede["idade"] = int(input("Informe a idade do hóspede: "))
        cpf = input("Informe o CPF do hóspede: ")

        if cpf.isdigit() and len(cpf) == 11:
            hospede["cpf"] = cpf
        else:
            print("CPF inválido")
            hospede["cpf"] = "inválido"

        print("Cadastrado com sucesso!!")
        return hospede
    except ValueError:
        print("Os dados foram informados incorretamente")
        return None


def reserva_quarto(hospedes):
    global standard, luxo, premium
    try:
        reserva = {}
        valor_reserva = 0
        contador = 0

        nome_busca = input("Informe o nome: ")

        for hospede in hospedes:
            if hospede["nome"] == nome_busca:
                while contador < 1:
                    print("--- RESERVA DE QUARTOS ---")
                    print("1 - Standard (120R$)")
                    print("2 - Luxo (250R$)")
                    print("3 - Premium (400R$)")

                    tipo = input("Escolha uma opção: ")
                    dias = int(input("Informe a quantidade de diárias: "))

                    if tipo == "1" and standard > 0:
                        valor_reserva = dias * 120
                        standard -= 1
                        contador = 1
                    elif tipo == "2" and luxo > 0:
                        valor_reserva = dias * 250
                        luxo -= 1
                        contador = 1
                    elif tipo == "3" and premium > 0:
                        valor_reserva = dias * 400
                        premium -= 1
                        contador = 1
                    else:
                        print("Quarto indisponível ou opção inválida!")

                reserva["tipo de quarto"] = tipo
                reserva["quantidade de diarias"] = dias
                reserva["valor total"] = valor_reserva

                if valor_reserva <= 500:
                    print("Situação: econômico")
                elif valor_reserva <= 1500:
                    print("Situação: intermediária")
                else:
                    print("Situação: premium")

                return reserva

        print("Hóspede não encontrado")
        return None

    except ValueError:
        print("Dados informados são inválidos")
        return None


def mostrar_relatorio(hospedes, reservas):
    print("=== HÓSPEDES ===")
    nome_busca = input("Informe o nome: ")

    encontrado = False #Ainda não encontrei ninguém
    for hospede in hospedes:#Durante a busca
        if hospede["nome"] == nome_busca:# fazendo a busca
            print(f"Nome: {hospede['nome']}")
            print(f"Idade: {hospede['idade']}")
            print(f"CPF: {hospede['cpf']}")
            print("-" * 30)
            encontrado = True #Sim, encontrei o hóspede

    if not encontrado:
        print("Hóspede não encontrado")

    print("=== RESERVAS ===")

    if len(reservas) == 0:
        print("Não há reservas")
    else:
        for reserva in reservas:
            print(f"Tipo de quarto: {reserva['tipo de quarto']}")
            print(f"Diárias: {reserva['quantidade de diarias']}")
            print(f"Valor: {reserva['valor total']}")
            print("-" * 30)


def menu():
    hospedes = []
    reservas = []
    while True:
        print("----MENU----")
        print("1 - Cadastrar hóspede")
        print("2 - Reserva de quartos")
        print("3 - Ver relatório")
        print("4 - SAIR")
        try:
            op = int(input("Qual opção deseja?: "))
            if op == 1:
                hospede = cadastrar_hospede()
                if hospede:
                    hospedes.append(hospede)

            elif op == 2:
                reserva = reserva_quarto(hospedes)
                if reserva:
                    reservas.append(reserva)

            elif op == 3:
                mostrar_relatorio(hospedes, reservas)
                print("-" * 20)

            elif op == 4:
                print("Saindo...")
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Digite apenas números no menu!")

menu()