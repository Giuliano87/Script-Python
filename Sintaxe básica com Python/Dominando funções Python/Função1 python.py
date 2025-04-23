# Função com retorno de valor
        
def soma_sub(x, y):
    return x + y, x - y
print(soma_sub(2, 3))   # Retorna uma tupla com os resultados da soma e subtração    
def soma(x, y):
    return x + y
def sub(x, y):
    return x - y
def mult(x, y):
    return x * y
def div(x, y):
    return x / y    
print(soma(2, 3))
print(sub(5, 3))
print(mult(2, 4))
print(div(10, 2))

# Criar carro com funções
def carro(marca, modelo, cor, ano):
    print("Marca:", marca)  
    print("Modelo:", modelo)
    print("Cor:", cor)
    print("Ano:", ano)

carro("Honda", "Civic", "Prata", 2021)   # Chamando a função

# Argumentos opcionais
def carro_op(marca, modelo, cor, ano=2021):
    print("Marca:", marca)  
    print("Modelo:", modelo)
    print("Cor:", cor)
    print("Ano:", ano)  
carro_op("Ford", "Mustang", "Azul")   # Chamando a função com argumentos opcionais
carro_op("Chevrolet", "Camaro", "Preto", 2020)   # Chamando a função com argumentos opcionais
# Função com retorno de valor
def soma_sub(x, y):
    return x + y, x - y
print(soma_sub(2, 3))   # Retorna uma tupla com os resultados da soma e subtração    

# Função com parâmetro de palavra-chave
def carro_kw(marca, modelo, **kwargs):
    print("Marca:", marca)  
    print("Modelo:", modelo)
    for key, value in kwargs.items():
        print(key, ":", value)
carro_kw("Toyota", "Corolla", cor="Prata", ano=2021)   # Chamando a função com parâmetro de palavra-chave   

# Função com argumentos posicionais e nomeados
def carro_pos_nome(marca, modelo, *args, cor, ano=2021):
    print("Marca:", marca)  
    print("Modelo:", modelo)
    for arg in args:
        print("Argumento posicional:", arg)
    print("Cor:", cor)
    print("Ano:", ano)

    # Keyword only 
    def carro_pos_nome_kw(marca, modelo, *args, **kwargs):
        print("Marca:", marca)  
        print("Modelo:", modelo)
        for arg in args:
            print("Argumento posicional:", arg)
        for key, value in kwargs.items():
            print(key, ":", value)
    carro_pos_nome_kw("Honda", "Accord", "4 portas", cor="Prata", ano=2021)   # Chamando a função com argumentos posicionais e nomeados
    carro_pos_nome("Ford", "Mustang", "4 portas", cor="Azul")   # Chamando a função com argumentos posicionais e nomeados

    # Função com argumentos posicionais e nomeados e com retorno de valor
    def soma_sub_pos_nome(x, y, *args, **kwargs):
        return x + y, x - y, args, kwargs
    print(soma_sub_pos_nome(2, 3, "4 portas", cor="Prata", ano=2021))   # Retorna uma tupla com os resultados da soma, subtração, argumentos posicionais e nomeados 

    #declaração invalida 
    # def carro_pos_nome_errado(marca, modelo, *args, cor, ano=2021, **kwargs):
    #     print("Marca:", marca)  
    #     print("Modelo:", modelo)
    #     for arg in args:
    #         print("Argumento posicional:", arg)
    #     print("Cor:", cor)
    #     print("Ano:", ano)
    # carro_pos_nome_errado("Honda", "Accord", "4 portas", cor="Prata", ano=2021, modelo="Civic")   # Chamando a função com argumentos posicionais e nomeados
    # Função com argumentos posicionais e nomeados e com retorno de valor
    # def soma_sub_pos_nome_errado(x, y, *args, **kwargs):
    #     return x + y, x - y, args, kwargs
    # print(soma_sub_pos_nome_errado(2, 3, "4 portas", cor="Prata", ano=2021, modelo="Civic"))   # Retorna uma tupla com os resultados da soma, subtração, argumentos posicionais e nomeados
    # Função com argumentos posicionais e nomeados e com retorno de valor
    # def soma_sub_pos_nome_errado(x, y, *args, **kwargs):
    #     return x + y, x - y, args, kwargs
    # print(soma_sub_pos_nome_errado(2, 3, "4 portas", cor="Prata", ano=2021, modelo="Civic"))   # Retorna uma tupla com os resultados da soma, subtração, argumentos posicionais e nomeados

    



