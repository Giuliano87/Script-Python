# Estruturas de dados em Python são usadas para armazenar e manipular dados em uma estrutura organizada.

# Listas são estruturas de dados que permitem armazenar vários valores em uma única variável.

# Acessando os dados de uma lista

# Para acessar os dados de uma lista, usamos o índice. O índice é o número que identifica a posição de um elemento na lista.

# A lista é indexada a partir do 0, ou seja, o primeiro elemento da lista tem índice 0, o segundo elemento tem índice 1, e assim por diante.

# Exemplo:

# Criando uma lista

frutas = ["banana", "maçã", "pera", "uva"]

# Acessando os dados da lista

# Para acessar os dados de uma lista, usamos o índice.

# Acessando o primeiro elemento da lista

print(frutas[0])  # Saída: banana

# Acessando o segundo elemento da lista

print(frutas[1])  # Saída: maçã

# Acessando o último elemento da lista

print(frutas[-1])  # Saída: uva

# Acessando um intervalo de elementos da lista

# Podemos acessar um intervalo de elementos da lista usando a sintaxe de fatiamento.

# A sintaxe de fatiamento é feita com dois pontos (:) e entre eles, podemos especificar o índice inicial e o índice final do intervalo.

# Exemplo:

# Acessando um intervalo de elementos da lista

print(frutas[1:3])  # Saída: ['maçã', 'pera']

# Acessando o intervalo de elementos da lista com passo

# Podemos acessar um intervalo de elementos da lista com passo usando a sintaxe de fatiamento com três pontos (:::).        
# A sintaxe de fatiamento com três pontos é feita com três pontos (:::) e entre eles, podemos especificar o índice inicial, o índice final e o passo do intervalo.

print(frutas[0:3:2])  # Saída: ['banana', 'pera']

# Acessando elementos da lista inverso

# Podemos acessar os elementos de uma lista inverso usando a notação de índice negativo.

# A notação de índice negativo é feita com um sinal de menos (-) antes do índice.

# Exemplo:

# Acessando elementos da lista inverso

print(frutas[-1:-4:-1])  # Saída: ['uva', 'pera', 'maçã']

# Acessando elementos da lista com passo inverso

# Podemos acessar os elementos de uma lista com passo inverso usando a notação de índice negativo com três pontos (:::).

# A notação de índice negativo com três pontos é feita com três pontos (:::) e entre eles, podemos especificar o índice inicial, o índice final e o passo do intervalo.

print(frutas[-1:0:-1])  # Saída: ['uva', 'maçã', 'pera', 'banana']

# Adicionando elementos a uma lista
# Podemos adicionar elementos a uma lista usando a função append().

# Exemplo:

# Adicionando elementos a uma lista

frutas.append("abacaxi")

print(frutas)  # Saída: ['banana', 'maçã', 'pera', 'uva', 'abacaxi']

# Inserindo elementos em uma lista
# Podemos inserir elementos em uma lista em uma posição específica usando a função insert().

# Exemplo:

# Inserindo elementos em uma lista

frutas.insert(2, "morango")

print(frutas)  # Saída: ['banana', 'maçã', 'morango', 'pera', 'uva', 'abacaxi']

# Removendo elementos de uma lista
# Podemos remover elementos de uma lista usando a função remove() ou pop().

# Exemplo:

# Removendo elementos de uma lista

frutas.remove("maçã")

print(frutas)  # Saída: ['banana', 'morango', 'pera', 'uva', 'abacaxi']

frutas.pop(1)

print(frutas)  # Saída: ['banana', 'pera', 'uva', 'abacaxi']

# Tamanho de uma lista
# Podemos obter o tamanho de uma lista usando a função len().

# Exemplo:

# Tamanho de uma lista

print(len(frutas))  # Saída: 4
# Ordenando uma lista
# Podemos ordenar uma lista usando a função sort().

# Exemplo:

# Ordenando uma lista

frutas.sort()

print(frutas)  # Saída: ['abacaxi', 'banana', 'pera', 'uva']

# Ordenando uma lista em ordem inversa
# Podemos ordenar uma lista em ordem inversa usando a função reverse().

# Exemplo:

# Ordenando uma lista em ordem inversa

frutas.reverse()

print(frutas)  # Saída: ['uva', 'pera', 'banana', 'abacaxi']
# Contando elementos em uma lista
# Podemos contar o número de ocorrências de um elemento em uma lista usando a função count().

# Exemplo:

# Contando elementos em uma lista

