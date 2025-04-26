# Explorando conjuntos em Python

# Criando um conjunto vazio
conjunto_vazio = set()
print(conjunto_vazio)

# Criando um conjunto com elementos
conjunto_com_elementos = {1, 2, 3, 4, 5}
print(conjunto_com_elementos)

# Adicionando elementos em um conjunto
conjunto_com_elementos.add(6)
print(conjunto_com_elementos)

# Remover elementos de um conjunto
conjunto_com_elementos.remove(2)
print(conjunto_com_elementos)

# Verificando se um elemento está em um conjunto
print(3 in conjunto_com_elementos)


# Criando conjuntos a partir de iteráveis
conjunto_a = set([1, 2, 3, 4, 5])   

# Criando conjuntos a partir de outros conjuntos
conjunto_b = set(conjunto_a)

# Criando conjuntos a partir de expressões geradoras
conjunto_c = {x**2 for x in range(1, 6)}

# Criando conjuntos a partir de funções geradoras
conjunto_d = set(range(1, 6))

# Criando conjuntos a partir de strings
conjunto_e = set("python")

# Criando conjuntos a partir de dicionários
dicionario = {'a': 1, 'b': 2, 'c': 3}
conjunto_f = set(dicionario.keys())

# Unindo conjuntos
conjunto_g = conjunto_a.union(conjunto_b)

# Interseção de conjuntos
conjunto_h = conjunto_a.intersection(conjunto_b)

# Diferença entre conjuntos
conjunto_i = conjunto_a.difference(conjunto_b)

# Criando conjuntos aninhados
conjunto_j = {1, 2, 3, {4, 5, 6}}

# Acessando elementos de um conjunto aninhado
print(conjunto_j.union())
print(conjunto_j.intersection())
print(conjunto_j.difference())  

# Criando conjuntos a partir de listas
lista = [1, 2, 3, 4, 5]
conjunto_k = set(lista)

# Criando conjuntos a partir de tuplas
tupla = (1, 2, 3, 4, 5)
conjunto_l = set(tupla) 

# Criando conjuntos a partir de dicionários
dicionario = {'a': 1, 'b': 2, 'c': 3}
conjunto_m = set(dicionario.values()) 

# Criando conjuntos a partir de strings
string = "python"
conjunto_n = set(string) 

# Criando conjuntos a partir de arquivos
arquivo = open("arquivo.txt", "r")
conjunto_o = set(arquivo) 

set_a = {1, 2, 3}
set_b = {2, 3, 4}

# União de conjuntos
set_c = set_a.union(set_b)
print(set_c)

# Interseção de conjuntos
set_d = set_a.intersection(set_b)
print(set_d)

# Diferença entre conjuntos
set_e = set_a.difference(set_b)
print(set_e)

# Diferença simétrica entre conjuntos
set_f = set_a.symmetric_difference(set_b)
print(set_f)

# Verificando se um conjunto é subconjunto de outro
set_g = {1, 2, 3, 4, 5}
set_h = {1, 2, 3}
print(set_h.issubset(set_g))

# Verificando se um conjunto é superconjunto de outro
set_i = {1, 2, 3, 4, 5}
set_j = {1, 2, 3, 4, 5, 6}
print(set_i.issuperset(set_j))
# Verificando se dois conjuntos são disjuntos
set_k = {1, 2, 3}
set_l = {4, 5, 6}
print(set_k.isdisjoint(set_l))  


# Criando conjuntos a partir de listas
lista = [1, 2, 3, 4, 5]
conjunto_k = set(lista)

# Criando conjuntos a partir de tuplas
tupla = (1, 2, 3, 4, 5)
conjunto_l = set(tupla) 

# Acessando os dados de um conjunto
print(conjunto_k)
print(conjunto_l)

# Acessando os elementos de um conjunto
print(conjunto_k.pop())
print(conjunto_l.pop())

# Criando conjuntos a partir de dicionários
dicionario = {'a': 1, 'b': 2, 'c': 3}
conjunto_m = set(dicionario.values()) 

# Criando conjuntos a partir de strings
string = "python"
conjunto_n = set(string) 

# Criando conjuntos a partir de arquivos
arquivo = open("arquivo.txt", "r")
conjunto_o = set(arquivo) 

