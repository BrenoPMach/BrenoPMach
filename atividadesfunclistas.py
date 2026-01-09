#Crie uma lista chamada numeros contendo os valores 5, 10, 15, 20. Em seguida, imprima a lista
#na tela.
# Cria a lista chamada 'numeros' com os valores especificados
'''numeros = [5, 10, 15, 20]

print(numeros)'''


#Dada a lista frutas = ['maçã', 'banana', 'uva', 'laranja'], exiba: - O primeiro elemento da lista. - O
#último elemento da lista
'''frutas = ['maçã', 'banana', 'uva', 'laranja']

print(frutas[0])
print(frutas[-1])'''


#Dada a lista cores = ['vermelho', 'azul', 'verde'], troque a cor 'azul' por 'amarelo' e imprima a nova
#lista.
'''cores = ['vermelho', 'azul', 'verde']
posicao_verde = cores.index('verde')
cores[posicao_verde] = 'preto'
print(cores)'''


#Crie uma lista vazia chamada animais. - Adicione 'cachorro' e 'gato' usando append(). - Adicione
#'pássaro' na posição 1 usando insert(). - Mostre a lista final.
'''animais = []

animais.append('cachorro')
animais.append('gato')

animais.insert(1, 'pássaro')

print(animais)'''


#Dada a lista linguagens = ['Python', 'Java', 'C', 'PHP', 'Ruby']: - Remova o último elemento. -
#Remova o primeiro elemento. - Remova 'Java' pelo valor. Mostre o resultado final.
'''linguagens = ['Python', 'Java', 'C', 'PHP', 'Ruby']

linguagens.pop()
print(f"Após remover o último elemento: {linguagens}")

linguagens.pop(0)
print(f"Após remover o primeiro elemento: {linguagens}")

linguagens.remove('Java')
print(f"Após remover 'Java': {linguagens}")'''


#Dada a lista numeros = [3, 8, 2, 10, 5]: - Mostre o tamanho da lista com len(). - Mostre o maior e
#o menor valor. - Mostre a soma dos valores.

'''numeros = [3, 8, 2, 10, 5]

print("Tamanho da lista:", len(numeros))
print("Maior valor:", max(numeros))
print("Menor valor:", min(numeros))
print("Soma dos valores:", sum(numeros))'''


#Dada a lista notas = [7.5, 8.0, 5.5, 9.0, 6.0]: - Organize a lista em ordem crescente. - Depois,
#inverta a ordem da lista.
'''notas = [7.5, 8.0, 5.5, 9.0, 6.0]
notas.sort()
notas.reverse()
print(notas)'''

#Dada a lista nomes = ['Ana', 'Bruno', 'Carla'], percorra os elementos com um for e imprima a
#frase: 'Olá, !' para cada item.
nomes = ['Ana', 'Breno', 'Carla']

'''for nome in nomes:
    print(f"Olá, {nome}!")'''


#Crie uma lista chamada mista com os valores: 25, 'Python', True, 3.14. Depois, exiba o elemento
#'Python' acessando pelo índice.
# Criando a lista mista com diferentes tipos de dados
'''mista = [25, 'Python', True, 3.14]
print(mista[1])'''

#Crie uma lista chamada compras com os itens: 'arroz', 'feijão', 'leite'. - Adicione 'pão'. - Troque
#'feijão' por 'macarrão'. - Remova 'leite'. - Mostre a lista final.
'''compras = ['arroz', 'feijão', 'leite']

compras.append('pão')

indice_feijao = compras.index('feijão')
compras[indice_feijao] = 'macarrão'

compras.remove('leite')

print(compras)'''

