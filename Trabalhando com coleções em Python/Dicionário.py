# Aprendendo a utilizar dicionários em Python

# Como usar o dicionario em Python?
# Dicionários são coleções de chave-valor, onde a chave é o identificador do valor e o valor é o conteúdo.
# Dicionários são representados por chaves {} e separados por dois pontos :.
# Cada chave e valor é separado por uma vírgula.
# Dicionários são mutáveis, isto é, podemos adicionar, modificar ou excluir chaves e valores.
# Dicionários são indexados por chaves, que são únicas.
# Dicionários são iteráveis, isto é, podemos usar loops para percorrer as chaves e valores. 
   #Exemplo: for chave, valor in dicionario.items():
       #print(chave, valor)
# Como criar um dicionário em Python?
# Para criar um dicionário em Python, usamos chaves {} e separamos as chaves e valores por dois pontos :.
# Exemplo: dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
# Aqui, 'chave1' e 'chave2' são as chaves e 'valor1' e 'valor2' são os valores.
 
dados = {'nome': 'John', 'idade': 30, 'cidade': 'New York'}
print(dados)

dados = {'nome': 'John', 'idade': 30, 'cidade': 'New York', 'estado': 'California'}
print(dados)
# Acessando os valores de um dicionário
print(dados['nome'])
print(dados['idade'])
print(dados['cidade'])

# Adicionando chave-valor em um dicionário
dados['estado'] = 'São Paulo'
print(dados)
print(dados['estado'])

# Acessando o valor de uma chave em um dicionário
print(dados['estado'])  



# Criando um dicionário com chaves e valores iniciais
dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}

# Criando um dicionário vazio
dicionario = {}

# Adicionando chave-valor em um dicionário
dicionario['chave1'] = 'valor1'
dicionario['chave2'] = 'valor2'

# Acessando o valor de uma chave em um dicionário
print(dicionario['chave1'])

    # Criando um dicionário com chaves e valores iniciais
dicionario2 = {'chave1': 'valor1', 'chave2': 'valor2'}

# Acessando o valor de uma chave em um dicionário
print(dicionario2['chave1'])

# Adicionando chave-valor em um dicionário
dicionario2['chave3'] = 'valor3'

# Acessando o valor de uma chave em um dicionário
print(dicionario2['chave3'])

# Acessando todas as chaves de um dicionário
print(dicionario2.keys())

# Acessando todos os valores de um dicionário
print(dicionario2.values())

# Acessando todos os itens de um dicionário
print(dicionario2.items())

# Atualizando o valor de uma chave em um dicionário
dicionario2['chave1'] = 'novo_valor1'

# Acessando o valor de uma chave em um dicionário
print(dicionario2['chave1'])

# Deletando uma chave-valor de um dicionário
del dicionario2['chave2']

# Acessando o valor de uma chave em um dicionário
print(dicionario2['chave2'])     # KeyError: 'chave2'   

# Deletando um dicionário
del dicionario2

# Acessando o valor de uma chave em um dicionário
print(dicionario2['chave1'])     # NameError: name 'dicionario2' is not defined 

# Criando um dicionário com itens de uma lista
lista = ['chave1', 'valor1', 'chave2', 'valor2']
dicionario3 = dict(zip(lista[::2], lista[1::2]))

# Acessando o valor de uma chave em um dicionário
print(dicionario3['chave1'])    

# Acessando todas as chaves de um dicionário
print(dicionario3.keys())   

# Acessando todos os valores de um dicionário
print(dicionario3.values()) 

# Acessando todos os itens de um dicionário
print(dicionario3.items()) 

# Atualizando o valor de uma chave em um dicionário
dicionario3['chave1'] = 'novo_valor1'

# Acessando o valor de uma chave em um dicionário
print(dicionario3['chave1'])    

# Deletando uma chave-valor de um dicionário
del dicionario3['chave2']

# Acessando o valor de uma chave em um dicionário
print(dicionario3['chave2'])     # KeyError: 'chave2'   

# Deletando um dicionário
del dicionario3

# Acessando o valor de uma chave em um dicionário
print(dicionario3['chave1'])     # NameError: name 'dicionario3' is not defined 

# Criando um dicionário com itens de uma tupla
tupla = ('chave1', 'valor1', 'chave2', 'valor2')
dicionario4 = dict(zip(tupla[::2], tupla[1::2]))

