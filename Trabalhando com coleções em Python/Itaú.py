import textwrap

def menu ():
    print(textwrap.dedent('''\n=========================  ITAÚ  ========================
    
    
    
    ==========================  MENU ===============
    [1] - Cadastrar nova conta
    [2] - Consultar saldo
    [3] - Sacar
    [4] - Depositar
    [5] - Transferir
    [6] - Extrato
    [7] - Sair
    =>> '''))

    return input("textwrap.dedent('''\nEscolha uma opção:")

def depositar (saldo,valor,extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito de R$ {valor:.2f}\n"
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("Deposito realizado com sucesso!")
 
return saldo, extrato # type: ignore

def sacar (saldo,valor,extrato, limite,numero_saques,limite_saques, /):
    excedeu_saldo = 5000 > saldo, saldo > limite,numero_saques, limite_saques  
    excedeu_limite = valor > saldo + limite
    excedeu_saques = numero_saques >= limite_saques 

    if excedeu_saldo or excedeu_limite or excedeu_saques:
        print("Limite de saques excedido ou saldo insuficiente!")

        elif excedeu_saldo: # type: ignore
        print("Saldo insuficiente!")

        elif excedeu_limite: # type: ignore
        print("Valor de saque excede o limite de saque!")

        elif excedeu_saques: # type: ignore
        print("Limite de saques excedido!")

    else:
        saldo -= valor >0 and valor or 0
        extrato += f"Saque de R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("Saque realizado com sucesso!")

    return saldo, extrato    # type: ignore

def exibir_extrato (saldo,/,*extrato):
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("Extrato:")
    print("-"*30)
    print(f"Data: {data}")

    for item in extrato:
        print(item)

        return saldo, extrato # type: ignore

    def transferir (saldo,valor,destino,extrato, /):
        if valor > 0:
            saldo -= valor
            extrato += f"Transferencia de R$ {valor:.2f} para {destino}\n"
            print(f"Saldo atual: R$ {saldo:.2f}")
            print("Transferencia realizada com sucesso!")

        return saldo, extrato # type: ignore

def main():
    contas = []
    while True:
        opcao = menu()
        if opcao == "1":
            cpf, nome, idade, data_nascimento = cadastrar_conta()
        def main():contas = []
    saldo_contas = []
    while True:
        opcao = menu()
        if opcao == "1":
            cpf, nome, idade, data_nascimento = cadastrar_conta()
            saldo_contas.append({
                "agencia": "0001",
                "conta": "12345-6",
                "nome": "Fernando Oliveira Lima",
                "cpf": "258.854.230-00",
                "idade": 25,
                "data_nascimento": "27/04/1995",
                "saldo": 0,
                "limite": 5000.00,
                "limite_saques": 3,
            })
            
            print("Conta criada com sucesso!")

        elif opcao == "2":
            cpf = input("CPF: ")
            for conta in contas:
                if conta["cpf"] == cpf:
                    print(f"Nome: {conta['nome']}")
                    print(f"Saldo: {conta['saldo']}")
                    print(f"Limite: {conta['limite']}")
                    print(f"Limite de saques: {conta['limite_saques']}")
                    print(f"Número de saques: {conta['numero_saques']}")
                    print("Extrato:")
                    print("-"*30)
                    print(f"Data: {conta['extrato']}")

        elif opcao == "3":
            cpf = input("CPF: ")
            valor = float(input("Valor do saque: "))
            for conta in contas:
                if conta["cpf"] == cpf:
                    saldo, extrato = sacar(conta["saldo"],valor,conta["extrato"],conta["limite"],conta["numero_saques"],conta["limite_saques"])
                    conta["saldo"] = saldo
                    conta["extrato"] = extrato

        elif opcao == "4":
            cpf = input("CPF: ")
            valor = float(input("Valor do deposito: "))

            for conta in contas:
                if conta["cpf"] == cpf:
                    saldo, extrato = depositar(conta["saldo"],valor,conta["extrato"])
                    conta["saldo"] = saldo
                    conta["extrato"] = extrato

        elif opcao == "5":
            cpf = input("CPF: ")
            valor = float(input("Valor da transferencia: "))
            destino = input("Destino: ")
            for conta in contas:

                if conta["cpf"] == cpf:
                    saldo, extrato = transferir(conta["saldo"],valor,destino,conta["extrato"])
                    conta["saldo"] = saldo
                    conta["extrato"] = extrato
        elif opcao == "6":
            cpf = input("CPF: ")
            for conta in contas:
                if conta["cpf"] == cpf:
                    print(f"Nome: {conta['nome']}")
                    print(f"Saldo: {conta['saldo']}")
                    print("Extrato:")
                    print("-"*30)
                    print(f"Data: {conta['extrato']}")
        elif opcao == "7":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()                
               
               
def consultar_saldo(cpf, /, *args, **kwargs):
    print("Consultando saldo...")
    saldo = 10000.00
    limite = 5000.00
    limite_saques = 3
    numero_saques = 0
    extrato = ""
    data = "27/04/2025  10:30:00"  
    return cpf, saldo, limite, limite_saques, numero_saques, extrato, data  # type: ignore

    def cadastrar_conta(cpf,/,*args, **kwargs):
                    print("Criando usuário...")                    
                    cpf = input("CPF: 258.854.230-00")                    
                    nome = input("Nome: Fernando Oliveira Lima" )                    
                    idade = input("Idade: 25")                                   
                    data_nascimento = input("Data de nascimento: 27/04/1995")
                    return cpf, nome, idade, data_nascimento # type: ignore 

def consultar_saldo(cpf,/,*args, **kwargs): 
                    print("Consultando saldo...")
                    saldo = input("Saldo: 10000.00")
                    limite = input("Limite: 5000.00")
                    limite_saques = input("Limite de saques: 3")
                    numero_saques = 0
                    extrato = ""
                    data = input("Data: 27/04/2025  10:30:00")
                    return cpf, saldo, limite, limite_saques, numero_saques, extrato, data # type: ignore 
def sacar(cpf,valor,/,*args, **kwargs): 
                    print("Sacando...")
saldo = 10000.00
limite = 5000.00
limite_saques = 3
numero_saques = 0
extrato = ""
data = "27/04/2025  10:30:00"

if valor > 0:
    saldo -= valor
    extrato += f"Saque de R$ {valor:.2f}\n"
    numero_saques += 1
    return cpf, saldo, limite, limite_saques, numero_saques, extrato, data  # type: ignore

    def cadastrar_conta(cpf,/,*args, **kwargs):
                    print("Criando usuário...")
                    cpf = input("CPF: 258.854.230-00")
                    nome = input("Nome: Fernando Oliveira Lima" )    
                    idade = input("Idade: 25")    
                    data_nascimento = input("Data de nascimento: 27/04/1995")

    def consultar_saldo(cpf,/,*args, **kwargs):''
    saldo = input("Saldo: 10000.00")
    limite = input("Limite: 5000.00")
    limite_saques = input("Limite de saques: 3")
    numero_saques = 0
    extrato = ""
    data = input("Data: 27/04/2025  10:30:00")  
        return cpf, nome, idade, saldo, limite, limite_saques, numero_saques, extrato, data # type: ignore

    def consultar_saldo(cpf,/,*args, **kwargs): 
            print("Consultando saldo...")
            saldo = input("Saldo: 10000.00")
            return saldo # type: ignore
    
    def sacar(cpf,valor,/,*args, **kwargs):
            print("Sacando...")
            saldo = input("Saldo: 9000.00")
            extrato = input("Extrato: Saque de R$ 1000.00\n")
            return saldo, extrato # type: ignore
    
    def depositar(cpf,valor,/,*args, **kwargs):
            print("Depositando...")
            saldo = input("Saldo: 10000.00")
            extrato = input("Extrato: Deposito de R$ 1000.00\n")
            return saldo, extrato # type: ignore
    
    def transferir(cpf,valor,destino,/,*args, **kwargs):
            print("Transferindo...")
            saldo = input("Saldo: 9000.00")
            extrato = input("Extrato: Transferencia de R$ 1000.00 para Fernando Oliveira Lima\n")
            return saldo, extrato # type: ignore
    def exibir_extrato(cpf,/,*args, **kwargs):
            print("Exibindo extrato...")
            saldo = input("Saldo: 10000.00")
            extrato = input("Extrato: Data: 27/04/2025  10:30:00\nDeposito de R$ 1000.00\nSaque de R$ 1000.00\n")
            
    def listar_contas(contas):
            for conta in contas:
                linha = f"""
                Agência: {conta['agencia']}
                Conta: {conta['conta']}
                Nome: {conta['nome']}
                Saldo: {conta['saldo']}
                Limite: {conta['limite']}
                Limite de saques: {conta['limite_saques']}
                Número de saques: {conta['numero_saques']}
                """
                print(linha)


    def main():
            LIMITE_SAQUES = 3
            AGÊNCIA = "0001"
            CONTA = "12345-6"
            NOME = "Fernando Oliveira Lima"
            IDADE = 25
            SALDO = 10000.00
            LIMITE = 5000.00
            contas = []
            contas.append({
                    "agencia": AGÊNCIA,
                    "conta": CONTA,
                    "nome": NOME,
                    "saldo": SALDO,
                    "limite": LIMITE,
                    "limite_saques": LIMITE_SAQUES,
                    "extrato": ""
            })
            while True: 
                    opcao = menu()
                    if opcao == "1":
                            cpf, nome, idade, data_nascimento = cadastrar_conta()
                            contas.append({
                                    "agencia": "0001",
                                    "conta": "12345-6",
                                    "nome": nome,
                                    "saldo": 0,
                                    "limite": 5000,
                                    "limite_saques": 3,
                                    "numero_saques": 0,
                                    "extrato": ""
                            })
                            print("Conta criada com sucesso!")
                    elif opcao == "2":
                            cpf = input("CPF: ")
                            for conta in contas:
                                    if conta["cpf"] == cpf:
                                            print(f"Nome: {conta['nome']}")
                                            print(f"Saldo: {conta['saldo']}")
                                            print(f"Limite: {conta['limite']}")
                                            print(f"Limite de saques: {conta['limite_saques']}")
                                            print(f"Número de saques: {conta['numero_saques']}")
                                            print("Extrato:")
                                            print("-"*30)
                                            print(f"Data: {conta['extrato']}")
                    elif opcao == "3":
                            cpf = input("CPF: ")
                            valor = float(input("Valor do saque: "))
                            for conta in contas:
                                    if conta["cpf"] == cpf:
                                            saldo, extrato = sacar(conta["saldo"],valor,conta["extrato"],conta["limite"],conta["numero_saques"],conta["limite_saques"])
                                            conta["saldo"] = saldo
                                            conta["extrato"] = extrato
                    elif opcao == "4":
                            cpf = input("CPF: ")
                            valor = float(input("Valor do deposito: "))
                            for conta in contas:
                                    if conta["cpf"] == cpf:
                                            saldo, extrato = depositar(conta["saldo"],valor,conta["extrato"])
                                            conta["saldo"] = saldo
                                            conta["extrato"] = extrato
                    elif opcao == "5":
                            cpf = input("CPF:384.000.123-   0") 
                            valor = float(input("Valor da transferencia: 1000.00"))
                            destino = input("Destino: Fernando Oliveira Lima")
                            for conta in contas:
                                    if conta["cpf"] == cpf:
                                            saldo, extrato = transferir(conta["saldo"],valor,destino,conta["extrato"])
                                            conta["saldo"] = saldo
                                            conta["extrato"] = extrato
                    elif opcao == "6":
                            cpf = input("CPF: ")
                            for conta in contas:
                                    if conta["cpf"] == cpf:
                                            print(f"Nome: {conta['nome']}")
                                            print(f"Saldo: {conta['saldo']}")
                                            print("Extrato:")
                                            print("-"*30)
                                            print(f"Data: {conta['extrato']}")
                    elif opcao == "7":
                            break
                    else:
                            print("Opção inválida!")
            listar_contas(contas)
            return contas # type: ignore validation     
            return contas # type: ignore valor = float(input("Valor da transferencia: "))
            return contas # type: ignore destino = input("Destino: ")
            return contas # type: ignore saldo, extrato = transferir(conta["saldo"],valor,destino,conta["extrato"])
            return contas # type: ignore conta["saldo"] = saldo
            return contas # type: ignore conta["extrato"] = extrato
            return contas # type: ignore saldo, extrato = depositar(conta["saldo"],valor,conta["extrato"])
            return contas # type: ignore conta["saldo"] = saldo
            return contas # type: ignore conta["extrato"] = extrato
            return contas # type: ignore saldo, extrato = sacar(conta["saldo"],valor,conta["extrato"],conta["limite"],conta["numero_saques"],conta["limite_saques"])
            return contas # type: ignore conta["saldo"] = saldo
            return contas # type: ignore conta["extrato"] = extrato
            return contas # type: ignore cpf, nome, idade, data_nascimento = cadastrar_conta()
            return contas # type: ignore print("Conta criada com sucesso!")
            return contas # type: ignore print(f"Nome: {conta['nome']}")
    for conta in contas:
                                    if conta["cpf"] == cpf:
                                            saldo, extrato = transferir(conta["saldo"],valor,destino,conta["extrato"])
                                            conta["saldo"] = saldo
                                            conta["extrato"] = extrato
                                return contas # type: ignore conta["saldo"] = saldo
                                return contas # type: ignore conta["extrato"] = extrato
                                return contas # type: ignore saldo, extrato = depositar(conta["saldo"],valor,conta["extrato"])
                                return contas # type: ignore conta["saldo"] = saldo
                                return contas # type: ignore conta["extrato"] = extrato
                                return contas # type: ignore saldo, extrato = sacar(conta["saldo"],valor,conta["extrato"],conta["limite"],conta["numero_saques"],conta["limite_saques"])
                                return contas # type: ignore conta["saldo"] = saldo
                                return contas # type: ignore conta["extrato"] = extrato
                                return contas # type: ignore cpf, nome, idade, data_nascimento = cadastrar_conta()
                                return contas # type: ignore print("Conta criada com sucesso!")
                                return contas # type: ignore print(f"Nome: {conta['nome']}")
                                return contas # type: ignore print(f"Saldo: {conta['saldo']}")
                                return contas # type: ignore print(f"Limite: {conta['limite']}")
                                return contas # type: ignore print(f"Limite de saques: {conta['limite_saques']}")
                                return contas # type: ignore print(f"Número de saques: {conta['numero_saques']}")
                                return contas # type: ignore print("Extrato:")
                                return contas # type: ignore print("-"*30)
                                return contas # type: ignore print(f"Data: {conta['extrato']}")
                                return contas # type: ignore print(f"Nome: {conta['nome']}")
                                return contas # type: ignore print(f"Saldo: {conta['saldo']}")
                                return contas # type: ignore print("Extrato:")
                                return contas # type: ignore print("-"*30)
                                return contas # type: ignore print(f"Data: {conta['extrato']}")
                                return contas # type: ignore print(f"Nome: {conta['nome']}")
                                return contas # type: ignore print(f"Saldo: {conta['saldo']}")
                                return contas # type: ignore print("Extrato:")
                                return contas # type: ignore print("-"*30)
                                return contas # type: ignore print(f"Data: {conta['extrato']}")
                                return contas # type: ignore print(f"Nome: {conta['nome']}")
                                return contas # type: ignore print(f"Saldo: {conta['saldo']}")
                                return contas # type: ignore print("Extrato:")
                                return contas # type: ignore print("-"*30)
                                return contas # type: ignore print(f"Data: {conta['extrato']}")
                                return contas # type: ignore print(f"Nome: {conta['nome']}")
                                return contas # type: ignore print(f"Saldo: {conta['saldo']}")
                                return contas # type: ignore print("Extrato:")
                                return contas # type: ignore print("-"*30)
                                
    
    
