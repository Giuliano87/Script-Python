# Métodos da classe list
# append() - Adiciona um item ao final da lista.
# clear() - Remove todos os itens da lista.
# copy() - Retorna uma cópia da lista.
# count() - Retorna o número de ocorrências de um item na lista.
# extend() - Adiciona itens de outra lista ao final da lista.
# index() - Retorna o índice de um item na lista.
# insert() - Insere um item em uma posição específica da lista.
# pop() - Remove e retorna um item da lista.
# remove() - Remove um item da lista.
# reverse() - Inverte a ordem dos itens na lista.
# sort() - Ordena os itens na lista.
# Exemplos:

# Exemplo 1:

lista = []

lista.append(1)
lista.append("Python")
lista.append[40, 30,20]

print(lista)     # [1, 'Python', [40, 30, 20]]

# Exemplo 2:

lista = [1, 2, 3, 4, 5]

lista.clear()

print(lista)     # []

# Exemplo 3:

lista1 = [1, 2, 3, 4, 5]

lista2 = lista1.copy()

print(lista2)    # [1, 2, 3, 4, 5]

# Exemplo 4:

lista = [1, 2, 3, 4, 5, 2, 3]

print(lista.count(2))    # 2

# Exemplo 5:

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista1.extend(lista2)

print(lista1)    # [1, 2, 3, 4, 5, 6]

# Exemplo 6:

lista = [1, 2, 3, 4, 5]

print(lista.index(3))    # 2

# Exemplo 7:

lista = [1, 2, 3, 4, 5]

lista.insert(2, 10)

print(lista)    # [1, 2, 10, 3, 4, 5]

# Exemplo 8:

lista = [1, 2, 3, 4, 5]

print(lista.pop())    # 5

print(lista)    # [1, 2, 3, 4]

# Exemplo 9:

lista = [1, 2, 3, 4, 5]

lista.remove(3)

print(lista)    # [1, 2, 4, 5]

# Exemplo 10:

lista = [1, 2, 3, 4, 5]

lista.reverse()

print(lista)    # [5, 4, 3, 2, 1]

# Exemplo 11:

lista = [5, 2, 4, 1, 3]

lista.sort()

print(lista)    # [1, 2, 3, 4, 5]   

# Exemplo 12:

lista = [1, 2, 3, 4, 5]

print(len(lista))    # 5    

# Exemplo 13:

lista = [1, 2, 3, 4, 5]

print(max(lista))    # 5

# Exemplo 14:

lista = [1, 2, 3, 4, 5]

print(min(lista))    # 1

# Exemplo 15:

lista = [1, 2, 3, 4, 5]

print(sum(lista))    # 15   

# Exemplo 16:

lista = [1, 2, 3, 4, 5]

print(lista.pop(2))    # 3

print(lista)    # [1, 2, 4, 5]  

# Exemplo 17:

lista = [1, 2, 3, 4, 5]

print(lista.index(3, 2))    # 2  

# Exemplo 18:

lista = [1, 2, 3, 4, 5]     

print(lista.count(2, 2, 4))    # 1  

# Exemplo 19:   

lista = [1, 2, 3, 4, 5]

print(lista.reverse())    # None  

# Exemplo 20:

lista = [1, 2, 3, 4, 5]

print(lista.sort())    # None   

# Exemplo 21:

lista = [1, 2, 3, 4, 5]

print(len(lista))    # 5     

# Exemplo 22:

lista = [1, 2, 3, 4, 5]

print(max(lista))    # 5    

# Exemplo 23:

lista = [1, 2, 3, 4, 5]

print(min(lista))    # 1    

# Exemplo 24:

lista = [1, 2, 3, 4, 5]
print(sum(lista))    # 15       

# Exemplo 25:

lista = [1, 2, 3, 4, 5]     

print(lista.pop(2))    # 3     

print(lista)    # [1, 2, 4, 5]      

# Exemplo 26:   

lista = [1, 2, 3, 4, 5]

print(lista.index(3, 2))    # 2     

# Exemplo 27:

lista = [1, 2, 3, 4, 5]     

print(lista.count(2, 2, 4))    # 1      


