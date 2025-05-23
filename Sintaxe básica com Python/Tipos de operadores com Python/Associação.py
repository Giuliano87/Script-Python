# Operadores de associação em Python
# Operadores de associação em Python são usados para agrupar operadores em expressões.
# Existem dois tipos de operadores de associação em Python:
# 1. Associação à esquerda (Left-associativity)
# 2. Associação à direita (Right-associativity)
# Associação à esquerda significa que os operadores são associados da esquerda para a direita.
# Associação à direita significa que os operadores são associados da direita para a esquerda.
# Em Python, a associação à esquerda é a padrão.
# A seguir, vamos ver exemplos de operadores de associação em Python.

# Exemplo 1: Operadores de associação à esquerda
# A associação à esquerda significa que os operadores são associados da esquerda para a direita.
# Em Python, a associação à esquerda é a padrão.
# A ordem de execução dos operadores é da esquerda para a direita.
# O exemplo a seguir mostra a execução dos operadores de associação à esquerda em Python.

# Exemplo 1:
# 1 + 2 + 3 + 4 + 5
# 1 + (2 + 3) + 4 + 5
# (1 + 2) + (3 + 4) + 5
# 3 + 7 + 5
# 12 + 5
# 17

# Exemplo 2:
# 2 ** 3 ** 2
# 2 ** (3 ** 2)
# (2 ** 3) ** 2
# 8 ** 2
# 64

# Exemplo 3:    
# 2 * 3 / 4
# 2 * (3 / 4)
# (2 * 3) / 4
# 6 / 4
# 1.5

# Exemplo 4:
# 2 + 3 - 4 * 5
# 2 + (3 - (4 * 5))
# (2 + 3) - (4 * 5)
# 5 - 20
# -15   

# Exemplo 5:
# 2 + 3 * 4 ** 2 / 5
# 2 + (3 * (4 ** 2) / 5)
# (2 + (3 * 4 ** 2)) / 5
# 2 + 16 * 4 ** 2
# 2 + 64
# 66

# Exemplo 6:
# 2 + 3 * 4 - 5 / 6
# 2 + (3 * 4 - (5 / 6))
# (2 + (3 * 4)) - (5 / 6)
# 2 + 12 - 1
# 14 - 1
# 13

# Exemplo 7:
# 2 + 3 * 4 - 5 / 6 ** 2
# 2 + (3 * 4 - (5 / (6 ** 2)))
# (2 + (3 * 4)) - (5 / 36)
# 2 + 12 - 1
# 14 - 1
# 13

# Exemplo 8:
# 2 + 3 * 4 - 5 / 6 ** 2 % 2
# 2 + (3 * 4 - (5 / (6 ** 2 % 2)))
# (2 + (3 * 4)) - (5 / 36 % 2)
# 2 + 12 - 1 % 2
# 14 - 1 % 2
# 13 % 2
# 1 % 2
# 1

# Exemplo 9:    
# 2 + 3 * (4 - 5 / 6) ** 2
# 2 + (3 * (4 - (5 / 6)) ** 2)  
# (2 + (3 * (4 - (5 / 6)))) ** 2
# (2 + (3 * -1)) ** 2
# 2 + 3 ** 2
# 2 + 9
# 11

# Exemplo 10:
# 2 + 3 * (4 - 5 / 6) ** 2 % 2
# 2 + (3 * (4 - (5 / 6)) ** 2 % 2)
# (2 + (3 * (4 - (5 / 6)))) ** 2 % 2
# (2 + (3 * -1)) ** 2 % 2
# 2 + 3 ** 2 % 2
# 2 + 9 % 2
# 11 % 2
# 1 % 2
# 1

# Exemplo 11:
# 2 + 3 * (4 - 5 / 6) ** 2 % 2 + 1
# 2 + (3 * (4 - (5 / 6)) ** 2 % 2) + 1
# (2 + (3 * (4 - (5 / 6)))) ** 2 % 2 + 1
# (2 + (3 * -1)) ** 2 % 2 + 1
# 2 + 3 ** 2 % 2 + 1
# 2 + 9 % 2 + 1
# 11 % 2 + 1
# 1 % 2 + 1
# 2

# Exemplo 12:
# 2 + 3 * (4 - 5 / 6) ** 2 % 2 + 1 - 2 * 3 / 4
# 2 + (3 * (4 - (5 / 6)) ** 2 % 2) + 1 - (2 * 3 / 4)
# (2 + (3 * (4 - (5 / 6)))) ** 2 % 2 + 1 - (2 * 3 / 4)
# (2 + (3 * -1)) ** 2 % 2 + 1 - (2 * 3 / 4)
# 2 + 3 ** 2 % 2 + 1 - (2 * 3 / 4)
# 2 + 9 % 2 + 1 - (2 * 3 / 4)
# 11 % 2 + 1 - (2 * 3 / 4)
# 1 % 2 + 1 - (2 * 3 / 4)
# 2 - 6 / 4
# -1.5  

