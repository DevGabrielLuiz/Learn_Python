'''1 - Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres '+' , '−' e '| '. 
 Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo 
 igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para 
 valores dentro da faixa de forma elegante.'''
#Recebendo os valores
linha=int(input("Digite a quantidade de linhas : "))
coluna=int(input("Digite a quantidade de colunas : "))
#Verificando se estão dentro da faixa correta
if linha<1:
    linha=1
elif linha>20:
    linha=20
if coluna<1:
    coluna=1
elif coluna>20:
    coluna=20
    
print('+'+'-'*(coluna-2)+'+') #impressão da parte de cima da caixa
for x in range(linha):
    print('|'+' '*(linha-2)+'|') #impressão da linhas 
print('+'+'-'*(coluna-2)+'+')# impressão da parte de baixo

'''2 - Escreva uma função que receba uma string e uma lista. A função deve comparar a string passada
com os elementos da lista, também passada como parâmetro. Retorne verdadeiro se a string for encontrada dentro da 
lista, e falso, caso contrário.'''
'''def comparacao(string, lista_palavras):
    # Verifica se a string está presente em cada palavra da lista
    for palavra in lista_palavras:
        if string == palavra:
            print(f"A string '{string}' está presente na palavra '{palavra}'")
        else:
            print(f"A string '{string}' não está presente na palavra '{palavra}'")

# Lendo a string
string = input('Digite a string: ')

# Inicializando uma lista 
palavras = [] 

# recebendo os valores da lista
for _ in range(4):
    palavra = input('Digite a palavra a ser adicionada na lista: ')
    palavras.append(palavra)

# Chama a função
comparacao(string, palavras)


#3 - Crie um programa que transfome o real em dólar
real=float(input("Digite um número: ")) # recebendo o valor 
dolar=real/4.50 #convertendo 
print("O valor em dolar é ",dolar) #impresssão do valor convertido

#4 - Crie um programa que calcule 25% de aumento no salário
sal_atual=float(input("Digite o salário atual do funcionario: "))   # recebendo o valor 
sal_aumento=sal_atual*1.25 #convertendo 
print(sal_aumento) # impressão do valor'''

#5 - Crie um programa que transfome a letra Maiuscula em Minuscula
caracteres=input("Digite os caracteres em letra maiscula")
#covertida=caracteres.lower()#transforma em minuscula
#covertidainverso=caracteres.upper()# transforma em maiscula
print(caracteres.lower()) #impressão

'''6 - Crie um programa que verifica se a pessoa está apta ou não para votar nas eleições.
Critérios:
Idade menor que 16: Não pode votar
16 <= Idade < 18: Opcional
18 <=Idade <= 65: Obrigatório
Idade maior que 65: Opcional'''
idade=int(input('Digite sua idade atual')) # recebendo as idades
#vericando as condicoes e já imprimindo
if 16<=idade<18:
    print('Voce é de menor,pode votar mas não é obrigado')
elif 18<=idade<=65:
    print('Voce é obrigado a votar ')
else:
    print('Voce já e idoso, não é mais obrigado a votar')

#7 - Crie um programa que leia o seu nome completo e que apresente somente o seu primeiro e último nomes
# Inicialize uma lista vazia para armazenar os nomes
nome_completo=[]
# Solicite ao usuário que insira os nomes e adicione-os à lista
while True:
    receba_nome = input("Digite um nome (ou digite 'fim' para encerrar): ").strip()
    if receba_nome.lower() == 'fim':
        break  # Encerra o loop se o usuário digitar fim
    nome_completo.append(receba_nome)  # Adiciona o nome à lista de nomes

# Imprima a lista de nomes
print("Lista de nomes inseridos:")
print(nome_completo[0])
print(nome_completo[-1])


#8 - Crie um programa que leia um número qualquer e informe se ele é par ou ímpar
'''num=float(input("Digite um número: "))
if num%2==0:
    print("PAR!!!")
else:
    print("IMPAR!!!")'''

#9 - Crie um programa que apresente o maior e o menor valores da sequência ([54, 10, 29, 87, 7, 64]
'''lista=[54, 10, 29, 87, 7, 64]
lista.sort()
print('O menor é',lista[0])
print('O maior é',lista[4])
menor=999
maior=999*-1'''
#outra resolução
'''
num_itens = int(input('Digite quantos itens a lista irá ter: '))

lista = []

# Pede ao usuário para inserir os valores na lista
for _ in range(num_itens):
    valor = int(input('Digite o valor da lista: '))
    lista.append(valor)  # Adiciona o valor à lista

# Inicializa as variáveis menor e maior com os primeiros valores da lista
menor = lista[0]
maior = lista[0]

# Encontra o menor e o maior valor na lista
for valor in lista:
    if valor < menor:
        menor = valor  # Atualiza o menor valor encontrado
    if valor > maior:
        maior = valor  # Atualiza o maior valor encontrado

# Imprime a lista original, o menor e o maior valor
print("Lista original:", lista)
print(f"O menor item da lista é {menor} e o maior item é {maior}")'''
