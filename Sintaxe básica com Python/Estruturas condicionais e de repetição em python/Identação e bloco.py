# Identação e bloco de código em Python

# Bloco de código é um conjunto de linhas de código que são executadas como uma unidade. Em Python, os blocos são definidos por identação.

# Em Python, a identação é feita com 4 espaços.

# Exemplo de bloco de código:

if True:
    print("Hello, World!")

# Neste exemplo, o bloco de código começa com a palavra-chave "if" e a condição "True". Depois disso, há uma identação (4 espaços) e a instrução "print" que exibe a mensagem "Hello, World!".

# A identação é importante em Python, pois ela define o escopo de cada bloco de código. Se houver uma identação errada, o Python irá gerar um erro de sintaxe.

# Exemplo de identação errada:

if True:
    print("Hello, World!")
print("Goodbye, World!")

# Neste exemplo, a instrução "print" que exibe a mensagem "Goodbye, World!" está fora do bloco de código do "if". Logo, o Python irá gerar um erro de sintaxe.
# Em Python, a identação é fundamental para definir blocos de código. Ela ajuda a manter o código organizado e fácil de ler.

# Exemplo de identação correta:

if True:
    print("Hello, World!")
else:
    print("Goodbye, World!")

# Neste exemplo, a instrução "print" que exibe a mensagem "Goodbye, World!" está dentro do bloco de código do "else", logo, ela será executada apenas se a condição do "if" for falsa.
# Blocos de código podem ser aninhados, ou seja, um bloco de código pode conter outro bloco de código.
# Exemplo de bloco de código aninhado:

if True:
    print("Hello, World!")
    if False:
        print("Goodbye, World!")

# Neste exemplo, o bloco de código aninhado começa com a palavra-chave "if" e a condição "False". Depois disso, há uma identação (4 espaços) e a instrução "print" que exibe a mensagem "Goodbye, World!".
# O bloco de código aninhado está contido no bloco de código do "if", logo, a instrução "print" que exibe a mensagem "Goodbye, World!" será executada apenas se a condição do "if" for verdadeira.
