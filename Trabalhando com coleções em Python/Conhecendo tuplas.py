# Conhecendo tuplas em Python

# Tuplas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura.

# Sintaxe

# Tuplas são definidas por parênteses () e separadas por vírgulas.

# Exemplos

tupla1 = (1, 2, 3, 4, 5)
tupla2 = ('a', 'b', 'c', 'd', 'e')
tupla3 = (True, False, True, False)

# Acessando elementos de uma tupla

# Podemos acessar elementos de uma tupla utilizando o índice.

# Exemplos

print(tupla1[0])  # 1
print(tupla2[1])  # 'b'
print(tupla3[2])  # True

# Tamanho de uma tupla

# Podemos obter o tamanho de uma tupla utilizando a função len().

# Exemplos

print(len(tupla1))  # 5
print(len(tupla2))  # 5
print(len(tupla3))  # 4

# Adicionando elementos em uma tupla

# Podemos adicionar elementos em uma tupla utilizando o método append().    

# Exemplos

tupla1 = (1, 2, 3, 4, 5)
tupla1.append(6)
print(tupla1)  # (1, 2, 3, 4, 5, 6)

# Removendo elementos de uma tupla

# Podemos remover elementos de uma tupla utilizando o método remove().

# Exemplos

tupla1 = (1, 2, 3, 4, 5)
tupla1.remove(3)
print(tupla1)  # (1, 2, 4, 5)

# Iterando sobre uma tupla

# Podemos iterar sobre uma tupla utilizando um laço for.

# Exemplos

tupla1 = (1, 2, 3, 4, 5)
for i in tupla1:
    print(i)

# Concatenando tuplas

# Podemos concatenar tuplas utilizando o operador +.

# Exemplos

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2
print(tupla3)  # (1, 2, 3, 4, 5, 6)

# Verificando se um elemento está em uma tupla

# Podemos verificar se um elemento está em uma tupla utilizando o método in.

# Exemplos  

tupla1 = (1, 2, 3, 4, 5)
print(3 in tupla1)  # True
print(6 in tupla1)  # False
# Ordenando uma tupla

# Podemos ordenar uma tupla utilizando o método sort().

# Exemplos

tupla1 = (5, 3, 1, 4, 2)
tupla1.sort()
print(tupla1)  # (1, 2, 3, 4, 5)    
# Funções aplicáveis a tuplas

# Podemos aplicar funções a tuplas utilizando o método map().

# Exemplos

tupla1 = (1, 2, 3, 4, 5)
tupla2 = tuple(map(lambda x: x*2, tupla1))
print(tupla2)  # (2, 4, 6, 8, 10)   
# Podemos converter uma lista em tupla utilizando o método tuple(). 

# Exemplos

lista1 = [1, 2, 3, 4, 5]
tupla1 = tuple(lista1)
print(tupla1)  # (1, 2, 3, 4, 5)

# Podemos converter uma tupla em lista utilizando o método list().

# Exemplos

tupla1 = (1, 2, 3, 4, 5)
lista1 = list(tupla1)
print(lista1)  # [1, 2, 3, 4, 5]    

# Podemos converter uma string em tupla utilizando o método tuple().

# Exemplos

string1 = 'abcde'
tupla1 = tuple(string1)
print(tupla1)  # ('a', 'b', 'c', 'd', 'e')

# Indices negativos

# Podemos acessar elementos de uma tupla utilizando índices negativos.

# Exemplos

tupla1 = (1, 2, 3, 4, 5)
print(tupla1[-1])  # 5
print(tupla1[-2])  # 4
print(tupla1[-3])  # 3
print(tupla1[-4])  # 2
print(tupla1[-5])  # 1
# Podemos usar índices negativos para alterar elementos de uma tupla.

# Exemplos

tupla1 = (1, 2, 3, 4, 5)
tupla1[-1] = 6
print(tupla1)  # (1, 2, 3, 4, 6)    

    # Tuplas aninhadas

# Tuplas podem conter outras tuplas.

# Exemplos

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = (tupla1, tupla2)
print(tupla3)  # ((1, 2, 3), (4, 5, 6))

    # Desempacotamento de tuplas

# Podemos desempacotar tuplas utilizando o operador *.

# Exemplos

tupla1 = (1, 2, 3)
a, b, c = tupla1
print(a)  # 1
print(b)  # 2
print(c)  # 3

# Podemos desempacotar tuplas em variáveis com nomes diferentes.

# Exemplos  

tupla1 = (1, 2, 3)
a, b, c = tupla1
d, e, f = (4, 5, 6)
print(a)  # 1
print(b)  # 2
print(c)  # 3
print(d)  # 4
print(e)  # 5
print(f)  # 6

# Fatiamento de tuplas

# Podemos fatiar tuplas utilizando o operador :.

# Exemplos

tupla1 = (1, 2, 3, 4, 5)    
tupla2 = tupla1[1:3]
print(tupla2)  # (2, 3)
tupla3 = tupla1[::2]
print(tupla3)  # (1, 3, 5)
tupla4 = tupla1[::-1]
print(tupla4)  # (5, 4, 3, 2, 1)
# Podemos utilizar o operador : para alterar elementos de uma tupla.

# Exemplos

tupla1 = (1, 2, 3, 4, 5)
tupla1[1:3] = (7, 8)
print(tupla1)  # (1, 7, 8, 4, 5)    

# conexão com mysql

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)      
  # conexão com sqlite3

import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute("SELECT * FROM customers")

result = cursor.fetchall()

for row in result:
  print(row)