# Criando um sistema bancário com Python
 

Depositar = 5000
Sacar = 2000
Saldo = 3000
Extrato = "Deposito: R$5000\nSaque: R$2000\nSaldo: R$3000"

print("Deposito:5000") ,
print("Saque:2000") 
print("Saldo:3000") 
print("Extrato: 3000")

# Adicionando a função de depositar
def deposito (Valor):
    global Deposito
    Deposito += 5000
    Saldo += 5000
    Saldo  += 5000
    print("Deposito realizado com sucesso!")
    print("Novo saldo: R$", Saldo)
    print("Extrato: ", Extrato)

# Adicionando a função de sacar 
def saque (Valor):
    global Sacar
    Sacar += 2000
    Saldo -= 2000
    print("Saque realizado com sucesso!")
    print("Novo saldo: R$", Saldo)
    print("Extrato: ", Extrato)

