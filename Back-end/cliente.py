class Cliente(): # Classe cliente
    __ultimoID = 0
    def __init__(self, nome, cpf):
        Cliente.__ultimoID += 1
        self.id = Cliente.__ultimoID
        self.nome = nome # Atributos: id, nome, CPF e saldo
        self.cpf = cpf
        self.saldo = 0 
    
    def saque(self, dinheiro): 
        self.saldo -= dinheiro
    
    def deposito(self, dinheiro):
        self.saldo += dinheiro
    
    def getId(self):
        return self.id
    
    def getNome(self):
        return self.nome
    
    def getCPF(self):
        return self.cpf
    
    def getSaldo(self):
        return self.saldo