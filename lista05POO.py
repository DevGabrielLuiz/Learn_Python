# 1 - Crie uma classe chamada "Retangulo" que tenha os atributos "largura" e "altura".
# Crie métodos para calcular a área e o perímetro do retângulo.

class Retangulo:
    def __init__(self, larg, alt):
        self.area = None
        self.perimetro = None
        self.largura = larg
        self.altura = alt
        self.calc_perimetro()
        self.calc_area()

    def calc_perimetro(self):
        self.perimetro = (self.altura * 2) + (self.largura * 2)

    def calc_area(self):
        self.area = self.largura * self.altura

    def __str__(self):
        return f'A largura do retangulo é {self.largura} e a altura é {self.altura} e a área é {self.area} e o perimetro é {self.perimetro}'


p1 = Retangulo(32, 22)
print(p1)


# 2 - Crie uma classe chamada "ContaBancaria" que tenha os atributos "titular" e "saldo". Crie métodos para depositar, sacar e exibir o saldo da conta.


class ContaBancaria:

    def __init__(self, tit, s):
        self.titular = tit
        self.saldo = s

        self.exibir()

    def exibir(self):
        print(f'O saldo da conta de {self.titular} é: {self.saldo}')

    def sacar(self, saque):
        self.saldo -= saque


c1 = ContaBancaria("Carlos", 200)
c1.sacar(200)
c1.exibir()
# 3 - Crie uma classe chamada "Carro" que tenha os atributos "marca", "modelo" e "ano". Crie um método para exibir as informações completas do carro.


# 4 - Crie uma classe chamada "Cachorro" que tenha os atributos "nome" e "idade". Crie um método para exibir o nome e a idade do cachorro e um método para latir.


# 5 - Observe o código a seguir e faça:


'''class Produto:
def __init__(self, codigo, nome, preco):
self.codigo = codigo
self.nome = nome
self.preco = preco

A sobrecarga do método str para retornar a instância do objeto "Produto" com seus atributos Exemplo:
print(produto2)
Código: 2, Nome: Calça Jeans, Preço: R$ 99.90
A sobrecarga dos métodos necessários para comparar o preço de dois produtos Exemplo:
print(produto1 >= produto2) #Deve retornar Sim se o preço do produto1 for maior ou igual ao preço do produto2
O preço do produto 1 é maior ou igual ao preço do produto 2? Sim'''

'''6 - Altere o código do exercício 1 para que seja possível:
Identificar se a figura é um quadrado (crie um método)
Testar se um retângulo é maior ou menor que outro retângulo (sobrecarga de operadores)'''
