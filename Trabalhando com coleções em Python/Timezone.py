# Como usar o time zone no Python:
# Exemplo de como definir o fuso horário e converter horários entre fusos horários.

# Definindo utc como o fuso horário padrão
import datetime
import pytz # type: ignore
utc = pytz.utc
timedelta = datetime.timedelta



# importando o pacote pytz para trabalhar com fusos horários

# Importando biblioteca de data e hora
from datetime import datetime, timedelta, timezone

# Definindo o fuso horário desejado     
now_utc = datetime.now(utc)
timezone = pytz.timezone('America/Sao_Paulo')
#pip install pytz
#pip install tzlocal
#pip install python-dateutil

# Obtendo a hora atual no fuso horário UTC
now_utc = datetime.now(utc)

# Exibindo a hora atual no fuso horário UTC
print(now_utc)   # 2021-10-12 18:30:00+00:00

# Convertendo a hora atual UTC para o fuso horário definido
now_timezone = now_utc.astimezone(timezone)

# Exibindo a hora atual no fuso horário definido
print(now_timezone)   # 2021-10-12 15:30:00-03:00

# Exibindo a hora atual no fuso horário definido formatada
print(now_timezone.strftime('%Y-%m-%d %H:%M:%S %Z%z'))   # 2021-10-12 15:30:00 -0300

# Exemplo de como definir o fuso horário UTC e converter horários entre fusos horários.
# Definindo o fuso horário

timezone = pytz.timezone('America/Sao_Paulo')
# Obtendo a hora atual no fuso horário UTC
now_utc = datetime.datetime.now(utc) # type: ignore
# Exibindo a hora atual no fuso horário UTC
print(now_utc)   # 2021-10-12 18:30:00+00:00
# Convertendo a hora atual UTC para o fuso horário definido
now_timezone = now_utc.astimezone(timezone)
# Exibindo a hora atual no fuso horário definido
print(now_timezone)   # 2021-10-12 15:30:00-03:00
# Exibindo a hora atual no fuso horário definido formatada
print(now_timezone.strftime('%Y-%m-%d %H:%M:%S %Z%z'))   # 2021-10-12 15:30:00 -0300

# Obtendo a hora atual no fuso horário definido
now = timezone.localize(datetime.datetime.now()) # type: ignore

# Exibindo a hora atual no fuso horário definido
print(now)   # 2021-10-12 15:30:00-03:00
# Convertendo a hora atual para o fuso horário UTC
now_utc = now.astimezone(pytz.utc)
print(now_utc)   # 2021-10-12 18:30:00+00:00    
# Convertendo a hora atual UTC para o fuso horário definido
now_timezone = now_utc.astimezone(timezone)
print(now_timezone)   # 2021-10-12 15:30:00-03:00 
# Exibindo a hora atual no fuso horário definido
print(now_timezone.strftime('%Y-%m-%d %H:%M:%S %Z%z'))   # 2021-10-12 15:30:00 -0300    
# Definindo o fuso horário UTC
utc = pytz.utc
# Convertendo a hora atual UTC para o fuso horário UTC
now_utc = now.astimezone(utc)
print(now_utc)   # 2021-10-12 18:30:00+00:00        

