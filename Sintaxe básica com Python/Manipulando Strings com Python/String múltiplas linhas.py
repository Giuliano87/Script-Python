# String múltiplas linhas

# Uma string pode ser definida em várias linhas, basta colocar o caractere de quebra de linha (\n) no final de cada linha.

# Exemplo:

string_multi = """
Este é um exemplo de string
em várias linhas.
"""

print(string_multi) # Saída: Este é um exemplo de string em várias linhas.
# O caractere de quebra de linha (\n) é interpretado como um espaço em branco, então a string é exibida com a quebra de linha no final.
# Podemos usar o caractere de quebra de linha (\n) para quebrar a string em várias linhas, porém, se quisermos quebrar a string em algum ponto específico, podemos usar o método split() para dividir a string em várias partes.
# Exemplo:

string_multi = "Este é um exemplo de string\nem várias linhas."

string_multi_split = string_multi.split("\n")

print(string_multi_split) # Saída: ['Este é um exemplo de string', 'em várias linhas.']
# A string foi dividida em duas partes, uma para cada quebra de linha (\n) encontrada.
# Podemos usar o método join() para reunir as partes da string em uma única string.
# Exemplo:

string_multi_join = "\n".join(string_multi_split)

print(string_multi_join) # Saída: Este é um exemplo de string\nem várias linhas.
# A string foi reunida com o caractere de quebra de linha (\n) entre as partes.
# Podemos usar o método replace() para substituir uma parte da string por outra.
# Exemplo:

string_multi_replace = string_multi.replace("exemplo", "teste")

print(string_multi_replace) # Saída: Este é um teste de string\nem várias linhas.
# A palavra "exemplo" foi substituida por "teste".
# Podemos usar o método strip() para remover espaços em branco no início e no final da string.
# Exemplo:

string_multi_strip = string_multi.strip()

print(string_multi_strip) # Saída: Este é um exemplo de string\nem várias linhas.   
# O método strip() remove os espaços em branco no início e no final da string.
# Podemos usar o método lstrip() para remover espaços em branco no início da string.
# Exemplo:

string_multi_lstrip = string_multi.lstrip()

print(string_multi_lstrip) # Saída: Este é um exemplo de string\nem várias linhas.
# O método lstrip() remove os espaços em branco no início da string.
# Podemos usar o método rstrip() para remover espaços em branco no final da string.
# Exemplo:

string_multi_rstrip = string_multi.rstrip()

print(string_multi_rstrip) # Saída: Este é um exemplo de string\nem várias linhas.  
# O método rstrip() remove os espaços em branco no final da string.
# Podemos usar o método count() para contar o número de ocorrências de uma substring em uma string.
# Exemplo:

string_multi_count = string_multi.count("e")

print(string_multi_count) # Saída: 10
# A substring "e" aparece 10 vezes na string.
# Podemos usar o método find() para localizar a posição de uma substring em uma string.
# Exemplo:

string_multi_find = string_multi.find("exemplo")

print(string_multi_find) # Saída: 10
# A substring "exemplo" aparece na posição 10 da string.
# Podemos usar o método rfind() para localizar a posição da última ocorrência de uma substring em uma string.
# Exemplo:

string_multi_rfind = string_multi.rfind("exemplo")

print(string_multi_rfind) # Saída: 10
# A substring "exemplo" aparece na posição 10 da string.    
