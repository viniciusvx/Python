'''CADASTRO DE PRODUTO    
-CATEGORIA
-QUANTIDADE DE ESTOQUE
 PREÇO

 RELATÓRIO
 -CATEGORIA
 QUANTIDADE
 PREÇO
 -SITUAÇÃO DE ESTOQUE
 QUANTIDADE > 10 = BOM
 QUANTIDADE >5 <10= MEDIO
 QUANTIDADE <5 = RUIM
    '''

def cadastrar_produto():# PARA EU VER TUDO ISSO ABAIXO EU TENHI QUE CHAMAR O NOME DA FUNÇÃO
    try:
     produto={} #PARA VER O DIC, TEM QUE CHAMAR O NOME DO DICIONÁRIO

     produto["nome"] = input("Informe o nome do produto: ")
     produto["preço"]= float(input("Informe o valor desse produto: "))
     produto["categoria"] =input("Informe a categoria do produto: ")
     produto["quantidade"] = int(input("Informe a quantidade do produto: "))
     print("Cadastro realizado!!")

    except ValueError:
        print("ERRO.Quantidade e preço devem ser numericos")

    finally:
        print("Finalizado!!!")
    
    return produto

def menu():
   produtos = []
   while True:
       print("--- MENU ---")
       print("1 - CADASTRAR PRODUTO")
       print("2 - VER RELATÓRIO")
       print("3 - Sair")
       op = input("Qual opção você deseja?: ")

       if op == "1":
          produto = cadastrar_produto()
          produtos.append(produto)

       elif op == "2":
           mostrar_relatorio(produtos)

       elif op == "3":
           print("Saindo...")
           exit()

       else: 
           print("opção inválida,digite novamente")
           continue
           
           
           

def mostrar_relatorio(produtos):
    if len(produtos) == 0:
        print("Nenhum produto cadastrado!!")
    else:
        print("---RELATÓRIO---")

        for produto in produtos:
            print(f"NOME: {produto["nome"]}")
            print(f"PREÇO: {produto["preço"]}R$")
            print(f"CATEGORIA: {produto["categoria"]}")
            print(f"QUANTIDADE: {produto["quantidade"]}")
            if produto["quantidade"] >=10:
                print ("a situação do estoque é boa")
            elif produto["quantidade"] >=5:
                print("A situação do estoque é média")
            else:
                print("A situação é péssima")
            print("-"*30)


menu()

           
           
   



       





    
    