# Criando conjuntos a partir de listas
lista = [1, 2, 3, 4, 5]
conjunto_p = set(lista)

# Criando conjuntos a partir de tuplas
tupla = (1, 2, 3, 4, 5)
conjunto_q = set(tupla) 

# Criando conjuntos a partir de dicionários
dicionario = {'a': 1, 'b': 2, 'c': 3}
conjunto_r = set(dicionario.values()) 

# Criando conjuntos a partir de strings
string = "python"
conjunto_s = set(string) 

# Criando conjuntos a partir de arquivos
arquivo = open("arquivo.txt", "r")
conjunto_t = set(arquivo) 

# Criando conjuntos a partir de listas
lista = [1, 2, 3, 4, 5]
conjunto_u = set(lista)

# Criando conjuntos a partir de tuplas
tupla = (1, 2, 3, 4, 5)
conjunto_v = set(tupla) 

# Criando conjuntos a partir de dicionários
dicionario = {'a': 1, 'b': 2, 'c': 3}
conjunto_w = set(dicionario.values()) 

# Criando conjuntos a partir de strings
string = "python"
conjunto_x = set(string) 

# Criando conjuntos a partir de arquivos
arquivo = open("arquivo.txt", "r")
conjunto_y = set(arquivo) 

# Criando conjuntos a partir de listas
lista = [1, 2, 3, 4, 5]
conjunto_z = set(lista)

# Criando conjuntos a partir de tuplas
tupla = (1, 2, 3, 4, 5)
conjunto_aa = set(tupla) 

# Criando conjuntos a partir de dicionários
dicionario = {'a': 1, 'b': 2, 'c': 3}
conjunto_bb = set(dicionario.values()) 

# Criando conjuntos a partir de strings
string = "python"
conjunto_cc = set(string) 

# Criando conjuntos a partir de arquivos
arquivo = open("arquivo.txt", "r")
conjunto_dd = set(arquivo) 

# Criando conjuntos a partir de listas
lista = [1, 2, 3, 4, 5]
conjunto_ee = set(lista)

# Criando conjuntos a partir de tuplas
tupla = (1, 2, 3, 4, 5)
conjunto_ff = set(tupla) 

# Criando conjuntos a partir de dicionários
dicionario = {'a': 1, 'b': 2, 'c': 3}
conjunto_gg = set(dicionario.values()) 

# Criando conjuntos a partir de strings
string = "python"
conjunto_hh = set(string) 

# Criando conjuntos a partir de arquivos
arquivo = open("arquivo.txt", "r")
conjunto_ii = set(arquivo) 

# Criando conjuntos a partir de listas
lista = [1, 2, 3, 4, 5]
conjunto_jj = set(lista)

# Criando conjuntos a partir de tuplas
tupla = (1, 2, 3, 4, 5)
conjunto_kk = set(tupla) 

# Criando conjuntos a partir de dicionários
dicionario = {'a': 1, 'b': 2, 'c': 3}
conjunto_ll = set(dicionario.values()) 

# Criando conjuntos a partir de strings
string = "python"
conjunto_mm = set(string) 

# Criando conjuntos a partir de arquivos
arquivo = open("arquivo.txt", "r")
conjunto_nn = set(arquivo) 

# Criando conjuntos a partir de listas
lista = [1, 2, 3, 4, 5]
conjunto_oo = set(lista)

# Criando conjuntos a partir de tuplas
tupla = (1, 2, 3, 4, 5)
conjunto_pp = set(tupla) 

# Criando conjuntos a partir de dicionários
dicionario = {'a': 1, 'b': 2, 'c': 3}
conjunto_qq = set(dicionario.values()) 

# Criando conjuntos a partir de strings
string = "python"
conjunto_rr = set(string) 

# Criando conjuntos a partir de arquivos
arquivo = open("arquivo.txt", "r")
conjunto_ss = set(arquivo) 

# Criando conjuntos a partir de listas
lista = [1, 2, 3, 4, 5]
conjunto_tt = set(lista)

# funcão enumerate()

# Criando conjuntos a partir de listas
lista = [1, 2, 3, 4, 5]
conjunto_uu = set(enumerate(lista))

