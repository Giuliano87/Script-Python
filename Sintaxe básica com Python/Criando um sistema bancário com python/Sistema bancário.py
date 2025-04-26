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

# Extrato do banco
def extrato():
    print("Extrato: ", Extrato)

# Menu de opções
def menu():
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Sair")
    opcao = int(input("Digite a opção: "))
    if opcao == 1:
        deposito(Deposito)
    elif opcao == 2:
        saque(Sacar)
    elif opcao == 3:
        extrato()
    elif opcao == 4:
        exit()
    else:
        print("Opção inválida!")
        menu()

menu()  