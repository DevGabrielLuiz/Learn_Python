from faker import Faker
fake = Faker('pt_BR')

class ContaBancaria:
    def __init__(self, tit, s):
        self.titular = tit
        self.saldo = s
        self.contTrans = 0
        self.extrato = []  # Lista para registrar depositos e saques
        self.operacoes = []  # Lista para detalhes das operações

    def depositar(self, valor):
        self.saldo += valor
        self.contTrans += 1
        self.extrato.append(f'Depósito: +{valor}')
        self.operacoes.append(f'Depósito de {valor}. Saldo atual: {self.saldo}')

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.contTrans += 1
            self.extrato.append(f'Saque: -{valor}')
            self.operacoes.append(f'Saque de {valor}. Saldo atual: {self.saldo}')
        else:
            print("Saldo insuficiente para efetuar o saque.")

    def imprimir_extrato(self):
        print(f"Extrato da conta de {self.titular}:")
        for transacao in self.extrato:
            print(transacao)
        print(f"Saldo atual: {self.saldo}")

    def __str__(self):
        return f'O titular da conta {self.titular} possui saldo de {self.saldo}.'

class Banco:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco
        self.clientes = []
        self.contas = []  # Lista para armazenar as instâncias de ContaBancaria

    def adicionar_cliente(self, nClientes):
        # Adiciona clientes fictícios usando o Faker
        for _ in range(nClientes):
            nome_cliente = fake.name()
            self.clientes.append(nome_cliente)

    def abrir_conta(self, novo_cliente):
        nova_conta = ContaBancaria(novo_cliente, 0)  # Cria nova conta com saldo inicial zero
        self.contas.append(nova_conta)
        print(f"Conta aberta para {novo_cliente}")

    def listar_contas(self):
        print(f"Contas do Banco {self.nome_banco}:")
        for conta in self.contas:
            print(f"Titular: {conta.titular}, Saldo: {conta.saldo}")

    def listar_saldo_maior_que_10000(self):
        print(f"Contas com saldo superior a 10000 no Banco {self.nome_banco}:")
        for conta in self.contas:
            if conta.saldo > 10000:
                print(f"Titular: {conta.titular}, Saldo: {conta.saldo}")

class ContaEspecial(ContaBancaria):
    def __init__(self, tit, s, limite):
        super().__init__(tit, s)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.contTrans += 1
            self.extrato.append(f'Saque: -{valor}')
            self.operacoes.append(f'Saque de {valor}. Saldo atual: {self.saldo}')
        else:
            print("Limite de saque excedido.")

# Exemplo de uso das classes
banco1 = Banco("Meu Banco")

# Adiciona clientes ao banco
banco1.adicionar_cliente(3)

# Abre contas para clientes
for cliente in banco1.clientes:
    banco1.abrir_conta(cliente)

# Realiza operações em uma conta específica
conta_exemplo = banco1.contas[0]
conta_exemplo.depositar(500)
conta_exemplo.sacar(200)
conta_exemplo.imprimir_extrato()

# Listar todas as contas do banco
banco1.listar_contas()

# Listar contas com saldo superior a 10000
banco1.listar_saldo_maior_que_10000()


conta_especial = ContaEspecial("Alice", 5000, 1000)
conta_especial.depositar(40553)
