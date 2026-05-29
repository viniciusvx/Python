perfis_permitidos = ("aluno","professor","tecnico") #TUPLA

usuarios=[] #ESA LISTA ARMAZENA OS USUARIOS CADASTRADOS

def cadastrar_usuario():
        usuario = {}

        usuario["Nome"]=input("Informe o seu nome completo: ")
        usuario["Login"]=input("Informe o seu login: ")
        usuario["Senha"]=input("Informe o sua senha: ")
        print("\n Perfis disponíveis")
        
        #PERCORRE A TUPLA DOS PERFIS
        for perfil in perfis_permitidos:
            #MOSTRA CADA PERFIL
            print("-",perfil)
        usuario['perfil'] = input("DIgite o perfil: ")

        #VERIFICA SE O PERFIL INFORMADO PELO USUARIO EXISTE
        if usuario["perfil"] not in perfis_permitidos:
            print("Perfil não cadastrado")
            return
        
        for i in usuarios: #PERCORRE A LISTA DE USUARIOS CADASTRADOS
         #VERIFICA SE O LOGIN JÁ EXISTE
         if i['Login'] == usuario['Login']:
            print("Esse login já existe")
            return
        #ADICIONA O USUARIO
        usuarios.append(usuario)
        salvar_usuario_arquivo(usuario)
        print("CADASTRO REALIZADO!!")

def fazer_login():
        login = input("Informe o login: ")
        senha = input("Informe a senha: ")
        
        for usuario in usuarios:
            if usuario["Login"] == login and usuario["Senha"] == senha:
                print("Login realizado")
                return usuario
        print("Login ou senhas incorretas!!")
        

#FUNÇÃO REPONSÁVEL PARA SALVAR OS DADOS DO USUSARIO EM ARQUIVO TXT 
def salvar_usuario_arquivo(usuario):#PARAMETRO USUARIO(DICT)
        #TEBTA ABRIR E GRAVAR NO ARQUIVO
    try:
            #ABRE O ARQUIVO
            arquivo = open('C:/Users/vboxuser/Documents/cadastro_usuario.txt', "w",encoding='utf-8')# encondig='utf-8', VAI ACEITAR ACENTUAÇÃO
            
            #ESCREVE OS DADOS DO USUSARIO EM TXT, SEPARANDO EM PONTO  VIRGULA
            arquivo.write(
                usuario['Nome'] + ';' + 
                usuario['Login'] + ';' +
                usuario['Senha'] + ';' +
                usuario['perfil'] + '\n' 

            )
            arquivo.close()
    except:
            print("Erro ao salvar os dados do usuário no aqruivo.")
        
    finally:
            #MOSTRA A MENSAGEM DE SUCESSO
            print("Dados salvo com sucesso.")

def menu_sistema():
       while True: 
        print("\n ==MENU SISTEMA==")
        print("1 - Registrar chamado")
        print("2 - Listar chamados")
        print("3 - Sair")
      
        try:
            op = int(input("Escolha um opção: "))
        except ValueError:
            
         print("Digite apenas numeros")
         continue
        
        if op == 1:
            print("Opção 1")
        
        elif op == 2:
            print("opcão 2")
        
        elif op == 3:
         print("Saindo da conta")
         break

        else:
            print("opção inválida")
     

def menu_principal():
    while True:

        print("\n === SISTEMA DE CHAMADOS ESCOLA ===")
        print("1-Cadastrar Usuários")
        print("2-Fazer login")
        print("3-Listar usuarios cadastrados")
        print("4-Sair")
      
        try:
         op = int(input("Escolha uma opção: "))
        except ValueError:
           print("EERO. digite apenas numeros")
           continue
        
        if op == 1:
            cadastrar_usuario()
        elif op == 2:
            usuario_logado = fazer_login
        
        elif op == 3:
            print(usuarios)
        
        elif op == 4:
            print("Sistema encerrado...")
            break 

        else:
            print("Inválido")

menu_principal()