print(frutas.count("banana"))  # Saída: 1

# Verificando se um elemento está em uma lista
# Podemos verificar se um elemento está em uma lista usando a função in.

# Exemplo:

# Verificando se um elemento está em uma lista

print("banana" in frutas)  # Saída: True
print("morango" in frutas)  # Saída: False
# Criando uma lista vazia
# Podemos criar uma lista vazia usando a função list().

# Exemplo:

# Criando uma lista vazia

frutas = list()

print(frutas)  # Saída: []
# Criando uma lista com valores iniciais
# Podemos criar uma lista com valores iniciais usando a sintaxe de colchetes e separando os valores com vírgulas.

# Exemplo:

# Criando uma lista com valores iniciais

frutas = ["banana", "maçã", "pera", "uva"]

print(frutas)  # Saída: ['banana', 'maçã', 'pera', 'uva']
# Criando uma lista com valores iniciais usando a função list()

# Exemplo:

# Criando uma lista com valores iniciais usando a função list()

frutas = list(["banana", "maçã", "pera", "uva"])

print(frutas)  # Saída: ['banana', 'maçã', 'pera', 'uva']

carro = ["Toyota", "Corola", "Cinza", "2021", "12500km"]
print(carro)  # Saída: ['Toyota', 'Corola', 'Cinza', '2021', '12500km']
print(carro)  # Saída: ['Marca', 'Modelo', 'Cor', 'Ano', 'Quilometragem']

# Lista aninhada
# Uma lista pode conter outras listas, conhecida como lista aninhada.

# Exemplo:

# Lista aninhada

pessoas = [
    ["João", 25],
    ["Maria", 30],        
    ["José", 40]
]

print(pessoas)  # Saída: [['João', 25], ['Maria', 30], ['José', 40]]

# Acessando os dados de uma lista aninhada

# Para acessar os dados de uma lista aninhada, usamos dois índices.

# Acessando o primeiro elemento da lista

print(pessoas[0])  # Saída: ['João', 25]

# Acessando o segundo elemento da lista

print(pessoas[1])  # Saída: ['Maria', 30]

# Acessando o primeiro elemento do primeiro elemento da lista

print(pessoas[0][0])  # Saída: João

# Acessando o segundo elemento do primeiro elemento da lista

print(pessoas[0][1])  # Saída: 25       
# Acessando o primeiro elemento do segundo elemento da lista

print(pessoas[1][0])  # Saída: Maria

# Acessando o segundo elemento do segundo elemento da lista

print(pessoas[1][1])  # Saída: 30   
# Acessando o primeiro elemento do terceiro elemento da lista       

print(pessoas[2][0])  # Saída: José

# Acessando o segundo elemento do terceiro elemento da lista

print(pessoas[2][1])  # Saída: 40

# Fatiamento em python
# O fatiamento em python é uma operação que permite acessar partes de uma sequência de dados.

# Exemplo:

# Fatiamento em python

frutas = ["banana", "maçã", "pera", "uva"]

# Acessando o primeiro elemento da lista

print(frutas[0])  # Saída: banana

# Acessando o intervalo de elementos da lista

print(frutas[1:3])  # Saída: ['maçã', 'pera']

# Acessando o intervalo de elementos da lista com passo

print(frutas[0:3:2])  # Saída: ['banana', 'pera']

# Acessando elementos da lista inverso

print(frutas[-1:-4:-1])  # Saída: ['uva', 'pera', 'maçã']

# Acessando elementos da lista com passo inverso

print(frutas[-1:0:-1])  # Saída: ['uva', 'maçã', 'pera', 'banana']
 
 # Listas são mutáveis

lista = [1, 2, 3, 4, 5]

print(lista)  # Saída: [1, 2, 3, 4, 5]

# Adicionando elementos a uma lista

lista.append(6)

print(lista)  # Saída: [1, 2, 3, 4, 5, 6]

# Inserindo elementos em uma lista

lista.insert(2, 7)

print(lista)  # Saída: [1, 2, 7, 3, 4, 5, 6]

# Removendo elementos de uma lista

lista.remove(2)

print(lista)  # Saída: [1, 7, 3, 4, 5, 6]

# Tamanho de uma lista

print(len(lista))  # Saída: 6

# Ordenando uma lista

lista.sort()

print(lista)  # Saída: [1, 3, 4, 5, 6, 7]

# Ordenando uma lista em ordem inversa

lista.reverse()

print(lista)  # Saída: [7, 6, 5, 4, 3, 1]

