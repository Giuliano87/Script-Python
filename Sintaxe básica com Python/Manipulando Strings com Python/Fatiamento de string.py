# Fatiamento de string

# O que é fatiamento de string?
# Fatiamento de string é a capacidade de selecionar partes de uma string de acordo com um intervalo de indices.

# Exemplos:

# 1. Fatiamento de string com índices positivos:

# A string "Hello World" possui 11 caracteres.

# Para fatiar a string de 0 a 5, usamos a notação de índices [0:6]:

string = "Hello World"
print(string[0:6]) # Saída: "Hello "

# 2. Fatiamento de string com índices negativos:

# A string "Hello World" possui 11 caracteres.

# Para fatiar a string de 6 a 10, usamos a notação de índices [6:11]:

string = "Hello World"
print(string[6:11]) # Saída: "World"

# 3. Fatiamento de string com índices negativos:

# A string "Hello World" possui 11 caracteres.

# Para fatiar a string de 6 a 10, usamos a notação de índices [-5:-1]:

string = "Hello World"
print(string[-5:-1]) # Saída: "World"

# 4. Fatiamento de string com passo:

# A string "Hello World" possui 11 caracteres.

# Para fatiar a string de 0 a 10 com passo de 2, usamos a notação de índices [0:11:2]:

string = "Hello World"
print(string[0:11:2]) # Saída: "HloWrd"

# 5. Fatiamento de string com passo negativo:

# A string "Hello World" possui 11 caracteres.

# Para fatiar a string de 10 a 0 com passo de -2, usamos a notação de índices [10:0:-2]:

string = "Hello World"
print(string[10:0:-2]) # Saída: "dlroW"
# 6. Fatiamento de string com índices de início e fim:


