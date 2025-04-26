# Listas em Python
# O que são listas em Python?

# Listas em Python são variáveis compostas que permitem armazenar vários valores em uma única estrutura.
# As listas são definidas por colchetes [] e os valores são separados por vírgulas.
# Exemplos de listas em Python:

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Lista de strings
frutas = ["banana", "laranja", "uva"]

# Lista de booleanos
verdadeiros = [True, True, False]

# Lista de listas
matrizes = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Como acessar elementos de uma lista?

# Para acessar um elemento específico de uma lista, basta usar o índice do elemento entre colchetes [].
# O primeiro elemento de uma lista tem índice 0, o segundo elemento tem índice 1, e assim por diante.

# Exemplo:

# Acessando o primeiro elemento de uma lista
frutas = ["banana", "laranja", "uva"]
print(frutas[0])  # Saída: "banana"

# Acessando o último elemento de uma lista
numeros = [1, 2, 3, 4, 5]
print(numeros[-1])  # Saída: 5

# Como modificar elementos de uma lista?

# Para modificar um elemento específico de uma lista, basta atribuir um novo valor a ele.
# O índice do elemento a ser modificado deve ser especificado entre colchetes [].

# Exemplo:

# Modificando o primeiro elemento de uma lista
frutas = ["banana", "laranja", "uva"]
frutas[0] = "abacaxi"
print(frutas)  # Saída: ["abacaxi", "laranja", "uva"]

# Como adicionar elementos a uma lista?

# Para adicionar um elemento a uma lista, basta usar a função append().
# Essa função adiciona o elemento ao final da lista.    

# Exemplo:

# Adicionando um elemento a uma lista
frutas = ["banana", "laranja", "uva"]
frutas.append("morango")
print(frutas)  # Saída: ["banana", "laranja", "uva", "morango"]

# Como remover elementos de uma lista?

# Para remover um elemento de uma lista, basta usar a função remove().
# Essa função remove o primeiro elemento encontrado que corresponde ao valor passado como argumento.

# Exemplo:

# Removendo um elemento de uma lista
frutas = ["banana", "laranja", "uva", "morango"]
frutas.remove("uva")
print(frutas)  # Saída: ["banana", "laranja", "morango"]

# Como ordenar uma lista?

# Para ordenar uma lista, basta usar a função sort().
# Essa função ordena a lista em ordem crescente.

# Exemplo:

# Ordenando uma lista
numeros = [5, 3, 1, 4, 2]
numeros.sort()
print(numeros)  # Saída: [1, 2, 3, 4, 5]

# Como inverter a ordem de uma lista?

# Para inverter a ordem de uma lista, basta usar a função reverse().
# Essa função inverte a ordem dos elementos da lista.

# Exemplo:

# Invertendo a ordem de uma lista
numeros = [5, 3, 1, 4, 2]
numeros.reverse()
print(numeros)  # Saída: [2, 4, 1, 3, 5]    

# Como contar o número de ocorrências de um valor em uma lista?

# Para contar o número de ocorrências de um valor em uma lista, basta usar a função count().
# Essa função retorna o número de vezes que o valor passado como argumento aparece na lista.

# Exemplo:

# Contando o número de ocorrências de um valor em uma lista
numeros = [5, 3, 1, 4, 2, 5]
print(numeros.count(5))  # Saída: 2    

# Como concatenar listas?

# Para concatenar listas, basta usar o operador +.
# Esse operador concatena as duas listas em uma única lista.

# Exemplo:

# Concatenando listas
numeros1 = [1, 2, 3]
numeros2 = [4, 5, 6]
numeros3 = numeros1 + numeros2
print(numeros3)  # Saída: [1, 2, 3, 4, 5, 6]

# Como copiar uma lista?

# Para copiar uma lista, basta usar a função copy().
# Essa função cria uma cópia da lista original.

# Exemplo:

# Copiando uma lista
numeros = [1, 2, 3]
numeros_copia = numeros.copy()
print(numeros_copia)  # Saída: [1, 2, 3]

# como verificar se um valor está em uma lista?

# Para verificar se um valor está em uma lista, basta usar a função in.
# Essa função retorna True se o valor estiver na lista, False caso contrário.

# Exemplo:

# Verificando se um valor está em uma lista
numeros = [1, 2, 3]
print(5 in numeros)  # Saída: False
print(2 in numeros)  # Saída: True

# Como iterar sobre uma lista?

# Para iterar sobre uma lista, basta usar um laço for.
# O laço for itera sobre os elementos da lista e executa uma instrução para cada elemento.