# Contando elementos em uma lista

print(lista.count(3))  # Saída: 1

# Verificando se um elemento está em uma lista

print(3 in lista)  # Saída: True

# Criando uma lista vazia

lista = []

print(lista)  # Saída: []

# Criando uma lista com valores iniciais

lista = [1, 2, 3, 4, 5]

print(lista)  # Saída: [1, 2, 3, 4, 5]

# Criando uma lista com valores iniciais usando a função list()

lista = list([1, 2, 3, 4, 5])    # O uso da função list() é opcional

print(lista)  # Saída: [1, 2, 3, 4, 5]  

for i in range(len(pessoas)):
    print(pessoas[i][0])  # Saída: João, Maria, José
    print(pessoas[i][1])  # Saída: 25, 30, 40   

# Compreensão de lista

# Uma lista pode ser criada usando a compreensão de lista.

# Exemplo:

# Compreensão de lista

lista = [x**2 for x in range(1, 6)]

print(lista)  # Saída: [1, 4, 9, 16, 25]

numeros = [1, 2, 3, 4, 5]

pares = [x for x in numeros if x % 2 == 0]

print(pares)  # Saída: [2, 4]

# Lista de tuplas

# Uma lista de tuplas é uma lista que contém vários valores, sendo que cada valor é uma tupla.

# Exemplo:

# Lista de tuplas

pessoas = [("João", 25), ("Maria", 30), ("José", 40)]

print(pessoas)  # Saída: [('João', 25), ('Maria', 30), ('José', 40)]

# Acessando os dados de uma lista de tuplas

# Para acessar os dados de uma lista de tuplas, usamos dois índices.

# Acessando o primeiro elemento da lista

print(pessoas[0])  # Saída: ('João', 25)

# Acessando o segundo elemento da lista

print(pessoas[1])  # Saída: ('Maria', 30)

# Acessando o primeiro elemento do primeiro elemento da lista

print(pessoas[0][0])  # Saída: João

# Acessando o segundo elemento do primeiro elemento da lista

print(pessoas[0][1])  # Saída: 25       

# Acessando o primeiro elemento do segundo elemento da lista

print(pessoas[1][0])  # Saída: Maria

# Acessando o segundo elemento do segundo elemento da lista

print(pessoas[1][1])  # Saída: 30   
# Acessando o primeiro elemento do terceiro elemento da lista       

print(pessoas[2][0])  # Saída: José

# Acessando o segundo elemento do terceiro elemento da lista

print(pessoas[2][1])  # Saída: 40

numeros = [1,30,21,2,9,65,34]
pares = []

for numeros in numeros:
    if numeros % 2 == 0:
        pares.append(numeros)

print(pares)  # Saída: [2, 21, 30, 64]

# O que é append() e insert() em Python?

# O método append() é usado para adicionar um elemento no final da lista.

# Exemplo:

# Usando o método append()

frutas = ["banana", "maçã", "pera", "uva"]

frutas.append("abacaxi")

print(frutas)  # Saída: ['banana', 'maçã', 'pera', 'uva', 'abacaxi']

# O método insert() é usado para inserir um elemento em uma posição específica da lista.

# Exemplo:

# Usando o método insert()

frutas = ["banana", "maçã", "pera", "uva"]

frutas.insert(1, "abacaxi")

print(frutas)  # Saída: ['banana', 'abacaxi', 'maçã', 'pera', 'uva']
# O que é remove() e pop() em Python?

# O método remove() é usado para remover o primeiro elemento de uma lista cujo valor é igual a um determinado valor.

# Exemplo:

# Usando o método remove()

frutas = ["banana", "maçã", "pera", "uva", "abacaxi"]

frutas.remove("maçã")

print(frutas)  # Saída: ['banana', 'pera', 'uva', 'abacaxi']

# O método pop() é usado para remover um elemento de uma lista pelo seu índice.

# Exemplo:

# Usando o método pop()

frutas = ["banana", "maçã", "pera", "uva", "abacaxi"]

frutas.pop(1)

print(frutas)  # Saída: ['banana', 'pera', 'uva', 'abacaxi']
# O que é sort() e reverse() em Python?

# O método sort() é usado para ordenar os elementos de uma lista em ordem crescente.

# Exemplo:

# Usando o método sort()

frutas = ["banana", "maçã", "pera", "uva", "abacaxi"]

frutas.sort()

print(frutas)  # Saída: ['abacaxi', 'banana', 'maçã', 'pera', 'uva']

