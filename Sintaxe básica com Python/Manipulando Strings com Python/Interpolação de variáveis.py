# Interpolação de variáveis

nome = "John"
idade = 30

print(f"Meu nome é {nome} e tenho {idade} anos.")    # Interpolação de variáveis    
# Saída: Meu nome é John e tenho 30 anos.
# O f antes da string permite a interpolação de variáveis.
    # A variável nome é inserida entre chaves {} e é substituída pelo seu valor.
    # A variável idade é inserida entre chaves {} e é substituída pelo seu valor.
    # O resultado é uma string formatada com os valores das variáveis.
   
    # Exemplo 2:
    # nome = "John"
    # idade = 30
    # altura = 1.80
    # print(f"Meu nome é {nome} e tenho {idade} anos e {altura:.2f} de altura.")
    # Saída: Meu nome é John e tenho 30 anos e 1.80 de altura.
    # Adicionamos a formatação de float com 2 casas decimais com o :.2f.
    # O resultado é uma string formatada com os valores das variáveis.

    # Exemplo 3:
    # nome = "John"
    # idade = 30
    # altura = 1.80
    # print(f"Meu nome é {nome} e tenho {idade} anos e {altura:.2f} de altura. Meu nome tem {len(nome)} letras.")
    # Saída: Meu nome é John e tenho 30 anos e 1.80 de altura. Meu nome tem 4 letras.
    # Adicionamos a formatação de float com 2 casas decimais com o :.2f.
    # Adicionamos a função len() para contar o número de caracteres do nome.
    # O resultado é uma string formatada com os valores das variáveis e a função len(). 

    # Exemplo 4:
    # nome = "John"
    # idade = 30
    # altura = 1.80
    # print(f"Meu nome é {nome} e tenho {idade} anos e {altura:.2f} de altura. Meu nome tem {len(nome)} letras. Minha idade é {idade+1}.")
    # Saída: Meu nome é John e tenho 30 anos e 1.80 de altura. Meu nome tem 4 letras. Minha idade é 31.
    # Adicionamos a formatação de float com 2 casas decimais com o :.2f.
    # Adicionamos a função len() para contar o número de caracteres do nome.
    # Adicionamos a soma de idade + 1 para aumentar a idade em 1 ano.
    # O resultado é uma string formatada com os valores das variáveis, a função len() e a soma de idade + 1.    

    # Exemplo 5:
    # nome = "John"
    # idade = 30
    # altura = 1.80
    # print(f"Meu nome é {nome} e tenho {idade} anos e {altura:.2f} de altura. Meu nome tem {len(nome)} letras. Minha idade é {idade+1}. A minha altura é {altura+0.1:.2f}.")
    # Saída: Meu nome é John e tenho 30 anos e 1.80 de altura. Meu nome tem 4 letras. Minha idade é 31. A minha altura é 1.90.
    # Adicionamos a formatação de float com 2 casas decimais com o :.2f.
    # Adicionamos a função len() para contar o número de caracteres do nome.
    # Adicionamos a soma de idade + 1 para aumentar a idade em 1 ano.
    # Adicionamos a soma de altura + 0.1 para aumentar a altura em 0.1.
    # O resultado é uma string formatada com os valores das variáveis, a função len() e a soma de idade + 1.

    # Exemplo 6:
    # nome = "John"
    # idade = 30
    # altura = 1.80
    # print(f"Meu nome é {nome} e tenho {idade} anos e {altura:.2f} de altura. Meu nome tem {len(nome)} letras. Minha idade é {idade+1}. A minha altura é {altura+0.1:.2f}. A minha idade em meses é {idade*12}.")
    # Saída: Meu nome é John e tenho 30 anos e 1.80 de altura. Meu nome tem 4 letras. Minha idade é 31. A minha altura é 1.90. A minha idade em meses é 360.
    # Adicionamos a formatação de float com 2 casas decimais com o :.2f.
    # Adicionamos a função len() para contar o número de caracteres do nome.
    # Adicionamos a soma de idade + 1 para aumentar a idade em 1 ano.
    # Adicionamos a soma de altura + 0.1 para aumentar a altura em 0.1.
    # Adicionamos a multiplicação de idade * 12 para converter a idade em meses.
    # O resultado é uma string formatada com os valores das variáveis, a função len() e a soma de idade + 1.

    # Exemplo 7:
    # nome = "John"
    # idade = 30
    # altura = 1.80
    # print(f"Meu nome é {nome} e tenho {idade} anos e {altura:.2f} de altura. Meu nome tem {len(nome)} letras. Minha idade é {idade+1}. A minha altura é {altura+0.1:.2f}. A minha idade em meses é {idade*12}. A minha altura em centímetros é {altura*100:.0f}.")
    # Saída: Meu nome é John e tenho 30 anos e 1.80 de altura. Meu nome tem 4 letras. Minha idade é 31. A minha altura é 1.90. A minha idade em meses é 360. A minha altura em centímetros é 180.
    # Adicionamos a formatação de float com 2 casas decimais com o :.2f.
    # Adicionamos a função len() para contar o número de caracteres do nome.
    # Adicionamos a soma de idade + 1 para aumentar a idade em 1 ano.
    # Adicionamos a soma de altura + 0.1 para aumentar a altura em 0.1.
    # Adicionamos a multiplicação de idade * 12 para converter a idade em meses.
    # Adicionamos a multiplicação de altura * 100 para converter a altura em centímetros.
    # A formatação de float com 0 casas decimais com o :.0f.
    # O resultado é uma string formatada com os valores das variáveis, a função len() e a soma de idade + 1.

    # Exemplo 8:
    # nome = "John"
    # idade = 30
    # altura = 1.80
    # print(f"Meu nome é {nome} e tenho {idade} anos e {altura:.2f} de altura. Meu nome tem {len(nome)} letras. Minha idade é {idade+1}. A minha altura é {altura+0.1:.2f}. A minha idade em meses é {idade*12}. A minha altura em centímetros é {altura*100:.0f}. A minha idade em dias é {idade*365}.")
    # Saída: Meu nome é John e tenho 30 anos e 1.80 de altura. Meu nome tem 4 letras. Minha idade é 31. A minha altura é 1.90. A minha idade em meses é 360. A minha altura em centímetros é 180. A minha idade em dias é 10950.
    # Adicionamos a formatação de float com 2 casas decimais com o :.2f.
    # Adicionamos a função len() para contar o número de caracteres do nome.
    # Adicionamos a soma de idade + 1 para aumentar a idade em 1 ano.
    # Adicionamos a soma de altura + 0.1 para aumentar a altura em 0.1.
    # Adicionamos a multiplicação de idade * 12 para converter a idade em meses.
    # Adicionamos a multiplicação de altura * 100 para converter a altura em centímetros.
    # A formatação de float com 0 casas decimais com o :.0f.
    # Adicionamos a multiplicação de idade * 365 para converter a idade em dias.
    # O resultado é uma string formatada com os valores das variáveis, a função len() e a soma de idade + 1.

    # Exemplo 9:
    # nome = "John"
    # idade = 30
    # altura = 1.80
    # print(f"Meu nome é {nome} e tenho {idade} anos e {altura:.2f} de altura. Meu nome tem {len(nome)} letras. Minha idade é {idade+1}. A minha altura é {altura+0.1:.2f}. A minha idade em meses é {idade*12}. A minha altura em centímetros é {altura*100:.0f}. A minha idade em dias é {idade*365}. A minha altura em metros é {altura*100:.2f}.")
    # Saída: Meu nome é John e tenho 30 anos e 1.80 de altura. Meu nome tem 4 letras. Minha idade é 31. A minha altura é 1.90. A minha idade em meses é 360. A minha altura em centímetros é 180. A minha idade em dias é 10950. A minha altura em metros é 180.00.
    # Adicionamos a formatação de float com 2 casas decimais com o :.2f.
    # Adicionamos a função len() para contar o número de caracteres do nome.
    # Adicionamos a soma de idade + 1 para aumentar a idade em 1 ano.
    # Adicionamos a soma de altura + 0.1 para aumentar a altura em 0.1.
    # Adicionamos a multiplicação de idade * 12 para converter a idade em meses.
    # Adicionamos a multiplicação de altura * 100 para converter a altura em centímetros.
    # A formatação de float com 0 casas decimais com o :.0f.
    # Adicionamos a multiplicação de idade * 365 para converter a idade em dias.
    # Adicionamos a formatação de float com 2 casas decimais com o :.2f.
    # O resultado é uma string formatada com os valores das variáveis, a função len() e a soma de idade + 1.

    # Exemplo 10:
    # nome = "John"
    # idade = 30
    # altura = 1.80
    # print(f"Meu nome é {nome} e tenho {idade} anos e {altura:.2f} de altura. Meu nome tem {len(nome)} letras. Minha idade é {idade+1}. A minha altura é {altura+0.1:.2f}. A minha idade em meses é {idade*12}. A minha altura em centímetros é {altura*100:.0f}. A minha idade em dias é {idade*365}. A minha altura em metros é {altura*100:.2f}. A minha idade em anos é {idade/365:.2f}.")
    # Saída: Meu nome é John e tenho 30 anos e 1.80 de altura. Meu nome tem 4 letras. Minha idade é 31. A minha altura é 1.90. A minha idade em meses é 360. A minha altura em centímetros é 180. A minha idade em dias é 10950. A minha altura em metros é 180.00. A minha idade em anos é 0.32.
    # Adicionamos a formatação de float com 2 casas decimais com o :.2f.
    # Adicionamos a função len() para contar o número de caracteres do nome.
    # Adicionamos a soma de idade + 1 para aumentar a idade em 1 ano.
    # Adicionamos a soma de altura + 0.1 para aumentar a altura em 0.1.
    # Adicionamos a multiplicação de idade * 12 para converter a idade em meses.
    # Adicionamos a multiplicação de altura * 100 para converter a altura em centímetros.
    # A formatação de float com 0 casas decimais com o :.0f.
    # Adicionamos a multiplicação de idade * 365 para converter a idade em dias.
    # Adicionamos a formatação de float com 2 casas decimais com o :.2f.
    # Adicionamos a divisão de idade / 365 para converter a idade em anos.
    # O resultado é uma string formatada com os valores das variáveis, a função len() e a soma de idade + 1.    

    # Exemplo 11:
    # nome = "John"
    # idade = 30
    # altura = 1.80
    # print(f"Meu nome é {nome} e tenho {idade} anos e {altura:.2f} de altura. Meu nome tem {len(nome)} letras. Minha idade é {idade+1}. A minha altura é {altura+0.1:.2f}. A minha idade em meses é {idade*12}. A minha altura em centímetros é {altura*100:.0f}. A minha idade em dias é {idade*365}. A minha altura em metros é {altura*100:.2f}. A minha idade em anos é {idade/365:.2f}. A minha altura em pés é {altura*3.28:.2f}.")
    # Saída: Meu nome é John e tenho 30 anos e 1.80 de altura. Meu nome tem 4 letras. Minha idade é 31. A minha altura é 1.90. A minha idade em meses é 360. A minha altura em centímetros é 180. A minha idade em dias é 10950. A minha altura em metros é 180.00. A minha idade em anos é 0.32. A minha altura em pés é 6.00.
    # Adicionamos a formatação de float com 2 casas decimais com o :.2f.
    # Adicionamos a função len() para contar o número de caracteres do nome.
    # Adicionamos a soma de idade + 1 para aumentar a idade em 1 ano.
    # Adicionamos a soma de altura + 0.1 para aumentar a altura em 0.1.
    # Adicionamos a multiplicação de idade * 12 para converter a idade em meses.
    # Adicionamos a multiplicação de altura * 100 para converter a altura em centímetros.
    # A formatação de float com 0 casas decimais com o :.0f.
    # Adicionamos a multiplicação de idade * 365 para converter a idade em dias.
    # Adicionamos a formatação de float com 2 casas decimais com o :.2f.
    # Adicionamos a divisão de idade / 365 para converter a idade em anos.
    # Adicionamos a multiplicação de altura * 3.28 para converter a altura em pés.
    # O resultado é uma string formatada com os valores das variáveis, a função len() e a soma de idade + 1.

    # Exemplo 12:
    # nome = "John"
    # idade = 30
    # altura = 1.80 
    

    # print(f"Meu nome é {nome} e tenho {idade} anos e {altura:.2f} de altura. Meu nome tem {len(nome)} letras. Minha idade é {idade+1}. A minha altura é {altura+0.1:.2f}. A minha idade em meses é {idade*12}. A minha altura em centímetros é {altura*100:.0f}. A minha idade em dias é {idade*365}. A minha altura em metros é {altura*100:.2f}. A minha idade em anos é {idade/365:.2f}. A minha altura em pés é {altura*3.28:.2f}.")
    # Saída: Meu nome é John e tenho 30 anos e 1.80 de altura. Meu nome tem 4 letras. Minha idade é 31. A minha altura é 1.90. A minha idade em meses é 360. A minha altura em centímetros é 180. A minha idade em dias é 10950. A minha altura em metros é 180.00. A minha idade em anos é 0.32. A minha altura em pés é 6.00.
    # Adicionamos a formatação de float com 2 casas decimais com o :.2f.
    # Adicionamos a função len() para contar o número de caracteres do nome.
    # Adicionamos a soma de idade + 1 para aumentar a idade em 1 ano.
    # Adicionamos a soma de altura + 0.1 para aumentar a altura em 0.1.
    # Adicionamos a multiplicação de idade * 12 para converter a idade em meses.
    # Adicionamos a multiplicação de altura * 100 para converter a altura em centímetros.
    # A formatação de float com 0 casas decimais com o :.0f.
    # Adicionamos a multiplicação de idade * 365 para converter a idade em dias.
    # Adicionamos a formatação de float com 2 casas decimais com o :.2f.
    # Adicionamos a divisão de idade / 365 para converter a idade em anos.
    # Adicionamos a multiplicação de altura * 3.28 para converter a altura em pés.
    # O resultado é uma string formatada com os valores das variáveis, a função len() e a soma de idade + 1.

    # Exemplo 13:
    # nome = "John"
    # idade = 30
    # altura = 1.80 
    # peso = 70
   