# Exemplo:

# Iterando sobre uma lista
numeros = [1, 2, 3]
for numero in numeros:
    print(numero)  # Saída: 1 2 3   

    # como converter uma lista em uma string?

# Para converter uma lista em uma string, basta usar a função join().
# Essa função concatena os elementos da lista com o separador passado como argumento.   
# Exemplo:

# Convertendo uma lista em uma string
numeros = [1, 2, 3]
string = ", ".join(str(x) for x in numeros)
print(string)  # Saída: "1, 2, 3"

# Como obter o tamanho de uma lista?

# Para obter o tamanho de uma lista, basta usar a função len().
# Essa função retorna o número de elementos da lista.

# Exemplo:  
# Obtendo o tamanho de uma lista
numeros = [1, 2, 3]
print(len(numeros))  # Saída: 3 


# Como obter o maior e o menor valor de uma lista?

# Para obter o maior e o menor valor de uma lista, basta usar as funções max() e min().
# Essas funções retornam o maior e o menor valor da lista, respectivamente.

# Exemplo:

# Obtendo o maior e o menor valor de uma lista
numeros = [5, 3, 1, 4, 2]
print(max(numeros))  # Saída: 5
print(min(numeros))  # Saída: 1 

# Como obter a soma de todos os elementos de uma lista?

# Para obter a soma de todos os elementos de uma lista, basta usar a função sum().
# Essa função retorna a soma de todos os elementos da lista.

# Exemplo:

# Obtendo a soma de todos os elementos de uma lista
numeros = [5, 3, 1, 4, 2]
print(sum(numeros))  # Saída: 15 

# Como obter a média aritmética de uma lista?

# Para obter a média aritmética de uma lista, basta calcular a soma de todos os elementos e dividir pelo número de elementos.

# Exemplo:

# Obtendo a média aritmética de uma lista
numeros = [5, 3, 1, 4, 2]
media = sum(numeros) / len(numeros)
print(media)  # Saída: 3.0 

# Como obter o índice de um elemento em uma lista?

# Para obter o índice de um elemento em uma lista, basta usar a função index().
# Essa função retorna o índice do primeiro elemento encontrado que corresponde ao valor passado como argumento.

# Exemplo:

# Obtendo o índice de um elemento em uma lista
numeros = [5, 3, 1, 4, 2]
print(numeros.index(3))  # Saída: 1 

# Como obter os elementos de uma lista em ordem inversa?

# Para obter os elementos de uma lista em ordem inversa, basta usar a função reversed().
# Essa função retorna um iterável que itera sobre os elementos da lista em ordem inversa.

# Exemplo:

# Obtendo os elementos de uma lista em ordem inversa
numeros = [5, 3, 1, 4, 2]
for numero in reversed(numeros):
    print(numero)  # Saída: 2 4 1 3 5 

# Como obter os elementos de uma lista que satisfazem uma condição?

# Para obter os elementos de uma lista que satisfazem uma condição, basta usar a função filter().
# Essa função retorna um iterável que itera sobre os elementos da lista que satisfazem a condição.

# Exemplo:

# Obtendo os elementos de uma lista que satisfazem uma condição
numeros = [5, 3, 1, 4, 2]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [5, 3, 1, 4] 

# Como obter os elementos de uma lista que não satisfazem uma condição?

# Para obter os elementos de uma lista que não satisfazem uma condição, basta usar a função filter() com a função negada.
# Essa função retorna um iterável que itera sobre os elementos da lista que não satisfazem a condição.

# Exemplo:

# Obtendo os elementos de uma lista que não satisfazem uma condição
numeros = [5, 3, 1, 4, 2]
impares = list(filter(lambda x: x % 2 == 1, numeros))
print(impares)  # Saída: [2] 

# Como obter os elementos de uma lista que estão em um intervalo?

# Para obter os elementos de uma lista que estão em um intervalo, basta usar a função range() e a função filter().
# Essa função retorna um iterável que itera sobre os elementos da lista que estão no intervalo.

# Exemplo:

# Obtendo os elementos de uma lista que estão em um intervalo
numeros = [5, 3, 1, 4, 2]
intervalo = list(filter(lambda x: 2 < x < 4, numeros))
print(intervalo)  # Saída: [3, 1] 

# Como obter os elementos de uma lista que estão em uma lista de valores?

# Para obter os elementos de uma lista que estão em uma lista de valores, basta usar a função filter().
# Essa função retorna um iterável que itera sobre os elementos da lista que estão na lista de valores.

