
def intrucoes():
    try:
        while True:
            print("===O QUE É PRECISO PARA DOAR SANGUE===")
            print("POSSUI DOCUMENTO OFICIAL COM FOTO?: ")
            op = int(input("1-sim 2-não\n"))

            if op != 1 and op != 2:
                print("Numero inválido")

            if op == 2:
                print("NÃO PODE REALIZAR A DOAÇÃO!")
                exit()

            if op == 1:
                print("SEU PESO É ACIMA DE 51 KG?: ")
                op = int(input("1-sim 2-não\n"))

                if op != 1 and op != 2:
                    print("Numero inválido")

                if op == 2:
                    print("NÃO PODE REALIZAR A DOAÇÃO!")
                    exit()

                if op == 1:
                    print("VOCÊ ESTÁ GRIPADO OU COM OUTRAS INFECÇÕES?: ")
                    op = int(input("1-sim 2-não\n"))

                    if op != 1 and op != 2:
                        print("Numero inválido")

                    elif op == 1:
                        print("NÃO PODE REALIZAR A DOAÇÃO")
                        exit()

                    elif op == 2:
                        print("VOCÊ ESTÁ DESCANSADO E ALIMENTADO?: ")
                        op = int(input("1-sim 2-não\n"))

                        if op != 1 and op != 2:
                            print("Numero inválido")

                        if op == 2:
                            print("NÃO PODE REALIZAR A DOAÇÃO!")
                            exit()

                        if op == 1:
                            idade = int(input("INFORME A SUA IDADE: "))

                            if idade >= 16 and idade < 18:
                                menor_idade = int(input("VOCÊ ESTÁ ACOMPANHADO E COM AUTORIZAÇÃO DO RESPONSÁVEL: 1-sim 2-não\n"))

                                if menor_idade == 1:
                                    print("PODE REALIZAR A DOAÇÃO")

                                elif menor_idade == 2:
                                    print("VOCÊ NÃO PODE REALIZAR A DOAÇÃO")

                            elif idade < 16:
                                print("VOCÊ NÃO PODE REALIZAR A DOAÇÃO")

                            elif idade >= 18 and idade <= 60:
                                print("PODE REALIZAR A DOAÇÃO")

                            elif idade >= 61:
                                print("É A SUA PRIMEIRA DOAÇÃO?")
                                op = int(input("1-sim 2-não\n"))

                                if op != 1 and op != 2:
                                    print("NUMERO INVÁLIDO")

                                if op == 1:
                                    print("VOCÊ NÃO PODE, O LIMITE PARA A PRIMEIRA DOAÇÃO É DE 60 anos, 11 meses e 29 dias")

                                else:
                                    print("PODE REALIZAR A DOAÇÃO")

    except ValueError:
        print("Dados inseridos de forma incorreta")


def espera():
    try:
        while True:
            print("===DEVE AGUARDAR PARA DOAR SANGUE===")

            print("TRANSFUSÃO DE\nTATUAGEM\nMICROPIGMENTAÇÃO\nPIERCING\nTOMOU VACINA ANTIRRÁBICA/dT(após exposição/mordedura)")
            print("PIERCING(oral e genital) após retirada, AMAMENTAÇÃO após data de parto")

            op = int(input("VOCÊ REALIZOU ALGUMA DESSAS OPERAÇÕES? 1-sim 2-não: "))

            if op != 1 and op != 2:
                print("NUMERO INVÁLIDO")
                break

            if op == 1:
                op = int(input("Você esperou o periodo de 1 ano? 1-sim 2-não: "))

                if op != 1 and op != 2:
                    print("NUMERO INVÁLIDO")
                    continue

                if op == 1:
                    print("PODE REALIZAR A DOAÇÃO")

                elif op == 2:
                    print("VOCE NÃO PODE REALIZAR A DOAÇÃO")

                exit()

            print("=" * 50)

            print("PROCEDIMENTOS ENDOSCÓPICOS(E PARCEIRO),DENGUE GRAVE")

            op = int(input("Você passou por alugum desses? 1-sim 2-não: "))

            if op != 1 and op != 2:
                print("Numero inválido")
                continue

            if op == 1:
                op = int(input("Você esperou o periodo de 6 meses? 1-sim 2-não: "))

                if op != 1 and op != 2:
                    print("Numero inválido")
                    continue

                if op == 1:
                    print("PODE REALIZAR A DOAÇÃO")

                else:
                    print("VOCÊ NÃO PODE REALIZAR A DOAÇÃO")

                exit()

            print("=" * 50)

            print("USO DE PREP/PEP ORAL(APÓS A ÚLTIMA APLICAÇÃO)")

            op = int(input("Você realizou esse procedimento? 1-sim 2-não: "))

            if op != 1 and op != 2:
                break

            if op == 1:
                op = int(input("Você esperou o periodo de 4 meses? 1-sim 2-não: "))

                if op != 1 and op != 2:
                    print("Numero inválido")
                    continue

                if op == 1:
                    print("PODE REALIZAR A DOAÇÃO")

                else:
                    print("VOCÊ NÃO PODE REALIZAR A DOAÇÃO")

                exit()

            print("=" * 50)

    except ValueError:
        print("DADOS INSERIDOS DE FORMA INCORRETA")


