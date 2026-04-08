import abc

#Classe abstrata que herda do módulo
class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float =0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    #Torna o método obrigatório nas subclassses
    @abc.abstractmethod
    def sacar(self, valor_saque: float) -> float:
        self.saldo -= valor_saque

    def depositar(self, valor_deposito: float) -> float:
        self.saldo += valor_deposito
        self.detalhes(f'(Depósito: {valor_deposito})')
        return self.saldo

    def detalhes(self, msg: str =''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}.')

class ContaPoupança(Conta):
    def sacar(self, valor_saque: float):
        valor_pos_saque = self.saldo - valor_saque
        
        if valor_pos_saque >= 0:
            self.saldo -= valor_saque
            self.detalhes(f'O saque está sendo efetuado no valor de {valor_saque}')
            return self.saldo
        else:
            print('Você não têm esse valor disponível para saque.')
            self.detalhes(f'Saque negado: {valor_saque}')
            return self.saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'  

class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float =0, limite: float =0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor_saque):
        valor_pos_saque = self.saldo - valor_saque
        limite_maximo = -self.limite
        
        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor_saque
            self.detalhes(f'O saque está sendo efetuado no valor de {valor_saque}')
            return self.saldo
        else:
            print(f'Seu limite é: {self.limite:.2f}')
            self.detalhes(f'Saque negado: {valor_saque}')
            return self.saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attrs}'        


if __name__ == '__main__':
    ...
