class EmailOuSenhaInvalidos(Exception):
    def __init__(self, mensagem="E-mail ou senha inválidos."):
        self.mensagem = mensagem
        super().__init__(self.mensagem)
