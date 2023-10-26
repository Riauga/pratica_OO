class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo conta {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Conta: {}\nTitular:{}\nSaldo:{}".format(self.__numero, self.__titular, self.__saldo))

    def deposito(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__limite + self.__saldo
        return valor_a_sacar <= valor_disponivel

    def saque(self, valor):
        if self.__pode_sacar:
            self.__saldo -= valor
        else:
            print("O valor {} passa do limite.".format(valor))

    def transferencia(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_b():
        codigo_b = "001"
        return codigo_b

    @staticmethod
    def codigos_b():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}