# O método reverse() é usado para ordenar os elementos de uma lista em ordem decrescente.

# Exemplo:

# Usando o método reverse()

frutas = ["banana", "maçã", "pera", "uva", "abacaxi"]

frutas.reverse()

print(frutas)  # Saída: ['uva', 'pera', 'maçã', 'banana', 'abacaxi']
# O que é count() em Python?

# O método count() é usado para contar o número de ocorrências de um elemento em uma lista.

# Exemplo:

# Usando o método count()

frutas = ["banana", "maçã", "pera", "uva", "abacaxi"]

print(frutas.count("banana"))  # Saída: 1

# O que é in em Python?

# O operador in é usado para verificar se um elemento está em uma lista.

# Exemplo:

# Usando o operador in

frutas = ["banana", "maçã", "pera", "uva", "abacaxi"]

print("banana" in frutas)  # Saída: True

print("morango" in frutas)  # Saída: False

# O que é len() em Python?

# O método len() é usado para retornar o número de elementos em uma lista.

# Exemplo:

# Usando o método len()
frutas = ["banana", "maçã", "pera", "uva", "abacaxi"]

print(len(frutas))  # Saída: 5
# O que é list() em Python?

# O método list() é usado para criar uma lista a partir de outra coleção.

# Exemplo:

# Usando o método list()

tupla = (1, 2, 3, 4, 5)

lista = list(tupla)

print(lista)  # Saída: [1, 2, 3, 4, 5]
# O que é tuple() em Python?

# O método tuple() é usado para converter uma lista em tupla.

# Exemplo:

# Usando o método tuple()

lista = [1, 2, 3, 4, 5]

tupla = tuple(lista)

print(tupla)  # Saída: (1, 2, 3, 4, 5)  
# O que é set() em Python?

# O método set() é usado para criar um conjunto de elementos únicos.

# Exemplo:

# Usando o método set()

lista = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

conjunto = set(lista)

print(conjunto)  # Saída: {1, 2, 3, 4, 5}
# O que é frozenset() em Python?

# O método frozenset() é usado para criar um conjunto imutável de elementos únicos.

# Exemplo:

# Usando o método frozenset()

lista = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

conjunto = frozenset(lista)

print(conjunto)  # Saída: frozenset({1, 2, 3, 4, 5})    
# O que é dict() em Python?

# O método dict() é usado para criar um dicionário.

# Exemplo:

# Usando o método dict()

d = dict(a=1, b=2, c=3)

print(d)  # Saída: {'a': 1, 'b': 2, 'c': 3}
# O que é enumerate() em Python?

# O método enumerate() é usado para criar um iterador que retorna as posições e valores de um objeto iterável.

# Exemplo:

# Usando o método enumerate()

frutas = ["banana", "maçã", "pera", "uva", "abacaxi"]

for i, f in enumerate(frutas):
    print(i, f)  # Saída: 0 banana 1 maçã 2 pera 3 uva 4 abacaxi
    # O que é zip() em Python?

# O método zip() é usado para combinar elementos de iteráveis.

# Exemplo:

# Usando o método zip()

frutas = ["banana", "maçã", "pera", "uva", "abacaxi"]

numeros = [1, 2, 3, 4, 5]

for f, n in zip(frutas, numeros):
    print(f, n)  # Saída: banana 1 maçã 2 pera 3 uva 4 abacaxi
    # O que é reversed() em Python?
    # O método reversed() é usado para reverter a ordem de elementos em uma lista.

# Exemplo:

# Usando o método reversed()

frutas = ["banana", "maçã", "pera", "uva", "abacaxi"]

for f in reversed(frutas):
    print(f)  # Saída: abacaxi uva pera maçã banana
    # O que é sorted() em Python?
    # O método sorted() é usado para ordenar os elementos de uma lista.

# Exemplo:

# Usando o método sorted()  
frutas = ["banana", "maçã", "pera", "uva", "abacaxi"]

for f in sorted(frutas):
    print(f)  # Saída: abacaxi banana maçã pera uva 
    # O que é max() e min() em Python?
    # O método max() e min() são usados para encontrar o maior e menor valor em uma lista.

# Exemplo:

# Usando o método max()

numeros = [1, 2, 3, 4, 5]

print(max(numeros))  # Saída: 5

# Usando o método min()

print(min(numeros))  # Saída: 1 
# O que é sum() em Python?  
# O método sum() é usado para somar os elementos de uma lista.

# Exemplo:

# Usando o método sum()

numeros = [1, 2, 3, 4, 5]

