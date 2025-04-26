# O que são vetores?
# Vetores são arrays de dados que podem armazenar vários valores de um mesmo tipo.
# Exemplos de vetores:
# - Números: [1, 2, 3, 4, 5]
# - Palavras: ["banana", "laranja", "uva"]
# - Caracteres: ['a', 'b', 'c', 'd', 'e']
# - Objetos: [objeto1, objeto2, objeto3]     # Exemplo: [1, "banana", True]

# Como criar vetores em Python?
# Vetores em Python são criados usando colchetes [] e separando os valores com vírgulas.
# Exemplos:
# - Números: [1, 2, 3, 4, 5]
# - Palavras: ["banana", "laranja", "uva"]
# - Caracteres: ['a', 'b', 'c', 'd', 'e']
# - Objetos: [objeto1, objeto2, objeto3]     # Exemplo: [1, "banana", True]

# Como acessar elementos de um vetor?
# Para acessar um elemento de um vetor em Python, usamos a notação de colchetes [] e o índice do elemento que queremos acessar.
# Exemplo:
# - Número: vetor[0]     # Acessa o primeiro elemento do vetor
# - Palavra: vetor[1]     # Acessa o segundo elemento do vetor
# - Caractere: vetor[2]   # Acessa o terceiro elemento do vetor
# - Objeto: vetor[3]      # Acessa o quarto elemento do vetor

# Como alterar elementos de um vetor?
# Para alterar um elemento de um vetor em Python, usamos a notação de colchetes [] e o índice do elemento que queremos alterar e atribuímos o novo valor.
# Exemplo:
# - Número: vetor[0] = 10     # Altera o primeiro elemento do vetor para 10
# - Palavra: vetor[1] = "maçã"     # Altera o segundo elemento do vetor para "maçã"
# - Caractere: vetor[2] = 'x'   # Altera o terceiro elemento do vetor para 'x'
# - Objeto: vetor[3] = objeto4   # Altera o quarto elemento do vetor para objeto4

# Como adicionar elementos a um vetor?
# Para adicionar elementos a um vetor em Python, usamos a função append().
# Exemplo:
# - Número: vetor.append(6)     # Adiciona o número 6 ao final do vetor
# - Palavra: vetor.append("pera")     # Adiciona a palavra "pera" ao final do vetor
# - Caractere: vetor.append('z')   # Adiciona o caractere 'z' ao final do vetor
# - Objeto: vetor.append(objeto5)   # Adiciona o objeto objeto5 ao final do vetor

# Exemplo de uso de vetores em Python
# Vamos criar um vetor de números e imprimir seus elementos:

# Criando o vetor de números
numeros = [1, 2, 3, 4, 5]

# Imprimindo os elementos do vetor
print("Vetor de números:")
for num in numeros:
    print(num)

# Vamos criar um vetor de palavras e imprimir seus elementos:

# Criando o vetor de palavras
palavras = ["banana", "laranja", "uva"]

# Imprimindo os elementos do vetor
print("\nVetor de palavras:")
for palavra in palavras:
    print(palavra)

# Vamos criar um vetor de caracteres e imprimir seus elementos:

# Criando o vetor de caracteres
caracteres = ['a', 'b', 'c', 'd', 'e']

# Imprimindo os elementos do vetor
print("\nVetor de caracteres:")
for char in caracteres:
    print(char)

# Vamos criar um vetor de objetos e imprimir seus elementos:

# Criando o vetor de objetos
objetos = [1, "banana", True]

# Imprimindo os elementos do vetor
print("\nVetor de objetos:")
for obj in objetos:
    print(obj)

# Vamos alterar o primeiro elemento do vetor de números:

# Alterando o primeiro elemento do vetor de números
numeros[0] = 10
# Imprimindo o vetor de números
print("\nVetor de números alterado:")
for num in numeros:
    print(num)

# Vamos adicionar um elemento ao final do vetor de palavras:

# Adicionando um elemento ao final do vetor de palavras
palavras.append("morango")

# Imprimindo o vetor de palavras
print("\nVetor de palavras com novo elemento:")
for palavra in palavras:
    print(palavra)

    