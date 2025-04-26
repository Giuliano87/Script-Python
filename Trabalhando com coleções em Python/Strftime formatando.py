# Como usar o método strftime() para formatar datas e horas em Python

# Strptime() - Converte uma string de data e hora em um objeto datetime
# Strftime() - Converte um objeto datetime em uma string de data e hora formatada.

from datetime import datetime, timedelta, timezone, timedelta # Importando o módulo datetime

# Exemplo 1: Formatação de data e hora
data = datetime.now(timezone)(timedelta(hours=3))    # Retorna a data e hora atual do sistema
data_formatada = data.strftime('%d/%m/%Y %H:%M:%S')

print(data_formatada)    # Saída: 20/05/2021 10:30:00

# Exemplo 2: Formatação de data

# Objeto datetime
data_hora = datetime.datetime.now()
# Formatação de data
data_formatada = data_hora.strftime('%d/%m/%Y')
data_formatada = data_hora.strftime('%d/%m/%Y %H:%M:%S')

print(data_formatada)

# Exemplo 2: Formatação de data

# Objeto datetime
data_hora = datetime.datetime.now()

# Formatação de data
data_formatada = data_hora.strftime('%d/%m/%Y')

print(data_formatada)

# Exemplo 3: Formatação de hora
datetime.now(timezone.utc)(timedelta(hours=3))    # Retorna a data e hora atual do sistema


# Exemplo 1: Formatação de data e hora
data_hora = datetime.now()


# Formatação de data e hora
data_formatada = data_hora.strftime('%d/%m/%Y %H:%M:%S')

print(data_formatada)

# Exemplo 2: Formatação de data

# Objeto datetime
data_hora = datetime.datetime.now()

# Formatação de data
data_formatada = data_hora.strftime('%d/%m/%Y')

print(data_formatada)

# Exemplo 3: Formatação de hora

# Objeto datetime
data_hora = datetime.datetime.now()

# Formatação de hora
hora_formatada = data_hora.strftime('%H:%M:%S')

print(hora_formatada)

# String parse time, como usar?

# O método strptime() é usado para converter uma string de data e hora em um objeto datetime.   
# Ele recebe dois argumentos: a string de data e hora e um formato de data e hora.

# Exemplo:

# String de data e hora
data_hora_str = '20/05/2021 10:30:00'

# Formato de data e hora
formato = '%d/%m/%Y %H:%M:%S'

# Converte string de data e hora para objeto datetime
data_hora_obj = datetime.datetime.strptime(data_hora_str, formato)

print(data_hora_obj)     # Saída: 2021-05-20 10:30:00   

from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = data_hora_atual.strftime('%d/%m/%Y %H:%M:%S')

print(data_hora_str)     # Saída: 20/05/2021 10:30:00       

# Exemplo 4: Formatação de data e hora com strftime()        
# O método strftime() é usado para converter um objeto datetime em uma string de data e hora formatada.   
# Ele recebe um argumento: o formato da string de data e hora.

# Exemplo:

# Objeto datetime
data_hora = datetime.datetime.now()

# Formato de data e hora
formato = '%d/%m/%Y %H:%M:%S'

# Converte objeto datetime para string de data e hora formatada
data_hora_str = data_hora.strftime(formato)

print(data_hora_str)     # Saída: 20/05/2021 10:30:00   

# Exemplo 5: Formatação de data com strftime()

# Objeto datetime
data_hora = datetime.datetime.now()

# Formato de data
formato = '%d/%m/%Y'

# Converte objeto datetime para string de data formatada
data_str = data_hora_atual = datetime.now()
data_hora_str = data_hora.strftime(formato)
mascara_ptbr = '%d/%m/%Y'
data_hora_str = datetime.datetime.strptime(data_hora_str, mascara_ptbr).strftime(formato)
print(data_hora_str)     # Saída: 20/05/2021   
# Exemplo 5: Formatação de data com strftime() e strptime() com mascara de data     

# String de data
data_str = '20/05/2021'

# Formato de data
formato = '%d/%m/%Y'

# Converte string de data para objeto datetime
data_obj = datetime.datetime.strptime(data_str, formato)

# Formato de data
formato = '%d/%m/%Y'

# Converte objeto datetime para string de data formatada
data_str = data_obj.strftime(formato)

print(data_str)     # Saída: 20/05/2021     
# Exemplo 5: Formatação de data com strftime() e strptime() com mascara de data     

# String de data
data_str = '20/05/2021'

# Formato de data
formato = '%d/%m/%Y'

# Converte string de data para objeto datetime
data_obj = datetime.datetime.strptime(data_str, formato)

# Formato de data
formato = '%d/%m/%Y'

# Converte objeto datetime para string de data formatada
data_str = data_obj.strftime(formato)

print(data_str)     # Saída: 20/05/2021         
# Exemplo 5: Formatação de data com strftime() e strptime() com mascara de data     

# String de data
data_str = '20/05/2021'

# Formato de data
formato = '%d/%m/%Y'

# Converte string de data para objeto datetime
data_obj = datetime.datetime.strptime(data_str, formato)

print(type(data_convertida)) # type: ignore
# Saída: <class 'datetime.datetime'>

# Formato de data
formato = '%d/%m/%Y'

# Converte objeto datetime para string de data formatada
data_str = data_obj.strftime(formato)
# Exemplo 6: Formatação de hora com strftime()

# Objeto datetime
data_hora = datetime.datetime.now()

# Formato de hora
formato = '%H:%M:%S'

# Converte objeto datetime para string de hora formatada
hora_str = data_hora.strftime(formato)

print(hora_str)     # Saída: 10:30:00   

# Exemplo 7: Formatação de data e hora com strftime() e strptime()

# String de data e hora
data_hora_str = '20/05/2021 10:30:00'

# Formato de data e hora
formato = '%d/%m/%Y %H:%M:%S'

# Converte string de data e hora para objeto datetime
data_hora_obj = datetime.datetime.strptime(data_hora_str, formato)

# Formato de data e hora