print(sum(numeros))  # Saída: 15    
# O que é map() em Python?  
# O método map() é usado para aplicar uma função a cada elemento de uma lista.

# Exemplo:

# Usando o método map()

def dobro(x):
    return x * 2

numeros = [1, 2, 3, 4, 5]

dobros = list(map(dobro, numeros))

print(dobros)  # Saída: [2, 4, 6, 8, 10]
# O que é filter() em Python?  
# O método filter() é usado para filtrar os elementos de uma lista.

# Exemplo:

# Usando o método filter()

def par(x):
    return x % 2 == 0

numeros = [1, 2, 3, 4, 5]

pares = list(filter(par, numeros))

print(pares)  # Saída: [2, 4]   
# O que é reduce() em Python?  
# O método reduce() é usado para aplicar uma função cumulativa a uma lista.

# Exemplo:

# Usando o método reduce()

from functools import reduce

def soma(x, y):
    return x + y

numeros = [1, 2, 3, 4, 5]

soma = reduce(soma, numeros)

print(soma)  # Saída: 15
# O que é all() e any() em Python?  
# O método all() e any() são usados para verificar se todos os elementos de uma lista são verdadeiros ou se pelo menos um elemento é verdadeiro.

# Exemplo:  

# Usando o método all()

numeros = [1, 2, 3, 4, 5]

print(all(numeros))  # Saída: True

# Usando o método any()

numeros = [0, 0, 0, 0, 0]

print(any(numeros))  # Saída: False 
# O que é itertools em Python?  
# O módulo itertools é usado para criar iteradores e geradores.

# Exemplo:  

# Usando o módulo itertools

import itertools

numeros = [1, 2, 3, 4, 5]

pares = list(itertools.compress(numeros, [True, False, True, False, True]))

print(pares)  # Saída: [1, 3, 5]    
# O que é operator em Python?  
# O módulo operator é usado para operações comuns em iteráveis.

# Exemplo:  

# Usando o módulo operator

import operator

numeros = [1, 2, 3, 4, 5]   
soma = reduce(operator.add, numeros)    
print(soma)  # Saída: 15    
# O que é functools em Python?  
# O módulo functools é usado para funções e operadores de alto nível.

# Exemplo:  

# Usando o módulo functools

import functools

numeros = [1, 2, 3, 4, 5]

soma = functools.reduce(lambda x, y: x + y, numeros)

print(soma)  # Saída: 15    
# O que é heapq em Python?  
# O módulo heapq é usado para operações com filas de prioridade.

# Exemplo:  

# Usando o módulo heapq

import heapq

fila = [1, 3, 5, 7, 9]

heapq.heapify(fila)

print(fila)  # Saída: [1, 3, 5, 7, 9]

heapq.heappush(fila, 4)

print(fila)  # Saída: [1, 3, 4, 5, 7, 9]

heapq.heappop(fila)

print(fila)  # Saída: [3, 4, 5, 7, 9]   
# O que é bisect em Python?  
# O módulo bisect é usado para inserir elementos em uma lista ordenada.

# Exemplo:  

# Usando o módulo bisect

import bisect

numeros = [1, 3, 5, 7, 9]

bisect.insort(numeros, 4)

print(numeros)  # Saída: [1, 3, 4, 5, 7, 9]     
# O que é array em Python?  
# O módulo array é usado para criar arrays de dados.

# Exemplo:  

# Usando o módulo array

import array

a = array.array('i', [1, 2, 3, 4, 5])

print(a[1])  # Saída: 2    
# O que é struct em Python?  
# O módulo struct é usado para criar estruturas de dados.

# Exemplo:      

# Usando o módulo struct

import struct

data = struct.pack('i', 10)

print(data)  # Saída: b'\n\x00\x00\x00'
num = struct.unpack('i', data)[0]

print(num)  # Saída: 10 
# O que é os e os.path em Python?  
# O módulo os e os.path são usados para manipular caminhos de arquivos e diretórios.

# Exemplo:  

# Usando o módulo os

import os

print(os.getcwd())  # Saída: C:\Users\User\OneDrive\Desktop\Script Python\Trabalhando com coleções em Python\Lista de Python

os.chdir('..')

print(os.getcwd())  # Saída: C:\Users\User\OneDrive\Desktop\Script Python\Trabalhando com coleções em Python    
# O que é sys em Python?  
# O módulo sys é usado para interagir com o interpretador.

# Exemplo:  

# Usando o módulo sys

import sys

