# Operadores de identidade

# Operador de identidade é o operador de igualdade que compara o endereço de memória dos objetos.

# Exemplo:

a = 10
b = 10

print(a is b) # True

# O operador de identidade retorna True se os objetos apontam para a mesma localização na memória.

# Exemplo:

a = 10
b = 20

print(a is b) # False

# O operador de identidade retorna False se os objetos apontam para diferentes localizações na memória.     
# O operador de identidade é útil para comparar se dois objetos são o mesmo objeto, mesmo que tenham valores diferentes.
# Exemplo:

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b) # False

# O operador de identidade retorna False porque a lista a e b são objetos diferentes na memória.    
# Exemplo:

a = 10
b = a

print(a is b) # True

# O operador de identidade retorna True porque a e b apontam para a mesma localização na memória.   
