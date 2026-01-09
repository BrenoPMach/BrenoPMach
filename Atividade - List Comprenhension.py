#Crie uma lista com os números de 0 a 9 usando list comprehension.
'''numeros = [i for i in range(10)]
print(numeros)'''


''#Gere uma lista com o quadrado dos números de 1 a 10.
'''quadrados = [i**2 for i in range(1, 11)]
print(quadrados)'''


#Crie uma lista apenas com os números pares de 0 a 20.
'''lista_pares = [i for i in range(0, 21) if i % 2 == 0]
print(lista_pares)'''


#Dada a lista ['ana', 'joão', 'maria', 'paulo'], use list comprehension para transformar todos os nomes em maiúsculas.
'''nomes = ['ana', 'joão', 'maria', 'paulo']
nomes_maiusculos = [nome.upper() for nome in nomes]
print(nomes_maiusculos)'''



#A partir da frase 'python é divertido de aprender', crie uma lista apenas com as palavras que tenham mais de 6 letras.
'''frase = (f'python é divertido de aprender')
lista_filtrada = [palavra for palavra in frase.split() if len(palavra) > 6]
print(lista_filtrada)'''


#Gere uma lista com os cubos (n³) dos números de 1 a 5.
'''cubos = [n**3 for n in range(1, 6)]
print(cubos)'''


#Crie uma lista com os múltiplos de 3 de 0 a 30.
'''multiplos_de_3 = []
for numero in range(31):
    if numero % 3 == 0:
        multiplos_de_3.append(numero)
        print(numero)'''


#Dada a lista [5, 12, 7, 18, 3, 21], use list comprehension para gerar uma nova lista apenas com os números maiores que 10.
'''lista_original = [5, 12, 7, 18, 3, 21]
nova_lista = [numero for numero in lista_original if numero > 10]
print(nova_lista)'''


#Crie uma lista com as primeiras letras de cada palavra da lista ['cachorro', 'gato', 'elefante', 'urso'].
'''animais = ['cachorro', 'gato', 'elefante', 'urso']
iniciais = [palavra[0] for palavra in animais]
print(iniciais)'''


#A partir da lista ['python', 'java', 'c', 'javascript'], crie uma nova lista apenas com as linguagens que têm mais de 4 letras.
'''linguagens = ['python', 'java', 'c', 'javascript']
linguagens_filtradas = [lingua for lingua in linguagens if len(lingua) > 4]
print(linguagens_filtradas)'''

