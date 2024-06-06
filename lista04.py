# 1 - Escreva uma função que receba uma lista de strings como argumento e retorne uma nova
# lista contendo apenas as strings que começam com a letra "a".
import re
import unicodedata
from functools import reduce
def Lista_1A(nlista):
    lista = []  # Cria uma lista vazia chamada 'lista'
    alista = []  # Cria uma lista vazia chamada 'alista'

    # Este loop solicita ao usuário inserir três strings e as adiciona à lista 'lista'
    for _ in range(nlista):  # Loop
        string = input("Digite as strings para a lista: ")  # Entrada
        lista.append(string)  # Adiciona a string a lista

    print(lista)  # Imprime a lista 'lista' com as strings inseridas pelo usuário
    for palavra in lista:
        primeira_letra = palavra[0].lower()
        if primeira_letra in ['a', 'á', 'à', 'ã', 'â']:#verifica
            alista.append(palavra)
    print(f"Lista contendo apenas palavras que começam com a letra |a| {alista}")
    return lista,alista
                                        #Feito
# 2 - Escreva uma função que receba uma lista de números como argumento e retorne o maior número da lista.
def Maior_Lista(nlista):
    lista=[]
    for _ in range(nlista):
        numeros=float(input("Digite os itens da sua lista: "))
        if numeros==int(numeros):
            lista.append(int(numeros))
        else:
            lista.append(numeros)
    lista.sort()
    if lista[-2]<lista[-1]>lista[-3]:
        print(f"O maior valor da lista é : {lista[-1]}")
    else:
        print(f"A lista não possui um valor maior que os outros!!")
    return lista
                    #FEITO

# 3 - Escreva uma função que recebe uma lista de números como parâmetro e retorna a soma total dos elementos da lista
def Soma_Lista(nlista):
    lista=[]
    #soma=0
    for _ in range(nlista):

        numeros=float(input("Digite os números da sua lista: "))
        #soma+=numeros #Outro jeito
        if numeros == int(numeros):
            lista.append(int(numeros))
        else:
            lista.append(numeros)
    print(f'A lista é {lista}, e a soma total dos valores da lista é {sum(lista)}')
    return lista
                        #FEITO
# 4 - Escreva uma função que recebe uma lista de números como parâmetro e retorna o produto total dos elementos da lista
def Multi_Lista(nlista):
    lista=[]
    mult=1
    for _ in range(nlista):

        numeros=float(input("Digite os números da sua lista: "))
        mult*=numeros
        if numeros == int(numeros):
            lista.append(int(numeros))
        else:
            lista.append(numeros)

    print(f'A lista é {lista}, e o valor multiplicação dos itens da lista é {mult}')
    return lista,mult
                        #FEITO
# 5 - Escreva uma função que recebe uma lista de números como parâmetro e retorna outra lista apenas com os números pares
def Lista_pares(nlista):
    lista=[]
    lista_pares=[]
    for _ in range(nlista):
        numero=int(input("Digite um número qualquer: "))
        lista.append(numero)
    for x in lista:
        if x%2==0:
            lista_pares.append(x)

    print(f"A lista original é {lista} \nLista apenas com os pares é {lista_pares}")
    return lista,lista_pares
                                    #FEITO
# 6 - Escreva uma função que recebe uma string como parâmetro e retorna outra string onde substitui as vogais por x
def x_troca_vogal(f_string):
    #for letra in f_string:
     #   if letra in 'aeiou':
    print(f_string)
    print(re.sub(r'a|e|i|o|u', 'X', f_string))
    return f_string
                    #FEITO

# 7 - Definir uma função que testa um caractere e retorna se é vogal ou não
def Testa_Vogal(f_string):
    vogais = 'aeiouAEIOU'
    if f_string in vogais:
        print("A letra |"+f_string+"| é vogal")
    else:
        print("A letra |"+f_string+"| não é vogal")

    return f_string in vogais
            #FEITO
# 8 - Reescreva o exercício 6 usando a função reduce e a função definida no exercício anterior
def x_Troca_Vogal_Com_reduce(f_string, Testa_Vogal):
    nova_string = reduce(lambda acc, f_string: acc + ('x' if Testa_Vogal(f_string) else f_string), f_string, "")
    print(nova_string)
                            # FEITO

# 9 - Crie uma função para percorrer uma string informando se o caracter é acentuado ou não
def Acentuado_ou_Nao(f_string):
    acentuados = []  # Lista para armazenar caracteres acentuados encontrados
    for letra in f_string:
        if unicodedata.category(letra)[0] == 'M':
            acentuados.append(letra)  # Adiciona o caractere acentuado à lista 'acentuados'
            print("Caracteres acentuados encontrados:")
            print(' As letras acentuadas são '.join(acentuados))  # Imprime os caracteres acentuados separados por espaço
        return acentuados
                                #FEITO pórem não está imprimindo nada


print('''Digite sua opção: 
[1]Para lista contendo apenas as strings que começam com a letra "a"
[2]Função que receba uma lista de números como argumento e retorne o maior número da lista.
[3]Função que recebe uma lista de números como parâmetro e retorna a soma total dos elementos da lista.
[4]Escreva uma função que recebe uma lista de números como parâmetro e retorna o produto total dos elementos da lista
[5]Função que recebe uma lista de números como parâmetro e retorna outra lista apenas com os números pares
[6]Função que recebe uma string como parâmetro e retorna outra string onde substitui as vogais por x
[7]Função que testa um caractere e retorna se é vogal ou não
[8]Exercício 6 usando a função reduce e a função definida no exercício anterior
[9]Função para percorrer uma string informando se o caracter é acentuado ou não
[10]Para encerrar''')

opcao=int(input("Digite a sua opção : "))
if opcao==1:
    num_lista = int(input("Digite a quantidade de caracteres da lista: "))

    Lista_1A(num_lista)

elif opcao==2:
    num_lista = int(input("Digite a quantidade de caracteres da lista: "))
    Maior_Lista(num_lista)

elif opcao==3:
    num_lista = int(input("Digite a quantidade de caracteres da lista: "))
    Soma_Lista(num_lista)

elif opcao==4:
    num_lista = int(input("Digite a quantidade de caracteres da lista: "))
    Multi_Lista(num_lista)

elif opcao==5:
    num_lista = int(input("Digite a quantidade de caracteres da lista: "))
    Lista_pares(num_lista)

elif opcao==6:
    string=input("Digite o texto que você deseja: ")
    x_troca_vogal(string)

elif opcao==7:
    string = input("Dgite o caracter que você deseja: ")
    Testa_Vogal(string)

elif opcao==8:
    string = input("Digite o texto que você deseja: ")
    x_Troca_Vogal_Com_reduce(string,Testa_Vogal)

elif opcao==9:
    string = input("Digite o texto que você deseja: ")
    Acentuado_ou_Nao(string)

else:
    print("Opção inválida!!!".upper())
