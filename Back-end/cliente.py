class Cliente(): # Classe cliente
    __ultimoID = 0
    def __init__(self, nome, cpf, senha):
        Cliente.__ultimoID += 1
        self.id = Cliente.__ultimoID
        self.nome = nome # Atributos: id, nome, CPF e saldo
        self.cpf = cpf
        self.senha = senha
        self.saldo = 1000.98 
    
    def saque(self, dinheiro): # Realiza saque
        self.saldo -= dinheiro
    
    def deposito(self, dinheiro): # Realiza depósito
        self.saldo += dinheiro
    
    def setSenha(self, senha): # Define senha
        self.senha = senha
    
    def getId(self): # Getters dos demais atributos
        return self.id
    
    def getNome(self):
        return self.nome
    
    def getCPF(self):
        return self.cpf
    
    def getSaldo(self):
        return self.saldo
