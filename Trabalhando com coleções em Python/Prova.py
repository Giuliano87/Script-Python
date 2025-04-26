import textwrap
from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime

class Pessoa(ABC):
    def __init__(self, nome = "Fagner", idade=37, cpf ="xxx.xxxx.xxx-xx"):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

class Conta(ABC):
   
   def __init__(self, Numero_da_Conta, Titular, Saldo, data, hora):
        self.Numero_da_Conta = Numero_da_Conta 
        self.Titular = "Fagner_Jacob"
        self.Saldo = 5000,00
        self.data = datetime.now()
        self.hora = datetime.now().time()
        self.limite = 0
        self.extrato()
        self.extrato_especial()

   def depositar(self, valor):
        self.Saldo += valor
        print("Deposito realizado com sucesso!")
        self.extrato()

   def sacar(self, valor):
        if self.Saldo >= valor:
            self.Saldo -= valor
            print("Saque realizado com sucesso!")
            self.extrato()
        else:
            print("Saldo insuficiente!")

   def transferir(self, valor, destino):
        if self.Saldo >= valor:
            self.Saldo -= valor
            destino.depositar(valor)
            print("Transferência realizada com sucesso!")
        else:
            print("Saldo insuficiente!")

   def extrato(self):
        print("Extrato da conta")
        print("Conta: ", self.Numero_da_Conta)
        print("Titular: ", self.Titular)
        print("Saldo: ", self.Saldo)
        print("Data: ", self.data)
        print("Hora: ", self.hora)

   def __str__(self):
        return f"Conta: {self.Numero_da_Conta}\nTitular: {self.Titular}\nSaldo: {self.Saldo}\nData: {self.data}\nHora: {self.hora}"

class ContaEspecial(Conta):
    def __init__(self, Numero_da_Conta, Titular, Saldo, data, hora, limite):
        super().__init__(Numero_da_Conta, Titular, Saldo, data, hora)
        self.limite = limite

    def sacar(self, valor):
        if self.Saldo + self.limite >= valor:
            self.Saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente!")

    def extrato(self):
        print("Extrato da conta especial")
        print("Conta: ", self.Numero_da_Conta)
        print("Titular: ", self.Titular)
        print("Saldo: ", self.Saldo)
        print("Limite: ", self.limite)
        print("Data: ", self.data)
        print("Hora: ", self.hora)

    def __str__(self):
        return f"Conta Especial: {self.Numero_da_Conta}\nTitular: {self.Titular}\nSaldo: {self.Saldo}\nLimite: {self.limite}\nData: {self.data}\nHora: {self.hora}"

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def abrir_conta(self, conta):
        self.contas.append(conta)

    def fechar_conta(self, conta):
        self.contas.remove(conta)

    def extrato(self, conta):
        conta.extrato()

    def transferencia(self, conta_origem, conta_destino, valor):
        conta_origem.transferir(valor, conta_destino)

    def __str__(self):
        return f"Banco: {self.nome}\nContas: {self.contas}"

class BancoItau(Banco):
    def __init__(self, Fagner_Jacob):
        super().__init__("Itau")
        self.Fagner_Jacob = Fagner_Jacob

    def abrir_conta(self, conta):
        if isinstance(conta, ContaEspecial):
            self.contas.append(conta)
        else:
            print("Conta especial é obrigatória para o Itau")
    def fechar_conta(self, conta):
        self.contas.remove(conta)        

    def extrato(self, conta):
        conta.extrato()     
        self.data = datetime.now()
        self.hora = datetime.now().time()

    def fechar_conta(self, conta):
        self.contas.remove(conta)

    def extrato(self, conta):
        conta.extrato()

    def transferencia(self, conta_origem, conta_destino, valor):
        conta_origem.transferir(valor, conta_destino)

    def __str__(self):
        return f"Banco Itau: {self.nome}\nContas: {self.contas}"       