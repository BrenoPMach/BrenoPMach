#Função de saudação Crie uma função chamada 'saudacao' que receba uma lista de nomes. A
#função deve percorrer a lista com um for e imprimir 'Olá, [nome]!' para cada pessoa.
'''saudacao = ['Breno', 'Pereira', 'Machado']
for x in saudacao:
    print(f'Olá, {x}!')'''



#Filtrar nomes curtos Escreva uma função chamada 'nomes_curtos' que receba uma lista de
#nomes e retorne apenas aqueles que possuem até 4 letras. Use if dentro de um for.
'''nome_curtos = ['Bren', 'Machado', 'Sala']
for x in nome_curtos:
    if len(x) <= 4:
        print(x)'''



#Lista até 'sair' Crie um programa que peça ao usuário nomes para adicionar em uma lista. O
#programa deve continuar pedindo nomes até que o usuário digite 'sair'. Depois, mostre a lista
#completa.

'''nomes = []
while True:
    nome = input("Digite um nome para adicionar à lista (ou 'Sair' para terminar): ")
    if nome.lower() == 'sair':
        break
    nomes.append(nome)
print("Lista completa de nomes:")
for nome in nomes:
    print(nome)'''


#Contar ocorrências Faça uma função chamada 'contar_ocorrencias' que receba uma lista de
#palavras e uma palavra específica. Use for para contar quantas vezes a palavra aparece e retorne
#o total.
'''def contar_ocorrencias(lista_de_palavras, palavra_especifica):

  contador = 0
  for palavra in lista_de_palavras:
    if palavra == palavra_especifica:
      contador += 1
  return contador

minha_lista = ["maçã", "banana", "maçã", "laranja", "maçã", "uva"]
palavra_para_contar = "maçã"

total = contar_ocorrencias(minha_lista, palavra_para_contar)
print(f"A palavra '{palavra_para_contar}' aparece {total} vezes na lista.")'''



#Lista de convidados Crie uma função chamada 'listar_convidados' que receba uma lista de
#nomes e, usando for, exiba: o número do convidado (posição na lista + 1) e o nome do convidado.
'''def listar_convidados(lista_de_convidados):
  for indice, nome in enumerate(lista_de_convidados):
    print(f"Convidado {indice + 1}: {nome}")

convidados = ["Breno", "Pereira", "Machado"]
listar_convidados(convidados)'''



#Remover duplicados Faça uma função que receba uma lista com nomes repetidos e retorne uma
#nova lista sem repetições. Utilize um for e if para verificar se o nome já foi adicionado.
'''def remover_duplicados(lista_original):
  lista_sem_duplicados = []

  for nome in lista_original:
    if nome not in lista_sem_duplicados:
      lista_sem_duplicados.append(nome)

  return lista_sem_duplicados

nomes_com_repeticao = ["Ana", "Breno", "Carlos", "Ana", "Daniel", "Breno", "Eva"]
nomes_unicos = remover_duplicados(nomes_com_repeticao)
print(nomes_unicos)'''


#Menu de opções Crie um programa que mostre um menu dentro de um while, com as opções: 1
#- Adicionar nome à lista, 2 - Listar todos os nomes, 3 - Sair. O programa deve continuar até que o
#usuário escolha a opção 3.
'''def menu_nomes():
    lista_nomes = []

    while True:
        print("\n--- Menu de Opções ---")
        print("1 - Adicionar nome à lista")
        print("2 - Listar todos os nomes")
        print("3 - Sair")

        escolha = input("Escolha uma opção (1-3): ")

        if escolha == '1':
            novo_nome = input("Digite o nome a adicionar: ")
            lista_nomes.append(novo_nome)
            print(f"'{novo_nome}' adicionado à lista.")
        elif escolha == '2':
            if lista_nomes:
                print("\n--- Lista de Nomes ---")
                for i, nome in enumerate(lista_nomes):
                    print(f"{i+1}. {nome}")
            else:
                print("A lista de nomes está vazia.")
        elif escolha == '3':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha entre 1, 2 ou 3.")

menu_nomes()'''



#Procurar em lista Escreva uma função 'buscar_nome' que receba uma lista de nomes e um
#nome a procurar. Use um for e if para verificar se o nome existe na lista. Se existir, retorne 'Nome
#encontrado'. Caso contrário, 'Nome não encontrado'.
'''def buscar_nome(lista_nomes, nome_procurado):

  for nome in lista_nomes:
    if nome == nome_procurado:
      return "Nome encontrado"
  return "Nome não encontrado"

nomes_registrados = ["Maria", "João", "Ana", "Pedro"]
nome1 = "Ana"
nome2 = "Carlos"

resultado1 = buscar_nome(nomes_registrados, nome1)
print(f"'{nome1}': {resultado1}")

resultado2 = buscar_nome(nomes_registrados, nome2)
print(f"'{nome2}': {resultado2}")'''


#Separar nomes por letra inicial Crie uma função que receba uma lista de nomes e organize-os
#em duas listas: uma com os que começam com a letra 'A' e outra com os demais. Retorne as duas
#listas.
'''def separar_nomes(lista_de_nomes):

    comecam_com_a = []
    outros_nomes = []

    for nome in lista_de_nomes:
        if nome.lower().startswith('a'):
            comecam_com_a.append(nome)
        else:
            outros_nomes.append(nome)

    return comecam_com_a, outros_nomes


lista_completa = ["Ana", "Breno", "Amanda", "Carlos", "Antônio", "Daniel"]
nomes_a, nomes_outros = separar_nomes(lista_completa)

print(f"Nomes que começam com 'A': {nomes_a}")
print(f"Nomes que não começam com 'A': {nomes_outros}")'''


#Simulador de senha Crie uma função chamada 'verificar_senha' que peça ao usuário digitar
#uma senha (ex.: 'python123') dentro de um while. O laço só deve terminar quando o usuário acertar
#a senha. Enquanto for errada, mostrar 'Senha incorreta, tente novamente.'.
'''def verificar_senha():

    senha_correta = 'python123'
    senha_digitada = ''

    while senha_digitada != senha_correta:
        senha_digitada = input('Digite a senha: ')
        if senha_digitada != senha_correta:
            print('Senha incorreta, tente novamente.')

    print('Senha correta. Acesso concedido!')

verificar_senha()'''

