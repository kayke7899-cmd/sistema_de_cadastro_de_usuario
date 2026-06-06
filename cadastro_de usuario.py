

print("--------------- SISTEMA DE CADASTRO -------------")

# Listas para armazenar os dados dos USUÁRIOS
nome_cadastro = []
email_cadastro = []
senha_cadastro = []
cpf_cadastro = []

# --- LOOP PRINCIPAL DO SISTEMA ---
continuar_sistema = True

while continuar_sistema:
    # Menu de opções para o usuário
    opcao_1 = "1 - Cadastrar usuário"
    opcao_2 = "2 - Login de usuário"
    opcao_3 = "3 - Recuperar conta"
    opcao_4 = "4 - Sair do sistema"
    
    opcao = input(f"\n{opcao_1}\n{opcao_2}\n{opcao_3}\n{opcao_4}\nEscolha uma opção: ")
    
    # Opção 1: Cadastro
    if opcao == "1":
        nome = input("Digite o nome: ")
        
        # Validação do email
        while True:
            email = input("Digite o email: ")
            if email == "":
                print("O email não pode estar vazio")
                continue
            if "@gmail.com" not in email and "@hotmail.com" not in email and "@outlook.com" not in email:
                print("Formato de email inválido")
                continue
            elif email in email_cadastro:
                print("Email já cadastrado. Digite outro email.")
                continue
            else:
                break 
        
        # Validação da senha
        while True:
            senha = input("Digite a senha: ")
            if senha == "":
                print("O campo senha não pode estar vazio")
                continue
            if len(senha) < 6:
                print("A senha deve conter no mínimo 6 caracteres")
                continue
            else:
                break
        
        # Validação do CPF
        while True:
            cpf = input("Digite o CPF: ")
            if cpf == "":
                print("O CPF não pode estar vazio")
                continue
            if len(cpf) != 11 or not cpf.isdigit():
                print("CPF inválido, deve conter 11 dígitos numéricos")
                continue
            elif cpf in cpf_cadastro:
                print("CPF já cadastrado. Digite outro CPF.")
                continue
            else:
                break
        
        if nome == "":
            print("Preencha todos os campos para realizar o cadastro")
            continue
        
        # Verifica duplicidade total (Nome + Email + CPF)
        usuario_ja_existe = False
        for i in range(len(nome_cadastro)):
            if (nome_cadastro[i] == nome and 
                email_cadastro[i] == email and 
                cpf_cadastro[i] == cpf):
                usuario_ja_existe = True
                break
        
        if usuario_ja_existe:
            print("Este usuário já está completamente cadastrado.")
            continue
        
        nome_cadastro.append(nome)
        email_cadastro.append(email)
        senha_cadastro.append(senha)
        cpf_cadastro.append(cpf)
        print("Cadastro realizado com sucesso!")
    
    # Opção 2: Login de Usuário
    elif opcao == "2":
        if len(nome_cadastro) == 0:
            print("Nenhum usuário cadastrado. Faça o cadastro primeiro.")
            continue
        
        while True:
            email_login = input("Digite o email para login: ")
            senha_login = input("Digite a senha para login: ")
            
            if email_login == "" or senha_login == "":
                print("Preencha os campos de email e senha.")
                continue
            
            if email_login in email_cadastro:
                indice = email_cadastro.index(email_login)
                if senha_cadastro[indice] == senha_login:
                    print("Login permitido")
                    print(f"Bem-vindo ao sistema: {nome_cadastro[indice]}")
                    
                    resposta = input("\nDeseja realizar outra operação? (s/n): ").lower()
                    if resposta == "s":
                        break # Sai do loop de login e volta ao menu principal
                    else:
                        print("Saindo do sistema...")
                        continuar_sistema = False # Encerra o loop principal
                        break # Sai do loop de login
                else:
                    print("Senha incorreta")
            else:
                print("Email ou senha incorretos")

    # Opção 3: Recuperação de conta
    elif opcao == "3":
        if len(nome_cadastro) == 0:
            print("Nenhum usuário cadastrado.")
            continue
        
        print("\n==== RECUPERAÇÃO DE CONTA ====")
        email_recuperacao = input("Digite o email de recuperação: ")
        
        if email_recuperacao == "":
            print("Campo vazio.")
            continue
        
        if "@gmail.com" in email_recuperacao or "@hotmail.com" in email_recuperacao or "@outlook.com" in email_recuperacao:
            if email_recuperacao in email_cadastro:
                print("Código enviado para seu email")
            else:
                print("Usuário não cadastrado")
        else:
            print("Formato de email inválido")
    
    # Opção 4: Sair
    elif opcao == "4":
        print("Saindo do sistema...")
        break
    
    # Opção Inválida
    else:
        print("Opção inválida")