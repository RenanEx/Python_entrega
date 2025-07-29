class Usuario:
    banco_usuarios = {}  # Atributo de classe: armazena todos os usuários

    def __init__(self, nome, senha, email, idade):
        self.nome = nome
        self.senha = senha
        self.email = email
        self.idade = idade

    def __str__(self):
        return f"{self.nome} ({self.email})"

    @classmethod
    def registrar_usuario(cls, nome, senha, email, idade):
        if nome in cls.banco_usuarios:
            print("Usuário já existe.\n")
            return None
        usuario = cls(nome, senha, email, idade)
        cls.banco_usuarios[nome] = usuario
        print(f"Usuário '{nome}' registrado com sucesso!\n")
        return usuario

    @classmethod
    def fazer_login(cls, nome, senha):
        if nome in cls.banco_usuarios and cls.banco_usuarios[nome].senha == senha:
            print(f"Login bem-sucedido! Bem-vindo, {nome}.\n")
        else:
            print("Nome de usuário ou senha incorretos.\n")

    @classmethod
    def exibir_usuarios(cls):
        if not cls.banco_usuarios:
            print("Nenhum usuário cadastrado.\n")
        else:
            print("Usuários cadastrados:")
            for usuario in cls.banco_usuarios.values():
                print(f"- {usuario}")
            print()