# Acessando o valor de uma chave em um dicionário
print(dicionario4['chave1'])    

# Acessando todas as chaves de um dicionário
print(dicionario4.keys())   

# Acessando todos os valores de um dicionário
print(dicionario4.values()) 

# Acessando todos os itens de um dicionário
print(dicionario4.items()) 

# Dicionário aninhados
# Dicionários podem conter outros dicionários, que são chamados de dicionários aninhados.
# Exemplo:

# Criando um dicionário aninhado
dicionario_aninhado = {'chave1': {'chave2': 'valor2', 'chave3': 'valor3'}, 'chave4': {'chave5': 'valor5', 'chave6': 'valor6'}}

# Acessando o valor de uma chave em um dicionário aninhado
print(dicionario_aninhado['chave1']['chave2'])

# Acessando todas as chaves de um dicionário aninhado
print(dicionario_aninhado.keys())

# Acessando todos os valores de um dicionário aninhado
print(dicionario_aninhado.values())

# Acessando todos os itens de um dicionário aninhado
print(dicionario_aninhado.items())

# Acessando o valor de uma chave em um dicionário aninhado
print(dicionario_aninhado['chave1']['chave2'])

# Dicionários são mutáveis, isto é, podemos adicionar, modificar ou excluir chaves e valores.
# Exemplo:  

# Adicionando chave-valor em um dicionário
dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
dicionario['chave3'] = 'valor3'

# Acessando o valor de uma chave em um dicionário
print(dicionario['chave3'])

# Atualizando o valor de uma chave em um dicionário
dicionario['chave1'] = 'novo_valor1'

# Acessando o valor de uma chave em um dicionário
print(dicionario['chave1'])

# Deletando uma chave-valor de um dicionário
del dicionario['chave2']

# Acessando o valor de uma chave em um dicionário
print(dicionario['chave2'])     # KeyError: 'chave2'   

# Deletando um dicionário
del dicionario

# Acessando o valor de uma chave em um dicionário
print(dicionario['chave1'])     # NameError: name 'dicionario' is not defined 

# Dicionários são indexados por chaves, que são únicas.
# Exemplo:

# Criando um dicionário
dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}

# Acessando o valor de uma chave em um dicionário
print(dicionario['chave1'])

# Dicionários são iteráveis, isto é, podemos usar loops para percorrer as chaves e valores. 
# Exemplo:

# Criando um dicionário
dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}

# Percorrendo as chaves e valores de um dicionário
for chave, valor in dicionario.items():
    print(chave, valor) 

# Acessando o valor de uma chave em um dicionário
print(dicionario['chave1']) 

# Dicionários são mutáveis, isto é, podemos adicionar, modificar ou excluir chaves e valores.
# Exemplo:

# Adicionando chave-valor em um dicionário
dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
dicionario['chave3'] = 'valor3'

# Acessando o valor de uma chave em um dicionário
print(dicionario['chave3'])

# Atualizando o valor de uma chave em um dicionário
dicionario['chave1'] = 'novo_valor1'

# Acessando o valor de uma chave em um dicionário
print(dicionario['chave1'])

# Deletando uma chave-valor de um dicionário
del dicionario['chave2']

# Acessando o valor de uma chave em um dicionário
print(dicionario['chave2'])     # KeyError: 'chave2'   

# Deletando um dicionário
del dicionario

# Acessando o valor de uma chave em um dicionário
print(dicionario['chave1'])     # NameError: name 'dicionario' is not defined 

# Interagindo com dicionários com for
# Podemos interagir com dicionários com for, para percorrer as chaves e valores.
# Exemplo:

# Criando um dicionário
dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}

# Percorrendo as chaves e valores de um dicionário
for chave in dicionario:
    print(chave, dicionario[chave]) 

# Acessando o valor de uma chave em um dicionário
print(dicionario['chave1']) 

# Interagindo com dicionários com while
# Podemos interagir com dicionários com while, para percorrer as chaves e valores.
# Exemplo:

# Criando um dicionário
dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}

# Percorrendo as chaves e valores de um dicionário
i = 0
while i < len(dicionario):
    chave = list(dicionario.keys())[i]
    valor = dicionario[chave]   
    print(chave, valor) 
    i += 1 

# Acessando o valor de uma chave em um dicionário
print(dicionario['chave1']) 

