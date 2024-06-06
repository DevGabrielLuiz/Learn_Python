class Cliente:
    def __init__(self, nome, senha, usuario, email, plano):
        self.nome = nome
        self.senha = senha
        self.usuario = usuario
        self.email = email
        self.lista_planos = ['basico', 'premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception('Plano Inválido')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano

    def ver_fime(self, filme, plano_filme):
        if self.plano == plano_filme:
            print('Assita')
        elif self.plano == "premium":
            print('assista')
        elif self.plano == 'basic' and plano_filme == 'premium':
            print('Não pode assistir faça upgrade')


cliente = Cliente("Gabriel", 32332, "GBZIN", "Gbasdi@gmail.com", "basico")