# Exemplo 13:
# 2 + 3 * (4 - 5 / 6) ** 2 % 2 + 1 - 2 * 3 / 4 + 5 * 6 ** 2
# 2 + (3 * (4 - (5 / 6)) ** 2 % 2) + 1 - (2 * 3 / 4) + (5 * 6 ** 2)
# (2 + (3 * (4 - (5 / 6)))) ** 2 % 2 + 1 - (2 * 3 / 4) + (5 * 6 ** 2)
# (2 + (3 * -1)) ** 2 % 2 + 1 - (2 * 3 / 4) + (5 * 6 ** 2)
# 2 + 3 ** 2 % 2 + 1 - (2 * 3 / 4) + (5 * 6 ** 2)
# 2 + 9 % 2 + 1 - (2 * 3 / 4) + (5 * 6 ** 2)
# 11 % 2 + 1 - (2 * 3 / 4) + (5 * 6 ** 2)
# 1 % 2 + 1 - (2 * 3 / 4) + (5 * 6 ** 2)
# 2 - 6 / 4 + (5 * 36)
# -1.5 + 180
# 179.5

# Exemplo 14:
# 2 + 3 * (4 - 5 / 6) ** 2 % 2 + 1 - 2 * 3 / 4 + 5 * 6 ** 2 - 7 * 8 ** 3
# 2 + (3 * (4 - (5 / 6)) ** 2 % 2) + 1 - (2 * 3 / 4) + (5 * 6 ** 2) - (7 * 8 ** 3)
# (2 + (3 * (4 - (5 / 6)))) ** 2 % 2 + 1 - (2 * 3 / 4) + (5 * 6 ** 2) - (7 * 8 ** 3)
# (2 + (3 * -1)) ** 2 % 2 + 1 - (2 * 3 / 4) + (5 * 6 ** 2) - (7 * 8 ** 3)
# 2 + 3 ** 2 % 2 + 1 - (2 * 3 / 4) + (5 * 6 ** 2) - (7 * 8 ** 3)
# 2 + 9 % 2 + 1 - (2 * 3 / 4) + (5 * 6 ** 2) - (7 * 8 ** 3)
# 11 % 2 + 1 - (2 * 3 / 4) + (5 * 6 ** 2) - (7 * 8 ** 3)
# 1 % 2 + 1 - (2 * 3 / 4) + (5 * 6 ** 2) - (7 * 8 ** 3)
# 2 - 6 / 4 + (5 * 36) - (7 * 512)
# -1.5 + 180 - (7 * 512)
# -511.5

# Exemplo 15:
# 2 + 3 * (4 - 5 / 6) ** 2 % 2 + 1 - 2 * 3 / 4 + 5 * 6 ** 2 - 7 * 8 ** 3 + 9 * 10 ** 4
# 2 + (3 * (4 - (5 / 6)) ** 2 % 2) + 1 - (2 * 3 / 4) + (5 * 6 ** 2) - (7 * 8 ** 3) + (9 * 10 ** 4)
# (2 + (3 * (4 - (5 / 6)))) ** 2 % 2 + 1 - (2 * 3 / 4) + (5 * 6 ** 2) - (7 * 8 ** 3) + (9 * 10 ** 4)        
# (2 + (3 * -1)) ** 2 % 2 + 1 - (2 * 3 / 4) + (5 * 6 ** 2) - (7 * 8 ** 3) + (9 * 10 ** 4)
# 2 + 3 ** 2 % 2 + 1 - (2 * 3 / 4) + (5 * 6 ** 2) - (7 * 8 ** 3) + (9 * 10 ** 4)
# 2 + 9 % 2 + 1 - (2 * 3 / 4) + (5 * 6 ** 2) - (7 * 8 ** 3) + (9 * 10 ** 4)
# 11 % 2 + 1 - (2 * 3 / 4) + (5 * 6 ** 2) - (7 * 8 ** 3) + (9 * 10 ** 4)
# 1 % 2 + 1 - (2 * 3 / 4) + (5 * 6 ** 2) - (7 * 8 ** 3) + (9 * 10 ** 4)
# 2 - 6 / 4 + (5 * 36) - (7 * 512) + (9 * 10000)
# -1.5 + 180 - (7 * 512) + (9 * 10000)
# -511.5 + 90000
# 89998.5

