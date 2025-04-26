# Lidando com, data,hora e fuso horário
# Módulo datetime
# O módulo datetime do Python fornece classes para trabalhar com datas, horas e fusos horários.
# Aqui, vamos aprender a trabalhar com datas, horas e fusos horários no Python.
# Importando o módulo datetime  
from datetime import datetime, time, timezone

# Obtendo a data e hora atual

now = datetime.datetime.now()
print("Data e hora atual:", now)

# Obtendo a data atual
today = datetime.date.today()
print("Data atual:", today)

# Módulo timezone
# O módulo timezone do Python fornece classes para trabalhar com fusos horários.
# Aqui, vamos aprender a trabalhar com fusos horários no Python.
# Importando o módulo timezone


# Obtendo o fuso horário local
timezone = pytz.timezone('America/Sao_Paulo') # type: ignore
print("Fuso horário local:", timezone)

# Convertendo uma data para um fuso horário específico
date = datetime.datetime(2021, 10, 1, 10, 30, tzinfo=timezone)
print("Data convertida para fuso horário:", date)

# Convertendo uma data em um fuso horário para o fuso horário local
date = date.astimezone()
print("Data convertida para fuso horário local:", date)


# Obtendo o fuso horário atual
timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
print("Fuso horário atual:", timezone)

# Convertendo uma data para o fuso horário atual
date = datetime.datetime(2021, 10, 1, 10, 30, tzinfo=timezone)
print("Data convertida para fuso horário atual:", date)

# Convertendo uma data em um fuso horário para o fuso horário atual
date = date.astimezone()
print("Data convertida para fuso horário atual:", date) 

# Conclusão
# Neste artigo, aprendemos a trabalhar com datas, horas e fusos horários no Python. Aprendemos a importar o módulo datetime e o módulo timezone, e a obter a data e hora atual, a data atual, o fuso horário local, o fuso horário atual e a data convertida para um fuso horário específico ou para o fuso horário atual.  

# Método today()
# O método today() do módulo datetime retorna a data atual. 
# Método now()
# O método now() do módulo datetime retorna a data e hora atual. 
# Método astimezone()
# O método astimezone() do módulo datetime converte uma data para um fuso horário específico ou para o fuso horário atual. 
# Método tzinfo
# O atributo tzinfo de uma data representa o fuso horário. 
# Módulo pytz
# O módulo pytz do Python fornece classes para trabalhar com fusos horários. 
# Aqui, vamos aprender a trabalhar com fusos horários no Python. 
# Importando o módulo pytz 
# Obtendo o fuso horário local
timezone = pytz.timezone('America/Sao_Paulo') # type: ignore
print("Fuso horário local:", timezone)

# Convertendo uma data para um fuso horário específico
date = datetime.datetime(2021, 10, 1, 10, 30, tzinfo=timezone)
print("Data convertida para fuso horário:", date)

# Obtendo o fuso horário atual
timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
print("Fuso horário atual:", timezone)

# Conclusão
# Objeto time ntptime()
# O objeto time do módulo ntptime() do Python fornece funções para trabalhar com datas e horas. 
# Aqui, vamos aprender a trabalhar com datas e horas no Python. 
# Importando o módulo time 
# Obtendo a data e hora atual
now = time.time()
print("Data e hora atual:", now)

# Conclusão
# Neste artigo, aprendemos a trabalhar com datas e horas no Python. Aprendemos a importar o módulo time e a obter a data e hora atual.

# Método time delta()
# O método timedelta() do módulo datetime retorna um objeto timedelta que representa uma quantidade de tempo. 
# Método strftime()
# O método strftime() do módulo datetime retorna uma string formatada de uma data. 
# Método strptime()
# O método strptime() do módulo datetime retorna uma data a partir de uma string formatada. 
# Método utcfromtimestamp()
# O método utcfromtimestamp() do módulo datetime retorna a data e hora UTC a partir de um timestamp. 
# Método utcnow()
# O método utcnow() do módulo datetime retorna a data e hora UTC atual. 
# Método fromtimestamp()
# O método fromtimestamp() do módulo datetime retorna a data e hora local a partir de um timestamp. 
# Método now()
# O método now() do módulo datetime retorna a data e hora local atual. 
# Método utc()
# O método utc() do módulo datetime retorna a data e hora UTC. 
# Método replace()
# O método replace() do módulo datetime retorna uma cópia da data com um novo valor. 
# Método astimezone()
# O método astimezone() do módulo datetime converte uma data para um fuso horário específico. 
# Método tzinfo
# O atributo tzinfo de uma data representa o fuso horário. 
# Módulo pytz
# O módulo pytz do Python fornece classes para trabalhar com fusos horários. 
# Aqui, vamos aprender a trabalhar com fusos horários no Python. 
# Importando o módulo pytz 
# Obtendo o fuso horário local
timezone = pytz.timezone('America/Sao_Paulo') # type: ignore
print("Fuso horário local:", timezone)

# Convertendo uma data para um fuso horário específico
date = datetime.datetime(2021, 10, 1, 10, 30, tzinfo=timezone)
print("Data convertida para fuso horário:", date)

# Conclusão