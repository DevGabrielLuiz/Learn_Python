'''#1) Imprimir seu nome com uma letra por linha'''


def letra_linha(name):
    for x in name:
        print(x)


# 2)Escreva uma função que receba uma string e conte o número de vogais dentro dela, por exemplo: entrada: 'Ciência de Dados',
def contv(palavra):
    contador = 0
    for x in palavra:
        if x.lower() in 'aeiou':
            contador += 1

    return contador


# 3) Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres '+' , '−' e '| '.
# Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão 
# é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, 
# eles devem ser modificados para valores dentro da faixa de forma elegante.
def dmoldura(lin, col):
    # Verifica se o valor de lin está dentro dos limites
    if lin > 20:
        print('O valor excedeu o limite e foi reajustado para 20')
        lin = 20
    elif lin < 1:
        print('O valor excedeu o limite e foi reajustado para 1')
        lin = 1
    # Verifica se o valor de col está dentro dos limites
    if col > 20:
        print('O valor excedeu o limite e foi reajustado para 20')
        col = 20
    elif col < 1:
        print('O valor excedeu o limite e foi reajustado para 1')
        col = 1

    # Laço para desenhar a moldura
    for _ in range(lin):
        # Imprime a linha superior da moldura
        print('-' + '+' * (col - 2) + '-')
        # Imprime as linhas intermediárias da moldura
        for _ in range(col - 2):
            print('|' + ' ' * (col - 2) + '|')
    # Imprime a linha inferior da moldura
    print('-' + '+' * (col - 2) + '-')


# 4) Crie um função que retorna o resto de uma divisão
def restodiv(divisor_func, dividendo_func):
    resto_func = dividendo_func % divisor_func
    print(resto_func)


# 5) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, 
# sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
def aluguel_carro(dia_func, km_rodado_func):
    car_func = 60.00
    val_km_func = 0.15
    pr_func = (car_func * dia_func) + (val_km_func * km_rodado_func)
    print("O valor total do aluguel do carro foi de ", pr_func)


# 6) Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# Considere que um fumante perde 10 minutos de vida a cada cigarro, 
# e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
def perda_de_vida(qtd_cig, qtd_anos):
    qtd_total_cig = qtd_cig * qtd_anos * 365
    perda_em_minutos = 10 * qtd_total_cig
    perda_em_dias = perda_em_minutos / (24 * 60)

    return perda_em_dias


# 7) Validar e corrigir número de telefone.Faça um programa que leia um número de telefone, e corrija o número
# no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou
# sem o traço separador
def val_numero(num_fone):
    num_fone = num_fone.replace('-', '')
    if len(num_fone) <= 7:
        num_fone = '(31)9' + num_fone
    elif len(num_fone) == 9:
        num_fone = '(31)' + num_fone
    else:
        num_fone = num_fone
    return num_fone


# 8) Faça uma função Calculadora que recebe uma expressão matemática e retorna o resultado
# Ex:
# Entrada: Digite uma expressão matemática: 4+5
# Saída: O resultado é 9
def calculadora(express):
    a = ""
    b = ""
    c = ""

    for x in express:
        if x.isdigit():
            if c == "":
                a += x
            else:
                b += x
        elif x in '/*-+':
            c = x

    a = int(a)
    b = int(b)

    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        return a / b
    elif c == '%':
        return a % b


print('Digite 1 para fazer isso: ')
print('Digite 2 para fazer isso: ')
print('Digite 3 para fazer isso: ')
print('Digite 4 para fazer isso: ')
print('Digite 5 para fazer isso: ')
print('Digite 6 para fazer isso: ')
print('Digite 7 para fazer isso: ')
print('Digite 8 para fazer isso: ')
print('Digite 9 para fechar: ')
opcao = int(input('Digite uma opção válida: '))

if opcao == 1:
    nome = input("Digite seu nome: ")
    letra_linha(nome)
elif opcao == 2:
    palavras = input("Digite uma palavra: ")
    qtd_vogais = contv(palavras)
    print(f'Foram digitados na /{palavras}/ {qtd_vogais} vogais:')

elif opcao == 3:
    lin = int(input("Digite um valor entre 1 e 20 para a linha: "))
    col = int(input("Digite um valor entre 1 e 20 para a coluna: "))
    dmoldura(lin, col)
elif opcao == 4:
    dividendo = int(input('Digite o dividendo : '))
    divisor = int(input('Digite o divisor: '))
    restodiv(divisor, dividendo)

elif opcao == 5:
    km_rodado = float(input('Quantos quilomêtros foram percorridos? '))
    dias_usados = int(input('Quantos dias o carro permanceu alugado? '))
    aluguel_carro(km_rodado, dias_usados)

elif opcao == 6:
    qtd_cig = int(input('Quantos cigarros são fumados por dia? '))
    qtd_anos = float(input('Quantos anos você fumou? '))
    tot_perd = perda_de_vida(qtd_cig, qtd_anos)
    print(f"Você perderá aproximadamente {tot_perd:.2f} dias de vida devido ao cigarro.")

elif opcao == 7:
    num_fone = input('Digite seu número de telefone: ')
    num_fone_formatado = val_numero(num_fone)
    print("Número de telefone formatado:", num_fone_formatado)
elif opcao == 8:
    expressao = input('Digite uma expressão matemática: ')
    resultado = calculadora(expressao)
    print("O resultado é:", resultado)
else:
    print('Opção invalida')
