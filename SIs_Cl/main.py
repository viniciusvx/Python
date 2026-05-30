perfis_permitidos = ("aluno","professor","tecnico") #TUPLA
tipos_problema = ("internet","computador","projetor","teclado","mouse")
usuarios=[] #ESA LISTA ARMAZENA OS USUARIOS CADASTRADOS
chamados = []
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
                print("Login realizado!!")
                return usuario
        print("Login ou senhas incorretas!!")
        return None #RETORNA VAZIO
        
def carregar_usuario(): 
    try:
        #REPONSÁVEL POR CARREGAR OS USUARIOS DO AQRQUIVO TXT
        arquivo=open('C:/Users/vboxuser/Documents/cadastro_usuario.txt', 'r', encoding='utf-8')

        for linha in arquivo:#PERCORRE CADA LINHA DO ARQUIVO TXT
            
            linha = linha.strip()#REMOVE O ESPAÇO DE LINHA

            if linha != '':#VERIFICA SE A LINHA ESÁ VAZIA
               
                dados = linha.split(';')#SEPARA OS DADOS USANDO ";"
                usuario={
                    "Nome": dados[0],
                    "Login": dados[1],
                    "Senha": dados[2],
                    "perfil": dados[3],
                }

                usuarios.append(usuario)#ADICIONA O USUARIO DENTRO DA LISTA DE USUARIOS
        
        arquivo.close()#FECHA O AQRUIVO APÓS A LEITURA
    
    except FileNotFoundError:# CASO O ARQUIVO AINDA NÃO EXISTA, ISSO AQUI VAI FUNCIONAR
        print("O arquivo não foi criado ainda")           

    finally:
        print("Usuarios carregados com sucesso")  
#FUNÇÃO REPONSÁVEL PARA SALVAR OS DADOS DO USUSARIO EM ARQUIVO TXT 
def salvar_usuario_arquivo(usuario):#PARAMETRO USUARIO(DICT)
        #TEBTA ABRIR E GRAVAR NO ARQUIVO
    try:
            #ABRE O ARQUIVO
            arquivo = open('C:/Users/vboxuser/Documents/cadastro_usuario.txt', "a",encoding='utf-8')# encondig='utf-8', VAI ACEITAR ACENTUAÇÃO
            
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

def registrar_chamado(usuario_logado):
    try:
        chamado ={}
        chamado['usuario'] = usuario_logado['Nome']
        print("=======TIPOS DE PROBLEMA=======")
        for tipo in tipos_problema:
            print(tipo)
        print("-" * 30)
        chamado['problema']=  input("Informe o motivo do seu chamado: ")
        if chamado['problema'] not in tipos_problema:
            print("Esse problema não consta nas opções")
            return
        chamado['descriçao']= input("Descreva o problema: ")
        chamado['status'] = "Aberto"
        print("Chamado realizado com sucesso!!")
    except:
        print("Dados inválidos")
    chamados.append(chamado)
    salvar_chamado(chamado)

def carregar_chamado(): 
    try:
        #REPONSÁVEL POR CARREGAR OS USUARIOS DO AQRQUIVO TXT
        arquivo_chamado=open('C:/Users/vboxuser/Documents/Chamados.txt', 'r', encoding='utf-8')

        for linha in arquivo_chamado:#PERCORRE CADA LINHA DO ARQUIVO TXT
            
            linha = linha.strip()#REMOVE O ESPAÇO DE LINHA

            if linha != '':#VERIFICA SE A LINHA ESÁ VAZIA
               
                dados = linha.split(';')#SEPARA OS DADOS USANDO ";"
                chamado = {
                    "usuario": dados[0],
                    "problema": dados[1],
                    "descriçao": dados[2],
                    "status": dados[3]
                }

                chamados.append(chamado)#ADICIONA O USUARIO DENTRO DA LISTA DE USUARIOS
        
        arquivo_chamado.close()#FECHA O AQRUIVO APÓS A LEITURA
    
    except FileNotFoundError:# CASO O ARQUIVO AINDA NÃO EXISTA, ISSO AQUI VAI FUNCIONAR
        print("O arquivo não foi criado ainda")           

    finally:
        print("Usuarios carregados com sucesso")  

def salvar_chamado(chamado):
    
    try:
        arquivo_chamado = open('C:/Users/vboxuser/Documents/Chamados.txt', "a",encoding='utf-8')

        arquivo_chamado.write(
            chamado['usuario'] + ';' +
            chamado['problema'] + ';' + 
            chamado['descriçao'] + ';'  +
            chamado['status'] + '\n'  
        )
        arquivo_chamado.close()
    except FileNotFoundError:
        print("O arquivo não foi criado ainda")           


def menu_sistema(usuario_logado):
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
            registrar_chamado(usuario_logado)
        
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
             usuario_logado = fazer_login()
             
             if usuario_logado != None:#VERIFICA SE O LOGIN ESTÁ VAZIO
                
                 menu_sistema(usuario_logado)  #CHAMA O MENU INTERNO     
        
        elif op == 3:
           if len(usuarios) == 0:
               print("Nenhum usuario cadastrado")
           else:
               for usuario in usuarios:#PERCORRE A LISTA DE USUARIO
                   
                   print(usuario['Nome'], '-', usuario['Login'], '-' ,usuario['perfil'])#MOSTRA O NOME<LOGIN E PERFIL DE TODOS OS CADASTRADOS
        
        elif op == 4:
            print("Sistema encerrado...")
            break 

        else:
            print("Inválido")
carregar_usuario()
menu_principal()