# Exemplo:

# Obtendo os elementos de uma lista que estão em uma lista de valores
numeros = [5, 3, 1, 4, 2]
valores = [3, 1]
lista_valores = list(filter(lambda x: x in valores, numeros))
print(lista_valores)  # Saída: [3, 1] 

# Como obter os elementos de uma lista que não estão em uma lista de valores?

# Para obter os elementos de uma lista que não estão em uma lista de valores, basta usar a função filter() com a função negada.
# Essa função retorna um iterável que itera sobre os elementos da lista que não estão na lista de valores.

# Exemplo:

# Obtendo os elementos de uma lista que não estão em uma lista de valores
numeros = [5, 3, 1, 4, 2]
valores = [3, 1]
nao_valores = list(filter(lambda x: x not in valores, numeros))
print(nao_valores)  # Saída: [5, 4, 2] 

# Como obter os elementos de uma lista que estão em uma faixa de valores?

# Para obter os elementos de uma lista que estão em uma faixa de valores, basta usar a função range() e a função filter().
# Essa função retorna um iterável que itera sobre os elementos da lista que estão na faixa de valores.

# Exemplo:

# Obtendo os elementos de uma lista que estão em uma faixa de valores
numeros = [5, 3, 1, 4, 2]
faixa = list(filter(lambda x: 2 < x < 4, numeros))
print(faixa)  # Saída: [3, 1] 

# Como obter os elementos de uma lista que não estão em uma faixa de valores?

# Para obter os elementos de uma lista que não estão em uma faixa de valores, basta usar a função filter() com a função negada.
# Essa função retorna um iterável que itera sobre os elementos da lista que não estão na faixa de valores.

# Exemplo:

# Obtendo os elementos de uma lista que não estão em uma faixa de valores
numeros = [5, 3, 1, 4, 2]
faixa = list(filter(lambda x: 2 < x < 4, numeros))
nao_faixa = list(filter(lambda x: x not in faixa, numeros))
print(nao_faixa)  # Saída: [5, 4, 2] 

# Como obter os elementos de uma lista que estão em uma faixa de valores e que não estão em uma lista de valores?

# Para obter os elementos de uma lista que estão em uma faixa de valores e que não estão em uma lista de valores, basta usar a função filter() com a função negada.
# Essa função retorna um iterável que itera sobre os elementos da lista que estão na faixa de valores e que não estão na lista de valores.

# Exemplo:

# Obtendo os elementos de uma lista que estão em uma faixa de valores e que não estão em uma lista de valores
numeros = [5, 3, 1, 4, 2]
faixa = list(filter(lambda x: 2 < x < 4, numeros))
valores = [3, 1]
faixa_nao_valores = list(filter(lambda x: x not in valores and x in faixa, numeros))
print(faixa_nao_valores)  # Saída: [1] 

# Como obter os elementos de uma lista que estão em uma faixa de valores e que não estão em uma faixa de valores?

# Para obter os elementos de uma lista que estão em uma faixa de valores e que não estão em uma faixa de valores, basta usar a função filter() com a função negada.
# Essa função retorna um iterável que itera sobre os elementos da lista que estão na faixa de valores e que não estão na faixa de valores.

# Exemplo:

# Obtendo os elementos de uma lista que estão em uma faixa de valores e que não estão em uma faixa de valores
numeros = [5, 3, 1, 4, 2]
faixa = list(filter(lambda x: 2 < x < 4, numeros))
faixa_nao_faixa = list(filter(lambda x: x not in faixa, numeros))
print(faixa_nao_faixa)  # Saída: [5, 4, 2] 

# Como ordenar uma lista?

# Para ordenar uma lista, basta usar a função sorted().
# Essa função retorna uma nova lista com os elementos da lista original ordenados.

# Exemplo:

# Ordenando uma lista
numeros = [5, 3, 1, 4, 2]
numeros_ordenados = sorted(numeros)
print(numeros_ordenados)  # Saída: [1, 2, 3, 4, 5] 

# Como ordenar uma lista em ordem inversa?

# Para ordenar uma lista em ordem inversa, basta usar a função sorted() com a opção reverse=True.
# Essa opção ordena a lista em ordem inversa.

# Exemplo:

# Ordenando uma lista em ordem inversa
numeros = [5, 3, 1, 4, 2]
numeros_ordenados_inverso = sorted(numeros, reverse=True)
print(numeros_ordenados_inverso)  # Saída: [5, 4, 3, 2, 1] 

