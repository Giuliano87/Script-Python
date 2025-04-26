# O que são matrizes:
# Matrizes são estruturas de dados que permitem armazenar dados em linhas e colunas.
# Cada elemento de uma matriz é chamado de elemento.
# Exemplos de matrizes:

# Matriz 2x3:
# | 1 2 3 |
# | 4 5 6 |

# Matriz 3x2:
# | 1 2 |
# | 3 4 |
# | 5 6 |

# Matriz 3x3:
# | 1 2 3 |
# | 4 5 6 |
# | 7 8 9 |

# Matriz 4x4:
# | 1 2 3 4 |
# | 5 6 7 8 |
# | 9 10 11 12 |
# | 13 14 15 16 |

# Como criar uma matriz em Python:
# Para criar uma matriz em Python, usamos a função `numpy.array()` que recebe uma lista de listas contendo os elementos da matriz.

import numpy as np # type: ignore

# Exemplos de martyrizes
# Matriz 2x3
matriz_2x3 = np.array([[1, 2, 3], [4, 5, 6]])
# Matriz 3x2
matriz_3x2 = np.array([[1, 2], [3, 4], [5, 6]])
print(matriz_3x2)

# Como acessar elementos de uma matriz:
# Para acessar um elemento específico de uma matriz, usamos a notação de colchetes.
# A primeira coluna é a coluna 0, a segunda coluna é a coluna 1, e assim por diante.

# Acessando o elemento (1, 2) da matriz 2x3
print(matriz_2x3[1][2])

# Acessando o elemento (2, 1) da matriz 3x2
print(matriz_3x2[2][1])

# Como alterar elementos de uma matriz:
# Para alterar um elemento específico de uma matriz, usamos a notação de colchetes e atribuímos o novo valor.

# Alterando o elemento (1, 2) da matriz 2x3 para 9
matriz_2x3[1][2] = 9
print(matriz_2x3)

# Alterando o elemento (2, 1) da matriz 3x2 para 7
matriz_3x2[2][1] = 7
print(matriz_3x2)

# Como adicionar linhas e colunas a uma matriz:
# Para adicionar linhas e colunas a uma matriz, usamos as funções `numpy.append()` e `numpy.insert()`.

# Adicionando uma linha a matriz 2x3

matriz_2x3 = np.append(matriz_2x3, [[7, 8, 9]], axis=0)
print(matriz_2x3)

# Adicionando uma coluna a matriz 3x2

matriz_3x2 = np.insert(matriz_3x2, 1, 0, axis=1)
print(matriz_3x2)

# Como remover linhas e colunas de uma matriz:
# Para remover linhas e colunas de uma matriz, usamos as funções `numpy.delete()` e `numpy.delete()`.

# Removendo a linha 1 da matriz 2x3

matriz_2x3 = np.delete(matriz_2x3, 1, axis=0)
print(matriz_2x3)

# Removendo a coluna 1 da matriz 3x2

matriz_3x2 = np.delete(matriz_3x2, 1, axis=1)
print(matriz_3x2)

