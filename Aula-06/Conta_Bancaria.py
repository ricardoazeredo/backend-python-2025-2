class ContaBancaria:
    def __init__(self,titular, saldo):
        self.titular = titular
        self.__saldo = saldo
    
    def depositar(self,valor):
        self.__saldo += valor
    
    def sacar(self,valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")    

    def mostrar_saldo(self):        
        print(f"Saldo atual: R$ {self.__saldo}")

conta1 = ContaBancaria('Ricardo', 7000)
conta1.mostrar_saldo()

conta1.depositar(3000)
conta1.mostrar_saldo()

conta1.sacar(8000)
conta1.mostrar_saldo()
conta1.sacar(1500)
conta1.mostrar_saldo()