# Como ordenar uma lista por uma chave?

# Para ordenar uma lista por uma chave, basta usar a função sorted() com a chave como argumento.
# Essa chave é uma função que retorna um valor que será usado para ordenar a lista.

# Exemplo:

# Ordenando uma lista por uma chave
numeros = [5, 3, 1, 4, 2]
numeros_ordenados_por_nome = sorted(numeros, key=lambda x: "abcde"[x-1])
print(numeros_ordenados_por_nome)  # Saída: [1, 2, 3, 4, 5] 

# Como ordenar uma lista por uma chave em ordem inversa?

# Para ordenar uma lista por uma chave em ordem inversa, basta usar a função sorted() com a chave e a opção reverse=True.
# Essa opção ordena a lista por uma chave em ordem inversa.

# Exemplo:

# Ordenando uma lista por uma chave em ordem inversa
numeros = [5, 3, 1, 4, 2]
numeros_ordenados_por_nome_inverso = sorted(numeros, key=lambda x: "abcde"[x-1], reverse=True)
print(numeros_ordenados_por_nome_inverso)  # Saída: [5, 4, 3, 2, 1] 

# Como remover um elemento de uma lista?

# Para remover um elemento de uma lista, basta usar a função remove().
# Essa função remove o primeiro elemento da lista que corresponde ao valor passado como argumento.

# Exemplo:

# Removendo um elemento de uma lista
numeros = [5, 3, 1, 4, 2]
numeros.remove(3)
print(numeros)  # Saída: [5, 1, 4, 2] 

# Como remover todos os elementos de uma lista?

# Para remover todos os elementos de uma lista, basta usar a função clear().
# Essa função remove todos os elementos da lista.

# Exemplo:

# Removendo todos os elementos de uma lista
numeros = [5, 3, 1, 4, 2]
numeros.clear()
print(numeros)  # Saída: [] 

# Como remover os elementos de uma lista que satisfazem uma condição?

# Para remover os elementos de uma lista que satisfazem uma condição, basta usar a função filter() com a função negada.
# Essa função remove os elementos da lista que satisfazem a condição.

# Exemplo:

# Removendo os elementos de uma lista que satisfazem uma condição    
numeros = [5, 3, 1, 4, 2]
numeros = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros)  # Saída: [5, 3, 1, 4] 
numeros = list(filter(lambda x: x % 2 == 1, numeros))
print(numeros)  # Saída: []  

# Como remover os elementos de uma lista que não estão em uma lista de valores?

# Para remover os elementos de uma lista que não estão em uma lista de valores, basta usar a função filter() com a função negada.
# Essa função remove os elementos da lista que não estão na lista de valores.

# Exemplo:

# Removendo os elementos de uma lista que não estão em uma lista de valores
numeros = [5, 3, 1, 4, 2]
valores = [3, 1]
numeros = list(filter(lambda x: x not in valores, numeros))
print(numeros)  # Saída: [5, 4, 2] 

# Como remover os elementos de uma lista que estão em uma faixa de valores?

# Para remover os elementos de uma lista que estão em uma faixa de valores, basta usar a função filter() com a função negada.
# Essa função remove os elementos da lista que estão na faixa de valores.

# Exemplo:

# Removendo os elementos de uma lista que estão em uma faixa de valores
numeros = [5, 3, 1, 4, 2]
faixa = list(filter(lambda x: 2 < x < 4, numeros))
numeros = list(filter(lambda x: x not in faixa, numeros))
print(numeros)  # Saída: [5, 4, 2] 

# Como remover os elementos de uma lista que estão em uma faixa de valores e que não estão em uma lista de valores?

# Para remover os elementos de uma lista que estão em uma faixa de valores e que não estão em uma lista de valores, basta usar a função filter() com a função negada.
# Essa função remove os elementos da lista que estão na faixa de valores e que não estão na lista de valores.

# Exemplo:

# Removendo os elementos de uma lista que estão em uma faixa de valores e que não estão em uma lista de valores
numeros = [5, 3, 1, 4, 2]
faixa = list(filter(lambda x: 2 < x < 4, numeros))
valores = [3, 1]
numeros = list(filter(lambda x: x not in valores and x not in faixa, numeros))
print(numeros)  # Saída: [5, 4, 2]  
# Como inserir um elemento em uma lista?

# Para inserir um elemento em uma lista, basta usar a função insert().
# Essa função insere o elemento no índice especificado.

# Exemplo:

# Inserindo um elemento em uma lista
numeros = [5, 3, 1, 4, 2]
numeros.insert(2, 6)
print(numeros)  # Saída: [5, 3, 6, 1, 4, 2] 

# Como inserir vários elementos em uma lista?

# Para inserir vários elementos em uma lista, basta usar a função extend().
# Essa função insere os elementos no final da lista.

# Exemplo:

# Inserindo vários elementos em uma lista
numeros = [5, 3, 1, 4, 2]
numeros.extend([7, 8, 9])
print(numeros)  # Saída: [5, 3, 1, 4, 2, 7, 8, 9]  

# Como concatenar duas listas?

# Para concatenar duas listas, basta usar a função +.
# Essa função retorna uma nova lista que contém os elementos das duas listas.

# Exemplo:

# Concatenando duas listas
numeros1 = [5, 3, 1, 4, 2]
numeros2 = [7, 8, 9]
numeros3 = numeros1 + numeros2
print(numeros3)  # Saída: [5, 3, 1, 4, 2, 7, 8, 9] 

# Como contar o número de ocorrências de um elemento em uma lista?

# Para contar o número de ocorrências de um elemento em uma lista, basta usar a função count().
# Essa função retorna o número de ocorrências do elemento na lista.

# Exemplo:

# Contando o número de ocorrências de um elemento em uma lista
numeros = [5, 3, 1, 4, 2, 5, 3, 1, 4, 2]
contagem = numeros.count(5)
print(contagem)  # Saída: 2 

# Como verificar se um elemento está em uma lista?

# Para verificar se um elemento está em uma lista, basta usar a função in.
# Essa função retorna True se o elemento está na lista, False caso contrário.

# Exemplo:

# Verificando se um elemento está em uma lista
numeros = [5, 3, 1, 4, 2]
if 3 in numeros:
    print("O elemento está na lista")
else:
    print("O elemento não está na lista")  # Saída: O elemento está na lista 

# Como verificar se todos os elementos de uma lista estão em outra lista?

# Para verificar se todos os elementos de uma lista estão em outra lista, basta usar a função all() com a função in.
# Essa função retorna True se todos os elementos estão na lista, False caso contrário.

# Exemplo:

# Verificando se todos os elementos de uma lista estão em outra lista
numeros1 = [5, 3, 1, 4, 2]
numeros2 = [3, 1, 5]
if numeros1.all(lambda x: x in numeros2):
    print("Todos os elementos estão na lista")
else:
    print("Todos os elementos não estão na lista")  # Saída: Todos os elementos estão na lista 

# Como verificar se algum dos elementos de uma lista estão em outra lista?

# Para verificar se algum dos elementos de uma lista estão em outra lista, basta usar a função any() com a função in.
# Essa função retorna True se algum dos elementos estão na lista, False caso contrário.

# Exemplo:

# Verificando se algum dos elementos de uma lista estão em outra lista
numeros1 = [5, 3, 1, 4, 2]
numeros2 = [3, 1, 5]
if numeros1.any(lambda x: x in numeros2):
    print("Algum dos elementos está na lista")
else:
    print("Nenhum dos elementos está na lista")  # Saída: Algum dos elementos está na lista 

# Como converter uma lista em uma string?

# Para converter uma lista em uma string, basta usar a função join().
# Essa função retorna uma string que contém os elementos da lista separados pelo separador passado como argumento.

# Exemplo:

# Convertendo uma lista em uma string
numeros = [5, 3, 1, 4, 2]
string = ", ".join(map(str, numeros))
print(string)  # Saída: "5, 3, 1, 4, 2" 

# Como converter uma string em uma lista?

# Para converter uma string em uma lista, basta usar a função split().
# Essa função retorna uma lista que contém os elementos da string separados pelo separador passado como argumento.

# Exemplo:

# Convertendo uma string em uma lista
string = "5, 3, 1, 4, 2"
numeros = string.split(", ")
print(numeros)  # Saída: ['5', '3', '1', '4', '2'] 

# Como converter uma lista de strings em uma lista de números?

# Para converter uma lista de strings em uma lista de números, basta usar a função map() com a função int.
# Essa função retorna um iterável que itera sobre os elementos da lista de strings e converte cada elemento em um número inteiro.

# Exemplo:

# Convertendo uma lista de strings em uma lista de números
strings = ["5", "3", "1", "4", "2"]
numeros = list(map(int, strings))
print(numeros)  # Saída: [5, 3, 1, 4, 2] 