print(sys.argv)  # Saída: ['C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\python.exe', 'C:\\Users\\User\\OneDrive\\Desktop\\Script Python\\Trabalhando com coleções em Python\\Lista de Python\\Criação acesso aos dados.py']
quit()
# O que é time em Python?  
# O módulo time é usado para manipular datas e horas.

# Exemplo:  

# Usando o módulo time

import time

print(time.time())  # Saída: 1622629543.9391123    
# O que é datetime em Python?  
# O módulo datetime é usado para manipular datas e horas.

# Exemplo:      

# Usando o módulo datetime

import datetime

data = datetime.datetime.now()

print(data)  # Saída: 2021-06-01 16:59:03.939112
data = datetime.datetime.strptime('01/06/2021', '%d/%m/%Y')

print(data)  # Saída: 2021-06-01 00:00:00   
# O que é re em Python?  
# O módulo re é usado para manipular expressões regulares.

# Exemplo:  

# Usando o módulo re

import re

texto = 'Meu nome é João'

match = re.search('nome', texto)

print(match)  # Saída: <re.Match object; span=(8, 12), match='nome'>
match = re.findall('o', texto)

print(match)  # Saída: ['o', 'o']   
match = re.sub('o', 'a', texto)

print(match)  # Saída: 'Meu nama é Jaon'    
# O que é math em Python?  
# O módulo math é usado para operações matemáticas.

# Exemplo:  

# Usando o módulo math

import math

num = 3.14159265359

print(math.floor(num))  # Saída: 3
print(math.ceil(num))  # Saída: 4
print(math.sqrt(num))  # Saída: 1.7724538509055159  
num = 10

print(math.log(num))  # Saída: 2.302585092994046
print(math.exp(num))  # Saída: 22026.465794806718   
# O que é random em Python?  
# O módulo random é usado para gerar números aleatórios.    
# Exemplo:  

# Usando o módulo random

import random

num = random.randint(1, 10)

print(num)  # Saída: 7
num = random.random()

print(num)  # Saída: 0.47101522414434273]
# O que é statistics em Python?  
# O módulo statistics é usado para estatísticas.

# Exemplo:  

# Usando o módulo statistics

import statistics

numeros = [1, 2, 3, 4, 5]

media = statistics.mean(numeros)

print(media)  # Saída: 3.0
desvio = statistics.stdev(numeros)      

print(desvio)  # Saída: 1.4142135623730951  
# O que é functools em Python?  
# O módulo functools é usado para funções e operadores de alto nível.

# Exemplo:  

# Usando o módulo functools

import functools

numeros = [1, 2, 3, 4, 5]

soma = functools.reduce(lambda x, y: x + y, numeros)

print(soma)  # Saída: 15    
# O que é heapq em Python?  
# O módulo heapq é usado para operações com filas de prioridade.

# Exemplo:  

# Usando o módulo heapq

import heapq

fila = [1, 3, 5, 7, 9]

heapq.heapify(fila)

print(fila)  # Saída: [1, 3, 5, 7, 9]

heapq.heappush(fila, 4)

print(fila)  # Saída: [1, 3, 4, 5, 7, 9]

heapq.heappop(fila)

print(fila)  # Saída: [3, 4, 5, 7, 9]   

# O que é sorted em Python?  
# O método sorted() é usado para ordenar os elementos de uma lista.

# Exemplo:  

# Usando o método sorted()

frutas = ["banana", "maçã", "pera", "uva", "abacaxi"]

for f in sorted(frutas):
    print(f)  # Saída: abacaxi banana maçã pera uva 
# O que é itertools em Python?  
# O módulo itertools é usado para criar iteradores e geradores.

    # Exemplo:  

# Usando o módulo itertools

import itertools

numeros = [1, 2, 3, 4, 5]

pares = list(itertools.compress(numeros, [True, False, True, False, True]))

print(pares)  # Saída: [1, 3, 5]    
# O que é operator em Python?  
# O módulo operator é usado para operações comuns em iteráveis.

    # Exemplo:  

# Usando o módulo operator

import operator

numeros = [1, 2, 3, 4, 5]   
soma = reduce(operator.add, numeros)    
print(soma)  # Saída: 15    
# O que é functools em Python?  
# O módulo functools é usado para funções e operadores de alto nível.

    # Exemplo:  

    # Usando o módulo functools

import functools

numeros = [1, 2, 3, 4, 5]

soma = functools.reduce(lambda x, y: x + y, numeros)

print(soma)  # Saída: 15    
