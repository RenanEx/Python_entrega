from usuarios_app.usuario import Usuario

def menu():
    while True:
        print("=== MENU ===")
        print("1. Registrar novo usuário")
        print("2. Fazer login")
        print("3. Exibir todos os usuários")
        print("4. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Nome: ").strip()
            senha = input("Senha: ").strip()
            email = input("Email: ").strip()
            idade = input("Idade: ").strip()
            Usuario.registrar_usuario(nome, senha, email, idade)

        elif opcao == "2":
            nome = input("Nome: ").strip()
            senha = input("Senha: ").strip()
            Usuario.fazer_login(nome, senha)

        elif opcao == "3":
            Usuario.exibir_usuarios()

        elif opcao == "4":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    menu()
