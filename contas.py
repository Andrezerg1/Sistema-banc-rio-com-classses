import abc

#Classe abstrata que herda do módulo
class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    #Torna o método obrigatório nas subclassses
    @abc.abstractmethod
    def sacar(self, valor_saque):
        self.saldo -= valor_saque

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito
        self.detalhes(f'(Depósito: {valor_deposito})')

    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}.')

class ContaPoupança(Conta):
    def sacar(self, valor_saque):
        valor_pos_saque = self.saldo - valor_saque
        
        if valor_pos_saque >= 0:
            self.saldo -= valor_saque
            self.detalhes(f'O saque está sendo efetuado no valor de {valor_saque}')
            return self.saldo
        else:
            print('Você não têm esse valor disponível para saque.')
            self.detalhes(f'Saque negado: {valor_saque}')

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0):
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



if __name__ == '__main__':
    #cp1 = ContaPoupança('0100-7', 1, 1500)
    #cp1.sacar(0)
    #cp1.depositar(100)
    #cp1.sacar(1600)

    #print('###')

    cc1 = ContaCorrente('0100-7', 1, 1500, 200)
    cc1.sacar(1800)
    #cc1.depositar(100)
    #cc1.sacar(1600)