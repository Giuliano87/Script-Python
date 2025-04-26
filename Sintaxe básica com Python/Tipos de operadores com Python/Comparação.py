# Operadores de comparação em Python

# O que são operadores de comparação?
# São operadores que realizam uma comparação entre dois valores e retornam um valor booleano (True ou False).

# Operadores de comparação em Python
# == (igualdade)
#!= (diferente)
# < (menor que)
# > (maior que)
# <= (menor ou igual a)
# >= (maior ou igual a)

# Exemplos

# Comparação de números
print(5 == 5) # True
print(5 == 6) # False
print(5!= 6) # True
print(5 < 6) # True
print(5 > 6) # False
print(5 <= 6) # True
print(5 >= 6) # False

# Comparação de strings
print("abc" == "abc") # True    
print("abc" == "def") # False
print("abc"!= "def") # True
print("abc" < "def") # True
print("abc" > "def") # False
print("abc" <= "def") # True        
print("abc" >= "def") # False
# Comparação de listas
print([1, 2, 3] == [1, 2, 3]) # True
print([1, 2, 3] == [1, 2, 4]) # False
print([1, 2, 3]!= [1, 2, 4]) # True
print([1, 2, 3] < [1, 2, 4]) # True
print([1, 2, 3] > [1, 2, 4]) # False
print([1, 2, 3] <= [1, 2, 4]) # True

# Comparação de dicionários
print({"a": 1, "b": 2} == {"a": 1, "b": 2}) # True
print({"a": 1, "b": 2} == {"a": 1, "b": 3}) # False
print({"a": 1, "b": 2}!= {"a": 1, "b": 3}) # True
print({"a": 1, "b": 2} < {"a": 1, "b": 3}) # True
print({"a": 1, "b": 2} > {"a": 1, "b": 3}) # False
print({"a": 1, "b": 2} <= {"a": 1, "b": 3}) # True
print({"a": 1, "b": 2} >= {"a": 1, "b": 3}) # False

# Exemplos de uso de operadores de comparação em Python

# Exemplo 1
# Verificar se o número é positivo
num = 5
if num > 0:
    print("O número é positivo")
else:
    print("O número não é positivo")

# Exemplo 2
# Verificar se o número é par
num = 6
if num % 2 == 0:
    print("O número é par")
else:
    print("O número não é par")

# Exemplo 3 
# Verificar se a string é igual a "abc"
string = "abc"
if string == "abc":
    print("A string é igual a 'abc'")
else:
    print("A string não é igual a 'abc'")

# Exemplo 4
# Verificar se a lista é igual a [1, 2, 3]
lista = [1, 2, 3]
if lista == [1, 2, 3]:
    print("A lista é igual a [1, 2, 3]")
else:
    print("A lista não é igual a [1, 2, 3]")    

    