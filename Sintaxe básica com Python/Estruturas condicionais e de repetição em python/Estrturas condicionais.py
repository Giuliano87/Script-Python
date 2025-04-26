# Estruturas condicionais em Python

# O que são estruturas condicionais?

# Estruturas condicionais são estruturas de código que permitem executar um bloco de código caso uma condição seja verdadeira.

# Existem três tipos de estruturas condicionais em Python:  

# 1. if
# 2. if-else
# 3. if-elif-else

# Vamos ver cada uma delas com exemplos.    

# 1. if

# A estrutura condicional if é a estrutura mais simples e comum em Python. Ela é usada para executar um bloco de código caso uma condição seja verdadeira.

# Exemplo:

# Considere que você deseja imprimir o nome de uma pessoa se ela tiver mais de 18 anos.

# Usando a estrutura condicional if:

age = 20

if age > 18:
    print("The person is older than 18.")

# O código acima imprime "The person is older than 18." porque a condição age > 18 é verdadeira.

# 2. if-else

# A estrutura condicional if-else é uma estrutura que permite executar um bloco de código caso uma condição seja verdadeira e outro bloco de código caso a condição seja falsa.

# Exemplo:

# Considere que você deseja imprimir o nome de uma pessoa se ela tiver mais de 18 anos, caso contrário, imprima a mensagem "The person is underage".

# Usando a estrutura condicional if-else:

age = 16

if age > 18:
    print("The person is older than 18.")
else:
    print("The person is underage.")

# O código acima imprime "The person is underage." porque a condição age > 18 é falsa.

# 3. if-elif-else

# A estrutura condicional if-elif-else é uma estrutura que permite executar um bloco de código caso uma condição seja verdadeira, caso contrário, verificar a condição do elif e caso ainda não seja verdadeira, executar o bloco de código do else.

# Exemplo:

# Considere que você deseja imprimir o nome de uma pessoa se ela tiver mais de 18 anos, caso contrário, se ela tiver 16 anos, imprima a mensagem "The person is a teenager", caso contrário, imprima a mensagem "The person is underage"