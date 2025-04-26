# time delta.py
# Como usar timedelta em Python?

from datetime import datetime, timedelta

# Criando um objeto datetime
now = datetime.now()

# Criando um objeto timedelta
one_day = timedelta(days=1)

# Adicionando um dia a um objeto datetime   
yesterday = now - one_day

# Exibindo o resultado
print(yesterday) # 2021-10-29 16:30:23.546489
# Exibindo o tipo do objeto
print(type(yesterday)) # <class 'datetime.datetime'>    
# Criando um objeto timedelta com horas, minutos e segundos
one_hour = timedelta(hours=1)

# Adicionando uma hora a um objeto datetime
one_hour_ago = now - one_hour

# Exibindo o resultado
print(one_hour_ago) # 2021-10-29 15:30:23.546489
# Exibindo o tipo do objeto
print(type(one_hour_ago)) # <class 'datetime.datetime'> 
# Criando um objeto timedelta com segundos
one_second = timedelta(seconds=1)

# Adicionando um segundo a um objeto datetime
one_second_ago = now - one_second

# Exibindo o resultado
print(one_second_ago) # 2021-10-29 16:30:22.546489
# Exibindo o tipo do objeto
print(type(one_second_ago)) # <class 'datetime.datetime'>   
# Criando um objeto timedelta com microsegundos
one_microsecond = timedelta(microseconds=1)

# Adicionando um microsegundo a um objeto datetime
one_microsecond_ago = now - one_microsecond

# Exibindo o resultado
print(one_microsecond_ago) # 2021-10-29 16:30:23.546488
# Exibindo o tipo do objeto 
print(type(one_microsecond_ago)) # <class 'datetime.datetime'>  
# Adicionando vários objetos timedelta
two_days = timedelta(days=2)
three_hours = timedelta(hours=3)
five_minutes = timedelta(minutes=5)

# Adicionando vários objetos timedelta a um objeto datetime
two_days_three_hours_five_minutes_ago = now - two_days - three_hours - five_minutes

# Exibindo o resultado
print(two_days_three_hours_five_minutes_ago) # 2021-10-27 13:25:23.546489
# Exibindo o tipo do objeto
print(type(two_days_three_hours_five_minutes_ago)) # <class 'datetime.datetime'>    
 
 # Aluguel de carro 
# Criando um objeto datetime para o aluguel
rent_date = datetime(2021, 10, 29, 10, 0, 0)

# Criando um objeto timedelta para o aluguel
rent_time = timedelta(hours=1)

# Adicionando o aluguel a um objeto datetime
rent_date_plus_rent_time = rent_date + rent_time

# Exibindo o resultado
print(rent_date_plus_rent_time) # 2021-10-29 11:00:00
# Exibindo o tipo do objeto
print(type(rent_date_plus_rent_time)) # <class 'datetime.datetime'> 

# Criando um objeto datetime para a devolução
return_date = datetime(2021, 10, 30, 17, 0, 0)

# Verificando se o carro foi alugado até a data de devolução
if rent_date_plus_rent_time <= return_date:
    print("O carro está alugado até a data de devolução.")
else:
    print("O carro não está alugado até a data de devolução.")
    # Exibindo o resultado
    print(rent_date_plus_rent_time) # 2021-10-29 11:00:00
    # Exibindo o tipo do objeto
    print(type(rent_date_plus_rent_time)) # <class 'datetime.datetime'>
    # Exibindo o resultado
    print(return_date) # 2021-10-30 17:00:00
    # Exibindo o tipo do objeto
    print(type(return_date)) # <class 'datetime.datetime'>  

    from datetime import datetime, timedelta

    tipo_carro = "P" # P,M,G
    tempo_pequeno = 30
    tempo_médio = 45
    tempo_grande = 60
    data_atual = datetime.now()

    if tipo_carro == "P":
        data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    elif tipo_carro == "P":
        data_estimada = data_atual + timedelta(minutes=tempo_médio)
    else:
        data_estimada = data_atual + timedelta(minutes=tempo_grande)

    print(f"Data estimada de devolução: {data_estimada.strftime('%d/%m/%Y %H:%M:%S')}") # 29/10/2021 11:30:00
    # Exibindo o resultado
    print(data_estimada) # 2021-10-29 11:30:00
    # Exibindo o tipo do objeto
    print(type(data_estimada)) # <class 'datetime.datetime'>
    # Verificando se o carro está alugado até a data de devolução
    if rent_date_plus_rent_time <= data_estimada:
        print("O carro está alugado até a data de devolução.")
    else:
        print("O carro não está alugado até a data de devolução.")  
        # Exibindo o resultado
        print(rent_date_plus_rent_time) # 2021-10-29 11:00:00
        # Exibindo o tipo do objeto
        print(type(rent_date_plus_rent_time)) # <class 'datetime.datetime'>
        # Exibindo o resultado
        print(data_estimada) # 2021-10-29 11:30:00
        # Exibindo o tipo do objeto
        print(type(data_estimada)) # <class 'datetime.datetime'>
 
 # Criando um objeto timedelta para o aluguel
rent_time = timedelta(hours=1)

# Adicionando o aluguel a um objeto datetime
rent_date_plus_rent_time = rent_date + rent_time

# Exibindo o resultado
print(rent_date_plus_rent_time) # 2021-10-29 11:00:00
# Exibindo o tipo do objeto
print(type(rent_date_plus_rent_time)) # <class 'datetime.datetime'> 

 # Criando um objeto datetime para a devolução
return_date = datetime(2021, 10, 30, 17, 0, 0)

 # Verificando se o carro foi alugado até a data de devolução
if rent_date_plus_rent_time <= return_date:
    print("O carro está alugado até a data de devolução.")
else:
    print("O carro não está alugado até a data de devolução.")
    # Exibindo o resultado
    print(rent_date_plus_rent_time) # 2021-10-29 11:00:00
    # Exibindo o tipo do objeto
    print(type(rent_date_plus_rent_time)) # <class 'datetime.datetime'>
    # Exibindo o resultado
    print(return_date) # 2021-10-30 17:00:00
    # Exibindo o tipo do objeto
    print(type(return_date)) # <class 'datetime.datetime'>  

    from datetime import datetime, timedelta

    tipo_carro = "P" # P,M,G
    tempo_pequeno = 30
    tempo_médio = 45
    tempo_grande = 60
    data_atual = datetime.now()

    if tipo_carro == "P":
        data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    elif tipo_carro == "P":
        data_estimada = data_atual + timedelta(minutes=tempo_médio)
    else:
        data_estimada = data_atual + timedelta(minutes=tempo_grande)

    print(f"Data estimada de devolução: {data_estimada.strftime('%d/%m/%Y %H:%M:%S')}") # 29/10/2021 11:30:00
    # Exibindo o resultado
    print(data_estimada) # 2021-10-29 11:30:00
    # Exibindo o tipo do objeto
    print(type(data_estimada)) # <class 'datetime.datetime'>
    # Verificando se o carro está alugado até a data de devolução
    if rent_date_plus_rent_time <= data_estimada:
        print("O carro está alugado até a data de devolução.")
    else:
        print("O carro não está alugado até a data de devolução.")  
        # Exibindo o resultado
        print(rent_date_plus_rent_time) # 2021-10-29 11:00:00
        # Exibindo o tipo do objeto
        print(type(rent_date_plus_rent_time)) # <class 'datetime.datetime'>
        # Exibindo o resultado
        print(data_estimada) # 2021-10-29 11:30:00
        # Exibindo o tipo do objeto
        print(type(data_estimada)) # <class 'datetime.datetime'>    