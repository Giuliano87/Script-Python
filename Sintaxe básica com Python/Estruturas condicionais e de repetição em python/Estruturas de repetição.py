# Estruturas de repetição em Python

# O que são estruturas de repetição?

# Estruturas de repetição são usadas para executar um bloco de código repetidamente até que uma condição seja satisfeita.

# Existem três tipos de estruturas de repetição em Python:


# For

# A estrutura For é usada para iterar sobre uma sequência (lista, tupla, string, etc.) ou sobre um intervalo de valores.
# A sintaxe da estrutura For é:

for item in...:
    # bloco de código a ser executado repetidamente

# Exemplo:
 for i in range(1, 11):
    print(i)

# O bloco de código será executado 10 vezes, imprimindo os números de 1 a 10.
#  While

# A estrutura While é usada para executar um bloco de código repetidamente enquanto uma condição for verdadeira.

# A sintaxe da estrutura While é:
    # bloco de código a ser executado repetidamente

# Exemplo:

 i = 1
while i <= 10:
    print(i)
    i += 1

    # O bloco de código será executado enquanto i for menor ou igual a 10, imprimindo os números de 1 a 10.
    # Break e Continue

    # O comando Break é usado para interromper a execução de um loop.

    # O comando Continue é usado para pular para a próxima iteração do loop.

    # Exemplo:

    for i in range(1, 11):
        if i == 5:
            break
        print(i)

    # O bloco de código acima imprimirá os números de 1 a 4, pois o loop foi interrompido quando i foi igual a 5.

    for i in range(1, 11):
        if i == 5:
            continue
        print(i)

    # O bloco de código acima imprimirá os números de 1 a 10, pois o loop pulou para a próxima iteração quando i foi igual a 5. 

# Conclusão

# A estrutura For e While são usadas para executar um bloco de código repetidamente. A estrutura For é usada para iterar sobre uma sequência ou sobre um intervalo de valores, enquanto a estrutura While é usada para executar um bloco de código repetidamente enquanto uma condição for verdadeira.  
# O comando Break e Continue são usados para interromper ou pular para a próxima iteração de um loop.   
