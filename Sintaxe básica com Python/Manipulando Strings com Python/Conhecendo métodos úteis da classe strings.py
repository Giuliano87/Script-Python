# Conhecendo métodos úteis da classe strings.py

# O que são métodos strings?
# Métodos são funções que são atribuídas a objetos do tipo string. Eles permitem realizar operações com strings de maneira simples e eficiente.

# Métodos úteis da classe strings
# Abaixo estão alguns métodos úteis da classe strings:

# 1. count(sub, start=0, end=len(string))
# O método count() retorna o número de vezes que a substring sub ocorre na string.

# Exemplo:
string = "Python é uma linguagem de programação multi-paradigma"
print(string.count("o")) # Output: 4

# 2. find(sub, start=0, end=len(string))
# O método find() retorna o índice da primeira ocorrência da substring sub na string.

# Exemplo:
string = "Python é uma linguagem de programação multi-paradigma"
print(string.find("Python")) # Output: 0

# 3. index(sub, start=0, end=len(string))
# O método index() é similar ao método find(), mas se a substring não for encontrada, um ValueError é lançado.

# Exemplo:
string = "Python é uma linguagem de programação multi-paradigma"
print(string.index("Python")) # Output: 0

# 4. isalnum()
# O método isalnum() retorna True se a string contém apenas letras e/ou números, False caso contrário.

# Exemplo:
string = "Python123"
print(string.isalnum()) # Output: True

# 5. isalpha()
# O método isalpha() retorna True se a string contém apenas letras, False caso contrário.

# Exemplo:
string = "Python"
print(string.isalpha()) # Output: True

# 6. isdigit()
# O método isdigit() retorna True se a string contém apenas dígitos, False caso contrário.

# Exemplo:
string = "12345"
print(string.isdigit()) # Output: True

# 7. islower()
# O método islower() retorna True se a string contém apenas letras minúsculas, False caso contrário.

# Exemplo:
string = "python"
print(string.islower()) # Output: True

# 8. isupper()
# O método isupper() retorna True se a string contém apenas letras maiúsculas, False caso contrário.

# Exemplo:
string = "PYTHON"
print(string.isupper()) # Output: True

# 9. join(iterable)
# O método join() retorna uma string que é o resultado da concatenação de todos os elementos do iterável iterable.

# Exemplo:
string = " "
lista = ["Python", "é", "uma", "linguagem", "de", "programação", "multi-paradigma"]
print(string.join(lista)) # Output: "Python é uma linguagem de programação multi-paradigma"

# 10. lower()
# O método lower() retorna uma string com todas as letras minúsculas.

# Exemplo:
string = "PYTHON"
print(string.lower()) # Output: "python"

# 11. upper()
# O método upper() retorna uma string com todas as letras maiúsculas.

# Exemplo:
string = "python"
print(string.upper()) # Output: "PYTHON"    

# 12. replace(old, new, count=-1)
# O método replace() retorna uma string com todas as ocorrências da substring old substituídas por new.

# Exemplo:
string = "Python é uma linguagem de programação multi-paradigma"
print(string.replace("Python", "Java")) # Output: "Java é uma linguagem de programação multi-paradigma"

# Conclusão
# A classe strings do Python fornece diversos métodos úteis para manipular strings de maneira simples e eficiente.  

# Interpolação de strings
# A interpolação de strings é a capacidade de incluir variáveis em uma string usando chaves {}.

# Exemplo:
nome = "João"
idade = 30
string = "Meu nome é {} e tenho {} anos."
print(string.format(nome, idade)) # Output: "Meu nome é João e tenho 30 anos."  

# O método format() é um método muito útil para interpolar strings. Ele substitui as chaves {} com os valores passados como argumentos. 

# Exemplo:
nome = "João"
idade = 30
string = "Meu nome é {0} e tenho {1} anos."
print(string.format(nome, idade)) # Output: "Meu nome é João e tenho 30 anos."  

# Nesse exemplo, {0} e {1} são os índices dos argumentos passados para o método format().
    # Outros métodos da classe strings
# A classe strings do Python fornece outros métodos úteis, como split(), rsplit(), lstrip(), rstrip(), strip(), etc.    
# Conclusão
# A manipulação de strings com Python é uma tarefa fundamental para qualquer programador. A classe strings do Python fornece diversos métodos úteis para realizar operações com strings de maneira simples e eficiente.