def restricoes():
    try:
        while True:
            print("-" * 10, "QUEM NÃO PODE DOAR SANGUE", "-" * 10)

            print("- Você teve Hepatite após 11 anos de idade?")
            op = int(input("1-sim 2-não\n"))

            if op == 1:
                print("NÃO PODE REALIZAR A DOAÇÃO!")
                exit()

            if op != 1 and op != 2:
                print("OPÇÃO INVÁLIDA")
                break

            if op == 2:
                print("-Você teve Doença de Chagas, Câncer, Sífilis?")
                op = int(input("1-sim 2-não\n"))

                if op != 1 and op != 2:
                    print("OPÇÃO INVÁLIDA")
                    break

                if op == 1:
                    print("NÃO PODE REALIZAR A DOAÇÃO!")
                    exit()

                if op == 2:
                    print("- Você se relacionou com pessoas infectadas pelo HIV e seus parceiros?")
                    op = int(input("1-sim 2-não\n"))

                    if op != 1 and op != 2:
                        print("OPÇÃO INVÁLIDA")
                        break

                    if op == 1:
                        print("NÃO PODE REALIZAR A DOAÇÃO!")
                        exit()

                    if op == 2:
                        print("- Você se relacionou com homens e mulheres com parceiro(a) eventual ou múltiplos parceiros sexuais?")
                        op = int(input("1-sim 2-não\n"))

                        if op != 1 and op != 2:
                            print("OPÇÃO INVÁLIDA")

                        if op == 1:
                            print("NÃO PODE REALIZAR A DOAÇÃO!")
                            exit()

                    if op == 2:
                        print("- Você compartilha seringas?")
                        op = int(input("1-sim 2-não\n"))

                        if op != 1 and op != 2:
                            print("OPÇÃO INVÁLIDA")
                            break

                        if op == 1:
                            print("NÃO PODE REALIZAR A DOAÇÃO!")
                            exit()

                        if op == 2:
                            print("- Você faz uso de drogas injetáveis ilícitas?")
                            op = int(input("1-sim 2-não\n"))

                            if op != 1 and op != 2:
                                print("OPÇÃO INVÁLIDA")
                                break

                            if op == 1:
                                print("NÃO PODE REALIZAR A DOAÇÃO!")
                                exit()

                            elif op == 2:
                                print("VOCÊ ESTÁ APTO PARA REALIZAR A DOAÇÃO")
                                exit()

    except ValueError:
        print("NUMERO INVALIDO")


def recomendacoes():
    try:
        while True:
            genero = input("Digite o seu genero [F][M]: ").upper()

            if genero != "F" and genero != "M":
                print("Dados inválidos")
                continue

            if genero == "F":
                dias = int(input("Escreva há quantos dias você fez sua última doação: "))

                if dias < 0:
                    print("Dados incorretos!")
                    break

                if dias <= 90:
                    print("Você deve aguardar até 90 dias para doar novamente")
                    exit()

                elif dias > 90:
                    print("PODE REALIZAR A DOAÇÃO")
                    exit()

            elif genero == "M":
                dias = int(input("Escreva há quantos dias você fez sua última doação: "))

                if dias < 0:
                    print("Dados incorretos!")
                    break

                if dias <= 60:
                    print("Você deve aguardar até 60 dias para doar novamente")
                    exit()

                elif dias > 60:
                    print("PODE REALIZAR A DOAÇÃO")
                    exit()

    except ValueError:
        print("DADOS INVÁLIDOS")
        exit()


def menu():
    try:
        while True:
            print("==========MENU==========")
            print("1 - RECOMENDAÇÕES")
            print("2 - INSTRUÇÕES")
            print("3 - RESTRIÇÕES")
            print("4 - TEMPO DE ESPERA")
            print("5 - SAIR")

            op = int(input("Informe a sua opção: "))

            if op < 1 or op > 5:
                print("OPÇÃO INVÁLIDA")
                break

            if op == 1:
                recomendacoes()

            elif op == 2:
                intrucoes()

            elif op == 3:
                restricoes()

            elif op == 4:
                espera()

            elif op == 5:
                print("SAINDO...")
                exit()

    except ValueError:
        print("Dados inseridos incorretamente")


menu()