# Criando conjuntos a partir de tuplas
tupla = (1, 2, 3, 4, 5)
conjunto_vv = set(enumerate(tupla)) 

# Criando conjuntos a partir de dicionários
dicionario = {'a': 1, 'b': 2, 'c': 3}
conjunto_ww = set(enumerate(dicionario.values())) 

# Criando conjuntos a partir de strings
string = "python"
conjunto_xx = set(enumerate(string)) 

# Criando conjuntos a partir de arquivos
arquivo = open("arquivo.txt", "r")
conjunto_yy = set(enumerate(arquivo)) 

# Criando metodos union()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# União de conjuntos
conjunto_c = conjunto_a.union(conjunto_b)
print(conjunto_c)

# Criando metodos intersection()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Interseção de conjuntos
conjunto_c = conjunto_a.intersection(conjunto_b)
print(conjunto_c)

# Criando metodos difference()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Diferença entre conjuntos
conjunto_c = conjunto_a.difference(conjunto_b)
print(conjunto_c)

# Criando metodos symmetric_difference()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Diferença simétrica entre conjuntos
conjunto_c = conjunto_a.symmetric_difference(conjunto_b)
print(conjunto_c)

# Criando metodos issubset()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Verificando se um conjunto é subconjunto de outro
print(conjunto_a.issubset(conjunto_b))

# Criando metodos issuperset()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Verificando se um conjunto é superconjunto de outro
print(conjunto_a.issuperset(conjunto_b))

# Criando metodos isdisjoint()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Verificando se dois conjuntos são disjuntos
print(conjunto_a.isdisjoint(conjunto_b))    

# Criando o metodo pop()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Removendo elementos de um conjunto
conjunto_a.pop()
conjunto_b.pop()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]   
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

#.Issuperset()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Verificando se um conjunto é superconjunto de outro
print(conjunto_a.issuperset(conjunto_b))

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Verificando se um conjunto é subconjunto de outro 
print(conjunto_a.issubset(conjunto_b))

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Verificando se dois conjuntos são disjuntos
print(conjunto_a.isdisjoint(conjunto_b))    

# isdisjoint()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Verificando se dois conjuntos são disjuntos
print(conjunto_a.isdisjoint(conjunto_b)) 

# Criando conjuntos a partir de listas      
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# add()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Adicionando elementos a um conjunto
conjunto_a.add(9)
conjunto_b.add(10)

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Copy()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Criando uma cópia de um conjunto
conjunto_c = conjunto_a.copy()
conjunto_d = conjunto_b.copy()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# discard()
# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Removendo elementos de um conjunto
conjunto_a.discard(2)
conjunto_b.discard(5)

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# remove()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Removendo elementos de um conjunto
conjunto_a.remove(2)
conjunto_b.remove(5)

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# clear()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Limpando um conjunto
conjunto_a.clear()
conjunto_b.clear()      
# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# update()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Atualizando um conjunto com elementos de outro
conjunto_a.update(conjunto_b)

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# union()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# União de conjuntos
conjunto_c = conjunto_a.union(conjunto_b)
print(conjunto_c)

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# intersection()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Interseção de conjuntos
conjunto_c = conjunto_a.intersection(conjunto_b)
print(conjunto_c)

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# difference()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Diferença entre conjuntos
conjunto_c = conjunto_a.difference(conjunto_b)
print(conjunto_c)

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# symmetric_difference()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Diferença simétrica entre conjuntos
conjunto_c = conjunto_a.symmetric_difference(conjunto_b)
print(conjunto_c)   
# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# issubset()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Verificando se um conjunto é subconjunto de outro
print(conjunto_a.issubset(conjunto_b))

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# issuperset()

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Verificando se um conjunto é superconjunto de outro
print(conjunto_a.issuperset(conjunto_b))

# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# isdisjoint()  
# Criando conjuntos a partir de listas
lista_a = [1, 2, 3, 4, 5]
conjunto_a = set(lista_a)   
lista_b = [4, 5, 6, 7, 8]
conjunto_b = set(lista_b)

# Verificando se dois conjuntos são disjuntos
print(conjunto_a.isdisjoint(conjunto_b)) 



                 